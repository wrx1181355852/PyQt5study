# coding:utf-8
# @时间 : 2021/3/24 16:46
# @文件名 : runbrowser.py
# @工程名:PyQt5 学习
# @用户：Administrator  1181355852@qq.com
# @IDE名字:PyCharm
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

import browser

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = browser.Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
