import os
import yaml

class FileTool:
    # 获取文件的方法
    @classmethod
    def get_interface_dir(self):
        # 获取当前目录的上两级目录文件夹路径，即项目文件夹绝对路径D:\temp\mygithub\qiyewework_test\qiye_interface_test
        r = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print(r)
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 实现yaml读取
    @classmethod
    def read_yaml(self,file_name):
        # 获取test_qiye_interface的目录
        _path=FileTool.get_interface_dir()
        # 根据文件名拼接路径D:\temp\mygithub\qiyewework_test\qiye_interface_test\datas\secrets
        yaml_file=os.sep.join([_path,"datas",file_name])
        print(yaml_file)
        # 打开文件流
        with open(yaml_file,encoding='utf-8') as f:
            # 使用yaml把文件流转换成Python对象返回出去
            return yaml.safe_load(f)

if __name__ == '__main__':
    print(FileTool.read_yaml("secrets"))