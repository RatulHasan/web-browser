import sys
import os
import json

from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel, QLineEdit, QTabBar,
                             QFrame, QStackedLayout, QTabWidget)

from PyQt5.QtGui import QIcon, QWindow, QImage
from PyQt5.QtCore import *

class AddressBar(QLineEdit):
    def __init__(self):
        super().__init__()

    def mousePressEvent(self, QMouseEvent):
        self.selectAll()


class App(QFrame):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Web Browser")

        self.create_app()
        self.setBaseSize(1366, 768)

    def create_app(self):
        self.layout = QVBoxLayout()

        # Create Tabs
        self.tabbar = QTabBar(movable = True, tabsClosable = True)
        self.tabbar.tabCloseRequested.connect(self.close_tab)

        self.tabbar.addTab("New Tab")
        self.tabbar.addTab("+")

        # self.tabbar = QTabWidget()
        # self.tabbar.addTab(QPushButton("Tab 1"), "New Tab")
        # self.tabbar.addTab(QPushButton("Tab 2"), "New Tab2")

        self.tabbar.setCurrentIndex(0)
        # End Tabs

        # Create AddressBar
        self.Toolbar = QWidget()
        self.ToolbarLayout = QHBoxLayout()
        self.addressbar = AddressBar()

        self.Toolbar.setLayout(self.ToolbarLayout)
        self.ToolbarLayout.addWidget(self.addressbar)
        # End AddressBar

        self.layout.addWidget(self.tabbar)
        self.layout.addWidget(self.Toolbar)
        self.setLayout(self.layout)

        self.show()

    def close_tab(self, i):
        self.tabbar.removeTab(i)
        print(i)


if __name__=="__main__":
    app = QApplication(sys.argv)
    window = App()
    sys.exit(app.exec_())