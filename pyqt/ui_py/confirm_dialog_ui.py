# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\pyqt\ui\confirm_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConfirmDialog(object):
    def setupUi(self, ConfirmDialog):
        ConfirmDialog.setObjectName("ConfirmDialog")
        ConfirmDialog.resize(414, 220)
        ConfirmDialog.setMinimumSize(QtCore.QSize(414, 220))
        ConfirmDialog.setMaximumSize(QtCore.QSize(414, 220))
        ConfirmDialog.setStyleSheet("* {margin:0; padding:0; border: 0}\n"
"\n"
"QDialog{background-color:#efefef}\n"
"\n"
"QPushButton{\n"
"    background-color: #ffdf00;\n"
"    border: 0;\n"
"border-radius:25; padding:0; margin:0\n"
"}\n"
"QPushButton::disabled{background-color:#cbcbcb}\n"
"QPushButton:hover{ background-color: #f1d100}\n"
"QPushButton:pressed{background-color:#dfc200 }\n"
"\n"
"QPushButton:focus {border: 0; outline:1px solid #ababab}\n"
"\n"
"QLineEdit{\n"
"background-color: transparent;\n"
"border: 2px solid #b0b0b0;\n"
"padding: 5 15;\n"
"border-radius: 18\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(ConfirmDialog)
        self.verticalLayout.setContentsMargins(9, 9, 9, 15)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(ConfirmDialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(15, 0, 15, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.description_text = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Equinox Bold")
        font.setPointSize(14)
        self.description_text.setFont(font)
        self.description_text.setAlignment(QtCore.Qt.AlignCenter)
        self.description_text.setWordWrap(True)
        self.description_text.setObjectName("description_text")
        self.verticalLayout_2.addWidget(self.description_text)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(ConfirmDialog)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 52))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 52))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(15, 0, 15, 0)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_confirm = QtWidgets.QPushButton(self.frame_2)
        self.btn_confirm.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_confirm.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Equinox Bold")
        font.setPointSize(14)
        self.btn_confirm.setFont(font)
        self.btn_confirm.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/assets/icons/icons/2x/sharp_check_black_48dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_confirm.setIcon(icon)
        self.btn_confirm.setIconSize(QtCore.QSize(25, 25))
        self.btn_confirm.setAutoDefault(False)
        self.btn_confirm.setDefault(True)
        self.btn_confirm.setObjectName("btn_confirm")
        self.horizontalLayout.addWidget(self.btn_confirm)
        self.btn_cancel = QtWidgets.QPushButton(self.frame_2)
        self.btn_cancel.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_cancel.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Equinox Bold")
        font.setPointSize(14)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cancel.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btn_cancel.setStyleSheet("* {\n"
"background-color: #eece00\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #ddbd00\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #ccac00\n"
"}\n"
"QPushButton::disabled{background-color:#cbcbcb}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/assets/icons/icons/2x/sharp_close_black_48dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cancel.setIcon(icon1)
        self.btn_cancel.setIconSize(QtCore.QSize(25, 25))
        self.btn_cancel.setAutoDefault(False)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout.addWidget(self.btn_cancel)
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(ConfirmDialog)
        QtCore.QMetaObject.connectSlotsByName(ConfirmDialog)

    def retranslateUi(self, ConfirmDialog):
        _translate = QtCore.QCoreApplication.translate
        ConfirmDialog.setWindowTitle(_translate("ConfirmDialog", "Confirmar ação"))
        self.description_text.setText(_translate("ConfirmDialog", "Cuidado, você vai movimentar o robô para a posição inicial, caso tenha risco de colisão, movimente o robô para a posição inicial manualmente!"))
        self.btn_confirm.setText(_translate("ConfirmDialog", "Confirmar"))
        self.btn_cancel.setText(_translate("ConfirmDialog", "Cancelar"))
import ui_py.icons_rc
