"""Support for Buienalarm weather service."""

from datetime import timedelta
from typing import Any, Mapping, Optional, Union

from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.components.sensor import SensorEntity
from homeassistant.const import (
    ATTR_ATTRIBUTION,
    CONF_LATITUDE,
    CONF_LONGITUDE,
    CONF_MONITORED_CONDITIONS,
    CONF_NAME,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
)
from homeassistant.util import dt as dt_util
from homeassistant.helpers import config_validation as cv
import voluptuous as vol

from buienalarm.pybuienalarm import Buienalarm
from .const import (
    ATTRIBUTION,
    CONF_TIMEFRAME,
    DEFAULT_NAME,
    DEFAULT_TIMEFRAME,
    ITEM_PRECIP_NOW,
    ITEM_TEMP,
    ITEM_PRECIP_FORECAST_TOTAL,
    ITEM_PRECIP_FORECAST_AVG,
    ITEM_NEXT_RAIN_FORECAST,
    LOGGER as _LOGGER,
    SENSOR_TYPES,
    SensorType,
    UPDATE_INTERVAL,
)


PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Optional(CONF_MONITORED_CONDITIONS, default=[ITEM_PRECIP_NOW]): vol.All(
            cv.ensure_list, vol.Length(min=1), [vol.In(SENSOR_TYPES.keys())]
        ),
        vol.Inclusive(
            CONF_LATITUDE, "coordinates", "Latitude and longitude must exist together"
        ): cv.latitude,
        vol.Inclusive(
            CONF_LONGITUDE, "coordinates", "Latitude and longitude must exist together"
        ): cv.longitude,
        vol.Optional(CONF_TIMEFRAME, default=DEFAULT_TIMEFRAME): vol.All(
            vol.Coerce(int), vol.Range(min=5, max=120)
        ),
        vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
    }
)

BUIENALARM_TZ = dt_util.get_time_zone("Europe/Amsterdam")


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    async_add_entities: AddEntitiesCallback,
    discovery_info: Optional[DiscoveryInfoType] = None,
) -> None:
    """Set up Buienalarm."""

    latitude = config.get(CONF_LATITUDE, hass.config.latitude)
    longitude = config.get(CONF_LONGITUDE, hass.config.longitude)
    timeframe = timedelta(minutes=config[CONF_TIMEFRAME])

    if None in (latitude, longitude):
        _LOGGER.error("Latitude or longitude not set in HomeAssistant config")
        return

    api = Buienalarm(longitude, latitude)

    client_name = config.get(CONF_NAME)
    async def async_api_update():
        """."""
        await hass.async_add_executor_job(api.update)
    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name=client_name,
        update_method=async_api_update,
        update_interval=UPDATE_INTERVAL,
    )
    entities = [
        BuienalarmSensor(coordinator, api, sensor, client_name, timeframe=timeframe)
        for sensor in config[CONF_MONITORED_CONDITIONS]
    ]
    async_add_entities(entities, True)


class BuienalarmSensor(CoordinatorEntity, SensorEntity):
    """Representation of Buienalarm."""

    def __init__(
        self,
        coordinator: DataUpdateCoordinator,
        api: Buienalarm,
        sensor_type_name: str,
        client_name: str,
        timeframe: timedelta = timedelta(minutes=60)
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._api = api
        self._sensor_type_name = sensor_type_name
        self._client_name = client_name
        self._timeframe = timeframe

    @property
    def name(self) -> str:
        """Return name."""
        return f"{self._client_name} {self._sensor_type.name}"

    @property
    def unit_of_measurement(self) -> str:
        """Return unit of measurement."""
        return self._sensor_type.unit

    @property
    def icon(self) -> str:
        """Return icon."""
        return self._sensor_type.icon

    @property
    def device_state_attributes(self) -> Mapping[str, Any]:
        """Return state attributes."""
        attr = {
            ATTR_ATTRIBUTION: ATTRIBUTION,
        }

        if "forecast" in self._sensor_type_name and \
            self._api.has_data:
            attr[CONF_TIMEFRAME] = self._timeframe / self._api.delta

        return attr

    @property
    def state(self) -> Optional[Union[str, float]]:
        """Get state."""
        _LOGGER.debug("Get state: %s", self._sensor_type_name)
        if not self._api.has_data:
            return None

        if self._sensor_type_name == ITEM_TEMP:
            return self._api.temperature
        elif self._sensor_type_name == ITEM_PRECIP_NOW:
            return self._precipitation_now
        elif self._sensor_type_name == ITEM_PRECIP_FORECAST_TOTAL:
            return self._precipitation_forecast_total
        elif self._sensor_type_name == ITEM_PRECIP_FORECAST_AVG:
            return self._precipitation_forecast_average
        elif self._sensor_type_name == ITEM_NEXT_RAIN_FORECAST:
            return self._next_rain_forecast
        else:
            raise NotImplementedError("Unknown sensor type")

    @property
    def _precipitation_forecast_average(self) -> float:
        """Get average precipitation forecast."""
        return sum(self._precipitation_values) / self._timeframe_value_count

    @property
    def _precipitation_forecast_total(self) -> float:
        """Get total precipitation forecast."""
        return sum(self._precipitation_values)

    @property
    def _precipitation_now(self) -> float:
        """Get current precipitation."""
        return self._precipitation_values[0]

    @property
    def _next_rain_forecast(self) -> Optional[str]:
        """Get next rain forecast."""
        for precip_at in self._precipitation:
            if precip_at.value > 0.0:
                return str(precip_at.timestamp)

        return None

    @property
    def _precipitation(self):
        """Get precipitation within timeframe, starting from now."""
        count = self._timeframe_value_count
        return self._api.precipitation_from_now[0:count]  # Slice up to our timeframe.

    @property
    def _precipitation_values(self):
        """Get precipitation values within timeframe, starting from now."""
        return [precip.value for precip in self._precipitation]

    @property
    def _timeframe_value_count(self):
        """Get number of precipitation slots within our timeframe."""
        return int(self._timeframe / self._api.delta)

    @property
    def _sensor_type(self) -> SensorType:
        """Get SensorType for self."""
        return SENSOR_TYPES[self._sensor_type_name]
