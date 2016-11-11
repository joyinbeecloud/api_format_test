# from common.common_func import *
from common.entity import *
import xlrd
import uuid
import os

fail_count = 0
success_count = 0
is_Pass = None
test_case = []
data = xlrd.open_workbook("..\\api_format_data.xls")  #上一级文件夹下的文件
all_sheet = data.sheet_names()#文件中所有sheet名
sheet_num = len(all_sheet)
table = data.sheet_by_name('bill')
nrows = table.nrows #行数
ncols = table.ncols #列数
# print('sheet个数%d'%len(all_sheet))
bill_no = str(uuid.uuid1()).replace('-','')

map = ['case_no','app_id','app_secret','app_sign','timestamp','channel','title',
       'total_fee','bill_no','optional','return_url','open_id','qr_pay_mode',
       'bill_timeout','analysis','result_code','result_msg','type','deal_field',
       'test_field','bank','card_no']
test_field_list = ['total_fee','optinal','analysis','bill_timeout']
pay_para = BCPayReqParams()
file_name = "E:\python learning\\api_format_test\Result\\bill_result\Bill_result"+str(time.strftime("%Y%m%d%H%M%S",time.localtime(time.time())))+".txt"
fp = open(file_name,'w+')

for i in range(101,102):
    test_case = table.row_values(i)
    deal_field = test_case[18]
    print('deal_field::'+deal_field)
    type_case = test_case[17]
    test_field = test_case[19]
    # print(test_case[map.index(deal_field)])
#这是测试的参数不同类型的转换
    if deal_field !='':
        if type_case == 'int':
            test_case[map.index(deal_field)]=int(test_case[map.index(deal_field)])
        elif type_case == 'dict':
            test_case[map.index(test_field)] = eval(test_case[map.index(test_field)])
        elif type_case == 'str':
            test_case[map.index(test_field)] = str(test_case[map.index(test_field)])
        elif type_case == 'float':
            test_case[map.index(test_field)] = float(test_case[map.index(test_field)])
        elif type_case == 'list':
            test_case[map.index(test_field)] =eval(test_case[map.index(test_field)])
        elif type_case =='True':
            test_case[map.index(test_field)]=True
        elif type_case =='False':
            test_case[map.index(test_field)]=False


#处理total_fee,optional,analysis,bill_timeout 类型问题，此时这四个应该是有效等价类
    if test_case[map.index('total_fee')] != '' and test_field != 'total_fee':
        test_case[map.index('total_fee')] = int(test_case[map.index('total_fee')])
    if test_case[map.index('optional')] != '' and test_field != 'optional':
        test_case[map.index('optional')] = eval(test_case[map.index('optional')])
    if test_case[map.index('analysis')] != '' and test_field != 'analysis':
        test_case[map.index('analysis')] = eval(test_case[map.index('analysis')])
    if test_case[map.index('bill_timeout')] != '' and test_field != 'bill_timeout':
        test_case[map.index('bill_timeout')] = int(test_case[map.index('bill_timeout')])


    tt = int(time.time())*1000
    if type_case =='none':
        test_case[map.index(deal_field)] = None
    pay_para.app_id=test_case[1]
    if test_field == 'timestamp':
        pay_para.timestamp = test_case[map.index('timestamp')]
    else:
        pay_para.timestamp = tt
    # BCPayReqParams.app_secret = test_case[1]
    s=str(str(test_case[1]))+str(tt)+str(test_case[2])
    sign = common_func.sign_md5(s)
    # pay_para.app_sign = sign
    if test_field == 'app_sign':
        pay_para.app_sign = test_case[map.index('app_sign')]
    else:
        pay_para.app_sign = sign
    # pay_para.timestamp = tt
    # test_case[6] = '0.0'
    if test_field != 'channel':
        pay_para.channel = test_case[5].strip()
    else:
        pay_para.channel = test_case[5]
    pay_para.title = test_case[6]
    # print('title'+test_case[6])
    pay_para.total_fee = test_case[7]
    if test_field !='bill_no':
        bill_no = str(uuid.uuid1()).replace('-','')
        pay_para.bill_no = bill_no
    else:
        pay_para.bill_no = test_case[8]
    pay_para.optional = test_case[9]
    pay_para.return_url = test_case[10]
    pay_para.openid = test_case[11]   #WX_JSAPI必填
    # pay_para.qr_pay_mode = test_case[12]   #ALI_WEB必填
    if test_case[13]=='':
        pay_para.bill_timeout = None
    else:
        pay_para.bill_timeout = test_case[13]
    if test_case[14]=='':
        pay_para.analysis = None
    else:
        pay_para.analysis = test_case[14]
    pay_para.bank = test_case[map.index('bank')]

    # jdata = {k: v for (k, v) in pay_para.__dict__.items() if v is not None}
    # common_func.print_resp(jdata)
    # print(jdata)
    print('传入参数')
    print('case_no:'+test_case[0])
    resp = common_func.request_post(url.url_dynamic+'/rest/bill',pay_para)
    if type(resp) is dict:
        if int(resp['result_code'])==int(test_case[15]) and resp['result_msg']==test_case[16]:
            print('pass')
            is_Pass = True
            success_count = success_count+1
            common_func.print_resp(resp)
        else:
            is_Pass = False
            fail_count = fail_count+1
            common_func.print_resp(resp)
        common_func.write_txt(fp,is_Pass,test_case[0],int(test_case[15]),test_case[16],resp,success_count,fail_count)
    else:
        fp.write("%s 用例执行失败! 返回内容：%s\n"%(test_case[map.index('case_no')],resp))
fp.close()

if os.path.exists(file_name) and os.path.getsize(file_name)==0:
    os.remove(file_name)

    # common_func.print_resp(resp['result_code'])