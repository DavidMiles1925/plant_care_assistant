# Plant Care Assistant

## Project Description

This project was developed to liven up my workspace. I wanted to have some plants, but historically I haven't kept them alive very well. I either over-water or under-water them. On top of that, my workspace gets no natural sunlight, so I wanted to make sure my plants got plenty of light. And lastly, my garage gets chilly in the winter, so I wanted my plants stay warm.

## Accepatance Criteria

This project, when it is complete will:

- Support up to 3 plants
- Monitor the moisture levels of the soil of each plant
- Water each plant when the soil is dry AND the soil has had an adequete period of dryness
- Provide adequete lighting for the plants with a timer function (future state idea: smart lighting through feedback from a photo-resistor)
- Provide gentle heat when soil temperature falls too low
- Log all metrics for debugging and historical reference

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

Instructions here

### Set Up the Pi

[See my github tutorial on how to set up the Raspberry Pi Zero 2 W](https://github.com/DavidMiles1925/pi_zero_setup)

- Make sure to also follow the instructions on that page on how to:
  [Set up a static IP address](https://github.com/DavidMiles1925/pi_zero_setup?tab=readme-ov-file#configure-static-ip-address)

### Set Up I2C/smbus

1. Enable I2C

```bash
sudo raspi-config
```

- Interface Options
- ARM I2C

2. Install smbus

```bash
sudo apt-get install python3-smbus
```

### Install Code

1. Install Git
2. Clone Repo

### Configuring the Program

- Important values to change in the config.py file

### Run the Program

- Navigating to directory
- Running program

```bash
sudo python plant.py
```

- Enabling program to run on startup (link to Pi Setup Page)

### Accessing the Logs

- Get into Pi via SSH
- Navigate to directory
- Open logs
- Basic nano navigation

## Gallery

![Hooked Up to Monitor](./readme_media/hooked_to_monitor.png)

![First Time Remote](./readme_media/first_time_remote.jpg)

![On the Shelf](./readme_media/on_the_shelf.jpg)

![Top View](./readme_media/top_view.jpg)

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
>
> > Spent a whole bunch of time working on the light. I ended up running light.py as a subprocess. That is fine, except I need to incorporate a more graceful way of terminating the processes. Maybe. The point of the thing is to keep running all the time.
>
> > I made the light start time into an array of start times. In order to avoid scorching the leaves, I will give the plants short bursts of diirected light throughout the day, rather than a sustained period.
