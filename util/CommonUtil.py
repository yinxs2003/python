# -*- coding: utf-8 -*-
# !/usr/bin/python

import __init__
import sys
import os
import ConfigParser
import time
import root_path
import datetime
import demjson


def getLogger(module_name):
    import logging
    # from logging.handlers import TimedRotatingFileHandler
    # print(module_name)
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='app_log.log',
                        filemode='a')

    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    console.setFormatter(formatter)
    mylog = logging.getLogger(module_name)
    mylog.addHandler(console)

    return mylog


# 读取conf下的所有配置文件
def get_config_parser():
    path = root_path.get_project_path() + os.sep + 'conf' + os.sep
    conf = ConfigParser.ConfigParser()
    files = []
    for f in os.listdir(path):
        files.append(path + os.sep + f)
    conf.read(files)
    return conf


config_parser = get_config_parser()


def get_dict(section):
    assert len(section) > 0
    tmp_dict = {}
    for obj in config_parser.items(section):
        tmp_dict.setdefault(obj[0], obj[1])
    return tmp_dict


def get_key_list(section):
    assert len(section) > 0
    key_list = []
    for obj in config_parser.items(section):
        key_list.append(obj[0])
    return key_list


def get_value_list(section):
    assert len(section) > 0
    obj_list = []
    for obj in config_parser.items(section):
        obj_list.append(obj[1])
    return obj_list


def get_int(section, key):
    return config_parser.getint(section, key)


def get_string(section, key):
    return config_parser.get(section, key)


def get_seconds():
    return str(int(time.time()))


def get_local_time():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


# 将string转换为dict类型
def unicode2dict(unicode_dict):
    return demjson.decode(unicode_dict)


logger = getLogger(__name__)
# if __name__ == "__main__":
# logger.debug('test get_seconds() ' + get_seconds())
# logger.debug('test get_string() ' + get_string('weixin', 'appID'))
# logger.debug('test get_string() ' + get_string('weixin', 'appSecret'))
# logger.debug(get_key_list('account'))
# logger.debug(get_value_list('account'))
