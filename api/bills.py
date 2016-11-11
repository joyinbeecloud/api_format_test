from common.entity import *
import xlrd,os

fail_count=0
success_count=0
is_Pass=None
test_case = []
#操作excel
data = xlrd.open_workbook("..\\api_format_data.xls")  #上一级文件夹下的文件
all_sheet = data.sheet_names()#文件中所有sheet名
sheet_num = len(all_sheet)
table = data.sheet_by_name('bills')
nrows = table.nrows #行数
ncols = table.ncols #列数
# print('sheet个数%d'%len(all_sheet))
map = ['case_no','app_id','app_secret','app_sign','timestamp','channel','bill_no',
       'spay_result','refund_result','need_detail','start_time','end_time','skip',
       'limit','result_code','result_msg','type','deal_field','test_field']
#记录测试结果
file_name = "E:\python learning\\api_format_test\Result\\bills_result\Bills_result"+str(time.strftime("%Y%m%d%H%M%S",time.localtime(time.time())))+".txt"
fp = open(file_name,'w+')

bills = BillsParams()
for i in range(2,3):
    test_case = table.row_values(i)
    print('case_no:%s'%test_case[map.index('case_no')])
    deal_field = test_case[map.index('deal_field')]
    test_field = test_case[map.index('test_field')]
    type_case = test_case[map.index('type')]
    # print('deal_field::'+deal_field)

    tt = int(time.time())*1000
    s=str(str(test_case[map.index('app_id')]))+str(tt)+str(test_case[map.index('app_secret')])
    sign = common_func.sign_md5(s)
    if deal_field !='':
        if type_case == 'int':
            test_case[map.index(deal_field)]=int(test_case[map.index(deal_field)])
        elif type_case == 'dict':
            test_case[map.index(deal_field)] = eval(test_case[map.index(deal_field)])
        elif type_case == 'str':
            test_case[map.index(deal_field)] = str(test_case[map.index(deal_field)])
        elif type_case == 'float':
            test_case[map.index(deal_field)] = float(test_case[map.index(deal_field)])
        elif type_case == 'list':
            test_case[map.index(deal_field)] =eval(test_case[map.index(deal_field)])
        elif type_case =='True':
            test_case[map.index(deal_field)]=True
        elif type_case =='False':
            test_case[map.index(deal_field)]=False
        elif type_case =='none':
            test_case[map.index(deal_field)]=None

    bills.app_id =test_case[map.index('app_id')]
    bills.app_secret = test_case[map.index('app_secret')]
    if test_field == 'app_sign':
        bills.app_sign = test_case[map.index('app_sign')]
    else:
        bills.app_sign = sign
    if test_field =='timestamp':
        bills.timestamp = test_case[map.index('timestamp')]
    else:
        bills.timestamp = tt
    bills.bill_no = test_case[map.index('bill_no')]
    bills.channel = test_case[map.index('channel')]
    if test_field == 'spay_result':
        bills.spay_result = test_case[map.index('spay_result')]
    else:
        bills.spay_result = None
    if test_field =='refund_result':
        bills.refund_result = test_case[map.index('refund_result')]
    else:
        bills.refund_result = None
    if test_field =='need_detail':
        bills.need_detail = test_case[map.index('need_detail')]
    else:
        bills.need_detail = None
    if test_field !='start_time':
        if test_case[map.index('start_time')] !='':
            bills.start_time = int(test_case[map.index('start_time')])
        else:
            bills.start_time = None
    else:
        bills.start_time = test_case[map.index('start_time')]
    if test_field !='end_time':
        if test_case[map.index('end_time')]!='':
            bills.end_time = int(test_case[map.index('end_time')])
        else:
            bills.end_time =None
    else:
        bills.end_time = test_case[map.index('end_time')]
    if test_field =='skip':
        bills.skip = test_case[map.index('skip')]
    else:
        bills.skip = None
    if test_field =='limit':
        bills.limit = test_case[map.index('limit')]
    else:
        bills.limit == None

    resp = common_func.request_get(url=url.url_dynamic+'/rest/bills',param1=bills)
    # common_func.print_resp(resp)
    print('*******返回值********')
    if type(resp) is dict:
        if resp['result_code']!='' and test_case[map.index('result_code')]!='':
            if int(resp['result_code'])==int(test_case[map.index('result_code')]) and resp['result_msg']==test_case[map.index('result_msg')]:
                is_Pass=True
                success_count=success_count+1
                common_func.print_resp(resp)
            else:
                is_Pass=False
                fail_count += fail_count
                common_func.print_resp(resp)
            common_func.write_txt(fp,is_Pass,test_case[0],int(test_case[map.index('result_code')]),test_case[map.index('result_msg')],resp,success_count,fail_count)
        else:
            common_func.write_txt(fp,'返回的code为空或者excel里的code为空')
    else:
        fp.write("%s 用例执行失败! 返回内容：%s\n"%(test_case[map.index('case_no')],resp))
fp.close()

# if os.path.exists(file_name) and os.path.getsize(file_name)==0:
#     os.remove(file_name)
