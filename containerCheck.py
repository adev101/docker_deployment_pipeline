import os
import subprocess


imageList = subprocess.Popen("docker images", shell=True, stdout=subprocess.PIPE)

print(imageList.stdout)
verison=""

imagename = "abhi2086/test"

containerList = subprocess.Popen("docker ps", shell=True, stdout=subprocess.PIPE)

for line in imageList.stdout:
    line = line.decode('utf-8')

    tempArr=line.split(" ")


    if imagename in line:
        imageId = tempArr[31]

        print("Latest Image Id: " + imageId)

        break



for line in containerList.stdout:
    line = line.decode('utf-8')

    if imageId in line:
        print("Container found running. " )

        tempArr=line.split(" ")
        os.system("docker kill "+ tempArr[0])
