#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

import time
from datetime import datetime, timedelta
import requests

from libs.dialog import dialog
from libs.global_variables import GDV
from tools.ace import AesEncrypt


def email_verification(email):
    """验证邮箱正确性"""
    import re
    pattern = r'^[a-zA-Z0-9_.-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$'
    if re.match(pattern, email):
        return True
    return False

def code_verification(code):
    """验证激活码正确性"""
    ace_list = AesEncrypt().decrypt(code).split("|")
    # print(ace_list)
    if ace_list[0] == "CateAide2":
        return True
    return False

def code_verify(email, code):
    """验证激活码有效性"""
    code_list = AesEncrypt().decrypt(code).split("|")
    data = {
        "email": email,
        "code": code,
        "start_time": int(time.time()),
        "day": code_list[1]
    }
    res = requests.post("http://43.155.4.69:9528/login", json=data).json()
    if res["code"] == "101":
        if res["message"]["email"] == email:
            start_time = datetime.fromtimestamp(res["message"]["start_time"]) + timedelta(days=int(res["message"][
                                                                                                       "day"]))
            current_time = datetime.fromtimestamp(int(time.time()))
            if current_time < start_time:
                GDV.vip = start_time
                # print(GDV.vip)
                dialog("✅登录成功", "👏欢迎使用 CateAide2.", cancel_hide=True)
                return True
            else:
                dialog("❌登录失败", "‼️激活码已过期. 请重新购买.", cancel_hide=True)
                return False
        else:
            dialog("❌登录失败", "激活码已被使用或与邮箱不匹配.", cancel_hide=True)
            return False
    elif res["code"] == "102":
        start_time = datetime.fromtimestamp(data["start_time"]) + timedelta(days=int(data["day"]))
        GDV.vip = start_time
        print(GDV.vip)
        dialog("✅激活成功", "👏欢迎使用 CateAide2.", cancel_hide=True)
        return True
    else:
        dialog("⚠️提示", "登录异常, 请联系管理员🕵️‍♂️.", cancel_hide=True)
        return False






if __name__ == '__main__':
    emails = "pupper.cheng@gmail.com"
    # print(email_verification(emails))

    codes = "bThPcFlj4WJHehzBtUfBhMsrjTHErxZBkdlZ8A+gyeY="
    code_verification(codes)