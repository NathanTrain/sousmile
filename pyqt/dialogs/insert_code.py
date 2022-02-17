"""Dialog for insert code manually in the HomeScreen"""

from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QDialog

from ui_py.ui_cod_dialog_win import Ui_Dialog
from utils.gui_functions import write_QlineEdit
from utils.Types import TagTypes

class InsertCodeDialog(QDialog):
    def __init__(self, parents=None):
        super(InsertCodeDialog, self).__init__(parents)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.TAG_INDEX: str = ""
        self.TAG_TYPE: TagTypes = ""

        regex = QRegExp(r"[\w\S]*")
        self.validator = QRegExpValidator(regex)

        self.set_button()

    def closeEvent(self, event) -> None:
        """Activated when the Dialog is closed"""
        self.ui.txt_code.clear()

    def show_dialog(self, tag: str, tag_type: TagTypes):
        """
        Pop up the dialog in the screen

        Params:
            tag: the PLC tag that the value of LineEdit will change
            tag_type = the value's type that will be sent to the PLC
        """
        self.TAG_INDEX = tag
        self.TAG_TYPE = tag_type
        self.ui.txt_code.setValidator(self.validator)
        self.exec_()

    def set_button(self):
        """Set the button of the dialog"""
        self.ui.btn_insert_code_man.clicked.connect(
            lambda: write_LineEdit(self.TAG_INDEX, self,
                                   self.ui.txt_code, self.TAG_TYPE)
        )
