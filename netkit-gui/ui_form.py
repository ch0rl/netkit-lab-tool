# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QToolButton, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1113, 658)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.menu_layout = QHBoxLayout()
        self.menu_layout.setObjectName(u"menu_layout")
        self.graph_button = QPushButton(self.centralwidget)
        self.graph_button.setObjectName(u"graph_button")

        self.menu_layout.addWidget(self.graph_button)

        self.export_button = QPushButton(self.centralwidget)
        self.export_button.setObjectName(u"export_button")

        self.menu_layout.addWidget(self.export_button)

        self.settings_button = QToolButton(self.centralwidget)
        self.settings_button.setObjectName(u"settings_button")

        self.menu_layout.addWidget(self.settings_button)


        self.verticalLayout.addLayout(self.menu_layout)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.rhs_layout = QVBoxLayout()
        self.rhs_layout.setObjectName(u"rhs_layout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.machine_name_edit = QLineEdit(self.centralwidget)
        self.machine_name_edit.setObjectName(u"machine_name_edit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.machine_name_edit)


        self.rhs_layout.addLayout(self.formLayout)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.interfaces = QListWidget(self.centralwidget)
        self.interfaces.setObjectName(u"interfaces")

        self.gridLayout_3.addWidget(self.interfaces, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.if_form_layout = QFormLayout()
        self.if_form_layout.setObjectName(u"if_form_layout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.if_form_layout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.interface_name_edit = QLineEdit(self.centralwidget)
        self.interface_name_edit.setObjectName(u"interface_name_edit")

        self.if_form_layout.setWidget(0, QFormLayout.FieldRole, self.interface_name_edit)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.if_form_layout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.lan_name_edit = QLineEdit(self.centralwidget)
        self.lan_name_edit.setObjectName(u"lan_name_edit")
        self.lan_name_edit.setReadOnly(False)

        self.if_form_layout.setWidget(1, QFormLayout.FieldRole, self.lan_name_edit)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.if_form_layout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.ip_address_edit = QLineEdit(self.centralwidget)
        self.ip_address_edit.setObjectName(u"ip_address_edit")

        self.if_form_layout.setWidget(2, QFormLayout.FieldRole, self.ip_address_edit)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.if_form_layout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.netmask_edit = QLineEdit(self.centralwidget)
        self.netmask_edit.setObjectName(u"netmask_edit")

        self.if_form_layout.setWidget(3, QFormLayout.FieldRole, self.netmask_edit)

        self.update_if_button = QPushButton(self.centralwidget)
        self.update_if_button.setObjectName(u"update_if_button")

        self.if_form_layout.setWidget(5, QFormLayout.SpanningRole, self.update_if_button)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.if_form_layout.setItem(4, QFormLayout.LabelRole, self.verticalSpacer)

        self.new_if_button = QPushButton(self.centralwidget)
        self.new_if_button.setObjectName(u"new_if_button")

        self.if_form_layout.setWidget(6, QFormLayout.LabelRole, self.new_if_button)

        self.delete_if_button = QPushButton(self.centralwidget)
        self.delete_if_button.setObjectName(u"delete_if_button")

        self.if_form_layout.setWidget(6, QFormLayout.FieldRole, self.delete_if_button)


        self.gridLayout_3.addLayout(self.if_form_layout, 0, 2, 1, 1)

        self.gridLayout_3.setColumnStretch(2, 1)

        self.rhs_layout.addLayout(self.gridLayout_3)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.rhs_layout.addWidget(self.label_6)

        self.startup_edit = QPlainTextEdit(self.centralwidget)
        self.startup_edit.setObjectName(u"startup_edit")

        self.rhs_layout.addWidget(self.startup_edit)


        self.gridLayout_2.addLayout(self.rhs_layout, 1, 2, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.update_button = QPushButton(self.centralwidget)
        self.update_button.setObjectName(u"update_button")

        self.horizontalLayout.addWidget(self.update_button)

        self.delete_machine_button = QPushButton(self.centralwidget)
        self.delete_machine_button.setObjectName(u"delete_machine_button")

        self.horizontalLayout.addWidget(self.delete_machine_button)


        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 2, 1, 1)

        self.machine_list = QListWidget(self.centralwidget)
        self.machine_list.setObjectName(u"machine_list")

        self.gridLayout_2.addWidget(self.machine_list, 1, 1, 1, 1)

        self.new_machine_button = QPushButton(self.centralwidget)
        self.new_machine_button.setObjectName(u"new_machine_button")

        self.gridLayout_2.addWidget(self.new_machine_button, 2, 1, 1, 1)

        self.gridLayout_2.setColumnStretch(2, 1)

        self.verticalLayout.addLayout(self.gridLayout_2)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.graph_button.setText(QCoreApplication.translate("MainWindow", u"Show Graph", None))
        self.export_button.setText(QCoreApplication.translate("MainWindow", u"Export Lab", None))
        self.settings_button.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Machine Name", None))
        self.machine_name_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name of the machine...", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Interface Name", None))
        self.interface_name_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Interface Name (ie., eth0)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"LAN Name", None))
        self.lan_name_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"LAN Name (in lab.conf)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"IP Address", None))
        self.ip_address_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"IP Address (x.x.x.x)", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Network Mask", None))
        self.netmask_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CIDR Network Mask", None))
        self.update_if_button.setText(QCoreApplication.translate("MainWindow", u"Save/Update Interface", None))
        self.new_if_button.setText(QCoreApplication.translate("MainWindow", u"New Interface", None))
        self.delete_if_button.setText(QCoreApplication.translate("MainWindow", u"Delete Current Interface", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Additional Startup Script", None))
        self.startup_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Text to insert in <machine_name>.startup after network interface configuration.", None))
        self.update_button.setText(QCoreApplication.translate("MainWindow", u"Save/Update Machine", None))
        self.delete_machine_button.setText(QCoreApplication.translate("MainWindow", u"Delete Machine", None))
        self.new_machine_button.setText(QCoreApplication.translate("MainWindow", u"New Machine", None))
    # retranslateUi

