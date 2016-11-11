import time
from common.common_func import *

version ='2'
class url:
    url_66_169 = 'http://182.92.66.169:8080/'+version#测试机
    url_3_98 = 'http://182.92.3.98:8080/'+version #测试机
    url_82_71 = 'http://123.56.82.71:8080/'+version #测试机
    url_sz_222_220 = 'http://120.24.222.220:8080/'+version
    url_qd_40_236='http://115.28.40.236:8080/'+version
    url_hz_120_98='http://121.41.120.98:8080/'+version
    url_dynamic = 'https://apidynamic.beecloud.cn/'+version #动态地址
    url_bj_domain = 'https://apibj.beecloud.cn/'+version  #bj1
    url_sz_domain = 'https://apisz.beecloud.cn/'+version  #bj2
    url_qd_domain = 'https://apiqd.beecloud.cn/'+version  #bj3
    url_hz_domain = 'https://apihz.beecloud.cn/'+version  #bj4
    # url_jj_domain = 'http://192.168.1.106:8080/2'
    url_gao = 'http://192.168.1.112:8080/'+version



    url_list = [url_bj_domain,url_sz_domain,url_qd_domain,url_hz_domain]

class app1():
    app_id="e66e760b-0f78-44bb-a9ae-b22729d51678"
    app_secret="6fb7db77-96ed-46ef-ae10-1118ee564dd3"
    tt = int(time.time())*1000
    sign = common_func.sign_md5(app_id+str(tt)+app_secret)

class app():
    joy_appID='1c3c01cf-43b4-4eed-83f2-62b58f6280e2'
    joy_appSecret='6f306bc2-3331-4bc0-a155-b19e1604c33a'
    joy_testSecret="afa20257-39a4-494c-82c3-3fe0a816377a"
    e66_appID='e66e760b-0f78-44bb-a9ae-b22729d51678'
    e66_appSecret='6fb7db77-96ed-46ef-ae10-1118ee564dd3'
    e66_appTestSecret='a1900cf2-2570-49a3-bfb8-c6e7a1bc1e21'
    c37_appID='c37d661d-7e61-49ea-96a5-68c34e83db3b'
    c37_appSecret='c37d661d-7e61-49ea-96a5-68c34e83db3b'
    qq_appID='f1aaaebd-4019-41a8-8925-0a8206b881f2'
    qq_appSecret='7d9d138f-5576-4e9b-b7f2-c01b54a6466a'
    wx_appID='62706f51-7d90-4383-8031-b6367e86189b'
    wx_appSecret='8d4ca8ff-cf52-4a40-8e65-429ba719a08a'
    beepay_appID='beacfdf5-badd-4a11-9b23-9ef3801732d1'
    beepay_appSecret='17bc2268-9964-4c33-9f7c-37cd561a8c5c'
    mf_appID = '667f64b1-97ca-420f-99de-dbf9f5a603b3'
    mf_appSecret = 'cefbb790-9b90-40dc-a147-7954bfaa9524'
    Yee_WAP_appID = '230b89e6-d7ff-46bb-b0b6-032f8de7c5d0'
    Yee_WAP_appSecret = '191418f6-c0f5-4943-8171-d07bfeff46b0'



class BCPayReqParams:
    def __init__(self):
        # 渠道类型
        self.app_id = None
        self.app_secret = None
        self.app_sign = None
        self.timestamp = None
        self.channel = None

        # 订单总金额
        self.total_fee = None

        # 商户订单号
        self.bill_no = None

        # 订单标题
        self.title = None

        # 附加数据
        self.optional = None

        # 分析数据
        self.analysis = None

        # 同步返回页面
        self.return_url = None

        # 订单失效时间
        self.bill_timeout = None
        self.openid = None
        self.qr_pay_mode = None
        self.bill_timeout = None
        self.bank = None





class BCRefundReqParams:
    def __init__(self):
        self.app_id = None
        self.app_secret = None
        self.app_sign = None
        self.timestamp = None
        # 渠道类型
        self.channel = None
        self.refund_no = None
        self.bill_no = None
        self.refund_fee = None
        self.optional = None
        # 是否为预退款
        self.need_approval = None
        self.refund_account = None


class BCAPP:
    def __init__(self):
        self.app_id = None
        self.app_secret = None
        self.test_secret = None
        self.master_secret = None
        self.is_test_mode = False
        # If you specify a single value for the timeout(seconds), the timeout value will be applied to both
        # the connect and the read timeouts. Specify a tuple if you would like to set the values separately.
        # If the remote server is very slow, you can tell Requests to wait forever for a response,
        # by passing None as a timeout value and then retrieving a cup of coffee.
        self.timeout = None  # (10, 60)


class result:
    def __init__(self):
        self.result_code = None
        self.result_msg = None

class BillsParams:
    def __init__(self):
        self.app_id = None
        self.app_secret = None
        self.app_sign = None
        self.timestamp = None
        self.channel = None

        # 订单总金额
        self.bill_no = None

        # 商户订单号
        self.spay_result = None

        # 订单标题
        self.refund_result = None

        # 附加数据
        self.need_detail = None

        # 分析数据
        self.start_time = None

        # 同步返回页面
        self.end_time = None

        # 订单失效时间
        self.skip = None
        self.limit = None

