#-*- encoding=utf-8 -*-
'''
    contestes informations provide by acmicpc.info
        http://acmicpc.info
'''
__author__ = 'liuchang'
from urllib import urlopen
import json

class contest(object):
    def __init__(self):
        self.url = 'http://contests.acmicpc.info/contests.json'
        try:
            self.data = json.loads(urlopen(self.url).read())
        except:
            print "init error!"

    def updata(self):
        try:
            self.data = json.loads(urlopen(self.url).read())
        except:
            print "updata error!"

    def __getitem__(self, item):
        return self.data[item]

    def __len__(self):
        return len(self.data)

if __name__ == "__main__":
    ctst =  contest()
    print ctst[0]
    print len(ctst)
