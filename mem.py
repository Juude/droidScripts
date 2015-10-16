# -*- encoding:utf-8 -*-
from __future__ import division  # 1.5

import sys
import threading
import subprocess

reload(sys)
sleep_time = 3.0


def is_mac_os():
    return not sys.platform.system().lower().find("windows") >= 0


def inred(s):
    return "%s[31;2m%s%s[0m" % (chr(27), s, chr(27))


def refresh_mem_info(package):
    try:
        cmd = 'adb shell dumpsys meminfo ' + package

        result = subprocess.check_output(cmd, shell=True)
        result = result.strip()
        results = result.split('\r\n')

        native_mem = 0
        java_mem = 0
        for line in results:
            line = line.replace(" ", "|")
            mem_array = line.split("|")
            pd_array = []
            for raw in mem_array:
                raw = raw.replace("|", "")
                if len(raw) > 0:
                    pd_array.append(raw)

            pd_len = len(pd_array)
            if pd_len >= 6 and pd_array[0] == 'Native':
                native_mem = int(pd_array[pd_len - 2])
            if pd_len >= 6 and pd_array[0] == 'Dalvik':
                java_mem = int(pd_array[pd_len - 2])
            if native_mem > 0 and java_mem > 0:
                break

        sys.stdout.write(
            "\r[{0}]   [{1}]   [{2}]".format('native alloc = ' + inred(str(native_mem)),
                                             'java alloc = ' + inred(str(java_mem)),
                                             'all alloc = ' + inred(str(java_mem + native_mem))))
        sys.stdout.flush()

    except Exception, e:
        print e.message
    else:
        pass
    finally:
        start_watcher()


def start_watcher():
    thread = threading.Timer(sleep_time, refresh_mem_info(sys.argv[1:][0]))
    thread.start()


if __name__ == "__main__":
    start_watcher()
