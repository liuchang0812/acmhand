#-*- encoding:utf-8 -*-
'''
 主文件
'''
__author__ = 'liuchang'

import sae
from rebot import robot

application = sae.create_wsgi_app(robot.wsgi)
