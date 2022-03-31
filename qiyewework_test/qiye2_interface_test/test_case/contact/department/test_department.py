import os

import allure
import pytest

from qiyewework_test.qiye2_interface_test.api.department import Department
from qiyewework_test.qiye2_interface_test.common.get_log import log


class TestDepartment():
    depart=Department()
    # 获取参数化的数据
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    base_path = os.path.dirname(base_path)
    para_path = os.path.join(base_path, "data/department/para_department.yml")
    para_data = depart.load_yaml("data/department/para_department.yml")

    get_data = para_data["get"]["data"]
    get_ids = para_data["get"]["ids"]

    add_data = para_data["add"]["data"]
    add_ids = para_data["add"]["ids"]

    delete_data = para_data["delete"]["data"]
    delete_ids = para_data["delete"]["ids"]

    edit_data = para_data["edit"]["data"]
    edit_ids = para_data["edit"]["ids"]

    @pytest.mark.parametrize(("id,errcode,errmsg"), get_data, ids=get_ids)
    def test_get_depart(self,id,errcode,errmsg):
        r=self.depart.get_depart(id)
        assert r.get("errcode")==errcode
        assert errmsg in r.get("errmsg")

    @pytest.mark.parametrize('parentid,name,errcode,errmsg',add_data,ids=add_ids)
    def test_add_depart(self,parentid,name,errcode,errmsg):
        r=self.depart.create_depart(parentid,name)
        assert r["errcode"] == errcode
        assert errmsg in r["errmsg"]

    @pytest.mark.parametrize('id,errcode,errmsg',delete_data,ids=delete_ids)
    def test_del_depart(self,id,errcode,errmsg):
        r=self.depart.del_depart(id)
        assert r["errcode"] == errcode
        assert errmsg in r["errmsg"]

    @pytest.mark.parametrize(("id,name,errcode,errmsg"), edit_data, ids=edit_ids)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_edit_depart(self, id, name, errcode, errmsg):
        log.info("-------------开始编辑部门测试---------")
        res = self.depart.edit_depart( id, name)
        log.info("-------------测试结束---------")
        assert res["errcode"] == errcode
        assert errmsg in res["errmsg"]

