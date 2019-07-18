# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   学习用 logging 模块
# ------------------------(max to 80 columns)-----------------------------------


import logging

# Phase 1:  基本用法
logging.basicConfig(level=logging.DEBUG,
                    filename='my.log',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

msg = '这是一条只有调试时才输出的日志'
logger.debug(msg)

msg = '证明事情按预期工作，可以输出也可以不输出'
logger.info(msg)

msg = '现在没问题，但将来可能会出现问题...'
logger.warning(msg)

msg = '严重的问题，部分功能已不能执行'
logger.error(msg)

msg = '致命性问题，程序崩溃'
logger.critical(msg)
