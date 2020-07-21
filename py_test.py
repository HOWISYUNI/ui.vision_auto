import os
import sys
import subprocess
import datetime
import time

def MakeErrlog(path):
    today = datetime.datetime
    # C:\Users\eagle\Desktop\test\log\error
    errorfolder = r'C:\Users\eagle\Desktop\test\log\error\\'
    filename = today.now().strftime('%H-%M-%S %Y-%m-%d')+'.txt'
    writer = open(errorfolder+filename,mode='wt', encoding='utf-8')
    reader = open(path,'r')
    writer.write('[error log]\n')

    while True:
        line = reader.readline()
        if not line: break
        if line.find('error') is not -1:
            writer.write(line+'\n')
    writer.close()
    


def PlayAndWait(macro, path_downloaddir, path_autorun_html, path_browser,var1 = '-', var2 = '-', var3 = '-'):
    assert os.path.exists(path_downloaddir)
    assert os.path.exists(path_autorun_html)
    assert os.path.exists(path_browser)

    today = datetime.datetime
    log = 'log_' + today.now().strftime('%H-%M-%S %Y-%m-%d') + '.txt'
    pathlog = os.path.join(path_downloaddir, log)

    args = r'file:///' + path_autorun_html + '?macro=' + macro + '&cmd_var1=' + var1 + '&cmd_var2=' + var2 + '&direct=1&savelog=' + log

    proc = subprocess.Popen([path_browser, args])
    print(pathlog)

    while not os.path.exists(pathlog):
        print('macro is working......')
        time.sleep(1)

    if os.path.exists(pathlog):
        print('[log file]' + pathlog)
        status = 0
    else:
        print('macro exits with an error')
        status = 1
        proc.kill()

    print('[EXIT]'+today.now().strftime('%H-%M-%S %Y-%m-%d'))
    MakeErrlog(pathlog)
    sys.exit(status)


if __name__ == '__main__':
    PlayAndWait('test', path_downloaddir = r'C:\Users\eagle\Downloads\\', path_autorun_html = r'C:\Users\eagle\Desktop\test\ui.vision.html', path_browser=r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')

    