########################################################################################
# Contorl of widgets home screen
########################################################################################
from pyqt.ui_py.ui_gui import Ui_MainWindow
from PyQt5.QtWidgets import QLabel
from pyqt.utils.gui_functions import set_reset_button
from pyqt.utils.Types import AltValShowDialog_WithoutText


def sts_string(id_num: int, widget: QLabel):
    if id_num == 100:
        widget.setText('Transferencia do codigo da peca habilitado para o lado A1')
    elif id_num == 110:
        widget.setText('Transferencia do lado A1 aguardando python iniciar a transferencia')
    elif id_num == 120:
        widget.setText('Transferencia iniciou A1  python -> CLP')
    elif id_num == 200:
        widget.setText('Transferencia do codigo da peca habilitado para o lado A2')
    elif id_num == 210:
        widget.setText('Transferencia do lado A2 aguardando python iniciar a transferencia')
    elif id_num == 220:
        widget.setText('Transferencia iniciou lado A2  python -> CLP')
    elif id_num == 0:
        widget.setText('Aguardando leitura do código')
    else:
        widget.setText('Erro')

def define_buttons(ui: Ui_MainWindow, show_dialog: AltValShowDialog_WithoutText):
    ui.btn_in_cod_man_a1.clicked.connect(lambda: show_dialog('DataCtrl_A1.ProdCode', "string"))
    ui.btn_in_cod_man_a2.clicked.connect(lambda: show_dialog('DataCtrl_A2.ProdCode', "string"))
    ui.btn_in_cod_man_b1.clicked.connect(lambda: show_dialog('DataCtrl_B1.ProdCode', "string"))
    ui.btn_in_cod_man_b2.clicked.connect(lambda: show_dialog('DataCtrl_B2.ProdCode', "string"))

    ui.btn_man_auto_lado_a.clicked.connect(lambda: set_reset_button('HMI.SideA.ModeValue',
                                                                    ui.btn_man_auto_lado_a,
                                                                    'Automático',
                                                                    'Manual'))
    ui.btn_man_auto_lado_b.clicked.connect(lambda: set_reset_button('HMI.SideB.ModeValue',
                                                                    ui.btn_man_auto_lado_b,
                                                                    'Automático',
                                                                    'Manual'))

def UpdateDataCtrl_A1(ui: Ui_MainWindow, tag):
    try:
        ui.lbl_ProdCode_A1.setText(tag['ProdCode'])
        ui.lbl_FileNumPos_A1.setText(str(tag['FileNumPos']))
        ui.lbl_NumPos_A1.setText(str(tag['NumPos']))
        ui.lbl_IndexPos_A1.setText(str(tag['IndexPos']))
    except:
        pass

def UpdateDataCtrl_A2(ui: Ui_MainWindow, tag):
    try:
        ui.lbl_ProdCode_A2.setText(tag['ProdCode'])
        ui.lbl_FileNumPos_A2.setText(str(tag['FileNumPos']))
        ui.lbl_NumPos_A2.setText(str(tag['NumPos']))
        ui.lbl_IndexPos_A2.setText(str(tag['IndexPos']))
    except:
        pass

def UpdateDataCtrl_B1(ui: Ui_MainWindow, tag):
    try:
        ui.lbl_ProdCode_B1.setText(tag['ProdCode'])
        ui.lbl_FileNumPos_B1.setText(str(tag['FileNumPos']))
        ui.lbl_NumPos_B1.setText(str(tag['NumPos']))
        ui.lbl_IndexPos_B1.setText(str(tag['IndexPos']))
    except:
        pass

def UpdateDataCtrl_B2(ui: Ui_MainWindow, tag):
    try:
        ui.lbl_ProdCode_B2.setText(tag['ProdCode'])
        ui.lbl_FileNumPos_B2.setText(str(tag['FileNumPos']))
        ui.lbl_NumPos_B2.setText(str(tag['NumPos']))
        ui.lbl_IndexPos_B2.setText(str(tag['IndexPos']))
    except:
        pass

def UpdateHMI(ui: Ui_MainWindow, tag):
    try:
        prodTag = tag["Production"]
        ui.lbl_production_TimeCutA1.setText(str(round(prodTag['TimeCutA1'], 2)))
        ui.lbl_production_TimeCutA2.setText(str(round(prodTag['TimeCutA2'], 2)))
        ui.lbl_production_TimeCutB1.setText(str(round(prodTag['TimeCutB1'], 2)))
        ui.lbl_production_TimeCutB2.setText(str(round(prodTag['TimeCutB2'], 2)))
        sts_string(tag['Sts']['TransDataSideA'], ui.lbl_sts_TransDataSideA)
        sts_string(tag['Sts']['TransDataSideB'], ui.lbl_sts_TransDataSideB)

        ### buttons manual <-> auto
        if tag['SideA']['ModeValue'] == 0:
            ui.btn_man_auto_lado_a.setChecked(True)
            ui.sts_auto_man_a.setEnabled(True)
            ui.btn_man_auto_lado_a.setText('Manual')
        else:
            ui.btn_man_auto_lado_a.setChecked(False)
            ui.sts_auto_man_a.setEnabled(False)
            ui.btn_man_auto_lado_a.setText('Automático')

        if tag['SideB']['ModeValue'] == 0:
            ui.btn_man_auto_lado_b.setChecked(True)
            ui.sts_auto_man_b.setEnabled(True)
            ui.btn_man_auto_lado_b.setText('Manual')
        else:
            ui.btn_man_auto_lado_b.setChecked(False)
            ui.sts_auto_man_b.setEnabled(False)
            ui.btn_man_auto_lado_b.setText('Automático')

        #### setting alarm status
        if tag["AlarmSideA"]:
            ui.sts_sem_alarm_a.setEnabled(False)
        else:
            ui.sts_sem_alarm_a.setEnabled(True)

        if tag["AlarmSideB"]:
            ui.sts_sem_alarm_b.setEnabled(False)
        else:
            ui.sts_sem_alarm_b.setEnabled(True)
    except Exception as e:
        print(e)
