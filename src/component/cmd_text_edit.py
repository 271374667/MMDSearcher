import json
import subprocess
import sys
import loguru
from typing import Union

from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QTextCursor
from PySide6.QtWidgets import QApplication, QTextEdit, QVBoxLayout, QWidget
from ansi2html import Ansi2HTMLConverter


class CmdRunnerThread(QThread):
    append_signal = Signal(str)

    def __init__(self, command, parent=None):
        super().__init__(parent)
        self.command = command

    def run(self):
        if isinstance(self.command, list):
            command_processed = self.command
        else:
            command_processed = self.command.split()

        proc = subprocess.Popen(
                command_processed, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
                )
        while True:
            output = proc.stdout.readline()
            if proc.poll() is not None and output == '':
                break
            if output:
                self.append_signal.emit(output.strip())


class CMDTextEdit(QWidget):
    """
    一个支持ANSI颜色代码的文本框

    Methods:
        - append_log: 添加一行消息
        - run_cmd: 运行一个cmd命令

    Signals:
        - append_signal: 添加消息的信号

    Note:
        - 颜色代码的转换使用了`loguru`和`ansi2html`库你需要安装这两个库
        - 你可以直接使用`loguru`库的`logger`对象来输出日志, 会自动上色并显示在文本框中
        - 你可以使用`run_cmd`方法来运行一个cmd命令
    """
    append_signal = Signal(str)

    def __init__(self):
        super().__init__()
        self._ansi2html_converter = Ansi2HTMLConverter()

        self.text_edit = QTextEdit(self)
        self.text_edit.setStyleSheet("background-color: black; color: white;")
        self.text_edit.setReadOnly(True)
        # 设置文本框的颜色css样式

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        self.setLayout(layout)

        self.append_signal.connect(self._append_log_slot)

        # 为了方便直接绑定loguru
        self._hook_loguru()

    def append_log(self, context: str) -> None:
        """手动添加一行消息"""
        self.append_signal.emit(self._ansi2html(context))

    def run_cmd(self, command: Union[str, list[str]]) -> None:
        """多线程运行一个cmd命令"""
        self.cmd_thread = CmdRunnerThread(command)
        self.cmd_thread.append_signal.connect(self._append_log_slot)
        self.cmd_thread.start()

    def _hook_loguru(self):
        """绑定loguru"""
        # 为了防止忘记导入loguru库
        import loguru  # noqa: F811

        def sink(message):
            ansi_color_text = json.loads(str(message))
            self.append_log(ansi_color_text['text'])

        loguru.logger.remove()
        loguru.logger.add(sink, colorize=True, serialize=True)

    def _append_log_slot(self, context: str) -> None:
        self.text_edit.moveCursor(QTextCursor.MoveOperation.End)
        self.text_edit.insertHtml(context + "<br>")

    def _ansi2html(self, ansi_content: str) -> str:
        convert = self._ansi2html_converter.convert(ansi_content, full=True, ensure_trailing_newline=True)

        return self._remove_html_space(convert)

    def _remove_html_space(self, html: str) -> str:
        return (html.replace('white-space: pre-wrap',
                             'white-space: nowrap')
        .replace('word-wrap: break-word',
                 'word-wrap: normal')
        .replace(
                'font-size: normal;',
                'font-size: medium; font-family: sans-serif;'
                )
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cte = CMDTextEdit()
    cte.show()
    # Example of running an external command:
    cte.run_cmd('ping 127.0.0.1')
    loguru.logger.info("Hello World!")
    loguru.logger.error("This is an error message")
    loguru.logger.warning("This is a warning message")
    loguru.logger.debug("This is a debug message")
    loguru.logger.critical("我是一段中文日志信息")

    # 一个绿色的ANSI颜色代码
    # text = "\x1b[94m\x1b[92m我是一个绿色的字\x1b[0m"
    # cte.append_log(text)

    sys.exit(app.exec())
