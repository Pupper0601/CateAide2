#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com
import json

from tools.logs import logger


def load_file(_path):
    try:
        with open(_path, 'r', encoding='utf-8') as f:
            return  json.load(f)
    except Exception as e:
        logger.error(f"无法读取配置文件 {_path}: {e}")
        return None