from common.entity import *
from common.common_func import *
import xlrd,os

fail_count=0
success_count=0
is_Pass=None
temp_url=url.url_dynamic+'/rest/refund'
data = xlrd.open_workbook("..\\api_format_data.xls")  #上一级文件夹下的文件
all_sheet = data.sheet_names()#文件中所有sheet名
sheet_num = len(all_sheet)
table = data.sheet_by_name('refund')
nrows = table.nrows #行数
ncols = table.ncols #列数
app_id=app.e66_appID
app_secret=app.e66_appSecret
dat=str(time.strftime("%Y%m%d",time.localtime(time.time())))
refund_no = dat+str(int(time.time()))
optional={"aa":"bb","aa1":"bb1","cc":"{'dd':'dd1'}"}
tt=int(time.time())*1000
colum_map=['case_no','app_id','app_secret','app_sign','timestamp','channel','refund_no','bill_no','refund_fee',
           'optional','need_approval','refund_account','result_code','result_msg','type','deal_field','test_field']

file_name = "E:\\python learning\\api_format_test\\result\\refund_result\\Refund_result"+str(time.strftime("%Y%m%d%H%M%S",time.localtime(time.time())))+".txt"
print(file_name)
fp = open(file_name,'w+')

refund_params = BCRefundReqParams()


for i in range(1,nrows):
    test_case = table.row_values(i)
    print(test_case[0])
    deal_field =test_case[colum_map.index('deal_field')]
    type_case = test_case[colum_map.index('type')]
    test_field = test_case[colum_map.index('test_field')]
    if deal_field !='':
        if type_case == 'int':
            test_case[colum_map.index(deal_field)]=int(test_case[colum_map.index(deal_field)])
        elif type_case == 'dict':
            test_case[colum_map.index(deal_field)] = eval(test_case[colum_map.index(deal_field)])
        elif type_case == 'str':
            test_case[colum_map.index(deal_field)] = str(test_case[colum_map.index(deal_field)])
        elif type_case == 'float':
            test_case[colum_map.index(deal_field)] = float(test_case[colum_map.index(deal_field)])
        elif type_case == 'list':
            test_case[colum_map.index(deal_field)] =eval(test_case[colum_map.index(deal_field)])
        elif type_case =='True':
            test_case[colum_map.index(deal_field)]=True
        elif type_case =='False':
            test_case[colum_map.index(deal_field)]=False
        elif type_case == 'None':
            test_case[colum_map.index(deal_field)]=None
    # 处理total_fee,optional,analysis,bill_timeout 类型问题，此时这四个应该是有效等价类
    if test_case[colum_map.index('refund_fee')] != '' and test_field != 'refund_fee':
        test_case[colum_map.index('refund_fee')] = int(test_case[colum_map.index('refund_fee')])
    if test_case[colum_map.index('optional')] != '' and test_field != 'optional':
        test_case[colum_map.index('optional')] = eval(test_case[colum_map.index('optional')])


    if test_case[colum_map.index('test_field')] !='app_id':
        refund_params.app_id = app_id
    else:
        refund_params.app_id = test_case[colum_map.index('app_id')]
    if test_case[colum_map.index('test_field')] != 'app_secret':
        refund_params.app_secret = app_secret
    else:
        refund_params.app_secret = test_case[colum_map.index('app_secret')]
    if test_case[colum_map.index('test_field')] != 'timestamp':
        refund_params.timestamp = tt
    else:
        refund_params.timestamp = test_case[colum_map.index('timestamp')]
    ss = str(refund_params.app_id) + str(refund_params.timestamp) + str(refund_params.app_secret)
    app_sign = common_func.sign_md5(ss)
    if test_case[colum_map.index('test_field')] !='app_sign':
        refund_params.app_sign = app_sign
    else:
        refund_params.app_sign = test_case[colum_map.index('app_sign')]

    refund_params.channel = test_case[colum_map.index('channel')]
    if test_case[colum_map.index('test_field')] != 'refund_no':
        refund_params.refund_no = refund_no
    else:
        refund_params.refund_no = test_case[colum_map.index('refund_no')]
    refund_params.bill_no = test_case[colum_map.index('bill_no')]
    refund_params.refund_fee = test_case[colum_map.index('refund_fee')]
    if test_case[colum_map.index('test_field')] != 'optional':
        refund_params.optional = optional
    else:
        refund_params.optional = test_case[colum_map.index('optional')]
    if test_case[colum_map.index('test_field')] != 'need_approval':
        refund_params.need_approval = False
    else:
        refund_params.need_approval = test_case[colum_map.index('need_approval')]
    if test_case[colum_map.index('test_field')] !='refund_account':
        refund_params.refund_account = 0
    else:
        refund_params.refund_account = test_case[colum_map.index('refund_account')]

    print('传入参数')
    resp = common_func.request_post(temp_url,refund_params)
    if type(resp) is dict:
        if int(resp['result_code'])==int(test_case[colum_map.index('result_code')]) and resp['result_msg']==test_case[colum_map.index('result_msg')]:
            print('pass')
            is_Pass=True
            success_count=success_count+1
            common_func.print_resp(resp)
        else:
            is_Pass=False
            fail_count = fail_count+1
            common_func.print_resp(resp)
        common_func.write_txt(fp,is_Pass,test_case[0],int(test_case[colum_map.index('result_code')]),test_case[colum_map.index('result_msg')],resp,success_count,fail_count)
    else:
        fp.write("%s 用例执行失败! 返回内容：%s\n"%(test_case[map.index('case_no')],resp))
fp.close()

if os.path.exists(file_name) and os.path.getsize(file_name)==0:
    os.remove(file_name)






