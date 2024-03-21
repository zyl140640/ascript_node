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

print("------欢迎使用ascript-node------")
print("------目前版本为测试版------")
print("------有好的封装提议请加QQ: 782045011------")
print("------依赖包检查------")

try:
    from .android.AirScriptPage import AirScriptPages

    page = AirScriptPages()
except Exception as e:
    print(f"AirScriptPages未安装,请使用 pip 安装它,报错详细内容{e}")

try:
    from .android.mysql_uitl import MySQLHelper

    mysql = MySQLHelper()
except Exception as e:
    print(f"pymysql未安装未安装,请使用 pip 安装它,报错详细内容{e}")

try:
    from .android.excel_uitl import ExcelHelper

    excel = ExcelHelper()
except Exception as e:
    print(f"openpyxl未安装未安装,请使用 pip 安装它,报错详细内容{e}")

try:
    from .android.pandas_uitl import PandasHandler

    pandas_excel = PandasHandler()
except Exception as e:
    print(f"pandas未安装,请使用 pip 安装它,报错详细内容{e}")

try:
    from .android.email_uitl import MessageSender

    message_sender = MessageSender()
except Exception as e:
    print(f"smtplib未安装,请使用 pip 安装它,报错详细内容{e}")

try:
    from .android.websockets_uitl import WebSocketClient

    webSockets = WebSocketClient()
except Exception as e:
    print(f"websockets未安装,请使用 pip 安装它,报错详细内容{e}")
