import requests

from qiyewework_test.qiye_interface_test.utils.logger_util import logger


class BaseApi:
    def send(self,method,url,tool,**kwargs):
        if tool == "requests":
            data = {
                "method": method,
                "url": url,
            }
            data.update(kwargs)
            logger.info(kwargs)
            res = requests.request(**data)
            logger.info(res.text)

            return res
        else:
            return True

