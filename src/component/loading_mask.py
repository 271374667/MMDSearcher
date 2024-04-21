from PySide6.QtCore import QRect, QTimer, Qt
from PySide6.QtGui import QBrush, QColor, QPainter
from PySide6.QtWidgets import QHBoxLayout, QLabel, QSizePolicy, QSpacerItem, QVBoxLayout, QWidget
from qfluentwidgets.components import IndeterminateProgressRing


class LoadingMask(QWidget):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.is_show: bool = False
        self.opacity: float = 0.6

        # 设置大小和父控件一致
        self.setGeometry(QRect(0, 0, parent.width(), parent.height()))

        self._init_ui()

        # 重写父控件的resizeEvent方法(邪教)
        parent.resizeEvent = self.resizeEvent

    def set_loading_text(self, text: str) -> None:
        self.loadingText.setText(text)

    def set_opacity(self, opacity: float) -> None:
        self._set_opacity(opacity)
        self.update()

    def set_loading_visiable(self, is_visiable: bool) -> None:
        if is_visiable:
            self.show()
            self.is_show = True
            return

        self.is_show = False
        self.hide()

    def _init_ui(self) -> None:
        self.progressRing = IndeterminateProgressRing()
        self.loadingText = QLabel("加载中")
        self.loadingText.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # 创建水平和垂直间距
        hspacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        vspacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        content_layout = QVBoxLayout()
        content_layout.addItem(vspacer)
        content_layout.addWidget(self.progressRing, 0, Qt.AlignmentFlag.AlignCenter)
        content_layout.addWidget(self.loadingText, 0, Qt.AlignmentFlag.AlignCenter)
        content_layout.addItem(vspacer)

        main_layout = QHBoxLayout()
        main_layout.addItem(hspacer)
        main_layout.addLayout(content_layout)
        main_layout.addItem(hspacer)

        self.setLayout(main_layout)

    def _set_opacity(self, opacity: float) -> None:
        self.opacity = opacity

    def _hide_mask(self) -> None:
        if not self.is_show:
            self.hide()
            return

    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.fillRect(self.rect(), QBrush(QColor(0, 0, 0, int(self.opacity * 255))))

    def resizeEvent(self, event) -> None:
        self.setGeometry(QRect(0, 0, self.parentWidget().width(), self.parentWidget().height()))
        self.updateGeometry()


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    window = QWidget()
    window.resize(640, 480)

    loadingMask = LoadingMask(window)
    loadingMask.set_loading_visiable(True)
    loadingMask.set_loading_text("这是一个测试")
    QTimer.singleShot(2000, lambda: loadingMask.set_loading_visiable(False))
    QTimer.singleShot(4000, lambda: loadingMask.set_loading_visiable(True))
    QTimer.singleShot(6000, lambda: loadingMask.set_loading_visiable(False))
    window.show()

    app.exec()
