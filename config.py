##########        Main Control Variables          ##########

PI_USERNAME = "bulbasuar"       # This is the username you log into your pi with.
NUMBER_OF_ANALOG_INPUTS = 3     # Maximum 3
DURATION_BETWEEN_CHECKS = 1800    # Time in seconds
DRY_COUNT_BEFORE_WATERING = 6   # How many times should a "dry" result be returned before the plant is watered?
WATER_IF_DRY = True             # Should the plant(s) be watered if it is dry?


##########               Lighting                 ##########

LIGHT_RELAY_PIN = 23
LIGHT_START_TIME_ARRAY = ["08:00:00", "10:00:00", "12:00:00", "14:00:00", "16:00:00", "18:00:00"]      # Format must be HH:MM:SS, 24 hr format
LIGHT_DURATION = 900              # Time in seconds
LIGHT_SCRIPT_PATH = f"/home/{PI_USERNAME}/plant_care_assistant/light.py"
LED_ARRAY_WATER_STATUS = [17, 27, 22]


##########      Capacitive Moisture Sensor        ##########

DRY_VALUE = 215
DRY_SOIL_VALUE = 195
MOIST_SOIL_VALUE = 160
WET_SOIL_VALUE = 115
WATER_VALUE = 100


##########               Water Pump              ##########

PUMP_ON_TIME = 1                # Time in seconds
WATER_PUMP_ARRAY = [5, 6, 13]


##########   ADS7830 (Or ADS1115) Analog-to-Digtal Converter   ##########


# Input Number:  0     1     2     3     4     5     6     7
#---------------------------------------------------------------
ADS_COMMANDS = [0x84, 0xc4, 0x94, 0xd4, 0xa4, 0xe4, 0xb4, 0xf4]
ADS_BYTE_ADDRESS = 0x4b

# To use the ADS1115, comment out the above constants, and uncomment the constants below.

ADS_COMMANDS = [0x40, 0x41, 0x42, 0x43]
ADS_BYTE_ADDRESS = 0x01


##########             Welcome Message            ##########

OPENING_MESSAGE = f"\n******************************************************************\n\nMain Program Started\n\nPlant will be watered when dry: {WATER_IF_DRY}\nCheck will be made every {DURATION_BETWEEN_CHECKS} seconds.\n\nCalibration Values:\nDry:\t\t{DRY_VALUE}\nDry Soil:\t{DRY_SOIL_VALUE}\nMoist Soil:\t{MOIST_SOIL_VALUE}\nWet Soil:\t{WET_SOIL_VALUE}\nWater:\t\t{WATER_VALUE}\n\n********************************************"
LIGHT_LOG_MESSAGE = f"\n\nLight Control Subprocess Started\n\nLight relay is using pin {LIGHT_RELAY_PIN}\nLight will turn on at {LIGHT_START_TIME_ARRAY}\nIt will remain on for {LIGHT_DURATION} seconds\n\n********************************************"

##########      Console Output and Logging        ##########

LOG_DIRECTORY_PATH = f"/home/{PI_USERNAME}/plant_care_assistant/logs"

CONSOLE_OUTPUT_ON = True
LOGGING_ENABLED = True

CLEAR_SCREEN_BEFORE_PRINT = True

##########                Reference               ##########

# Seconds in a
#       Hour:   3600
#       Day:    86,400
#       Week:   604,800