#-*-encoding:utf-8-*-
__author__ = 'liuchang'


import werobot
from contests import contest
from werobot.reply import Article , ArticlesReply
from datetime import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


robot = werobot.WeRoBot(token='helloacmer')
last = {}
cont = contest()
lastconteststime = datetime.now()
helpstr = u"搞acm没妹子哟"

@robot.text
def parsetext(message):
    print "text message"
    
    print message.content
    
    msg = str(message.content)
   
    user = str(message.source)
    
    print msg , user
    
    if msg == u"最近比赛" or msg==u"比赛" or msg ==u"contests" :
        if datetime.now().day != lastconteststime.day:
            cont.update()

        reply = ArticlesReply(message=message)
        reply.add_article(
            Article(
            title = "发现最近有不少比赛哟！快去虐菜吧！！点击下面看详细   ps:比赛信息由acmicpc提供" ,
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
    return helpstr

def echo(message):
    return '''
    欢迎关注本公众平台~~~~~\n 将为你每天推送比赛信息，acm,noip等算法竞赛相关新闻 ， 更多功能正在开发\n\n
    回复"比赛" ， 查询最近的比赛信息

    回复"建议" + 你对本主页的建议

    谢谢 。 另外温馨提示： 搞acm找不到妹子哟
    '''