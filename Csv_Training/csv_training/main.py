# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   模拟一个发牌机器和一个发牌员的场景
#   Ver 3.0
# ------------------------(max to 80 columns)-----------------------------------

import csv
import os

# Global: Define file name & path
filename = 'test_write.csv'
out_path = os.getcwd() + '\\csv_files\\' + filename

# Practice 1  - write
# write a row once
header_data = ["行号", "列名1", "列名2"]
row_data = [1, '第1列数据', '第2列数据']  # data of a row
with open(out_path, "w", encoding='utf8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header_data)
    writer.writerow(row_data)


# write serval rows by for
header_data = ["行号", "列名1", "列名2"]
row_data = [1, '第1列数据', '第2列数据']  # data of a row
with open(out_path, "w", encoding='utf8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header_data)
    for cnt in range(10):
        writer.writerow(row_data)

# Practice 2 - read
with open(out_path, "r", encoding='utf8') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        print(line)

# Practice 3 - get filed(cell)
with open(out_path, "r", encoding='utf8') as csvfile:
    reader = csv.reader(csvfile)
    row_cnt = 0
    for line in reader:
        row_cnt += 1
        print('第 %d 行， 第一列是 %s, 第二列是 %s' % (row_cnt,line[1],line[2]))
