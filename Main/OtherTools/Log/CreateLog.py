#!/usr/bin/env python
# --encoding=utf-8
# Copyright (c) 2018-2022,Zhejiang Uniview Technology Co.,Ltd. All rights reserved.
# ===============================================================#
#           Function:   Create Log                               #
#           Author:     huxiaohua h03965                         #
#           Version:    2020-04-10 16:33                         #
# ===============================================================#
import os
import logging
from logging.handlers import RotatingFileHandler
from Main.__init__ import HOMEPATH


class CreateLog():
    def __init__(self, level='DEBUG'):
        # path = os.getcwd() + "\Log"
        path = HOMEPATH + "\Log"
        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs(path)
        file_path = path + '\ToolLog.log'
        self.logger = logging.getLogger(file_path)
        self.logger.setLevel(level)  # 日志收集器的级别

        # 输出渠道 相对路径
        fh = RotatingFileHandler(file_path, mode='a', maxBytes=5 * 1024 * 1024, backupCount=3, encoding='UTF-8',
                                 delay=False)
        # sh = logging.StreamHandler()

        fh.setLevel(level)  # 输出渠道的级别
        # sh.setLevel(level)

        formatter = logging.Formatter('%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d] : %(message)s')
        fh.setFormatter(formatter)
        # sh.setFormatter(formatter)

        # 对接日志收集器 以及输出渠道
        # logger.addHandler(sh)
        self.logger.addHandler(fh)

    def get_logger(self):
        return self.logger


if __name__ == '__main__':
    log = CreateLog().get_logger()
    log.info('我是好人')
    log.debug('我是好人')
    log.warning('我是好人')
    log.error('我是好人1')
    log.critical('我是好人1')
