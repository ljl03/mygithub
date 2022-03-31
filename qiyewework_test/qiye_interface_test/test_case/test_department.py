import uuid

import allure
import pytest
from jsonpath import jsonpath

from qiyewework_test.qiye_interface_test.apis.department import Department


@allure.feature("Test Department api")
class TestDepartment:
    def setup_class(self):
        self.depart= Department()

    def get_uuid(self):
        """之前使用时间戳避免重复，现在使用UUID一段保证不重复"""
        return str(uuid.uuid1()).split("-")[0]
    @allure.story('Test get')
    def test_get(self):
        r=self.depart.get()
        assert  r.json().get("errcode")==0

    @allure.story('Test create')
    @pytest.mark.parametrize("name,name_en,parentid,expect1,expect2",
                             [("研发中心ce", "RDGZce", 1, 0, True), ("", "RDGZ", 1, 40058, False)])
    def test_create(self,name,name_en,parentid,expect1,expect2):
        '''创建部门'''
        with allure.step("创建部门"):
            uid=self.get_uuid()
            data = {
                "name": f"{name}_{uid}" if name else "",#参数化，执行第二个用例，当{name}传为空时，确保name值为空
                "name_en": f"{name_en}_{uid}",
                "parentid": parentid
            }
            r = self.depart.create_department(data)
            # # 返回码断言
            assert r.json().get("errcode") == expect1
            # # 获取部门信息列表，并断言
            # lis = self.depart.get().json()
            # # 获取当前新增部门的ID值
            # dpt_id = r.json().get("id")
            # # assert f"研发中心_{uid}" in jsonpath(lis,"$.department.[*].name")
            # # 根据id值拼接jsonpath的匹配表达式
            # expr = f"$.department[?(@.id=={dpt_id})].name"
            # # 获取jsonpath表达式匹配的结果列表
            # li = jsonpath(lis, expr)
            # if li:
            #     # 如果列表存在进行判断
            #     # assert f"研发中心_{uid}" ==jsonpath(lis,expr)[0]
            #     rst = f"{name}_{uid}" == jsonpath(lis, expr)[0]
            #     logger.warning(rst)
            #     assert rst == expect2
            # else:
            #     assert li == expect2

    @allure.story('Test update')
    def test_update(self):
        # 先创建在更新
        uid = self.get_uuid()
        # 组装创建部门的请求json
        data = {
            "name": f"研发中心_{uid}",
            "name_en": f"RDGZ_{uid}",
            "parentid": 1,
        }
        # 调起department封装中的创建部门接口
        r = self.depart.create_department(data)
        # 获取部门ID值
        dpt = r.json().get("id")
        uid = self.get_uuid()
        data={
            "id": dpt,
            "name": f"研发中心_update{uid}",
            "name_en": f"RDGZ_update{uid}",
            "parentid": 1,

        }
        self.depart.update_department(data)
        assert r.json().get("errcode") == 0

    @allure.story('Test delete')
    def test_del(self):
        uid = self.get_uuid()
        # 组装创建部门的请求json
        data = {
            "name": f"研发中心_{uid}",
            "name_en": f"RDGZ_{uid}",
            "parentid": 1,
        }
        # 调起department封装中的创建部门接口
        r = self.depart.create_department(data)
        # 获取部门ID值
        dpt = r.json().get("id")

        self.depart.delete(dpt)
        assert r.json().get("errcode") == 0