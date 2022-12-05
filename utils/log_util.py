import logging
import os
import time

log_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'log')
print(log_path)

# 设置日志级别: debug调试, info信息, warning警告, error错误, critical危险
level = logging.DEBUG


class Logger:
    def __init__(self):
        # 定义日志位置和文件名
        self.logName = os.path.join(log_path, "{}.log".format(time.strftime("%Y-%m-%d")))
        # 定义一个日志容器
        self.logger = logging.getLogger("log")
        # 设置打印日志的级别
        self.logger.setLevel(level)
        # 创建日志输入的格式
        self.forMater = logging.Formatter(
            '[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s]'
        )
        # 创建日志处理器，用来存放日志文件
        self.fileLogger = logging.FileHandler(self.logName, mode='a', encoding='UTF-8', delay=False, errors=None)
        # 设置日志存放级别
        self.fileLogger.setLevel(level)
        # 设置存放日志格式
        self.fileLogger.setFormatter(self.forMater)

        # 创建日志处理器，在控制台打印
        self.console = logging.StreamHandler()
        # 设置控制台打印日志级别
        self.console.setLevel(logging.DEBUG)
        # 设置控制台日志格式
        self.console.setFormatter(self.forMater)
        # 将日志输出渠道添加到日志收集器中
        self.logger.addHandler(self.fileLogger)
        self.logger.addHandler(self.console)


logger = Logger().logger

if __name__ == '__main__':
    logger.debug("输出bug日志")
    logger.info("输出info日志")
    logger.warning("输出warning日志")
    logger.error("输出error日志")
