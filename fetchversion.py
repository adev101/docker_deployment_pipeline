import os
import subprocess

imagename = "abhi2086/test"

#var = os.system("docker images")

proc = subprocess.Popen("docker images", shell=True, stdout=subprocess.PIPE)


print(proc.stdout)


for line in proc.stdout:

    line = line.decode('utf-8')

    if imagename in line:
        arr=line.split(" ")

        version = arr[3]

        print(version)


        break
