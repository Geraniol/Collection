import os
import time

os.system("sudo apachectl start")
print(time.strftime("\033c%Y/%m/%d %H:%M:%S UTC%z: Service Started."))

os.system("sudo apachectl restart")
print(time.strftime("%Y/%m/%d %H:%M:%S UTC%z: Service Restarted."))

# "/Library/WebServer/Documents"
