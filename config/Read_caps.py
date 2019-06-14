# @File   :   Read_caps.py
# @Author :   July401
# @Date   :   2019/6/5
# @Email  :   july401@qq.com

import yaml

from common.Read_path import CONF_DIR


class CapsRead:
    def read_caps(self):
        yaml_path = CONF_DIR + r'caps.yaml'
        with open(yaml_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            return data


my_caps = CapsRead().read_caps()
