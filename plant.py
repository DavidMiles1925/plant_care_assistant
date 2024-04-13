from smbus import SMBus
from time import sleep
import os

from config import ADS_COMMANDS
from logger import console_and_log

bus = SMBus(1)

def read_sensor(input):
    bus.write_byte(0x4b, ADS_COMMANDS[input])
    return bus.read_byte(0x4b)

def output_sensor_data(value, status):
    console_and_log(f"The value the sensor returned is: {value}\t{status}")

def determine_soil_status(value):
    if value >= 200:
        return ""
    else:
        return ""
    

if __name__ == "__main__":
    try:
        os.system("clear")
        
        while True:
            sensor_value = read_sensor(0)

            soil_status = determine_soil_status(sensor_value)
            
            output_sensor_data(sensor_value, soil_status)

            sleep(1)

    except Exception as e:
        console_and_log(f"An exception was caught in the main function: {e}")

    except KeyboardInterrupt:
        console_and_log(f"The program was terminated using Ctrl+C")