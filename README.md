## ascript_node 插件使用教程

### 简介

本教程指导您如何使用 ascript_node 插件

#### 目前已封装操作
* 控件
* mysql相关操作
* Excel相关操作
* pandas操作Excel
* 发送qq邮箱、钉钉、163邮箱、飞书
* webSocket通讯方法

### 要求

* 安装并配置 AirScript
* 熟悉 Android UI 层次结构
* 安装了相关依赖如pymysql openpyxl
* 不安装也没关系,插件会检测用户是否安装,不安装则无法使用相关依赖;

#### 步骤

### 导入必要的模块

```python
from ascript.android import plug

plug.load("ascript_node")
from ascript_node import *
```

### 引用控件方法

```python
from ascript_node import *
node_page = page()
node_page.要使用的方法
```

### 常用方法

您可以使用以下方法与元素交互：

* open_app(app_name)：打开指定应用程序。
* click(selector)：点击元素。
* find(selector)：查找元素并返回其引用。
* find_all(selector)：查找所有匹配元素并返回它们的引用列表。
* wait_for_selector(selector)：等待元素出现，然后返回其引用。
* get_text(selector)：获取元素的文本内容。
* swipe(selector, inputs)：在元素上执行滑动操作。
* random_sleep()：随机等待 2 到 5 秒。
* action_back()：执行返回操作。
* action_swipe(x, y, x1, y1)：执行滑动操作。
* action_click(x, y)：执行元素坐标点击操作。

#### Selector 讲解

```python
使用前先讲解一下后续各方法内的selector是填入什么
selector: 控件地址
Selector(2).type("LinearLayout").find()
Selector(2).type("LinearLayout").find_all()
只需将find_all()
或者find()
去除填入相应方法内即可
```

#### 示例

```python
# 打开应用程序
pages.open_app("com.example.my_app")

noeds = Selector(2).type("LinearLayout")

# 查找单个元素并返回其引用。
pages.find(noeds)

# 查找所有匹配元素并返回它们的引用列表。
pages.find_all(noeds)

# 查找并点击按钮
pages.click(noeds, "登录按钮")

# 获取文本输入框的文本
text = pages.get_text(noeds, "搜索输入框")

# 在文本输入框中输入文本
pages.swipe(noeds, "test")

# 随机等待 2 到 5 秒
pages.random_sleep()

# 执行返回操作
pages.action_back()

# 执行滑动操作
pages.action_swipe(100, 100, 200, 200)

# 执行元素坐标点击操作
pages.action_click(100, 100)

```

### Excel方法使用教程

### 方法

- **get_sheet(sheet_name=None)**: 获取工作表
- **get_cell_value(sheet_name, row, column)**: 获取单元格值
- **set_cell_value(sheet_name, row, column, value)**: 设置单元格值
- **save()**: 保存工作簿
- **get_sheet_names()**: 获取所有工作表名称
- **create_sheet(sheet_name)**: 创建工作表
- **delete_sheet(sheet_name)**: 删除工作表

### 用法示例

```python
from ascript_node import *
filename = 'example.xlsx'
excel_helper = excel(filename)

# 获取工作表
sheet = excel_helper.get_sheet()  # 默认获取第一个工作表

# 获取单元格值
cell_value = excel_helper.get_cell_value('Sheet1', 1, 1)

# 设置单元格值
excel_helper.set_cell_value('Sheet1', 1, 1, '新值')

# 保存工作簿
excel_helper.save()
```

## MySQL数据库相关操作方法

### 方法

- **connect()**: 连接到 MySQL 数据库
- **execute_query(query, params=None)**: 执行查询操作
- **execute_update(query, params=None)**: 执行更新操作
- **execute_insert(query, params=None)**: 执行插入操作
- **execute_delete(query, params=None)**: 执行删除操作
- **close()**: 关闭数据库连接

### 用法示例

```python
from ascript_node import *
# 数据库连接参数
params = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'database': 'test',
}
# 初始化 MySQLHelper 对象
mysql_helper = mysql(params)
# 连接到数据库
if mysql_helper.connect():
    # 执行查询操作
    query = 'SELECT * FROM users'
    result = mysql_helper.execute_query(query)
    print(result)

    # 执行更新操作
    query = 'UPDATE users SET name = %s WHERE id = %s'
    params = ('Michael', 1)
    mysql_helper.execute_update(query, params)

    # 执行插入操作
    query = 'INSERT INTO users (name, email) VALUES (%s, %s)'
    params = ('John', 'john@example.com')
    mysql_helper.execute_insert(query, params)

    # 执行删除操作
    query = 'DELETE FROM users WHERE id = %s'
    params = (2,)
    mysql_helper.execute_delete(query, params)

    # 关闭数据库连接
    mysql_helper.close()
```

## pandas操作Excel方法总结
### 引用
```python
from ascript_node import *
excel = pandas_excel()
excel.要使用的方法
```

### 方法
```python
from ascript_node import *

# 创建 ExcelHandler 对象
excel_handler = pandas_excel('文件路径')

# 常用操作
excel_handler.read_excel() #读取 Excel 文件并存储在 DataFrame 中。
excel_handler.write_excel('新文件路径') # 将 DataFrame 写入 Excel 文件。
excel_handler.append_excel('新文件路径') #将 DataFrame 追加到 Excel 文件。
excel_handler.create_pivot_table('行索引', '列索引', '值') #建透视表

# 增删改查
excel_handler.add_row({'列名1': '值1', '列名2': '值2'})
excel_handler.delete_row(0)
excel_handler.update_row(0, {'列名1': '新值1', '列名2': '新值2'})
excel_handler.query_data('列名1 == "值1"')

# 其它操作
excel_handler.set_column_names(['新列名1', '新列名2', ...])
excel_handler.set_row_index(['新索引1', '新索引2', ...])
excel_handler.sort_data('列名', ascending=True/False)
excel_handler.drop_duplicates(['列名1', '列名2', ...])
excel_handler.fillna(0)

```

## 发送邮箱操作

### 使用方法

```python
from ascript_node import *
# 创建消息发送器实例
sender = message_sender()

# 发送电子邮件
sender.send_email('邮箱账号', '邮箱密码', '收件人邮箱', '邮箱内容', 'qq或者163')

# 发送钉钉消息
sender.send_dingding_message('webhook_url', {'content': '钉钉消息内容'})
# 发送飞书
sender.send_feishu_message("接口地址",'access_token令牌', {'content': '飞书消息内容'})


```


## WebSocket 使用教程

```python
# 使用示例
from ascript_node import *
with webSocket_clien("ws://localhost:8000/websocket") as client:
    client.send("Hello, world!")
    message = client.receive()
    print(message)

```