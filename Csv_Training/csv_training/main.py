# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   学习CSV文件的常用读写方法
# ------------------------(max to 80 columns)-----------------------------------

import csv
import os
import logging

# 定义了 logger 的名字
app_name = 'main2'
logger = logging.getLogger(app_name)

# 按  时间-文件名-模块名-函数名-行号-信息输出
log_path = os.getcwd() + '\\logs\\' + app_name + '.log'
logging.basicConfig(level=logging.DEBUG,
                    filename=log_path,
                    format='%(asctime)s - %(levelname)s : %(name)s - %(filename)s -%(funcName)s() -No.%(lineno)d - %(message)s')

# Global: Define file name & path
filename = 'test_write.csv'
csv_path = os.getcwd() + '\\csv_files\\' + filename

# Practice 1  - write
# write a row once
header_data = ["行号", "列名1", "列名2"]
row_data = [1, '第1列数据', '第2列数据']  # data of a row
with open(csv_path, "w", encoding='utf8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header_data)
    writer.writerow(row_data)
msg = '输出了一行 CSV 数据'
logger.debug(msg)

# write serval rows by for
header_data = ["行号", "列名1", "列名2"]
repeat_times = 10
with open(csv_path, "w", encoding='utf8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header_data)
    for cnt in range(repeat_times):
        row_data = [cnt, '第1列数据', '第2列数据']  # data of a row
        writer.writerow(row_data)
msg = '输出了 %d 行 CSV 数据' % (repeat_times)
logger.info(msg)

# Practice 2 - read
with open(csv_path, "r", encoding='utf8') as csvfile:
    reader = csv.reader(csvfile)
    cnt = 0
    for line in reader:
        cnt += 1
        print(line)
msg = '读取了 %d 行 CSV 数据' % (cnt)
logger.info(msg)

# Practice 3 - get filed(cell)
with open(csv_path, "r", encoding='utf8') as csvfile:
    reader = csv.reader(csvfile)
    row_cnt = 0
    for line in reader:
        row_cnt += 1
        print('第 %d 行， 行号是 %s, 第一列是 %s, 第二列是 %s' %
              (row_cnt, line[0], line[1], line[2]))
