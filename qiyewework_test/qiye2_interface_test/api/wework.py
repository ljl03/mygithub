from qiyewework_test.qiye2_interface_test.api.base_api import BaseApi
from qiyewework_test.qiye2_interface_test.common.config import cf


class Wework(BaseApi):
    """
        获取企业微信的access_token，后续应该得写在BaseApi的父类，这个类没啥必要了

        CORP_ID:企业微信的企业id
    """

    def get_token(self,corp_id,corpsecret):
        data={
            "method": "GET",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": f"corpid={corp_id}&corpsecret={corpsecret}"
        }
        res=self.send_api(data)
        self.token=res.get("access_token")
        return self.token
if __name__ == "__main__":
    a = Wework()
    # 通过配置文件获取企业微信的id
    corp_id=cf.get_key("wwork", "corp_id")
    corpsecret=cf.get_key("wwork", "contact_secret")
    print(a.get_token(corp_id,corpsecret))