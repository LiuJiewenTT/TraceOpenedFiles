import sys
import time

import psutil
import difflib

divider = '========================================='
subdivider = divider.replace('=', '-')


def TraceOpenedFiles(PID: int):
    print('Start Tracing on PID:[{0}]'.format(PID))
    l = l_prev = []
    p = psutil.Process(PID)
    differ = difflib.Differ()
    while True:
        try:
            l = p.open_files()
        except psutil.NoSuchProcess as e:
            print(e)
            break
        l = [x[0] for x in l]
        difflist = differ.compare(l_prev, l)
        # print(type(difflist))

        newprint = True
        diffcnt = 0
        for item in difflist:
            if item[0] != ' ':
                if newprint:
                    newprint = False
                    print(divider)
                print(item)
                diffcnt += 1

        if newprint is False:
            print(subdivider)
            print('Count of differences: [{}]'.format(diffcnt))
            print(divider)
        l_prev = l
        # time.sleep(0.1)


if __name__ == '__main__':
    pid = None
    filepath = None
    name = None

    if sys.argv.__len__() > 1:
        if '-pid' in sys.argv:
            pid = int(sys.argv[sys.argv.index('-pid')+1])
        if '-file' in sys.argv:
            filepath = sys.argv[sys.argv.index('-file')+1]
        if '-name' in sys.argv:
            name = sys.argv[sys.argv.index('-name') + 1]

    # name = 'IGCC.exe'

    if name is not None:
        while pid is None:
            pids = psutil.pids()
            for i in pids:
                try:
                    p = psutil.Process(i)
                    if p.name() == name:
                        pid = i
                        break
                except psutil.NoSuchProcess as e:
                    pass

    if filepath is None and pid is None and name is None:
        filepath = input('File path: ')
        print('File Path: [{}]'.format(filepath))
        p = psutil.Popen(filepath)
        # p = psutil.o
        pid = p.pid

    # pid = eval(input('PID: '))
    # pid = 20008
    print(pid)
    TraceOpenedFiles(pid)
    pass

