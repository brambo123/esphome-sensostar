# esphome-sensostar
### Custom ESPHome component use with Engelmann SensoStar heat meters
This component allows you to read the current status of Engelmann SensoStar heat meters.  
Both the mechanical SensoStar E meter (and the measuring capsule: A, I, T, M and Q) and the ultrasonic SensoStar U meter use the same SensoStar calculation modules.  
In addition to the original Engelmann meters, there are also white-label meters on the market.  
Some known compatible product series:
- Engelmann SensoStar
- Maddalena microCLIMA
- Wasser-Geräte VoluMess VI

There are probably many more brands, feel free to create an issue to add brands.

### Hardware
Let's start with a few important notes...
> [!CAUTION]
> Some readout modules power the heat meter directly through the onboard connector.  
> Ensure that the standard battery is not connected directly to the meter, but to the readout modules.  
> Failure to do this may cause the non-rechargeable battery to be charged and __catch fire__.

> [!IMPORTANT]
> Adding a custom module to the heat meter is entirely at your own risk.  
> The modules have not been officially tested by the manufacturer.  
> Therefore, it's impossible to say with certainty that it won't affect the meter's accuracy.  
> This will invalidate the official MID certification (and, of course, void the warranty).

The first version of the module had almost the same galvanic isolation in the data connection as the original Modbus module.  
However, this galvanic isolation isn't strictly necessary for personal use.  
Therefore, the new modules require fewer components, making them more compact and cost-effective.  

###### SensoStar-ESP v2
![SensoStar-ESP v2](/PCB/SensoStar-ESP%20-%20v2/SensoStar-ESP%20-%20v2.png)
The newest version is based on an ESP32-C6-MINI-1 module and uses USB for both power and programming.
The PCB uses as many 'Basic' or 'Promotional Extended' components from JLCPCB as possible.  
All necessary files for ordering directly from JLCPCB are available here.  
Side note: the first version is still on order, so it has not been tested yet!  

An RS485 connection is available as an option.  
This allows you to read a Modbus electricity meter, making it possible to calculate the heat pump's COP.  
Wiki: [How‐to: Real‐time COP calculation]([/wiki/How%E2%80%90to:-Real%E2%80%90time-COP-calculation](https://github.com/brambo123/esphome-sensostar/wiki/How%E2%80%90to:-Real%E2%80%90time-COP-calculation))  


