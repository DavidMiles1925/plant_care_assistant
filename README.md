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
| MicroSD card (For Raspberry Pi)          |    1     | link goes here |
| 20x2 Pin Header for Raspberry Pi         |    1     | link goes here |
| ADS7830 Analog-to-Digital Converter      |    1     | link goes here |
| Capacitive Moisture Sensor(s)            |  1-3\*   | link goes here |
| Water Pump(s) and Line                   |  1-3\*   | link goes here |
| 5V USB Grow Light                        |    1     | link goes here |
| 5V Relay                                 |  2-4\*   | link goes here |
| Solderless Breadboard                    |    1     | link goes here |
| Dupont Cables 10cm and 30cm              |   Many   | link goes here |

\*Quantity is dependent on how many plants you want to care for.

### Diagram

Diagram will be posted when project is complete

### Set Up the Pi

[See my github tutorial on how to set up the Raspberry Pi Zero 2 W](https://github.com/DavidMiles1925/pi_zero_setup)

- If you want to run the code via SSH, make sure to also follow the instructions on that page on how to:
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

```bash
sudo apt-get install git
```

2. Clone Repo

```bash
git clone https://github.com/DavidMiles1925/plant_care_assistant.git
```

### Configuring the Program

See the video for a detailed walkthrough of the configuration values. Otherwise

### Run the Program

- Navigating to directory

```bash
cd plant_care_assistant
```

- Run the program

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
