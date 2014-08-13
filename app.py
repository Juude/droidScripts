#!/usr/bin/env python
import sys, os

def command(cmd):
    print cmd
    os.system(cmd)

def details(args):
    package = args[0]
    command("adb shell am start -a android.settings.APPLICATION_DETAILS_SETTINGS -d package:%s" % package)

def clear(args):
    package = args[0]
    command("adb shell pm clear %s" % package)

def list(args):
    package = args[0]
    command("adb shell pm list package | grep %s " % package)

def editme(args):
    command("vi /home/jdsong/workspace/scripts/app.py")

def dump(args):
    package = args[0]
    command("adb shell dumpsys package %s" % package)

def main():
    action = sys.argv[1]
    args = sys.argv[2:]
    call = "%s(%s)" % (action, args)
    print call
    exec(call)


if __name__ == "__main__":
    main()


