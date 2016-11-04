from common.entity import *
import xlrd,os

data = xlrd.open_workbook("..\\api_format_data.xls")  #上一级文件夹下的文件
all_sheet = data.sheet_names()#文件中所有sheet名
sheet_num = len(all_sheet)
table = data.sheet_by_name('bills')
nrows = table.nrows #行数
ncols = table.ncols #列数

colum_map=['case_no','app_id','app_secret','app_sign','timestamp','channel','refund_no','bill_no','refund_fee',
           'optional','need_approval','result_code','result_msg','type','deal_field','test_field']

file_name = "E:\python learning\\api_format_test\Result\\bills result\\refund result"+str(time.strftime("%Y%m%d%H%M%S",time.localtime(time.time())))+".txt"
fp = open(file_name,'w+')

bills = BCRefundReqParams()



