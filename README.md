# cooler
This project controls a closed source smart plug using google assistant
API by using temperature sensor.

Prequisites:
1. Python
2. Flask
3. Google Assistant SDK Python Samples:
https://github.com/googlesamples/assistant-sdk-python
4. Raspberry Pi (also using as temperature sensor)
5. DS18B20 Temperature Sensor Module (Currently not using)


**Change Log:**

**2021-04-27**
*README.md: Added description about the project

*textinput.py: Added email notification when credential expires

*cooler.sh:
After system clock unsynchronized, time is fixed at every
startup to avoid inconsistent time reeading by the main program

*cooler.c:
Removed hardcoding of temperature and saving into file.
Addition of changing temperature via web app.

*cooler.py:
Added as new Flask web app
Takes temperature from web browser and saves to file.

**2021-04-19**
Initial Release
