#-*- coding:utf-8 -*-
__author__ = 'liuchang'
import urllib
from xml.dom import minidom
class topcode(object):
    def __init__(self):
        self.crurl = "http://community.topcoder.com/tc?module=SimpleSearch&ha=%s"
        self.ratingurl = "http://community.topcoder.com/tc?module=BasicData&c=dd_rating_history&cr=%s"

    def getcr(self, id):
        try:
            url = self.crurl % id
            r = urllib.urlopen(url).geturl()
            return str(r)[str(r).index("&cr=") + 4 : ]
        except :
            return None

    def getrating(self , cr , id):
        if cr == None:
            return u"好像没有这个ID啊，请重新输入一下。 格式： rating id  （ id 为你的id )"
        else:
            dm = minidom.parse( urllib.urlopen( self.ratingurl % cr) )
            n = len(dm.firstChild.childNodes) - 1
            print "n:%d"% n
            if n == -1:
                return u"好像没有这个ID啊，请重新输入一下。 格式： rating id  （ id 为你的id )"
            srmname = dm.firstChild.childNodes[n].childNodes[3].firstChild.data
            oldrating = dm.firstChild.childNodes[n].childNodes[5].firstChild.data
            newrating = dm.firstChild.childNodes[n].childNodes[6].firstChild.data
            rank = dm.firstChild.childNodes[n].childNodes[7].firstChild.data
            #print srmname , oldrating , newrating , rank
            return u"%s 在最近的 %s 比赛中，排行 %s 名，rating由 %s 变为了 %s ! 继续加油！" % ( id , srmname , rank , oldrating , newrating)
        return u"好像没有这个ID啊，请重新输入一下。 格式： rating id  （ id 为你的id )"