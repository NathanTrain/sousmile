# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\pyqt\ui\cod_dialog_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 275)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(480, 275))
        Dialog.setMaximumSize(QtCore.QSize(480, 275))
        Dialog.setStyleSheet("* {margin:0; padding:0; border: 0}\n"
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
"QLineEdit{\n"
"background-color: white;\n"
"border: 2px solid #b0b0b0;\n"
"border-radius: 18\n"
"}\n"
"QLineEdit {\\ncolor: black; \\nbackground-color: white;\\nborder-width: 1px;\\nborder-radius: 25px;\\n}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 120))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_4.setMaximumSize(QtCore.QSize(230, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Equinox Bold")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.frame_7 = QtWidgets.QFrame(self.frame_4)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.le_etapa = QtWidgets.QLineEdit(self.frame_7)
        self.le_etapa.setMinimumSize(QtCore.QSize(90, 45))
        self.le_etapa.setMaximumSize(QtCore.QSize(90, 45))
        font = QtGui.QFont()
        font.setFamily("Equinox Bold")
        font.setPointSize(14)
        self.le_etapa.setFont(font)
        self.le_etapa.setText("")
        self.le_etapa.setAlignment(QtCore.Qt.AlignCenter)
        self.le_etapa.setObjectName("le_etapa")
        self.horizontalLayout_4.addWidget(self.le_etapa)
        self.verticalLayout_3.addWidget(self.frame_7)
        self.horizontalLayout_3.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_5.setMaximumSize(QtCore.QSize(230, 16777215))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Equinox Bold")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.le_pos = QtWidgets.QLineEdit(self.frame_6)
        self.le_pos.setMinimumSize(QtCore.QSize(90, 45))
        self.le_pos.setMaximumSize(QtCore.QSize(90, 45))
        font = QtGui.QFont()
        font.setFamily("Equinox Bold")
        font.setPointSize(14)
        self.le_pos.setFont(font)
        self.le_pos.setText("")
        self.le_pos.setAlignment(QtCore.Qt.AlignCenter)
        self.le_pos.setObjectName("le_pos")
        self.horizontalLayout_6.addWidget(self.le_pos)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.horizontalLayout_3.addWidget(self.frame_5)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setMinimumSize(QtCore.QSize(0, 46))
        self.frame.setMaximumSize(QtCore.QSize(10000, 46))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(25, 0, 25, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 25))
        self.label.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Equinox Bold")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.le_code = QtWidgets.QLineEdit(self.frame)
        self.le_code.setMinimumSize(QtCore.QSize(280, 45))
        self.le_code.setMaximumSize(QtCore.QSize(280, 45))
        font = QtGui.QFont()
        font.setFamily("Equinox Bold")
        font.setPointSize(14)
        self.le_code.setFont(font)
        self.le_code.setText("")
        self.le_code.setAlignment(QtCore.Qt.AlignCenter)
        self.le_code.setObjectName("le_code")
        self.horizontalLayout.addWidget(self.le_code)
        self.verticalLayout.addWidget(self.frame)
        self.frame_8 = QtWidgets.QFrame(Dialog)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 20))
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 20))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lbl_info = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setFamily("Equinox Bold")
        font.setPointSize(10)
        self.lbl_info.setFont(font)
        self.lbl_info.setText("")
        self.lbl_info.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_info.setObjectName("lbl_info")
        self.horizontalLayout_5.addWidget(self.lbl_info)
        self.verticalLayout.addWidget(self.frame_8)
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 52))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 52))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_insert_code_man = QtWidgets.QPushButton(self.frame_2)
        self.btn_insert_code_man.setMinimumSize(QtCore.QSize(320, 50))
        self.btn_insert_code_man.setMaximumSize(QtCore.QSize(320, 50))
        font = QtGui.QFont()
        font.setFamily("Equinox Bold")
        font.setPointSize(14)
        self.btn_insert_code_man.setFont(font)
        self.btn_insert_code_man.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_insert_code_man.setStyleSheet("")
        self.btn_insert_code_man.setAutoDefault(False)
        self.btn_insert_code_man.setDefault(True)
        self.btn_insert_code_man.setObjectName("btn_insert_code_man")
        self.horizontalLayout_2.addWidget(self.btn_insert_code_man)
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Inserir código manualmente"))
        self.label_2.setText(_translate("Dialog", "Etapa:"))
        self.le_etapa.setPlaceholderText(_translate("Dialog", "00"))
        self.label_3.setText(_translate("Dialog", "Posição:"))
        self.le_pos.setPlaceholderText(_translate("Dialog", "a"))
        self.label.setText(_translate("Dialog", "Código:"))
        self.le_code.setPlaceholderText(_translate("Dialog", "abcd"))
        self.btn_insert_code_man.setText(_translate("Dialog", "Inserir código"))
