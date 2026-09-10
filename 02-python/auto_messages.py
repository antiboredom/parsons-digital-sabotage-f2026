import time
from subprocess import run

lines = open("./thetrial.txt").readlines()

number = "+15555555555"

for line in lines:
    line = line.strip()
    if line == "":
        continue
    message = line.replace("\\", "\\\\").replace('"', '\\"')
    command = f'tell application "Messages" to send "{message}" to buddy "{number}"'
    run(["osascript", "-e", command])
    time.sleep(1)
