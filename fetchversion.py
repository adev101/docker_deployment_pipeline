import os
import subprocess
import re


imagename = "abhi2086/test"

#var = os.system("docker images")

proc = subprocess.Popen("docker images", shell=True, stdout=subprocess.PIPE)


print(proc.stdout)
verison=""

for line in proc.stdout:

    line = line.decode('utf-8')

    if imagename in line:
        arr=line.split(" ")

        version = arr[3]

        print(version)

        temp = re.compile("([a-zA-Z]+)([0-9]+)")
        res = temp.match(version).groups()

        print(res[0])
        print(res[1])


        version = int(res[1])+1
        version="env.version=\""+res[0]+str(version)+"\""

        file = open('version.groovy', 'w')
        file.write(version)
        file.close()
        break
