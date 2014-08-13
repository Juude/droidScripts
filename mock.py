#!/usr/bin/env python
import sys, os

def command(cmd):
    print cmd
    os.system(cmd)

def main():
    args = sys.argv[1:]
    cmd = "adb shell am broadcast -a android.mock -e a " + " ".join(args)
    command(cmd)
if __name__ == "__main__":
    main()


