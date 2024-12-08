#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com


import os
import sys

def get_project_root():
    # 如果是在打包后的环境中运行
    if hasattr(sys, '_MEIPASS'):
        project_root  =  os.path.abspath(sys._MEIPASS)
    else:
        # 获得当前脚本文件所在的目录
        project_root  =  os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    return project_root.replace('\\', '/')

def get_current_file_path():
    # 获取当前文件的路径
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__))).replace('\\', '/')

def object_join_path(*paths):
    """项目根路径拼接"""
    return get_project_root() + '/' + '/'.join(paths)

def current_join_path(*paths):
    """当前文件路径拼接"""
    return get_current_file_path() + '/' + '/'.join(paths)

def join_paths(*paths):
    """拼接多个路径"""
    return os.path.normpath(os.path.join(*paths)).replace('\\', '/')


if __name__ == "__main__":
    print(join_paths("/path/to", "another/path", "file.txt"))  # /path/to/file.txt
    print(current_join_path("another/path", "file.txt"))  # /path/to/another/path/file.txt
