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

    def getrating(self , cr):
        if cr == None:
            return -1
        else:
            dm = minidom.parse( urllib.urlopen( self.ratingurl % cr) )
            srmname = dm.firstChild.childNodes[0].childNodes[3].firstChild.data
            oldrating = dm.firstChild.childNodes[0].childNodes[5].firstChild.data
            newrating = dm.firstChild.childNodes[0].childNodes[6].firstChild.data
            rank = dm.firstChild.childNodes[0].childNodes[7].firstChild.data
            print srmname , oldrating , newrating , rank
            return u"你在最近的%s比赛中，排行%s名，rating由%s变为了%s! 继续加油！" % ( srmname , rank , oldrating , newrating)
        return 0


if __name__ == "__main__":
    tp = topcode()
    print tp.getrating("22873410")