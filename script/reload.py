import os, time, importlib

import sys

name = lambda n=0: sys._getframe(n + 1).f_code.co_name


oldtime = 0

path = "script/hotreload.py"


def autoReload(function, args, solan=1):
    global oldtime
    global functionRun
    n = 0
    function_string = "script.hotreload." + function
    mod_name, func_name = function_string.rsplit(".", 1)
    loaded = False
    while True:
        try:
            if os.path.isfile(path):
                timemodify = os.path.getmtime(path)
                if timemodify != oldtime:
                    oldtime = timemodify
                    if not loaded:
                        mod = importlib.import_module(mod_name)
                        loaded = True
                    else:
                        importlib.reload(mod)
                    functionRun = getattr(mod, func_name)
                functionRun(args)
        except Exception as e:
            print(e)
        n = n + 1
        if n >= solan:
            return
        time.sleep(1)
