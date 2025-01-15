#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com

debug = False

config_file_path = r"C:/CuteAide2/config.json"

discern_means = 1 # 识别方式，0为SSIM，1为SIFT

qq = ('https://qm.qq.com/cgi-bin/qm/qr?k=C_li-vF5tFboRacsQm7II86lwsY1P4gg&jump_from=webapi&authKey=IN7xudayhxrku'
      '/cQCHZkluKEZxuPQo2dX3UYei3E/vfGz932L96LV76u17VB4D8f')

KEY = 'F4JHs7EbUDWpDukK'
IV = "LV56kp3YI9RgXUZz"

# 定义虚拟键代码
VK_LBUTTON = 0x01   # 鼠标左键
VK_RBUTTON = 0x02   # 鼠标右键
VK_MENU = 0x12      # Alt 键

# 音量控制
volume_control = 2


TRANSLATE = {
    "weapon_none" : "无武器",
    "stock_none"  : "无枪托",
    "scope_none"  : "无倍镜",
    "muzzle_none" : "无枪口",
    "grip_none"   : "无握把",
    "qingxin"     : "轻型",
    "zhijiao"     : "直角",
    "banjie"      : "半截",
    "chuizhi"     : "垂直",
    "jiguang"     : "激光",
    "muzhi"       : "拇指",
    "buchang-b"   : "补偿",
    "buchang-c"   : "补偿",
    "buchang-j"   : "补偿",
    "eliuquan.png": "扼流圈",
    "xiaoyan-b"   : "消焰",
    "xiaoyan-c"   : "消焰",
    "xiaoyan-j"   : "消焰",
    "xiaoyin-b"   : "消音",
    "xiaoyin-c"   : "消音",
    "xiaoyin-j"   : "消音",
    "yazui"       : "鸭嘴",
    "zhituiqi"    : "制退器",
    "hongdian"    : "红点",
    "quanxi"      : "全息",
    "x2"          : "2倍镜",
    "x3"          : "3倍镜",
    "x4"          : "4倍镜",
    "x6"          : "6倍镜",
    "x8"          : "8倍镜",
    "tosaiban"    : "托腮板",
    "zhanshu"     : "战术枪托",
    "zhedie"      : "折叠枪托",
    "zhongxing"   : "重型枪托",
    "zidandai"    : "子弹袋",
    "AKM"         : "AKM",
    "M762"        : "Beryl M762",
    "G36C"        : "G36C",
    "M416"        : "M416",
    "M16A4"       : "M16A4",
    "SCARL"       : "SCAR-L",
    "MK47"        : "MK47 Mutant",
    "QBZ"         : "QBZ",
    "AUG"         : "AUG",
    "GROZA"       : "Groza",
    "ACE32"       : "ACE32",
    "K2"          : "K2",
    "FAMAS"       : "FAMAS",
    "98K"         : "Kar98K",
    "M24"         : "M24",
    "AWM"         : "AWM",
    "AMR"         : "Lynx AMR",
    "WIN94"       : "Win94",
    "MXNG"        : "莫辛纳甘步枪",
    "MXNG_1": "莫辛纳甘步枪",
    "ZDZT"        : "自动装填步枪",
    "ZDZT_1"        : "自动装填步枪",
    "MINI14"      : "Mini14",
    "SKS"         : "SKS",
    "VSS"         : "VSS",
    "QBU"         : "QBU",
    "MK14"        : "Mk14",
    "MK12"        : "Mk12",
    "DLGNF"       : "德拉贡诺夫",
    "DLGNF_1"       : "德拉贡诺夫",
    "S686"        : "S686",
    "S12K"        : "S12K",
    "S1897"       : "S1897",
    "DBS"         : "DBS",
    "O12"         : "O12",
    "PP19"        : "PP-19 Bizon",
    "TMX"         : "汤姆逊冲锋枪",
    "TMX_1"         : "汤姆逊冲锋枪",
    "UMP"         : "UMP",
    "UZI"         : "微型 UZI",
    "VECTOR"      : "Vector",
    "MP5K"        : "MP5K",
    "P90"         : "P90",
    "JS9"         : "JS9",
    "MP9"         : "MP9",
    "DP28"        : "DP-28",
    "M249"        : "M249",
    "MG3"         : "MG3"
}