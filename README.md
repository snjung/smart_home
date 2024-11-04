# smart_home
Collection of stuff related to home automatization and smart home

This repository is a personal collection of information, tools and solutions for my home. Probably of little interest for anybody else - nevertheless, suit yourself if there is anything interesting for you.

## Vitodens W200 boiler

The gas heater has a serial interface, that can be optically accessed. While being proprietary, it is well documented by community projects

### Ressources

Here are some interesting ressources to start with:

Wiki containing description and tutorials (building diy hardware-interfaces, protocol information, link to usable software tools)
https://github.com/openv/openv/wiki/

For implementation of the protocol on an ESP8266 microcontroller, there is a library called VitoWiFi
https://github.com/bertmelis/VitoWifi

I have to figure out, how to use this library to transfer information somewhere to a logging device within my intranet.

Possible implementations:
https://github.com/Schnup89/OpenV_NodeMCU

Sehr vielversprechend:
- Ist für Vitodens 200-W
- Sendet an MQTT-Broker, hat aber auch ein Webinterface
https://github.com/empty88/OptoLink


### Test Results
According to all information on the net, the W200 (Vitodens W200) should be periodically sending 0x05 via the serial interface expecting an immediate response, if someone wants to start communication.
However, my W200 sends 0xFD instead.
