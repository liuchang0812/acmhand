#-*- encoding=utf-8 -*-
__author__ = 'liuchang'


import werobot
robot = werobot.WeRoBot(token='helloacmer')

@robot.handler
def echo(message):
    return "hello world!"
