# This is my current Home Assistant installation.

### Home page
![home_page](https://git.digitaal-rechercheurs.nl:9090/squandor/homeassistant/raw/branch/master/www/img/home_page.png)


<!-- start-table -->

<table>
    <thead>
        <tr>
            <th>Switches 🎚</th>
            <th>Software</th>
            <th>Units (#)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Sonoff</td>
            <td>ESPHome</td>
            <td>3</td>
        </tr>
        <tr>
            <td>Shelly 1</td>
            <td>ESPHome</td>
            <td>1</td>
        </tr>
        <tr>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
        </tr>
    </tbody>
    <thead>
        <tr>
            <th>Sensors 🌡</th>
            <th>Software</th>
            <th>Type</th>
            <th>Units (#)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Wemos</td>
            <td>ESPHome</td>
            <td>PIR, Temperature, Humidity, Lightslevel</td>
            <td>1</td>
        </tr>
        <tr>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
        </tr>
    </tbody>
    <thead>
        <tr>
            <th>Media player 📺🔈</th>
            <th>Units (#)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Raspberry Pi 3B OSMC</td>
            <td>1</td>
        </tr>
        <tr>
            <td>Sony OLED 48</td>
            <td>1</td>
        </tr>
        <tr>
           <td>Google Chromecast</td>
           <td>3</td>
        <tr>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
        </tr>
    </tbody>
    <thead>
        <tr>
            <th>Lights 💡</th>
            <th>Units (#)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Philips Hue White Filament Bulb ST64 E27</td>
            <td>1</td>
        </tr>
        <tr>
            <td>Milight E27 6W RGB CCT</td>
            <td>4</td>
        </tr>
        <tr>
            <td>Milight FUT039 RGB CCT LED Controller</td>
            <td>1</td>
        </tr>
        <tr>
            <td>Milight E27 9W RGB CCT with HUB</td>
            <td>1</td>
        </tr>
        <tr>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
        </tr>
    </tbody>
    <thead>
        <tr>
            <th>Hubs 🌎</th>
            <th>Units (#)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>ConBee II</td>
            <td>1</td>
        </tr>
        </tr>
            <td>esp8266 Milight Hub</td>
            <td>1</td>
        </tr>
        <tr>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
        </tr>
    </tbody>
    <thead>
        <tr>
            <th>Server 🖥</th>
            <th>Units (#)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Raspberry Pi 4, 4GB RAM, with Supervised Home Assistant</td>
            <td>1</td>
        </tr>
        <tr>
            <td>Raspberry Pi 4 FLIRC Case</td>
            <td>1</td>
        </tr>
        <tr>
            <td>SanDisk Ultra microSDHC Memory Card 32GB</td>
            <td>1</td>
        </tr>
        <tr>
            <td>Raspberry Pi 3 Model B</td>
            <td>1</td>
        </tr>
        <tr>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
        </tr>
    </tbody>
    <thead>
        <tr>
            <th>Device tracker 🔍</th>
            <th>Units (#)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>iPhone X with the new iOS app</td>
            <td>2</td>
        </tr>
        <tr>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
        </tr>
    </tbody>
    <thead>
        <tr>
            <th>Other</th>
            <th>Units (#)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>PlayStation Eye Webcam and Microphone array</td>
            <td>1</td>
        </tr>
        <tr>
            <td>DSMR - Slimme Meter kabel</td>
            <td>1</td>
        </tr>
        <tr>
            <td>Nodo-Shop – OpenTherm Gateway (OTGW) with NodeMCU</td>
            <td>1</td>
        </tr>
        <tr>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
        </tr>
    </tbody>
</table>
<!-- end-table -->

## Some statistics about my installation:

Name | Version running | Latest Version
-- | -- | --
Home Assistant | 2021.5.1 | 2021.5.1
ESPHome | fdgl | blaat


Description | value
-- | --
Number of entities | 563
Number of sensors | 346


## The integrations that I use

- [Browser mod](https://github.com/thomasloven/hass-browser_mod/blob/master/README.md)
  Turns your browser into a controllable entity
- [HACS](https://hacs.xyz/docs/configuration/start)
  a powerful UI to handle downloads of all your custom needs
- [Sensor OvApi](https://github.com/Paul-dH/Home-Assisant-Sensor-OvApi)
- [FRITZ!Box Tools](https://github.com/mammuth/ha-fritzbox-tools/blob/master/README.md)
- [Generate readme](https://github.com/custom-components/readme)
  Generates this awesome readme file.
- [Grocy](https://github.com/custom-components/grocy)
  Connection to my Grocy installation
- [Buienalarm](https://github.com/gieljnssns/buienalarm-sensor-homeassistant/tree/master)
  Get local weather info
- [Monitor Docker](https://github.com/ualex73/monitor_docker)
  Get info from the docker which runs it all
- [Adaptive Lighting](https://www.home-assistant.io/integrations/adaptive_lighting)
  Changes the settings of your lights throughout the day
- [Neerslag App (Buienalarm / Buienradar)](https://github.com/aex351/home-assistant-neerslag-app)
  Display rain forecast using Buienalarm and/or Buienradar sensor data

***



Generated by the [custom readme integration](https://github.com/custom-components/readme)