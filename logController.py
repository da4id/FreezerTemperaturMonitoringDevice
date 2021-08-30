import ujson

import boardUtil
import http
import tmp75


class LogController:

    def __init__(self):
        self.TEMP_ERROR_VALUE = -100
        self.boardTemperature = self.TEMP_ERROR_VALUE

    def readSensorValues(self):
        try:
            self.boardTemperature = tmp75.readTemperature(0x48)
        except:
            pass

    def writeLogToServer(self):
        print("write Logdata to server")
        sensor1 = {"dbid": 1, "value": self.boardTemperature}
        sensors = [sensor1]

        data = {"UniqueId": "1234", "Sensors": sensors}

        s = ujson.dumps(data)
        http.http_post(s)
        print(s)
