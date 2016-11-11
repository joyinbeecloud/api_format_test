import requests,urllib,json,hashlib
import xlrd

class common_func:
    def __init__(self):
        self.bcapp = None
    def registerApp(self,bcapp):
        self.bcapp = bcapp
    def request_post(url,param):
        print(url)
        if type(param) is not dict:
            req_param = {k: v for (k, v) in param.__dict__.items() if v is not None}
        else:
            req_param = param
        common_func.print_resp(req_param)
        print('返回内容')
        jdata = json.dumps(req_param)
        # print(jdata)
        #r1 = requests.get('http://en.wikipedia.org/wiki/Monty_Python')
        try:
            r=requests.post(url,json=req_param,timeout=30)
            #print(r.status_code)
        except requests.exceptions.HTTPError:
            return "httperror"
        print(r.status_code)
        if r.status_code==200:
             # print('common function200')
             resp=r.json()
             return resp
        else:
            # print('common_func'+str(r.status_code))
            r=r.json()
            return r
            # return r.status_code
    def request_get(url,param1):
        if type(param1) is not dict:
            get_req_param = {k: v for (k, v) in param1.__dict__.items() if v is not None}
        else:
            get_req_param = param1

        param2=json.dumps(get_req_param)
        param=urllib.parse.quote_plus(param2)
        url=url+'?para='+param
        print(url)
        common_func.print_resp(get_req_param)
        resp_get = requests.get(url)
        if resp_get.status_code==200:
            resp = resp_get.json()
            return resp
        else:
            return resp_get


    def request_put(url,param):
        jdata = json.dumps(param)
        r = requests.put(url, json=param)

    def sign_md5(str):
        m=hashlib.md5()
        m.update(str.encode('utf-8'))
        get_md5= m.hexdigest()
        return get_md5

    def print_resp(resp):
        dict={'name':'python','english':33,'math':35}
        l=[]
        if type(l) is type(resp):
            for r in resp:
                if type(r) is type(dict):
                    for i in r:
                        #print("%s："%i,resp[i])
                        #if i=='html':
                        print("%s:%s"%(i,r[i]))
                else:
                    print(resp)
        else:
            if type(resp) is type(dict):
                    for i in resp:
                        #print("%s："%i,resp[i])
                        #if i=='html':
                        print("%s:%s"%(i,resp[i]))
            else:
                print(resp)

    def url_encode(paramm):
        param1=paramm
        param2=json.dumps(param1)
        param=urllib.parse.quote_plus(param2)
        return param

    def dealwith_excel(self):
        # file_name = "E:\python learning\\api-test\Result\Result"+str(int(time.time()))+".txt"
        # fp = open(file_name,'w+')#打开或者新建txt文件

        data = xlrd.open_workbook("REST_API.xls")
        all_sheet=data.sheet_names()#文件中所有sheet名
        table = data.sheet_by_name('bill')
        nrows = table.nrows#行数
        ncols = table.ncols#列数

    def obj_to_dict(obj):
        return {k: v for (k, v) in obj.__dict__.items() if v is not None}


    def write_txt(fp,is_pass,case_no,result_code,result_msg,resp,success_account,fail_account):
        d={}
        if is_pass:
            fp.write("%s 用例执行通过! \n"%case_no)
        else:
            fp.write("%s 用例执行失败! \n"%case_no)

        fp.write("预期结果：\nresult_code:%d result_msg:%s"%(result_code,result_msg))
        if type(resp) is not type(d):
            fp.write("\n实际结果: %s\n"%resp)
        else:
            fp.write("\n实际结果: result_code:%d result_msg:%s\n"%(resp['result_code'],resp['result_msg']))
        fp.write("\n通过用例个数%r"%success_account)
        fp.write("\n失败用例个数%r"%fail_account)



