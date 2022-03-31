from qiyewework_test.qiye_interface_test.apis.base_api import BaseApi


class Wework(BaseApi):
    def get_access_token(self,corpid,corpsecret):
        # corpid = 'wwbadb21313a760479'
        # corpsecret = 'aBQDiu09qqvjxao87Mmsi9ljEGWh14mwhmNGRFH5yjY'

        url = f" https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        params = {
            'corpid': corpid,
            'corpsecret': corpsecret
        }

        # 发送get请求，获取access_token
        r =self.send("get",url,tool="requests",params=params)
        self.access_token = r.json().get('access_token')
        return self.access_token
