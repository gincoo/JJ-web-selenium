# coding=utf-8
import logging
import os
import datetime


#
# 自定义log 日志模块
# 支持 文件输出日志和控制台输出
#
class UserLog(object):

    def __init__(self):
        self.logger1 = logging.getLogger(__name__)
        self.logger1.manager.loggerDict.pop(__name__)
        self.logger1.handlers = []
        self.logger1.removeHandler(self.logger1.handlers)

        if not self.logger1.handlers:
            self.logger1.setLevel(logging.DEBUG)
            # 文件名 生成
            base_dir = os.path.dirname(os.path.abspath(__file__))
            log_dir = os.path.join(base_dir, "logs")
            log_file = datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
            log_name = log_dir + "/" + log_file
            print('输出路径', log_name)

            # 文件输出日志
            self.file_handle = logging.FileHandler(log_name, 'a', encoding='utf-8')
            self.file_handle.setLevel(logging.INFO)

            # 控制台输出日志
            self.cmd_Handler = logging.StreamHandler()
            self.cmd_Handler.setLevel(logging.INFO)

            formatter = logging.Formatter(
                '%(asctime)s %(filename)s--> %(funcName)s %(levelno)s: %(levelname)s ----->%(message)s')
            self.cmd_Handler.setFormatter(formatter)
            self.file_handle.setFormatter(formatter)

            self.logger1.addHandler(self.file_handle)
            self.logger1.addHandler(self.cmd_Handler)

    def get_log(self):
        return self.logger1

    def close_handle(self):
        self.logger1.removeHandler(self.file_handle)
        self.file_handle.close()


if __name__ == '__main__':
    user = UserLog()
    log = user.get_log()
    log.info('首页日志-----')
    log.info('订单日志-----')
    log.info('活动页日志-----')
    user.close_handle()
