from pyedo import edo
#mediapipe (for accesing external media on platform fx. access to pc camera)
import mediapipe as mp
#open cv (computervision):
import cv2 as cv
#Robot Operating System:
import roslibpy as ros
#pynput
import pynput as pyn 
#pynput

import time
import math
from pyedo import edo

import unittest

myedo = edo('192.168.12.1')


def StartUp(myedo):
    myedo.init7Axes()
    myedo.disengageStd()
    myedo.moveJoints(-45, -45, 96, 17, 100, -11)


print(StartUp(myedo))