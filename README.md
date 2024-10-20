# Plant Care Assistant

## Video

[Project Video Link](https://www.youtube.com/watch?v=mg84hZeF66U&t=700s)
![Video Image](./readme_media/finished_product.jpg)

## Project Description

This project was developed to liven up my workspace. I wanted to have some plants, but historically I haven't kept them alive very well. I either over-water or under-water them. On top of that, my workspace gets no natural sunlight, so I wanted to make sure my plants got plenty of light. And lastly, my garage gets chilly in the winter, so I wanted my plants stay warm.

## Accepatance Criteria

**This project, when it is complete will:**

- ✔ Support up to 3 plants
- ✔ Monitor the moisture levels of the soil of each plant
- ✔ Water each plant when the soil is dry AND the soil has had an adequete period of dryness
- ✔ Provide adequete lighting for the plants with a timer function
- ✔ Log all metrics for debugging and historical reference
- **✔ NEW:** The amount of water dispensed can be counted from the logs programmatically

**Future State:**

- Provide gentle heat when soil temperature falls too low (future state)
- Smart lighting through feedback from a photo-resistor

## Seting up the Device

### Parts List

| Item                                     | Quantity | Link                                                                                                                                |
| :--------------------------------------- | :------: | :---------------------------------------------------------------------------------------------------------------------------------- |
| Raspberry Pi Zero 2 W (Any Pi will work) |    1     | [Microcenter](https://www.microcenter.com/product/643085/raspberry-pi-zero-2-w)                                                     |
| MicroSD card (For Raspberry Pi)          |    1     | [Microcenter](https://www.microcenter.com/product/658767/micro-center-64gb-ultra-microsdxc-class-10-flash-memory-card-with-adapter) |
| 20x2 Pin Header for Raspberry Pi         |    1     | [Microcenter](https://www.amazon.com/gp/product/B083DYVWDN/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)                         |
| ADS7830 Analog-to-Digital Converter      |    1     | No Link Available                                                                                                                   |
| Capacitive Moisture Sensor(s)            |  1-3\*   | [Amazon](https://www.amazon.com/gp/product/B07SYBSHGX/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)                              |
| Water Pump(s) and Line                   |  1-3\*   | [Amazon](https://www.amazon.com/gp/product/B07TMW5CDM/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)                              |
| 5V USB Grow Light                        |    1     | [Amazon](https://www.amazon.com/gp/product/B0BXKWMTPF/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)                              |
| 5V Relay                                 |  2-4\*   | [Amazon](https://www.amazon.com/gp/product/B09SLS3QT1/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)                              |
| LED                                      |  1-3\*   | [Amazon](https://www.amazon.com/gp/product/B07QXR5MZB/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)                              |
| 220 Ohm Reistor                          |  1-3\*   | [Amazon](https://www.amazon.com/gp/product/B07ZX2CB6B/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)                              |
| Solderless Breadboard                    |    1     | [Amazon](https://www.amazon.com/gp/product/B07PBFPJC6/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)                              |
| Dupont Cables 10cm and 30cm              |   Many   | [Amazon](https://www.amazon.com/gp/product/B01EV70C78/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)                              |

\*Quantity is dependent on how many plants you want to care for.

### Diagram

<img src="./readme_media/diagram.png" width="800" alt="diagram">

### Pin Assignments

**Note that all pins are in BCM mode**

| Component                           | Pi/Connection |    Power     |
| :---------------------------------- | :-----------: | :----------: |
| ADS7830 (or 1115)                   |     2, 3      |  3.3V (Pi)   |
| Capacitive Moisture Sensor v 1.2 #1 |   A0 (ADS)    |  3.3V (Pi)   |
| Capacitive Moisture Sensor v 1.2 #1 |   A1 (ADS)    |  3.3V (Pi)   |
| Capacitive Moisture Sensor v 1.2 #1 |   A2 (ADS)    |  3.3V (Pi)   |
| LED #1                              |      17       |  3.3V (Pi)   |
| LED #2                              |      27       |  3.3V (Pi)   |
| LED #3                              |      22       |  3.3V (Pi)   |
| Pump **Relay** #1                   |       5       |   5V (Pi)    |
| Pump **Relay** #2 (Optional)        |       6       |   5V (Pi)    |
| Pump **Relay** #3 (Optional)        |      13       |   5V (Pi)    |
| Light Relay #4                      |      23       |   5V (Pi)    |
| Water Pump #1                       |    Relay 1    | 5V (**USB**) |
| Water Pump #2 (Optional)            |    Relay 2    | 5V (**USB**) |
| Water Pump #3 (Optional)            |    Relay 3    | 5V (**USB**) |
| Light                               |    Relay 4    | 5V (**USB**) |

### Set Up the Pi

[See my github tutorial on how to set up the Raspberry Pi Zero 2 W](https://github.com/DavidMiles1925/pi_zero_setup)

- If you want to run the code via SSH, make sure to also follow the instructions on that page on how to:
  [Set up a static IP address](https://github.com/DavidMiles1925/pi_zero_setup?tab=readme-ov-file#configure-static-ip-address)

### Set Up the Capacitive Moisture Sensor v1.2

1. Get the pins connected:  
   &emsp;See the [diagram](#diagram), [pin assignments](#pin-assignments), and [parts list](#parts-list) above.

<img src="./readme_media/sensor1.jpg" width="300" alt="sensor1">
<img src="./readme_media/sensor2.jpg" width="300" alt="sensor2">

2. Make sure to calibrate your values with dry air, water, and everything in between (later after you get the code running):

<img src="./readme_media/calibration.png" width="300" alt="calibration">

### Set Up Relays For Pumps

You'll need to wire up the relays as shown in the [diagram](#diagram).

<img src="./readme_media/relay_pi_side.png" width="300" alt="relay_pi_side">

- `DC+` may be labeled as `VCC`
- `DC-` may be labeled as `GND`
- `IN` may be labeled as `PIN`

<img src="./readme_media/relay_pump_side.png" width="300" alt="relay_pump_side">

- Use the `NO` and `COM` ports. The NC port will turn the circuit on by default.

### Set Up the Pumps

1. Wire up the power for the pump using batteries or a USB cable. **DO NOT POWER THESE PUMPS DIRECTLY WITH THE PI!!!**

**See the [Video](#video) for tips on working with the tiny leads on the pump.**

<img src="./readme_media/pump.png" width="300" alt="pump">
<img src="./readme_media/pump_wires.png" width="300" alt="pump_wires">
<img src="./readme_media/batteries.png" width="300" alt="pump">

2. Connect pumps to relays. See [pins](#pin-assignments) above for hookup to Pi.

<img src="./readme_media/pump to relay.png" width="300" alt="pump_to_relay">

3. **Ensure your wires are guarded from any contact with the water.**

4. (Optional) Print the Water Tank from the [3D_prints_files](https://github.com/DavidMiles1925/plant_care_assistant/tree/main/3D_print_files) folder at the top of the page.

<img src="./readme_media/water tank.png" width="300" alt="water_tank">

5. (Optional) Print the Plant Pot Hose Clips from the [3D_prints_files](https://github.com/DavidMiles1925/plant_care_assistant/tree/main/3D_print_files) folder at the top of the page.

<img src="./readme_media/clip.png" width="300" alt="hose_clip">

6. Hook your hose up to the pumps, and run them to the pot.

### Set Up the Light

1. The light is powered just like the [pumps](#set-up-the-pumps), in that it needs to be powered by an external power source. **NOT THE PI!**

2. The light connects to a [relay](#set-up-relays-for-pumps) the same way the pumps do.

3. **See the [video](#video) for information about removing the module on the light.**

### Set Up I2C/smbus

1. From the Raspberry Pi terminal, run the following command:

```bash
sudo raspi-config
```

- Select Option 3: Interface Options
- Enable `ARM I2C`

2. Install `smbus`

```bash
sudo apt-get install python3-smbus
```

### Install Git and Code

1. From the Raspberry Pi terminal, run the following command:

```bash
sudo apt-get install git
```

- Make sure to push an uppercase `Y` when you select "yes" to installing.

2. Clone the code to your Pi by entering the following command.

```bash
git clone https://github.com/DavidMiles1925/plant_care_assistant.git
```

### Navigate to the Directory

- After installing your code:

```bash
cd plant_care_assistant
```

### Configuring the Program

Configuration instructions coming soon.

See the video for a detailed walkthrough of the configuration values.

### Run the Program

- Run the program

```bash
sudo python plant.py
```

### Accessing the Logs

- Navigate to `/logs` directory

```bash
cd logs/
```

- Check log names

```bash
ls
```

- Open logs

```bash
sudo nano FILENAME.txt
```

- Basic nano navigation

More detailed info coming soon. Check out the [video](#video) for more details.

### Counting the Log Files

I've added a script called `log_counter.py`.

The purpose of this script is to count the number of times water was dispensed from each sensor, based on the logs in the `logs/` directory.

## Gallery

![Overhed](./readme_media/relay_overhead.png)

![Top View](./readme_media/top_view.jpg)

## Acknowldegements

### Picture of ADS7830

Picture source: (https://www.js4iot.com/2021/06/06/ADC_RPIO.html)

This picture is such a wonderful representation of the ADS7830. Check out the link above, this developer uses JavaScript for his code, something I've never even done with a Pi! So cool.

### Background Music for Intro

Music I use: https://www.bensound.com  
License code: WUITXNB2OK8EGMAO
