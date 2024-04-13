# Plant Care Assistant

## Development Notes

Started the project by doing discovery on the Capacitive Moisture Sensor (CMS). I found that higher values equate to dryer conditions.

Completely Dry: 217  
Dry Soil: 205  
Very Wet Soil: 130  
Water: 103

Parts:
Raspberry Pi
ADS7830 Analog-to-Digital Converter
Capacitive Mositure Sensor v1.2
Jumper Cables


Now getting a different set of values...

Completely Dry: 156 
Dry Soil: 153 
Very Wet Soil: 57  
Water: 40

About the same range between min and max, so theoretically one could have a calibration function?
~Water = Dry - 115

After a lot of testing it seems to have stuck with this second range.