from datetime import datetime
import os
import sys
import time
import commands

yaka_dir = 'yakayaka'


def make_yaka():
    os.system('mkdir -p ' + yaka_dir )
    os.system('cp yakayaka.png ' + yaka_dir + '/')


def fork():
    if os.fork():
        sys.exit()


def throw_away_io():
    stdin = open(os.devnull, 'rb')
    stdout = open(os.devnull, 'ab+')
    stderr = open(os.devnull, 'ab+', 0)

    for (null_io, std_io) in zip((stdin, stdout, stderr),(sys.stdin, sys.stdout, sys.stderr)):
        os.dup2(null_io.fileno(), std_io.fileno())


def daemonize():
    fork()
    os.setsid()
    #fork()
    #throw_away_io()


def log_yaka():
    #filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)),'yaka/yakayaka.log')
    filepath = (yaka_dir + '/yakayaka.log')
    now = datetime.now().strftime('%Y/%m/%d. %H:%M:%S')

    with open(filepath, 'w') as f:
        f.write(now + ' -> ' + str(os.getpid()))


def cp_yaka(num):
    os.system('cp yakayaka.png ' + yaka_dir + '/yakayaka' + str(num) + '.png ')


def crazy_yaka(interval=2):
    log_yaka()
    count = 0

    while True:
        count += 1
        cp_yaka(count)
        time.sleep(interval)



if __name__ == '__main__':
    make_yaka()
    daemonize()
    crazy_yaka()

