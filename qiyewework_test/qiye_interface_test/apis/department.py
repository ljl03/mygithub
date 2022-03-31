from qiyewework_test.qiye_interface_test.apis.wework import Wework
from qiyewework_test.qiye_interface_test.utils.file_tools import FileTool


class Department(Wework):
    def __init__(self):
        # 如果实例化部门管理的话，使用此access_token
        # 调用文件的读取方法获取yaml数据
        yaml_data = FileTool.read_yaml("secrets")
        # 从yaml数据中获取所需的corpid，corpsecret
        corpid = yaml_data.get("corpid").get("pacs")
        corpsecret = yaml_data.get("corpsecret").get("department")
        # 调用父类实现的token方法
        self.access_token = self.get_access_token(corpid, corpsecret)

    def create_department(self,data):
        create_url=f'https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.access_token}'
        r=self.send("POST",create_url,tool="requests",json=data)
        return r

    def update_department(self,data):
        update_url=f'https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.access_token}'
        r=self.send("POST",update_url,tool="requests",json=data)
        return r

    def delete(self, dpt_id):
        '''删除部门，dpt_id 删除所需要的部门ID'''
        # 字面量赋值的方式进行url的拼接
        del_url = f'https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.access_token}&id={dpt_id}'
        # 调用send方法，来自baseapi，发起对接口的调用
        r = self.send("GET", del_url, tool="requests")
        return r

    def get(self):
        '''获取部门列表信息'''
        # 字面量赋值的方式进行url的拼接
        dep_url = f'https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.access_token}'
        # 调用send方法，来自baseapi，发起对接口的调用
        r = self.send("GET", dep_url, tool="requests")
        return r