import logging
import os
from qiyewework_test.qiye_interface_test.utils.file_tools import FileTool


logger=logging.getLogger(__name__)
# sep传递一个列表参数，拼接logs的文件夹，封装logger可以在任意地方调用
file_path=os.sep.join([FileTool.get_interface_dir(),"logs"])
# 文件夹不存在就创建
if not os.path.exists(file_path):
    # 创建文件夹
    os.mkdir(file_path)
# 拼接log文件夹路径和句柄
fileHandler=logging.FileHandler(filename=file_path+"/apitest.log",encoding='utf-8')
# 日志格式：当前时间、文件名字、调用函数、行、日志级别、日志的消息
formatter=logging.Formatter('[%(asctime)s] %(filename)s - %(funcName)s line:%(lineno)d [%(levelname)s]: %(message)s')
# 日志绑定，文件句柄绑定格式
fileHandler.setFormatter(formatter)
# 控制台句柄定义,句柄是日志承载的对象
streamHandler=logging.StreamHandler()
# 控制台句柄绑定格式
streamHandler.setFormatter(formatter)
# 设置生效
logger.addHandler(fileHandler)
logger.addHandler(streamHandler)
# 设置日志级别
logger.setLevel(logging.INFO)