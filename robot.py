#-*-encoding:utf-8-*-
__author__ = 'liuchang'


import werobot
from contests import contest
from werobot.reply import Article , ArticlesReply
from datetime import datetime
import sys
from topcoder import topcode
from codeforces import codeforces
try:
    import sae.kvdb
except ImportError:
    pass
reload(sys)
sys.setdefaultencoding('utf-8')


robot = werobot.WeRoBot(token='helloacmer')
kv = sae.kvdb.KVClient()
cont = contest()
tp = topcode()
lastconteststime = datetime.now()
hellostr = '''欢迎关注本公众平台~~~~~\n 将为你每天推送比赛信 ， 更多功能正在开发\n\n
    回复 "比赛"  ， 查询最近的比赛信息 。
    回复 "cf id" ,  查询该id的tc rating 。
    回复 "tc id" ,  查询该id的cf rating 。
    
    谢谢 。
    '''
helpstr = '''回复"比赛"或者"bs","contests",查询最近的比赛信息 。
回复"cf id" ,  查询该id的tc rating 。
回复"tc id" ,  查询该id的cf rating 。
    
    谢谢 。
    '''
cf = codeforces()
def querycontests(message):
    if datetime.now().day != lastconteststime.day:
        cont.update()

    reply = ArticlesReply(message=message)
    reply.add_article(
        Article(
            title = "发现最近有不少比赛哟！快去虐菜吧！！点击下面看详细" ,
            img = "https://raw.github.com/Liuchang0812/acmhand/master/acmhand/img/acmlogo.jpg" ,
            url = " http://acmicpc.info",
            description= ''
        )
    )
    for i in range(min(7,len(cont))):
        reply.add_article(Article(
            title=  cont[i]['start_time'] +' '  + cont[i]['oj'] + ' ' + cont[i]['access'] + " \n " + cont[i]['name'] ,
            url=cont[i]['link'] ,
            description= '',
            img = ''
        ))
    reply.add_article(Article(
        title = "查看所有比赛信息" ,
        url = "http://3.wechatforwuluo.sinaapp.com/contests" ,
        description='' ,
        img=''
    ))
    return reply

def queryrating(id):
    cr = kv.get("tp"+id)
    print "cr: %s " % cr
    if cr != None:
        return tp.getrating(cr,id)
    else :
        cr = tp.getcr(id)
        if (cr == None):
            return u"好像没有这个ID啊，请重新输入一下。 格式：tc id  （ id 为你的tc id )"
        else:
            kv.set("tp"+id ,cr)
            return tp.getrating(cr,id)


def queryRegion(message):
    status = 1
    res = ""
    if message in [u'xian', u'西安', u'西安赛区'] :
        res = u"西安赛区现场赛于2014年10月26日9:00~14:00在西北工业大学举办，比赛的排行榜地址是：<a href=\"http://board.acmicpc.info/icpc2014/nwpu_onsite.php\">欢迎访问</a>"
    elif message in [u'guangzhou', u'广州', u'广州赛区']:
        res = u"广州赛区现场赛于2014年11月23日9:00~14:00在华南理工大学举办，比赛的排行榜地址是：<a href=\"http://board.acmicpc.info/icpc2014/scut_onsite.php\">欢迎访问</a>"
    elif message in [u'beijing', u'北京', u'北京赛区']:
        res = u"北安赛区现场赛于2014年11月16日9:00~14:00在北京师范大学举办，比赛的排行榜地址是：<a href=\"http://board.acmicpc.info/icpc2014/bnu_onsite.php\">欢迎访问</a>"
    elif message in [u'shanghai', u'上海', u'上海赛区']:
        res = u"上海赛区现场赛于2014年12月06日9:00~14:00在上海大学举办，比赛的排行榜地址是：<a href=\"http://board.acmicpc.info/icpc2014/shu_onsite.php\">欢迎访问</a>"
    else:
        status = 0
        res = ""
    return status, res


@robot.text
def parsetext(message):
    try:
        print "text message"
        msg = str(message.content)
        user = str(message.source)
  
        print "msg : %s , user : %s" % ( msg , user)
      
        if msg == u"bs" or msg==u"比赛" or msg ==u"contests" :
                return querycontests(message)
        if msg.startswith(u"tc") :
                id = msg[msg.index(' '):].strip()
                print "id: %s" % id
                return queryrating(id)
        if msg.startswith(u"cf") :
                id = msg[msg.index(' '):].strip()
                print "id: %s" % id
                return cf.getrating(id)
        status, res =  queryRegion(msg)    
        if status == 1:
            return res
        return helpstr
    except :
        return "服务器好像出问题了，过一会儿再试一下吧"

@robot.handler
def echo(message):
    return hellostr

if __name__ == "__main__":
    print queryRegion("xian")
    print queryRegion("shanghai")
    print queryRegion("beijing")
    print queryRegion("广州")
    print queryRegion("现场赛")
