# Form implementation generated from reading ui file '/home/nixgnauhcuy/My/git_repo/Python/pyqt/QtComMate/src/main.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralWidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.SerialReceiveGroupBox = QtWidgets.QGroupBox(parent=self.centralWidget)
        self.SerialReceiveGroupBox.setGeometry(QtCore.QRect(5, 5, 790, 350))
        self.SerialReceiveGroupBox.setCheckable(False)
        self.SerialReceiveGroupBox.setObjectName("SerialReceiveGroupBox")
        self.formLayoutWidget = QtWidgets.QWidget(parent=self.SerialReceiveGroupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 168, 300))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.SerialReceiveFormLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.SerialReceiveFormLayout.setContentsMargins(0, 0, 0, 0)
        self.SerialReceiveFormLayout.setObjectName("SerialReceiveFormLayout")
        self.SerialComLabel = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.SerialComLabel.setObjectName("SerialComLabel")
        self.SerialReceiveFormLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.SerialComLabel)
        self.SerialComboBox = SerialPort_ComBoBox(parent=self.formLayoutWidget)
        self.SerialComboBox.setObjectName("SerialComboBox")
        self.SerialReceiveFormLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.SerialComboBox)
        self.SerialBaudrateLabel = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.SerialBaudrateLabel.setObjectName("SerialBaudrateLabel")
        self.SerialReceiveFormLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.SerialBaudrateLabel)
        self.SerialBaudrateComboBox = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        self.SerialBaudrateComboBox.setObjectName("SerialBaudrateComboBox")
        self.SerialBaudrateComboBox.addItem("")
        self.SerialBaudrateComboBox.addItem("")
        self.SerialBaudrateComboBox.addItem("")
        self.SerialBaudrateComboBox.addItem("")
        self.SerialBaudrateComboBox.addItem("")
        self.SerialBaudrateComboBox.addItem("")
        self.SerialBaudrateComboBox.addItem("")
        self.SerialBaudrateComboBox.addItem("")
        self.SerialBaudrateComboBox.addItem("")
        self.SerialBaudrateComboBox.addItem("")
        self.SerialBaudrateComboBox.addItem("")
        self.SerialBaudrateComboBox.addItem("")
        self.SerialBaudrateComboBox.addItem("")
        self.SerialBaudrateComboBox.addItem("")
        self.SerialBaudrateComboBox.addItem("")
        self.SerialBaudrateComboBox.addItem("")
        self.SerialBaudrateComboBox.addItem("")
        self.SerialBaudrateComboBox.addItem("")
        self.SerialBaudrateComboBox.addItem("")
        self.SerialBaudrateComboBox.addItem("")
        self.SerialBaudrateComboBox.addItem("")
        self.SerialBaudrateComboBox.addItem("")
        self.SerialBaudrateComboBox.addItem("")
        self.SerialReceiveFormLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.SerialBaudrateComboBox)
        self.SerialStopBitLabel = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.SerialStopBitLabel.setObjectName("SerialStopBitLabel")
        self.SerialReceiveFormLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.SerialStopBitLabel)
        self.SerialStopBitComboBox = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        self.SerialStopBitComboBox.setObjectName("SerialStopBitComboBox")
        self.SerialStopBitComboBox.addItem("")
        self.SerialStopBitComboBox.addItem("")
        self.SerialStopBitComboBox.addItem("")
        self.SerialReceiveFormLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.SerialStopBitComboBox)
        self.SerialDataBitLabel = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.SerialDataBitLabel.setObjectName("SerialDataBitLabel")
        self.SerialReceiveFormLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.SerialDataBitLabel)
        self.SerialDataBitcomboBox = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        self.SerialDataBitcomboBox.setObjectName("SerialDataBitcomboBox")
        self.SerialDataBitcomboBox.addItem("")
        self.SerialDataBitcomboBox.addItem("")
        self.SerialDataBitcomboBox.addItem("")
        self.SerialDataBitcomboBox.addItem("")
        self.SerialReceiveFormLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.SerialDataBitcomboBox)
        self.SerialChecksumBitLabel = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.SerialChecksumBitLabel.setObjectName("SerialChecksumBitLabel")
        self.SerialReceiveFormLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.SerialChecksumBitLabel)
        self.SerialChecksumBitComboBox = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        self.SerialChecksumBitComboBox.setObjectName("SerialChecksumBitComboBox")
        self.SerialChecksumBitComboBox.addItem("")
        self.SerialChecksumBitComboBox.addItem("")
        self.SerialChecksumBitComboBox.addItem("")
        self.SerialChecksumBitComboBox.addItem("")
        self.SerialChecksumBitComboBox.addItem("")
        self.SerialReceiveFormLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.SerialChecksumBitComboBox)
        self.SerialReceiveHexCheckBox = QtWidgets.QCheckBox(parent=self.formLayoutWidget)
        self.SerialReceiveHexCheckBox.setObjectName("SerialReceiveHexCheckBox")
        self.SerialReceiveFormLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.SerialReceiveHexCheckBox)
        self.SerialReceiveTimestampCheckBox = QtWidgets.QCheckBox(parent=self.formLayoutWidget)
        self.SerialReceiveTimestampCheckBox.setObjectName("SerialReceiveTimestampCheckBox")
        self.SerialReceiveFormLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.SerialReceiveTimestampCheckBox)
        self.SerialReceiveClearPushButton = QtWidgets.QPushButton(parent=self.formLayoutWidget)
        self.SerialReceiveClearPushButton.setObjectName("SerialReceiveClearPushButton")
        self.SerialReceiveFormLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.SerialReceiveClearPushButton)
        self.SerialConnectComPushButton = QtWidgets.QPushButton(parent=self.formLayoutWidget)
        self.SerialConnectComPushButton.setObjectName("SerialConnectComPushButton")
        self.SerialReceiveFormLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.SerialConnectComPushButton)
        self.SerialReceiveTextEdit = QtWidgets.QTextEdit(parent=self.SerialReceiveGroupBox)
        self.SerialReceiveTextEdit.setGeometry(QtCore.QRect(190, 30, 591, 311))
        self.SerialReceiveTextEdit.setObjectName("SerialReceiveTextEdit")
        self.SerialSendGroupBox = QtWidgets.QGroupBox(parent=self.centralWidget)
        self.SerialSendGroupBox.setGeometry(QtCore.QRect(5, 360, 790, 211))
        self.SerialSendGroupBox.setObjectName("SerialSendGroupBox")
        self.SerialSendTextEdit = QtWidgets.QTextEdit(parent=self.SerialSendGroupBox)
        self.SerialSendTextEdit.setGeometry(QtCore.QRect(10, 30, 641, 111))
        self.SerialSendTextEdit.setObjectName("SerialSendTextEdit")
        self.SerialSendRepeatGroupBox = QtWidgets.QGroupBox(parent=self.SerialSendGroupBox)
        self.SerialSendRepeatGroupBox.setGeometry(QtCore.QRect(270, 150, 141, 51))
        self.SerialSendRepeatGroupBox.setObjectName("SerialSendRepeatGroupBox")
        self.SerialSendRepeatCheckBox = QtWidgets.QCheckBox(parent=self.SerialSendRepeatGroupBox)
        self.SerialSendRepeatCheckBox.setGeometry(QtCore.QRect(10, 25, 21, 21))
        self.SerialSendRepeatCheckBox.setText("")
        self.SerialSendRepeatCheckBox.setObjectName("SerialSendRepeatCheckBox")
        self.SerialSendRepeatDurationLineEdit = QtWidgets.QLineEdit(parent=self.SerialSendRepeatGroupBox)
        self.SerialSendRepeatDurationLineEdit.setGeometry(QtCore.QRect(35, 25, 71, 20))
        self.SerialSendRepeatDurationLineEdit.setObjectName("SerialSendRepeatDurationLineEdit")
        self.SerialSendRepeatUnitLabel = QtWidgets.QLabel(parent=self.SerialSendRepeatGroupBox)
        self.SerialSendRepeatUnitLabel.setGeometry(QtCore.QRect(110, 23, 25, 21))
        self.SerialSendRepeatUnitLabel.setObjectName("SerialSendRepeatUnitLabel")
        self.SerialSendPushButton = QtWidgets.QPushButton(parent=self.SerialSendGroupBox)
        self.SerialSendPushButton.setGeometry(QtCore.QRect(660, 120, 121, 21))
        self.SerialSendPushButton.setObjectName("SerialSendPushButton")
        self.SerialHardFlowControlGroupBox = QtWidgets.QGroupBox(parent=self.SerialSendGroupBox)
        self.SerialHardFlowControlGroupBox.setGeometry(QtCore.QRect(110, 150, 151, 51))
        self.SerialHardFlowControlGroupBox.setObjectName("SerialHardFlowControlGroupBox")
        self.SerialHardFlowControlDSRDTRCheckBox = QtWidgets.QCheckBox(parent=self.SerialHardFlowControlGroupBox)
        self.SerialHardFlowControlDSRDTRCheckBox.setGeometry(QtCore.QRect(10, 25, 71, 20))
        self.SerialHardFlowControlDSRDTRCheckBox.setObjectName("SerialHardFlowControlDSRDTRCheckBox")
        self.SerialHardFlowControlRTSCTSCheckBox = QtWidgets.QCheckBox(parent=self.SerialHardFlowControlGroupBox)
        self.SerialHardFlowControlRTSCTSCheckBox.setGeometry(QtCore.QRect(80, 25, 61, 20))
        self.SerialHardFlowControlRTSCTSCheckBox.setObjectName("SerialHardFlowControlRTSCTSCheckBox")
        self.SerialSendLineFeedGroupBox = QtWidgets.QGroupBox(parent=self.SerialSendGroupBox)
        self.SerialSendLineFeedGroupBox.setGeometry(QtCore.QRect(420, 150, 101, 51))
        self.SerialSendLineFeedGroupBox.setObjectName("SerialSendLineFeedGroupBox")
        self.SerialSendLineFeedComboBox = QtWidgets.QComboBox(parent=self.SerialSendLineFeedGroupBox)
        self.SerialSendLineFeedComboBox.setGeometry(QtCore.QRect(10, 25, 81, 21))
        self.SerialSendLineFeedComboBox.setObjectName("SerialSendLineFeedComboBox")
        self.SerialSendLineFeedComboBox.addItem("")
        self.SerialSendLineFeedComboBox.addItem("")
        self.SerialSendLineFeedComboBox.addItem("")
        self.SerialSendHexCheckBox = QtWidgets.QCheckBox(parent=self.SerialSendGroupBox)
        self.SerialSendHexCheckBox.setGeometry(QtCore.QRect(660, 30, 50, 20))
        self.SerialSendHexCheckBox.setObjectName("SerialSendHexCheckBox")
        self.SerialSoftFlowControlGroupBox = QtWidgets.QGroupBox(parent=self.SerialSendGroupBox)
        self.SerialSoftFlowControlGroupBox.setGeometry(QtCore.QRect(10, 150, 91, 51))
        self.SerialSoftFlowControlGroupBox.setObjectName("SerialSoftFlowControlGroupBox")
        self.SerialSoftFlowControlCheckBox = QtWidgets.QCheckBox(parent=self.SerialSoftFlowControlGroupBox)
        self.SerialSoftFlowControlCheckBox.setGeometry(QtCore.QRect(5, 25, 81, 20))
        self.SerialSoftFlowControlCheckBox.setObjectName("SerialSoftFlowControlCheckBox")
        MainWindow.setCentralWidget(self.centralWidget)
        self.SerialStatusBar = QtWidgets.QStatusBar(parent=MainWindow)
        self.SerialStatusBar.setObjectName("SerialStatusBar")
        MainWindow.setStatusBar(self.SerialStatusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QtComMate"))
        self.SerialReceiveGroupBox.setTitle(_translate("MainWindow", "串口接收设置"))
        self.SerialComLabel.setText(_translate("MainWindow", "COM"))
        self.SerialBaudrateLabel.setText(_translate("MainWindow", "波特率"))
        self.SerialBaudrateComboBox.setItemText(0, _translate("MainWindow", "custom"))
        self.SerialBaudrateComboBox.setItemText(1, _translate("MainWindow", "110"))
        self.SerialBaudrateComboBox.setItemText(2, _translate("MainWindow", "300"))
        self.SerialBaudrateComboBox.setItemText(3, _translate("MainWindow", "600"))
        self.SerialBaudrateComboBox.setItemText(4, _translate("MainWindow", "1200"))
        self.SerialBaudrateComboBox.setItemText(5, _translate("MainWindow", "2400"))
        self.SerialBaudrateComboBox.setItemText(6, _translate("MainWindow", "4800"))
        self.SerialBaudrateComboBox.setItemText(7, _translate("MainWindow", "9600"))
        self.SerialBaudrateComboBox.setItemText(8, _translate("MainWindow", "19200"))
        self.SerialBaudrateComboBox.setItemText(9, _translate("MainWindow", "38400"))
        self.SerialBaudrateComboBox.setItemText(10, _translate("MainWindow", "57600"))
        self.SerialBaudrateComboBox.setItemText(11, _translate("MainWindow", "76800"))
        self.SerialBaudrateComboBox.setItemText(12, _translate("MainWindow", "115200"))
        self.SerialBaudrateComboBox.setItemText(13, _translate("MainWindow", "128000"))
        self.SerialBaudrateComboBox.setItemText(14, _translate("MainWindow", "230400"))
        self.SerialBaudrateComboBox.setItemText(15, _translate("MainWindow", "256000"))
        self.SerialBaudrateComboBox.setItemText(16, _translate("MainWindow", "460800"))
        self.SerialBaudrateComboBox.setItemText(17, _translate("MainWindow", "512000"))
        self.SerialBaudrateComboBox.setItemText(18, _translate("MainWindow", "576000"))
        self.SerialBaudrateComboBox.setItemText(19, _translate("MainWindow", "921600"))
        self.SerialBaudrateComboBox.setItemText(20, _translate("MainWindow", "1000000"))
        self.SerialBaudrateComboBox.setItemText(21, _translate("MainWindow", "1500000"))
        self.SerialBaudrateComboBox.setItemText(22, _translate("MainWindow", "2000000"))
        self.SerialStopBitLabel.setText(_translate("MainWindow", "停止位"))
        self.SerialStopBitComboBox.setItemText(0, _translate("MainWindow", "1"))
        self.SerialStopBitComboBox.setItemText(1, _translate("MainWindow", "1.5"))
        self.SerialStopBitComboBox.setItemText(2, _translate("MainWindow", "2"))
        self.SerialDataBitLabel.setText(_translate("MainWindow", "数据位"))
        self.SerialDataBitcomboBox.setItemText(0, _translate("MainWindow", "5"))
        self.SerialDataBitcomboBox.setItemText(1, _translate("MainWindow", "6"))
        self.SerialDataBitcomboBox.setItemText(2, _translate("MainWindow", "7"))
        self.SerialDataBitcomboBox.setItemText(3, _translate("MainWindow", "8"))
        self.SerialChecksumBitLabel.setText(_translate("MainWindow", "校验位"))
        self.SerialChecksumBitComboBox.setItemText(0, _translate("MainWindow", "None"))
        self.SerialChecksumBitComboBox.setItemText(1, _translate("MainWindow", "Even"))
        self.SerialChecksumBitComboBox.setItemText(2, _translate("MainWindow", "Odd"))
        self.SerialChecksumBitComboBox.setItemText(3, _translate("MainWindow", "Mark"))
        self.SerialChecksumBitComboBox.setItemText(4, _translate("MainWindow", "Space"))
        self.SerialReceiveHexCheckBox.setText(_translate("MainWindow", "Hex"))
        self.SerialReceiveTimestampCheckBox.setText(_translate("MainWindow", "时间戳"))
        self.SerialReceiveClearPushButton.setText(_translate("MainWindow", "清空接收区"))
        self.SerialConnectComPushButton.setText(_translate("MainWindow", "连接COM"))
        self.SerialSendGroupBox.setTitle(_translate("MainWindow", "串口发送设置"))
        self.SerialSendRepeatGroupBox.setTitle(_translate("MainWindow", "重复"))
        self.SerialSendRepeatUnitLabel.setText(_translate("MainWindow", "ms"))
        self.SerialSendPushButton.setText(_translate("MainWindow", "发送"))
        self.SerialHardFlowControlGroupBox.setTitle(_translate("MainWindow", "硬件流控"))
        self.SerialHardFlowControlDSRDTRCheckBox.setText(_translate("MainWindow", "dsr/dtr"))
        self.SerialHardFlowControlRTSCTSCheckBox.setText(_translate("MainWindow", "rts/cts"))
        self.SerialSendLineFeedGroupBox.setTitle(_translate("MainWindow", "换行"))
        self.SerialSendLineFeedComboBox.setItemText(0, _translate("MainWindow", "None"))
        self.SerialSendLineFeedComboBox.setItemText(1, _translate("MainWindow", "/r/n"))
        self.SerialSendLineFeedComboBox.setItemText(2, _translate("MainWindow", "/n"))
        self.SerialSendHexCheckBox.setText(_translate("MainWindow", "Hex"))
        self.SerialSoftFlowControlGroupBox.setTitle(_translate("MainWindow", "软件流控"))
        self.SerialSoftFlowControlCheckBox.setText(_translate("MainWindow", "xon/xoff"))
from serialport_combobox import SerialPort_ComBoBox