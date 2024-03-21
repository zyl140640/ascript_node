import random
import time
from ascript.android import action
from ascript.android import system
from .log_uitl import setup_logging


class AirScriptPages:
    def __init__(self):
        self.system = system
        self.node = None
        self.result = None
        self.logger = setup_logging()

    def open_app(self, app_name):
        """
        打开指定App
        :param app_name: APP名称或者包名称
        """
        try:
            self.logger.info(f"打开{app_name}应用")
            self.system.open(app_name)
        except Exception as e:
            self.logger.info(f"未找到{app_name}应用")
            raise e

    def find(self, selector):
        try:
            self.node = selector.find()
            self.logger.info("查找页面元素")
            return self.node
        except Exception as e:
            self.logger.info(f"未找到元素[{selector}],报错内容: {e}")
            return None

    def find_all(self, selector):
        try:
            self.node = selector.find_all()
            self.logger.info("查找页面所有相同元素")
            return self.node
        except Exception as e:
            self.logger.info(f"未找到元素[{selector}],报错内容: {e}")
            return None

    def wait_for_selector(self, selector, max_attempts=10, interval=1):
        """
        查找并等待元素，查找成功后返回元素本身
        :param selector:  元素方法
        :param max_attempts:  循环次数
        :param interval:   循环间隔
        :return:  元素本身
        """
        attempts = 1
        while attempts <= max_attempts:
            self.logger.info(f"尝试查找元素，尝试次数: {attempts}", )
            self.node = selector.find()
            if self.node:
                return self.node
            attempts += 1
            time.sleep(interval)
        self.logger.info("未找到元素。")
        return None

    def click(self, selector, text=None):
        """
        元素点击
        :param selector:
        :param text:
        :return:
        """
        try:
            self.node = self.wait_for_selector(selector)
            self.node.click()
            self.logger.info(f"点击: [{text}]")
            return self.node
        except Exception as e:
            self.logger.info(f"点击元素 [{selector}] 时报错,报错内容: {e}")

    def long_click(self, selector, text=None):
        """
        长按
        :param selector:  元素本身
        :param text:  操作名称
        :return: 元素本身
        """
        try:
            self.node = self.wait_for_selector(selector)
            self.node.long_click()
            self.logger.info(f"长按点击: [{text}]")
            return self.node
        except Exception as e:
            self.logger.info(f"长按点击元素 [{selector}] 时报错,报错内容: {e}")

    def get_text(self, selector, text=None):
        """
         获取元素的文本内容
        :param selector: 元素
        :param text:   操作名称
        :return:  元素本身
        """
        try:
            self.node = self.wait_for_selector(selector)
            self.logger.info(f"获取: [{text}] 文本内容")
            return self.node.text
        except Exception as e:
            self.logger.info(f"获取元素 [{selector}] 的文本时报错,报错内容: {e}")

    def swipe(self, selector, inputs, text=None):
        try:
            self.node = self.wait_for_selector(selector)
            self.node.swipe(inputs)
            self.logger.info(f"控件输入: [{text}],输入内容: [{inputs}]")
            return self.node
        except Exception as e:
            self.logger.info(f"元素 [{selector}] 输入时报错,报错内容: {e}")

    def random_sleep(self):
        """随机等待2到5秒之间的时间。"""
        self.result = random.randint(2, 4)
        self.logger.info(f"随机等待{self.result}秒")
        time.sleep(self.result)

    def action_back(self):
        self.result = action.Key.back()
        self.logger.info("执行返回操作")

    def action_swipe(self, x, y, x1, y1):
        self.result = action.swipe(x, y, x1, y1)
        self.logger.info("执行滑动操作")

    def action_click(self, x, y):
        self.result = action.click(x, y)
        self.logger.info("执行元素坐标点击操作")
