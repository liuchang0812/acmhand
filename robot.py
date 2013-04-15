#-*-encoding:utf-8-*-
__author__ = 'liuchang'


import werobot
from contests import contest
from werobot.reply import Article , ArticlesReply
from datetime import datetime
import sys
from topcoder import topcode
import sae.kvdb
reload(sys)
sys.setdefaultencoding('utf-8')


robot = werobot.WeRoBot(token='helloacmer')
kv = sae.kvdb.KVClient()
cont = contest()
tp = topcode()
lastconteststime = datetime.now()
helpstr = '''欢迎关注本公众平台~~~~~\n 将为你每天推送比赛信息，acm,noip等算法竞赛相关新闻 ， 更多功能正在开发\n\n
    回复"比赛" ， 查询最近的比赛信息 。
    回复"rating id" , 查询该id的topcoder rating 。
    回复"建议" + 你对本主页的建议 。

    谢谢 。
    '''

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
            title=  cont[i]['start_time'] + " \n " + cont[i]['name'] ,
            url=cont[i]['link'] ,
            description= '',
            img = ''
        ))

    return reply

def queryrating(id):
    cr = kv.get("tp"+id)
    print "cr: %s " % cr
    if cr != None:
        return tp.getrating(cr)
    else :
        cr = tp.getcr(id)
        kv.set("tp"+id ,cr)
        return tp.getrating(cr)


@robot.text
def parsetext(message):
    print "text message"
    msg = str(message.content)
    user = str(message.source)
    print kv.get("status"+user)

    print "msg : %s , user : %s" % ( msg , user)
    '''
    if msg == "取消" :
        kv.set("status" + user , "index")
        return helpstr
    '''
    #if kv.get("status" + user) == "index":
    if msg == u"最近比赛" or msg==u"比赛" or msg ==u"contests" :
            return querycontests(message)
    if msg.startswith(u"rating") :
            #last[user] = "topcoder"
            #kv.set("status" + user , "topcoder")
            #return u'''回复topcoder的id , 查询rating ！
            #      回复“取消” ， 退出查rating功能 !
            #        '''
            id = msg[msg.index(' '):].strip()
            print "id: %s" % id
            return queryrating(id)

    return helpstr
    

@robot.handler
def echo(message):
    return helpstr