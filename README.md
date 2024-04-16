# Plant Care Assistant

## Project Description

## Seting up the Device

### Parts List

| Item                                     | Quantity | Link           |
| :--------------------------------------- | :------: | :------------- |
| Raspberry Pi Zero 2 W (Any Pi will work) |    1     | link goes here |
| ADS7830 Analog-to-Digital Converter      |    1     | link goes here |
| Capacitive Moisture Sensor(s)            |   1-3    | link goes here |
| Water Pump(s) and Line                   |   1-3    | link goes here |
| 5V Relay                                 |   2-4    | link goes here |
| Solderless Breadboard                    |    1     | link goes here |
| Dupont Cables 10cm and 30cm              |   Many   | link goes here |

### Diagram

Diagram will be posted when project is complete

### Build the Board

### Set Up the Pi

[See my github tutorial on how to set up the Raspberry Pi Zero 2 W](https://github.com/DavidMiles1925/pi_zero_setup)

### Set Up I2C/smbus

1. Enable I2C
2. Install smbus

```bash
sudo apt-get install python3-smbus
```

### Install Code

1. Install Git
2. Clone Repo

### Run the Program

### Accessing the Logs

## Development Notes

> > Started the project by doing discovery on the Capacitive Moisture Sensor (CMS). I found that higher values equate to dryer conditions.
> >
> > Completely Dry: 217  
> > Dry Soil: 205  
> > Very Wet Soil: 130  
> > Water: 103
> >
> > Parts:
> > Raspberry Pi
> > ADS7830 Analog-to-Digital Converter
> > Capacitive Mositure Sensor v1.2
> > Jumper Cables
>
> > Now getting a different set of values...
> >
> > Completely Dry: 156
> > Dry Soil: 153
> > Very Wet Soil: 57  
> > Water: 40
> >
> > About the same range between min and max, so theoretically one could have a calibration function?
> > ~Water = Dry - 115
> >
> > After a lot of testing it seems to have stuck with this second range.
>
> > > Nevermind, after turning it on again we are back to the first range. Thinking about it, I don't think I ever restarted the device. Maybe that was what needed to happend?
> >
> > Yep that was it.
>
> > Added code to collect data from multiple analog inputs. Bought 3 plants and got sensors in them. Need to go back and get the watering functionallity working with multiple channels.
> >
> > Added Red LEDs for each of the 3 channels to indicate the need for watering. These will eventually (Once care is automated) be replaced with an RGB LED to indicate a broad status of the plants. (3 pins used for 1 each of the red LEDs, those same 3 pins used for a single RGB LED)
> > Pins 17, 27, 22
>
> > Added logic for "watering" multiple channels, still using LEDs as substitutes.
>
> > Added ability to turn single light on and off
> > Pin 23
>
> > Didn't think hard enough about the logic on my light. I will just write a separate script instead of trying to incorporate it into my already growing .py file.
