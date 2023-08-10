from PyQt5 import QtCore, QtGui, QtWidgets
import datetime


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 500)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 500))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 500))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.fundo_frame = QtWidgets.QFrame(self.centralwidget)
        self.fundo_frame.setEnabled(True)
        self.fundo_frame.setAutoFillBackground(False)
        self.fundo_frame.setStyleSheet("background-color: rgb(44, 44, 44);")
        self.fundo_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fundo_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fundo_frame.setObjectName("fundo_frame")

        self.local_button = QtWidgets.QPushButton(self.fundo_frame)
        self.local_button.setGeometry(QtCore.QRect(20, 440, 141, 41))
        self.local_button.setMinimumSize(QtCore.QSize(10, 0))
        self.local_button.setStyleSheet("QPushButton{\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"\n"
"    color: rgb(188, 188, 188);\n"
"}\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(77, 77, 77);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(117, 117, 117);\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/pngwing.com.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.local_button.setIcon(icon)
        self.local_button.setObjectName("local_button")

        self.info_frame = QtWidgets.QFrame(self.fundo_frame)
        self.info_frame.setGeometry(QtCore.QRect(390, 60, 210, 200))
        self.info_frame.setMaximumSize(QtCore.QSize(210, 200))
        self.info_frame.setAutoFillBackground(False)
        self.info_frame.setStyleSheet("QFrame{\n"
"    background-color: rgb(44, 44, 44);\n"
"}")
        self.info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.info_frame.setObjectName("info_frame")

        self.icon_temp = QtWidgets.QLabel(self.info_frame)
        self.icon_temp.setEnabled(True)
        self.icon_temp.setGeometry(QtCore.QRect(0, 30, 211, 131))
        self.icon_temp.setText("")
        self.icon_temp.setPixmap(QtGui.QPixmap(":/days/chuva e nublado.png"))
        self.icon_temp.setScaledContents(True)
        self.icon_temp.setObjectName("icon_temp")

        self.dia = QtWidgets.QLabel(self.info_frame)
        self.dia.setGeometry(QtCore.QRect(70, 160, 61, 31))
        self.dia.setStyleSheet("")
        self.dia.setScaledContents(False)
        self.dia.setAlignment(QtCore.Qt.AlignCenter)
        self.dia.setWordWrap(False)
        self.dia.setObjectName("dia")

        self.temp = QtWidgets.QLabel(self.info_frame)
        self.temp.setGeometry(QtCore.QRect(50, 20, 41, 21))
        self.temp.setObjectName("temp")

        self.temp_icon = QtWidgets.QLabel(self.info_frame)
        self.temp_icon.setGeometry(QtCore.QRect(10, 20, 41, 31))
        self.temp_icon.setStyleSheet("image: url(:/logo/temp.png);")
        self.temp_icon.setText("")
        self.temp_icon.setPixmap(QtGui.QPixmap(":/logo/kisspng-temperature-thermometer-computer-icons-clip-art-temperature-png-transparent-images-5aae92a8a3c7e9.9723450715213902486709.png"))
        self.temp_icon.setScaledContents(True)
        self.temp_icon.setObjectName("temp_icon")

        self.latitude_entry = QtWidgets.QLineEdit(self.fundo_frame)
        self.latitude_entry.setGeometry(QtCore.QRect(380, 290, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.latitude_entry.setFont(font)
        self.latitude_entry.setAutoFillBackground(False)
        self.latitude_entry.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    background-color: rgb(30, 30, 30);\n"
"    color: rgb(188, 188, 188);\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(55, 55, 55);\n"
"}")
        self.latitude_entry.setMaxLength(32)
        self.latitude_entry.setObjectName("latitude_entry")

        self.longitude_entry = QtWidgets.QLineEdit(self.fundo_frame)
        self.longitude_entry.setGeometry(QtCore.QRect(380, 340, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.longitude_entry.setFont(font)
        self.longitude_entry.setAutoFillBackground(False)
        self.longitude_entry.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    background-color: rgb(30, 30, 30);\n"
"\n"
"    color: rgb(188, 188, 188);\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(55, 55, 55);\n"
"}")
        self.longitude_entry.setMaxLength(32)
        self.longitude_entry.setObjectName("longitude_entry")

        self.voltar_button = QtWidgets.QPushButton(self.fundo_frame)
        self.voltar_button.setEnabled(True)
        self.voltar_button.setGeometry(QtCore.QRect(330, 160, 50, 100))
        self.voltar_button.setMinimumSize(QtCore.QSize(50, 50))
        self.voltar_button.setMaximumSize(QtCore.QSize(100, 100))
        self.voltar_button.setStyleSheet("QPushButton{\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    \n"
"    image: url(:/logo/setaesquerda.png);\n"
"    color: rgb(188, 188, 188);\n"
"}\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(77, 77, 77);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(117, 117, 117);\n"
"}")
        self.voltar_button.setText("")
        self.voltar_button.setAutoDefault(False)
        self.voltar_button.setDefault(False)
        self.voltar_button.setFlat(False)
        self.voltar_button.setObjectName("voltar_button")

        self.seta_direita = QtWidgets.QPushButton(self.fundo_frame)
        self.seta_direita.setGeometry(QtCore.QRect(610, 160, 50, 100))
        self.seta_direita.setMinimumSize(QtCore.QSize(50, 50))
        self.seta_direita.setMaximumSize(QtCore.QSize(100, 100))
        self.seta_direita.setStyleSheet("QPushButton{\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    image: url(:/logo/setadireita.png);\n"
"    color: rgb(188, 188, 188);\n"
"}\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(77, 77, 77);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(117, 117, 117);\n"
"}")
        self.seta_direita.setText("")
        self.seta_direita.setObjectName("seta_direita")

        self.botao_previsao = QtWidgets.QPushButton(self.fundo_frame)
        self.botao_previsao.setGeometry(QtCore.QRect(440, 400, 101, 31))
        self.botao_previsao.setStyleSheet("QPushButton{\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"\n"
"    color: rgb(188, 188, 188);\n"
"}\n"
"QPushButton:hover{\n"
"    border: 2px solid rgb(77, 77, 77);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(117, 117, 117);\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/logo/botao-play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_previsao.setIcon(icon1)
        self.botao_previsao.setObjectName("botao_previsao")

        self.verticalLayout.addWidget(self.fundo_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Previsão do Tempo"))
        self.local_button.setText(_translate("MainWindow", "Buscar localização"))

        data = datetime.datetime.now()
        dia = data.strftime('%d/%m')
        self.dia.setText(_translate("MainWindow", "<html><head/><body><p><span style=\""
                                                  " font-size:12pt; font-weight:700; "
                                                  f"color:#797979;\">{dia}</span></p></body></html>"))

        self.temp.setText(_translate("MainWindow", "<html><head/><body><p><span style="
                                                   " font-size:12pt; font-weight:700;"
                                                   " font-style:italic; color:#7a7a7a;\""
                                                   ">23°</span></p></body></html>"))
        self.latitude_entry.setPlaceholderText(_translate("MainWindow", "Latitude"))
        self.longitude_entry.setPlaceholderText(_translate("MainWindow", "Longitude"))

        self.temp_icon.hide()
        self.temp.hide()
        self.seta_direita.hide()
        self.voltar_button.hide()
        self.icon_temp.hide()

import img


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())