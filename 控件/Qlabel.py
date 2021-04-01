# coding:utf-8
# @时间 : 2021/3/25 12:40
# @文件名 : Qlabel.py
# @工程名:PyQt5 学习
# @用户：Administrator  1181355852@qq.com
# @IDE名字:PyCharm

import sys
from PyQt5.QtWidgets import QVBoxLayout, QApplication, QLabel, QWidget
from PyQt5.QtCore import Qt

from PyQt5.QtGui import QPalette, QPixmap


class Qlabeldemo(QWidget):
    def __init__(self):
        super(Qlabeldemo, self).__init__()
        self.initui()

    def initui(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText('<font color=yellow>这是一个文本标签。</font>')
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText('<a href="#">欢迎使用Python GUI程序。</a>')

        label3.setAlignment(Qt.AlignCenter)

        label3.setToolTip('这是一个图片标签。')

        label3.setPixmap(QPixmap('./images/python.jpg'))
        # label4.setOpenExternalLinks(True)
        label4.setText("<a href='https://item.jd.com/31817766588.html'>感谢挂住《Python从菜鸟到高手》</a>")
        label4.setAlignment(Qt.AlignRight)

        label4.setToolTip('这是一个超链接')

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        label2.linkHovered.connect(self.linkhouered)
        label4.linkActivated.connect(self.linkclicked)

        self.setLayout(vbox)
        self.setWindowTitle('Qlabel控件演示')

    def linkhouered(self):
        print('当鼠标划过label2标签是，触发事件.')

    def linkclicked(self):
        print('当鼠标单击label4标签是，触发事件。')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Qlabeldemo()
    main.show()
    sys.exit(app.exec())
