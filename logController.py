import ujson

import boardUtil
import config
import http
import tmp75


class LogController:

    def __init__(self):
        self.data = {"UniqueId": config.uniqueId, "Sensors": []}
        self.errorValue = -100

    def readSensorValues(self):

        for sensor in self.data["Sensors"]:
            try:
                sensor["value"] = tmp75.readTemperature(int(sensor["i2cAdr"], 16))
            except:
                sensor["value"] = self.errorValue
                pass
        print(self.data)
        self.data["Sensors"] = list(filter(lambda a: a["value"] != self.errorValue, self.data["Sensors"]))
        print(self.data)

    def writeLogToServer(self):
        print("write Logdata to server")
        s = ujson.dumps(self.data)
        http.http_post(config.baseurl + "/submit.php", s)
        print(s)

    def readSensorInfosFromServer(self):
        print("Read Sensor Infos from Server")
        s = http.http_get(config.baseurl + "/sensors.php?id=" + config.uniqueId)
        self.data = ujson.loads(s)
        return
