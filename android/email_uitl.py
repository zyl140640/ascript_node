import smtplib
import requests


class MessageSender:
    @staticmethod
    def send_email(sender_email, sender_password, receiver_email, message, email_provider='qq'):
        """
        使用 SMTP 发送电子邮件。
        Args:
            receiver_email (str): 收件人邮箱地址。
            message (str): 邮件正文。
            email_provider (str, optional): 邮箱提供商，可选值为 'qq' 或 '163'。默认为 'qq'。
            :param email_provider:
            :param message:
            :param receiver_email:
            :param sender_password:
            :param sender_email:
        """

        if email_provider == 'qq':
            # QQ 邮箱的 SMTP 服务器和端口
            smtp_server = 'smtp.qq.com'
            smtp_port = 465
        elif email_provider == '163':
            # 163 邮箱的 SMTP 服务器和端口
            smtp_server = 'smtp.163.com'
            smtp_port = 994
        else:
            raise ValueError(f'不支持的邮箱提供商：{email_provider}')

        # 创建 SMTP 对象
        smtpObj = smtplib.SMTP_SSL(smtp_server, smtp_port)

        # 登录到邮件服务器
        smtpObj.login(sender_email, sender_password)

        # 发送邮件
        smtpObj.sendmail(sender_email, receiver_email, message)

        # 断开与邮件服务器的连接
        smtpObj.quit()

    @staticmethod
    def send_dingding_message(webhook, message):
        """
        使用钉钉群机器人的 webhook 发送消息。

        Args:
            webhook (str): 钉钉群机器人的 webhook 地址。
            message (dict): 消息内容。
        """

        # 发送消息
        requests.post(webhook, json=message)

    @staticmethod
    def send_feishu_message(url, access_token, message):
        """
        使用飞书推送 API 发送消息。

        Args:
            url: 地址
            access_token (str): 飞书推送 API 的 Access Token。
            message (dict): 消息内容。
        """

        # 设置飞书推送 API 的 URL
        feishu_api_url = url

        # 设置请求头
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }

        # 发送消息
        response = requests.post(feishu_api_url, headers=headers, json=message)

        # 检查响应状态码
        if response.status_code != 200:
            raise Exception(f'飞书推送 API 调用失败，状态码：{response.status_code}')

        # 返回响应内容
        return response.json()
