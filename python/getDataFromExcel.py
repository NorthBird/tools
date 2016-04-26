# -*- coding: utf-8
import xlrd
import json


data = xlrd.open_workbook('locshare_group.xlsx')

fw = open('result.txt','a')

for i in range(4):
    sheet = data.sheets()[i]
    rows = sheet.nrows
    cols = sheet.ncols    
    for row in range(1,rows):
        group = dict()
        group['avatar'] = int(sheet.cell(row,0).value)
        group['group_name'] = sheet.cell(row,2).value
        group['group_intro'] = sheet.cell(row,4).value
        group['group_tag'] = i+1
        groupJson = json.dumps(group)
        if group['avatar'] == 40013:
            print group
        fw.write(groupJson+"\n")
