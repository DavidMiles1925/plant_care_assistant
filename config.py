##########        Main Control Variables          ##########

NUMBER_OF_ANALOG_INPUTS = 3     # Maximum 3
DURATION_BETWEEN_CHECKS = 1     # seconds
DRY_COUNT_BEFORE_WATERING = 6   # How many times should a "dry" result be returned before the plant is watered?
WATER_IF_DRY = False            # Should the plant(s) be watered if it is dry?


##########      Capacitive Moisture Sensor        ##########

DRY_VALUE = 215
DRY_SOIL_VALUE = 195
MOIST_SOIL_VALUE = 160
WET_SOIL_VALUE = 115
WATER_VALUE = 100


##########      Console Output and Logging        ##########

LOG_DIRECTORY_PATH = "/home/astro/plant_care_assistant/logs"

CONSOLE_OUTPUT_ON = True
LOGGING_ENABLED = True

CLEAR_SCREEN_BEFORE_PRINT = True


##########   ADS7830 Analog-to-Digtal Converter   ##########

# Input Number:  0     1     2     3     4     5     6     7
#---------------------------------------------------------------
ADS_COMMANDS = [0x84, 0xc4, 0x94, 0xd4, 0xa4, 0xe4, 0xb4, 0xf4]


##########             Welcome Message            ##########

LED_ARRAY_WATER_STATUS = [17, 27, 22]
# Future State: RELAY_ARRAY_WATER_STATUS = [17,27,22,...]


##########             Welcome Message            ##########

OPENING_MESSAGE = f"\n******************************************************************\n\nProgram Started\n\nPlant will be watered when dry: {WATER_IF_DRY}\nCheck will be made every {DURATION_BETWEEN_CHECKS} seconds.\n\nCalibration Values:\nDry:\t\t{DRY_VALUE}\nDry Soil:\t{DRY_SOIL_VALUE}\nMoist Soil:\t{MOIST_SOIL_VALUE}\nWet Soil:\t{WET_SOIL_VALUE}\nWater:\t\t{WATER_VALUE}\n\n********************************************"