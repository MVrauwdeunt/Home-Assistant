[![HA Version](https://img.shields.io/badge/Home%20Assistant-2021.10.2-brightgreen)](https://github.com/home-assistant/home-assistant/releases/2021.10.2)
# Home Assistant Configuration
---
This is repo is the current [Home Assistant](https://home-assistant.io) configuration. Below you'll find links to the devices and custom components used.

Feel free to use the code as you like.

---
## System

Home Assistant runs in a [Docker](https://www.docker.com) container on a server running [Debian 10 (Buster)](https://www.debian.org/). The server also doubles as a Network Attached Storage serving files over NFS and SMB.

The system consists of:

Type | Discription
-- | --
Mainboard | ASRock B85M Pro4
CPU | Intel Celeron G1840
Memory | Crucial 16GB

By no means is it a powerhouse. But even with these specs I have no issues. Most of the time it is idle or just above idle.
I am runing [Debian 10 (Buster)](https://www.debian.org/). The server also doubles as a Network Attached Storage serving files over NFS and SMB. 

In total there are 36 docker containers running. Some are related to my smarthome Home Assistant offcourse :), ESPHome, Mosquitto.
There are a couple of containers which work with Home Assistant but could be fun or usefull in other situations. For instance Grocy, Barcode Buddy, VSCode and Rhasspy.
Then there are several containers related to my multimedia setup. Automated download and handling of audio, video and subtitles and such. And last the containers for controlling, 
securing and backup of the server and network. Authelia, Duplicati and Unifi among others.

---
## My Design Philosophy


### Keep it local:
&emsp;&emsp;
As a rule of thumb everything should be local. Basic things like light, heating but also multimedia should be available without an internet connection.

### Minimal interation: 
&emsp;&emsp;
Home-automation should not be some fancy remote control but an inteligent system which takes action based on sensors or indirect actions.<br/>
&emsp;&emsp;
For instance the lights in my livingroom should turn on when there is low light and someone is home. When arriving after dark lights should turn on whitout intervention. 

### Add functionality don't take away any.
&emsp;&emsp;
For a good user experience basic things like light switches should more or less work as you expect. 


---
## Custom Components

I use [HACS](https://github.com/hacs/integration) to add integrations I miss currently I use these:


- [HACS](https://hacs.xyz/docs/configuration/start)
  a powerful UI to handle downloads of all your custom needs
- [Generate readme](https://github.com/custom-components/readme)
  Generates this awesome readme file.
- [Neerslag App (Buienalarm / Buienradar)](https://github.com/aex351/home-assistant-neerslag-app)
  Display rain forecast using Buienalarm and/or Buienradar sensor data
- [Browser mod](https://github.com/thomasloven/hass-browser_mod/blob/master/README.md)
  Turns your browser into a controllable entity
- [Breaking Changes](https://github.com/custom-components/breaking_changes)
  This will list breaking changes on versions for versions released after the one you are running up to the latest stable version.
- [Sensor OvApi](https://github.com/Paul-dH/Home-Assisant-Sensor-OvApi)
  Public Transport information from OVapi
- [Monitor Docker](https://github.com/ualex73/monitor_docker)
  Get info from the docker which runs it all
- [Grocy](https://github.com/custom-components/grocy)
  Connection to my Grocy installation
- [Climate Group](https://github.com/daenny/climate_group)
  Groups multiple climate devices to a single entity. Useful if you have for instance multiple radiator thermostats in a room and want to control them all together.
- [Adaptive Lighting](https://github.com/basnijholt/adaptive-lighting#readme)
  Changes the settings of my lights throughout the day

***


Description | value
-- | --
Number of automations | 53
Number of entities | 727
Number of sensors | 462


---

## Images


### Wallpanel running on a Samsun 10.1 inch tablet
![Wallpanel](https://raw.githubusercontent.com/Warlock77/Home-Assistant/main/www/images/screenshots/Wallpanel2.png)

Description | value
-- | --
Number of automations | 53
Number of entities | 727
Number of sensors | 462


## The integrations that I use

- [HACS](https://hacs.xyz/docs/configuration/start)
  a powerful UI to handle downloads of all your custom needs
- [Generate readme](https://github.com/custom-components/readme)
  Generates this awesome readme file.
- [Neerslag App (Buienalarm / Buienradar)](https://github.com/aex351/home-assistant-neerslag-app)
  Display rain forecast using Buienalarm and/or Buienradar sensor data
- [Browser mod](https://github.com/thomasloven/hass-browser_mod/blob/master/README.md)
  Turns your browser into a controllable entity
- [Breaking Changes](https://github.com/custom-components/breaking_changes)
  This will list breaking changes on versions for versions released after the one you are running up to the latest stable version.
- [Sensor OvApi](https://github.com/Paul-dH/Home-Assisant-Sensor-OvApi)
  Public Transport information from OVapi
- [Monitor Docker](https://github.com/ualex73/monitor_docker)
  Get info from the docker which runs it all
- [Grocy](https://github.com/custom-components/grocy)
  Connection to my Grocy installation
- [Climate Group](https://github.com/daenny/climate_group)
  Groups multiple climate devices to a single entity. Useful if you have for instance multiple radiator thermostats in a room and want to control them all together.
- [Adaptive Lighting](https://github.com/basnijholt/adaptive-lighting#readme)
  Changes the settings of my lights throughout the day

***



Generated by the [custom readme integration](https://github.com/custom-components/readme)