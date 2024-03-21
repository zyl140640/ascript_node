# __init__.py 为初始化加载文件
import logging
import os

# 导入系统资源模块
from ascript.android.system import R
# 导入动作模块
from ascript.android import action
# 导入节点检索模块
from ascript.android import node
# 导入图色检索模块
from ascript.android import screen


def page():
    try:
        from .android.AirScriptPage import AirScriptPages
        return AirScriptPages()
    except Exception as e:
        print(f"AirScriptPages未安装,请使用 pip 安装它,报错详细内容{e}")


def mysql(params):
    try:
        from .android.mysql_uitl import MySQLHelper
        return MySQLHelper(params)
    except Exception as e:
        print(f"pymysql未安装未安装,请使用 pip 安装它,报错详细内容{e}")


def excel(filename):
    try:
        from .android.excel_uitl import ExcelHelper
        return ExcelHelper(filename)
    except Exception as e:
        print(f"openpyxl未安装未安装,请使用 pip 安装它,报错详细内容{e}")


def pandas_excel(filename):
    try:
        from .android.pandas_uitl import PandasHandler
        return PandasHandler(filename)
    except Exception as e:
        print(f"pandas未安装,请使用 pip 安装它,报错详细内容{e}")


def message_sender():
    try:
        from .android.email_uitl import MessageSender
        return MessageSender()
    except Exception as e:
        print(f"smtplib未安装,请使用 pip 安装它,报错详细内容{e}")


def webSocket_client(url):
    try:
        from .android.websockets_uitl import WebSocketClient
        return WebSocketClient(url)
    except Exception as e:
        print(f"websockets未安装,请使用 pip 安装它,报错详细内容{e}")


print("------欢迎使用ascript-node------")
print("------目前版本为测试版------")
print("------有好的封装提议请加QQ: 782045011------")
