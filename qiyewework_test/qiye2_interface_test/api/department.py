from qiyewework_test.qiye2_interface_test.api.base_api import BaseApi
from qiyewework_test.qiye2_interface_test.api.wework import Wework
from qiyewework_test.qiye2_interface_test.common.config import cf


class Department(Wework):
    def __init__(self):
        corpid = cf.get_key("wwork", "corp_id")
        corpsecret = cf.get_key("wwork", "contact_secret")
        self.token=self.get_token(corpid, corpsecret)

    def get_depart(self,id):
        # Template模板二次修改的值，p_data
        p_data = {"ip": self.ip, "token":self.token, "id": id}
        res = self.send_api_data("data/department/department_api.yml", p_data, "get")
        return res

    def create_depart(self,parentid,name):
        p_data = {"ip": self.ip, "token": self.token, "name":name,"parentid": parentid}
        res = self.send_api_data("data/department/department_api.yml", p_data, "add")
        return res

    def del_depart(self,id):
        p_data = {"ip": self.ip, "token": self.token, "id": id}
        res = self.send_api_data("data/department/department_api.yml", p_data, "delete")
        return res

    def edit_depart(self,id,name):
        p_data = {"ip": self.ip, "token": self.token, "name":name,"id": id}
        res = self.send_api_data("data/department/department_api.yml", p_data, "edit")
        return res
if __name__ == "__main__":
    a = Department()
    print(a.get_depart(1))
