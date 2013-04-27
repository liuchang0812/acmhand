# -*- encoding:utf-8 -*-
from urllib import urlopen
import re
import json
class codeforces(object):
    def __init__(self):
        self.url = 'http://codeforces.com/profile/%s'

    def getrating(self , id ):
        profileurl = self.url % id
        print profileurl
        r = urlopen(profileurl)
        if r.geturl() == profileurl :
            rep = r.read()
            #print rep
            st = rep.index("data.push(")
            st = st + 10
            ed = rep.index(");" , st)
            s = rep[st:ed]
            #print s
            js = json.loads(s)
            print js[len(js) - 1]
            contest_name = js[len(js) - 1][3]
            rating = js[len(js) - 1][1]
            rank = js[len(js) - 1 ][6]
            change = js[len(js) -1 ][5]
            print contest_name , rating , rank , change
            if  int(change) > 0 :
                return u"%s 在最近的 %s 比赛中，排名 %s ，rating 变为 %s , 涨了 %s 点。Orz神牛啊~"%( id , contest_name , rank , rating , change)
            else:
                change = -int(change)
                return u"%s 在最近的 %s 比赛中，排名 %s , rating 变为 %s , 跌了 %d 点。继续加油吧~"%( id , contest_name , rank , rating , change)
        return " 好想没有这个ID，请重新输入 "

if __name__ == "__main__":

    cd = codeforces()
    print   cd.getrating('chang.mei')
            
            
        
