#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
import json
from pathlib import Path

from libs.config import config_file_path
from tools.logs import logger


def load_file(_path):
    try:
        with open(_path, 'r', encoding='utf-8') as f:
            return  json.load(f)
    except Exception as e:
        logger.error(f"无法读取配置文件 {_path}: {e}")
        return None

def save_file(_path, _data):
    try:
        with open(_path, 'w', encoding='utf-8') as f:
            json.dump(_data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        logger.error(f"无法保存配置文件 {_path}: {e}")
        return None


def write_config(data):
    config_path = Path(config_file_path)
    if not config_path.is_file():
        config_path.parent.mkdir(parents=True, exist_ok=True)
        config_path.touch()

    with open(config_file_path, 'w', encoding='utf-8') as f:
        f.write(data)


def read_config():
    config_path = Path(config_file_path)
    if config_path.is_file():
        with open(config_file_path, 'r', encoding='utf-8') as f:
            return f.read()
    return {}


if __name__ == '__main__':
    print(load_file("../gun_data.json")["global_recoil"])