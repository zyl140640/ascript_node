import pymysql

from .log_uitl import setup_logging


class MySQLHelper:
    def __init__(self, params):
        self.host = params['host']
        self.port = params['port']
        self.user = params['user']
        self.password = params['password']
        self.database = params['database']
        self.charset = params.get('charset', 'utf8mb4')
        self.connection = None
        self.cursor = None
        self.logger = setup_logging()  # 初始化日志记录器

    def connect(self):
        """连接到MySQL数据库"""
        try:
            self.connection = pymysql.connect(host=self.host,
                                              port=self.port,
                                              user=self.user,
                                              password=self.password,
                                              database=self.database,
                                              charset=self.charset,
                                              cursorclass=pymysql.cursors.DictCursor)
            self.cursor = self.connection.cursor()
            self.logger.info("成功连接到 MySQL 数据库。")
            return True
        except pymysql.MySQLError as e:
            self.logger.error("连接到 MySQL 数据库时发生错误: %s", e)
            return False

    def execute_query(self, query, params=None):
        """执行查询操作"""
        try:
            self.cursor.execute(query, params)
            result = self.cursor.fetchall()
            self.logger.info("查询结果: %s", result)
            return result
        except pymysql.MySQLError as e:
            self.logger.error("执行查询时发生错误: %s", e)
            return None

    def execute_update(self, query, params=None):
        """执行更新操作"""
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            self.logger.info("更新成功。")
            return True
        except pymysql.MySQLError as e:
            self.logger.error("执行更新时出错: %s", e)
            self.connection.rollback()
            return False

    def execute_insert(self, query, params=None):
        """执行插入操作"""
        self.logger.info("新增成功。")
        return self.execute_update(query, params)

    def execute_delete(self, query, params=None):
        """执行删除操作"""
        self.logger.info("删除成功。")
        return self.execute_update(query, params)

    def close(self):
        """关闭数据库连接"""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            self.logger.info("MySQL 连接已关闭。")
