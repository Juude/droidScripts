#!/usr/bin/env python
import sys,os
args = sys.argv
if(len(args) < 2):
    action = "fatal"
else:
    action = args[1]
print "action : ", action
if action == "fatal":
    os.system("adb logcat -s AndroidRuntime:*")
