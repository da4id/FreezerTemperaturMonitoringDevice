import logController
import boardUtil

sleep = 10

try:
    log = logController.LogController()

    log.readSensorValues()
    log.writeLogToServer()
except:
    print("Error during write Log")

if boardUtil.keepOn():
    print("keep On")
else:
    boardUtil.sleepMinutes(sleep)
