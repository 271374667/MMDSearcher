"""
config是程序的配置文件，包括数据库的配置、日志的配置、缓存的配置等
在运行的过程中无法更改，只能在程序启动时加载
"""
from datetime import timedelta

# 服务器host
HOST: str = '127.0.0.1'
# 服务器端口
PORT: int = 55000
# 默认每一页的数量
DEFAULT_PAGE_SIZE: int = 15
# 日志超过这个时间会被打包成压缩文件
LOG_ROTATION: timedelta = timedelta(days=1)
# 日志超过这个时间会被删除
LOG_RETENTION: timedelta = timedelta(days=7)
# 日志的编码格式
LOG_ENCODING: str = 'utf-8'
# 远程仓库的地址
REMOTE_REPOSITORY: str = 'https://github.com/271374667/MMDSearcher'
# 数据库meta文件的地址
DATABASE_META_URL: str = r'https://raw.githubusercontent.com/271374667/MMDSearcher/master/database_meta.json'
# 数据库文件的地址
DATABASE_FILE_URL: str = r'https://raw.githubusercontent.com/271374667/MMDSearcher/master/database.db'
