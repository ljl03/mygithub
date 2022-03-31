import threading
import time
import requests

class TestDepartment:
    def setup_class(self):
        corpid = 'wwbadb21313a760479'
        corpsecret = 'aBQDiu09qqvjxao87Mmsi9ljEGWh14mwhmNGRFH5yjY'
        url = f" https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {
            'corpid': corpid,
            'corpsecret': corpsecret
        }

        # 发送get请求，获取access_token
        r = requests.get(url, params=params)
        self.access_token = r.json().get('access_token')

    def test_get_department_list(self):
        '''获取部门列表'''
        dep_url=f'https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.access_token}'
        r=requests.get(dep_url)
        print(r.json())
        assert r.json().get("errcode")==0

    def test_create_department(self):
        '''创建部门'''
        tim = int(time.time())  # 加个时间戳
        url=f'https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.access_token}'
        data={
            "name":f"广州研发中心{tim}",
            "name_en": f"RDGZ{tim}",
            "parentid": 1
        }
        r=requests.post(url,json=data)
        print(r.json())
        assert r.json().get('errcode')==0

    def test_update_department(self):
        '''修改部门'''
        # 确保脚本独立性，修改部门接口需要一个部门ID，那在方法开始就调用创建部门接口产生一个部门ID
        tim = int(time.time())  # 加个时间戳
        r=self.create()
        assert r.json().get('errcode') == 0
        url=f'https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.access_token}'
        data={
            "id": r.json().get('id'),
            "name": f"广州研发中心_update{tim}",
            "name_en": f"RDGZ_update{tim}",
            "parentid": 1,
            "order": 1
        }
        r=requests.post(url,json=data)
        print(r.json())
        assert r.json().get('errcode') == 0
    def test_del_department(self):
        '''删除部门'''
        r = self.create()
        ID=r.json().get('id')
        url=f'https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.access_token}&id={ID}'
        r=requests.get(url)
        print(r.json())
        assert r.json().get('errcode') == 0

    def create(self):
        '''创建部门'''
        url = f'https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.access_token}'
        tim=int(time.time())#加个时间戳
        nam=threading.Thread.__name__#如果是线程跑用例,同一时间执行，可以在加一个nam
        data = {
            "name": f"广州研发中心24{tim}_{nam}",
            "name_en": f"RDGZ24{tim}",
            "parentid": 1
        }
        r = requests.post(url, json=data)
        return r