from PyQt5 import QtCore, QtGui, QtWidgets
from testcase import network_layer_for_computer
from main import run_simulation, SimulationReader
from time import sleep


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(240, 260, 321, 16))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(240, 300, 321, 16))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 120, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Wire0to1 = QtWidgets.QLabel(self.centralwidget)
        self.Wire0to1.setGeometry(QtCore.QRect(250, 150, 95, 108))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Wire0to1.setFont(font)
        self.Wire0to1.setObjectName("Wire0to1")
        self.Error0to1 = QtWidgets.QCheckBox(self.centralwidget)
        self.Error0to1.setEnabled(False)
        self.Error0to1.setGeometry(QtCore.QRect(440, 220, 66, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.Error0to1.setFont(font)
        self.Error0to1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Error0to1.setChecked(False)
        self.Error0to1.setObjectName("Error0to1")
        self.Error1to0 = QtWidgets.QCheckBox(self.centralwidget)
        self.Error1to0.setEnabled(False)
        self.Error1to0.setGeometry(QtCore.QRect(290, 320, 66, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.Error1to0.setFont(font)
        self.Error1to0.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Error1to0.setChecked(False)
        self.Error1to0.setObjectName("Error1to0")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(420, 320, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setUnderline(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Wire1to0 = QtWidgets.QLabel(self.centralwidget)
        self.Wire1to0.setGeometry(QtCore.QRect(420, 350, 121, 108))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Wire1to0.setFont(font)
        self.Wire1to0.setObjectName("Wire1to0")
        self.TimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.TimeLabel.setGeometry(QtCore.QRect(360, 30, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TimeLabel.setFont(font)
        self.TimeLabel.setObjectName("TimeLabel")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 500, 761, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.PrevStepBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.PrevStepBtn.setObjectName("PrevStepBtn")
        self.horizontalLayout.addWidget(self.PrevStepBtn)
        self.NextStepBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.NextStepBtn.setObjectName("NextStepBtn")
        self.horizontalLayout.addWidget(self.NextStepBtn)
        self.StopBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.StopBtn.setObjectName("StopBtn")
        self.horizontalLayout.addWidget(self.StopBtn)
        self.AutoPlayBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.AutoPlayBtn.setObjectName("AutoPlayBtn")
        self.horizontalLayout.addWidget(self.AutoPlayBtn)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 10, 202, 478))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.Comp0NetS = QtWidgets.QLabel(self.layoutWidget1)
        self.Comp0NetS.setMinimumSize(QtCore.QSize(0, 110))
        self.Comp0NetS.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Comp0NetS.setFont(font)
        self.Comp0NetS.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Comp0NetS.setObjectName("Comp0NetS")
        self.verticalLayout.addWidget(self.Comp0NetS)
        self.Comp0TextEdit = QtWidgets.QTextEdit(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Comp0TextEdit.sizePolicy().hasHeightForWidth())
        self.Comp0TextEdit.setSizePolicy(sizePolicy)
        self.Comp0TextEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.Comp0TextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Comp0TextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Comp0TextEdit.setReadOnly(True)
        self.Comp0TextEdit.setObjectName("Comp0TextEdit")
        self.verticalLayout.addWidget(self.Comp0TextEdit)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setUnderline(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.Comp0NetR = QtWidgets.QLabel(self.layoutWidget1)
        self.Comp0NetR.setMinimumSize(QtCore.QSize(0, 110))
        self.Comp0NetR.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Comp0NetR.setFont(font)
        self.Comp0NetR.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Comp0NetR.setObjectName("Comp0NetR")
        self.verticalLayout.addWidget(self.Comp0NetR)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(557, 10, 258, 478))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setUnderline(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.Comp1NetS = QtWidgets.QLabel(self.layoutWidget2)
        self.Comp1NetS.setMinimumSize(QtCore.QSize(0, 110))
        self.Comp1NetS.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Comp1NetS.setFont(font)
        self.Comp1NetS.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Comp1NetS.setObjectName("Comp1NetS")
        self.verticalLayout_2.addWidget(self.Comp1NetS)
        self.Comp1TextEdit = QtWidgets.QTextEdit(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Comp1TextEdit.sizePolicy().hasHeightForWidth())
        self.Comp1TextEdit.setSizePolicy(sizePolicy)
        self.Comp1TextEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        self.Comp1TextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Comp1TextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Comp1TextEdit.setReadOnly(True)
        self.Comp1TextEdit.setObjectName("Comp1TextEdit")
        self.verticalLayout_2.addWidget(self.Comp1TextEdit)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setUnderline(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.Comp1NetR = QtWidgets.QLabel(self.layoutWidget2)
        self.Comp1NetR.setMinimumSize(QtCore.QSize(0, 110))
        self.Comp1NetR.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Comp1NetR.setFont(font)
        self.Comp1NetR.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Comp1NetR.setObjectName("Comp1NetR")
        self.verticalLayout_2.addWidget(self.Comp1NetR)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSelectSimulationFile = QtWidgets.QAction(MainWindow)
        self.actionSelectSimulationFile.setObjectName("actionSelectSimulationFile")
        self.menuFile.addAction(self.actionSelectSimulationFile)
        self.menubar.addAction(self.menuFile.menuAction())
        self.Comp0NetS.setWordWrap(True)
        self.Comp0NetR.setWordWrap(True)
        self.Comp1NetS.setWordWrap(True)
        self.Comp1NetR.setWordWrap(True)
        self.AutoPlayBtn.setEnabled(False)

        self.NextStepBtn.clicked.connect(self.next_timestep)
        self.PrevStepBtn.clicked.connect(self.prev_timestep)
        self.AutoPlayBtn.clicked.connect(self.auto_play)
        self.StopBtn.clicked.connect(self.stop)

        self.reader = SimulationReader()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DataLink Layer Simulator"))
        self.label_2.setText(_translate("MainWindow", "Wire From 0 to 1:"))
        self.Wire0to1.setText(_translate("MainWindow", "Frame(\n"
"    kind=None,\n"
"   seq=None,\n"
"   ack=None,\n"
"   info=None\n"
")"))
        self.Error0to1.setText(_translate("MainWindow", "Error"))
        self.Error1to0.setText(_translate("MainWindow", "Error"))
        self.label_4.setText(_translate("MainWindow", "Wire From 1 to 0:"))
        self.Wire1to0.setText(_translate("MainWindow", "Frame(\n"
"    kind=None,\n"
"   seq=None,\n"
"   ack=None,\n"
"   info=None\n"
")"))
        self.TimeLabel.setText(_translate("MainWindow", "t=-1"))
        self.PrevStepBtn.setText(_translate("MainWindow", "Prev. Time Step"))
        self.NextStepBtn.setText(_translate("MainWindow", "Next Time Step"))
        self.StopBtn.setText(_translate("MainWindow", "Stop"))
        self.AutoPlayBtn.setText(_translate("MainWindow", "Auto Play"))
        self.label.setText(_translate("MainWindow", "Network Layer to Send:"))
        print(network_layer_for_computer)
        self.Comp0NetS.setText(_translate("MainWindow", str(network_layer_for_computer[0])))
        self.Comp0TextEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; text-decoration: underline;\">C0 Datalink Layer:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">events =</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">[]</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">buffer: </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">[None, None, None, None,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">None, None, None, None]</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">n_buffered: 0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">next_frame_to_send: 0</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "Network Layer Received:"))
        self.Comp0NetR.setText(_translate("MainWindow", ""))
        self.label_3.setText(_translate("MainWindow", "Network Layer to Send:"))
        self.Comp1NetS.setText(_translate("MainWindow",  str(network_layer_for_computer[1])))
        self.Comp1TextEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; text-decoration: underline;\">C1 Datalink Layer:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">events:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">[]</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">buffer: </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">[None, None, None, None,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">None, None, None, None]</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">n_buffered: 0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">next_frame_to_send: 0</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "Network Layer Received:"))
        self.Comp1NetR.setText(_translate("MainWindow", ""))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSelectSimulationFile.setText(_translate("MainWindow", "Select Simulation File"))


    def _show(self, state):
        t, computeri, network_layer_data_to_send, network_layer_data_received, events, buffer, n_buffered, next_frame_to_send, error, wire_fromi = state

        events = [event.name for event in events]
        # buffer = '[{},{},{},{},\n{},{},{},{}]'.format(*buffer)
        wire_fromi = ('Frame(\n    kind={}\n    seq={}\n    ack={}\n    info={}\n)'
                      .format(wire_fromi.kind.name, wire_fromi.seq, wire_fromi.ack, wire_fromi.info)
                      if wire_fromi is not None else str(None))
        compi_text = ("C{} Datalink Layer:\nevents:\n{}\n\nbuffer:\n{}\n\nn_buffered:{}\nnext_frame_to_send:{}"
                      .format(computeri, events, buffer, n_buffered, next_frame_to_send))

        self.TimeLabel.setText('t=' + str(t))
        if computeri == 0:
            self.Comp0NetS.setText(str(network_layer_data_to_send))
            self.Comp0NetR.setText(str(network_layer_data_received))
            self.Comp0TextEdit.setText(compi_text)
            self.Wire0to1.setText(wire_fromi)
            self.Error0to1.setChecked(error)
        else:
            self.Comp1NetS.setText(str(network_layer_data_to_send))
            self.Comp1NetR.setText(str(network_layer_data_received))
            self.Comp1TextEdit.setText(compi_text)
            self.Wire1to0.setText(wire_fromi)
            self.Error1to0.setChecked(error)

    def next_timestep(self):
        if self.TimeLabel.text() == 't=99':
            return
        state = self.reader.get_next_timestep()
        self._show(state)

    def prev_timestep(self):
        t_prev = int(self.TimeLabel.text()[2:]) - 1
        t_prev = t_prev if t_prev>0 else 0
        state = self.reader.get_specific_timestep(t_prev-1)
        self._show(state)
        state = self.reader.get_next_timestep()
        self._show(state)

    def stop(self):
        self.stop_autoplay = True

    def auto_play(self):
        self.stop_autoplay = False
        self.reader.reset()
        for state in self.reader:
            self._show(state)
            sleep(0.5)
            if self.stop_autoplay:
                break


if __name__ == "__main__":
    import sys
    run_simulation()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
