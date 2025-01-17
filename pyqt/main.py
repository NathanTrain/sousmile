#######################################################################################################
### CR 967 - Sousmile
### RN Robotics
#######################################################################################################
# Importações
#######################################################################################################
import sys

import serial
from PyQt5.QtCore import QThreadPool
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication

from ui_py.ui_gui_final import Ui_MainWindow

from security.functions import UpdateUserAccess

from utils.functions.serial_ports import get_serial_ports, set_my_port, get_my_port
from utils.workers.workers import *

from screens import home, robot, alarms, \
    production as prod, maintenance as maint, \
    engineering as eng, in_out as inOut, coord_filter as cf

from dialogs.alarm import AlarmDialog
from dialogs.barcode_config import BarCodeDialog
# from dialogs.checkUF import CheckUserFrame
from dialogs.check_uf import CheckUF
from dialogs.confirmation import ConfirmationDialog
from dialogs.login import LoginDialog
from dialogs.insert_code import InsertCodeDialog


#######################################################################################################

class RnRobotics_Gui(QMainWindow):
    def __init__(self):
        super(RnRobotics_Gui, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        ##################################################################
        # Defining dialogs
        ##################################################################
        self.alarm_dialog = AlarmDialog(self)
        self.config_barcode_dialog = BarCodeDialog(self)
        # self.check_uf = CheckUserFrame(self)
        self.check_uf = CheckUF(self)
        self.confirm_dialog = ConfirmationDialog(self)
        self.login_dialog = LoginDialog(self)
        self.insert_code_dialog = InsertCodeDialog(self)
        ##################################################################
        # Initial configuration
        ##################################################################
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_screen)
        self.setWindowTitle("HMI SouSmile")
        self.ui.lbl_username.setText("Nenhum usuário logado")
        ##################################################################
        # Thread - to update PLC values
        ##################################################################
        self.threadpool_1 = QThreadPool()
        self.threadpool_2 = QThreadPool()
        self.threadpool_3 = QThreadPool()
        self.threadpool_4 = QThreadPool()
        self.threadpool_5 = QThreadPool()
        self.threadpool_6 = QThreadPool()
        self.threadpool_7 = QThreadPool()
        self.threadpool_8 = QThreadPool()
        self.threadpool_9 = QThreadPool()
        self.threadpool_10 = QThreadPool()
        self.threadpool_11 = QThreadPool()
        self.threadpool_12 = QThreadPool()
        self.threadpool_13 = QThreadPool()
        self.threadpool_14 = QThreadPool()
        self.threadpool_15 = QThreadPool()
        self.thread_read_tags = QThreadPool()
        ###################################################################
        # Workers
        ###################################################################
        self.worker_data_ctrl_a1 = Worker_Data_Ctrl_A1()
        self.worker_data_ctrl_a2 = Worker_Data_Ctrl_A2()
        self.worker_data_ctrl_b1 = Worker_Data_Ctrl_B1()
        self.worker_data_ctrl_b2 = Worker_Data_Ctrl_B2()
        self.worker_hmi = Worker_HMI()
        self.worker_config_pts = Worker_Config_Pts()
        self.worker_cylDoorA = Worker_Cyl_Door_A()
        self.worker_cylDoorB = Worker_Cyl_Door_B()
        self.worker_cylSpindle = Worker_Cyl_Spindle()
        self.worker_robotInputs = Worker_Robot_Inputs()
        self.worker_robotOutputs = Worker_Robot_Outputs()
        self.worker_indexRobotPos = Worker_IndexRobotPos()
        self.worker_alarm = Worker_Alarms()
        self.worker_inOut = Worker_InOut()
        self.worker_user = Worker_User()
        self.worker_read_tags = Worker_ReadTags()
        ###########################################################################################
        # Connect results of the workers
        ###########################################################################################
        self.worker_data_ctrl_a1.signal_a1.result.connect(self.update_DataCtrl_A1)
        self.worker_data_ctrl_a2.signal_a2.result.connect(self.update_DataCtrl_A2)
        self.worker_data_ctrl_b1.signal_b1.result.connect(self.update_DataCtrl_B1)
        self.worker_data_ctrl_b2.signal_b2.result.connect(self.update_DataCtrl_B2)
        ###########################################################################################
        # !!! Update tag HMI --> Quando um erro acontece o sinal de erro também chama a função para
        # que mude os status dos botões e outros widgets
        ###########################################################################################
        self.worker_hmi.signal_hmi.result.connect(self.update_hmi)
        self.worker_hmi.signal_hmi.error.connect(self.update_hmi)
        ###########################################################################################
        self.worker_config_pts.signal_configPts.result.connect(self.update_ConfigPontos)
        self.worker_cylDoorA.signal_cylDoorA.result.connect(self.update_CylDoorSideA)
        self.worker_cylDoorB.signal_cylDoorB.result.connect(self.update_CylDoorSideB)
        self.worker_cylSpindle.signal_cylSpindle.result.connect(self.update_CylSpindle)
        self.worker_indexRobotPos.signal_indexRobotPos.result.connect(self.update_indexRobotPos)
        self.worker_robotInputs.signal_roboInput.result.connect(self.update_RoboInput)
        self.worker_robotOutputs.signal_robotOutput.result.connect(self.update_RoboOutput)
        self.worker_alarm.signal_alarm.result.connect(self.update_Alarms)
        self.worker_inOut.signal_inOut.result.connect(self.update_InOut)
        self.worker_user.signal_user.result.connect(lambda signal: UpdateUserAccess(signal, self.ui))
        self.worker_read_tags.signal_ReadTags.result.connect(self.update_tag_list)
        ###################################################################
        # Start the threads
        ###################################################################
        self.threadpool_1.start(self.worker_data_ctrl_a1)
        self.threadpool_2.start(self.worker_data_ctrl_a2)
        self.threadpool_3.start(self.worker_data_ctrl_b1)
        self.threadpool_4.start(self.worker_data_ctrl_b2)
        self.threadpool_5.start(self.worker_hmi)
        self.threadpool_6.start(self.worker_config_pts)
        self.threadpool_7.start(self.worker_cylDoorA)
        self.threadpool_8.start(self.worker_cylDoorB)
        self.threadpool_9.start(self.worker_robotInputs)
        self.threadpool_10.start(self.worker_robotOutputs)
        self.threadpool_11.start(self.worker_cylSpindle)
        self.threadpool_12.start(self.worker_indexRobotPos)
        self.threadpool_13.start(self.worker_alarm)
        self.threadpool_14.start(self.worker_inOut)
        self.threadpool_15.start(self.worker_user)
        self.thread_read_tags.start(self.worker_read_tags)
        ###################################################################
        # Defining buttons of screens
        ###################################################################
        self.define_navigate_buttons()
        home.define_buttons(self.ui, self.insert_code_dialog)
        robot.define_buttons(self.ui)
        alarms.define_buttons(self.ui, self.alarm_dialog, self.show_alarm)
        prod.define_buttons(self.ui)
        maint.define_buttons(self.ui, self.confirm_dialog, self.check_uf)
        eng.define_buttons(self.ui, self.config_barcode_dialog)
        inOut.define_buttons(self.ui, self.show_maintenance)
        ###################################################################
        # Defining Coord Filter
        ###################################################################
        self.coord_filter = cf.CoordFilter(self.ui, self.ui.coord_filter)
        self.coord_filter.my_worker_bcscanner.signal.result.connect(self.update_BarCode)
        ###################################################################
        if self.coord_filter.my_worker_bcscanner.device_connected:
            self.ui.btn_config_barcode.setEnabled(False)
        else:
            self.ui.btn_config_barcode.setEnabled(True)
        ###################################################################
        self.ui.graphicView_A1.scale(2.5, 2.5)
        self.ui.graphicView_A1.rotate(180)
        self.ui.graphicView_A2.scale(2.5, 2.5)
        self.ui.graphicView_A2.rotate(180)
        self.ui.graphicView_B1.scale(2.5, 2.5)
        self.ui.graphicView_B1.rotate(180)
        self.ui.graphicView_B2.scale(2.5, 2.5)
        self.ui.graphicView_B2.rotate(180)

    ####################################################################
    # Bar Code Scanner Function
    ####################################################################
    def create_device(self):
        self.port = get_my_port()
        time.sleep(1)
        try:
            if self.port:
                self.device = serial.Serial(self.port, timeout=0.5)
                self.device_connected = True
                print("Dispositivo conectado")
            else:
                raise Exception("Nenhuma ou mais de uma porta serial encontrada")
        except Exception as e:
            print(e)
            time.sleep(2)

    ####################################################################
    # functions to navigate between screens
    ####################################################################
    def define_navigate_buttons(self):
        ### control screen
        self.ui.btnHomeScreen.clicked.connect(self.show_home)
        self.ui.btnRobotScreen.clicked.connect(self.show_robot)
        self.ui.btnAlarmScreen.clicked.connect(self.show_alarm)
        self.ui.btnProductionScreen.clicked.connect(self.show_production)
        self.ui.btnMaintenaceScreen.clicked.connect(self.show_maintenance)
        self.ui.btnEngineeringScreen.clicked.connect(self.show_engineering)
        self.ui.btn_in_out_screen.clicked.connect(self.show_in_out)
        self.ui.btnCoordFilterScreen.clicked.connect(self.show_coor_filter)
        ### login and logout
        self.ui.btnLogin.clicked.connect(lambda: self.login_dialog.show_dialog(self.ui.lbl_username))
        self.ui.btnLogout.clicked.connect(self.login_dialog.logout_user)
        ### alarm
        self.ui.btn_atual_alarm.clicked.connect(self.show_alarm)
        self.ui.btn_hist_alarm.clicked.connect(self.show_alarm_history)

    #######################################################################
    def show_home(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_screen)

    #######################################################################
    def show_robot(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.robot_screen)

    #######################################################################
    def show_alarm(self):
        self.ui.alarm_list_widget.horizontalHeader().setVisible(True)
        self.ui.stackedWidget.setCurrentWidget(self.ui.alarms_screen)

    #######################################################################
    def show_production(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.production_screen)

    #######################################################################
    def show_coor_filter(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.coord_filter)

    #######################################################################
    def show_maintenance(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.maintenace_screen)

    #######################################################################
    def show_in_out(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.inOut_screen)

    #######################################################################
    def show_engineering(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.engineering_screen)

    #######################################################################
    def show_alarm_history(self):
        self.ui.hist_alarm_list_widget.horizontalHeader().setVisible(True)
        self.ui.stackedWidget.setCurrentWidget(self.ui.alarm_history_screen)

    #######################################################################
    # Updating Tags on the PLC
    #######################################################################
    def update_DataCtrl_A1(self, tag):
        if self.ui.stackedWidget.currentIndex() == 0:
            home.UpdateDataCtrl_A1(tag)
        elif self.ui.stackedWidget.currentIndex() == 3:
            prod.UpdateDataCtrl_A1(tag)

    #######################################################################
    def update_DataCtrl_A2(self, tag):
        if self.ui.stackedWidget.currentIndex() == 0:
            home.UpdateDataCtrl_A2(tag)
        elif self.ui.stackedWidget.currentIndex() == 3:
            prod.UpdateDataCtrl_A2(tag)

    #######################################################################
    def update_DataCtrl_B1(self, tag):
        if self.ui.stackedWidget.currentIndex() == 0:
            home.UpdateDataCtrl_B1(tag)
        elif self.ui.stackedWidget.currentIndex() == 3:
            prod.UpdateDataCtrl_B1(tag)

    #######################################################################
    def update_DataCtrl_B2(self, tag):
        if self.ui.stackedWidget.currentIndex() == 0:
            home.UpdateDataCtrl_B2(tag)
        elif self.ui.stackedWidget.currentIndex() == 3:
            prod.UpdateDataCtrl_B2(tag)

    #######################################################################
    def update_hmi(self, tag):
        if type(tag) is tuple:
            home.UpdateHMI(tag)
            robot.UpdateHMI(tag)
            prod.UpdateHMI(tag)
            maint.UpdateHMI(tag)
            eng.UpdateHMI(tag)
        else:
            if self.ui.stackedWidget.currentIndex() == 0:
                home.UpdateHMI(tag)
            elif self.ui.stackedWidget.currentIndex() == 1:
                robot.UpdateHMI(tag)
            elif self.ui.stackedWidget.currentIndex() == 3:
                prod.UpdateHMI(tag)
            elif self.ui.stackedWidget.currentIndex() == 5:
                maint.UpdateHMI(tag)
            elif self.ui.stackedWidget.currentIndex() == 7:
                eng.UpdateHMI(tag)

    ########################################################################
    def update_ConfigPontos(self, tag):
        if self.ui.stackedWidget.currentIndex() == 7:
            eng.UpdateConfigPts(tag)

    ########################################################################
    def update_CylDoorSideA(self, tag):
        if self.ui.stackedWidget.currentIndex() == 5:
            maint.UpdateCylA(tag)
        elif self.ui.stackedWidget.currentIndex() == 7:
            eng.UpdateCylA(tag)

    ########################################################################
    def update_CylDoorSideB(self, tag):
        if self.ui.stackedWidget.currentIndex() == 5:
            maint.UpdateCylB(tag)
        elif self.ui.stackedWidget.currentIndex() == 7:
            eng.UpdateCylB(tag)

    ########################################################################
    def update_CylSpindle(self, tag):
        if self.ui.stackedWidget.currentIndex() == 5:
            maint.UpdateCylSpindle(tag)

    ########################################################################
    def update_indexRobotPos(self, tag):
        if self.ui.stackedWidget.currentIndex() == 7:
            eng.UpdateRobotPos(tag)

    ########################################################################
    def update_RoboInput(self, tag):
        if self.ui.stackedWidget.currentIndex() == 0:
            home.UpdateRobotInput(tag)
        elif self.ui.stackedWidget.currentIndex() == 1:
            robot.UpdateInput(tag)
        elif self.ui.stackedWidget.currentIndex() == 5:
            maint.UpdateRobotInput(tag)

    ########################################################################
    def update_RoboOutput(self, tag):
        if self.ui.stackedWidget.currentIndex() == 1:
            robot.UpdateOutput(tag)
        elif self.ui.stackedWidget.currentIndex() == 5:
            maint.UpdateRobotOutputs(tag)
        elif self.ui.stackedWidget.currentIndex() == 7:
            eng.UpdateRobotOutput(tag)

    ########################################################################
    def update_BarCode(self, tag):
        maint.UpdateBarCode(tag)

        if tag["Connected"]:
            self.ui.btn_config_barcode.setEnabled(False)
        else:
            self.ui.btn_config_barcode.setEnabled(True)

        serial_ports = get_serial_ports()
        if len(serial_ports) == 1:
            set_my_port(serial_ports[0])

    ########################################################################
    def update_Alarms(self, tag):
        alarms.UpdateAlarms(tag)

    ########################################################################
    def update_InOut(self, tag):
        if self.ui.stackedWidget.currentIndex() == 5:
            inOut.UpdateInOut(tag)

    ########################################################################
    def update_tag_list(self, tags):
        if self.ui.stackedWidget.currentIndex() == 0:
            home.UpdateTagsList(tags)
        elif self.ui.stackedWidget.currentIndex() == 1:
            robot.UpdateTagsList(tags)
        elif self.ui.stackedWidget.currentIndex() == 5:
            maint.UpdateTagsList(tags)
        elif self.ui.stackedWidget.currentIndex() == 7:
            eng.UpdateTagsList(tags)

    ########################################################################
    # Stop Threads
    ########################################################################
    def stop_threads(self):
        print("Finalizando Threads")
        try:
            self.worker_data_ctrl_a1.stop()
            self.worker_data_ctrl_a2.stop()
            self.worker_data_ctrl_b1.stop()
            self.worker_data_ctrl_b2.stop()
            self.worker_hmi.stop()
            self.worker_config_pts.stop()
            self.worker_cylDoorA.stop()
            self.worker_cylDoorB.stop()
            self.worker_robotInputs.stop()
            self.worker_robotOutputs.stop()
            self.worker_cylSpindle.stop()
            self.worker_indexRobotPos.stop()
            self.worker_alarm.stop()
            self.worker_inOut.stop()
            self.worker_user.stop()
            self.worker_read_tags.stop()
            self.coord_filter.stop_threads()
        except Exception as e:
            print(f"{e} -> main.py - stop_threads")
        print("Threads finalizadas")


#######################################################################################################

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = RnRobotics_Gui()
    main_win.showMaximized()
    main_win.setWindowIcon(QIcon("./assets/images/RN_Logo.png"))
    app.aboutToQuit.connect(main_win.stop_threads)
    sys.exit(app.exec_())
