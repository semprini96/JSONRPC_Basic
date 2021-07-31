import sys

import numpy as np
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication
from jsonrpcclient.clients.http_client import HTTPClient
from jsonrpcclient.requests import Request

from json_utils import dump_json_to_numpy, dump_numpy_to_json
from qt_client import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_signals_slots()
        self.client = HTTPClient('http://localhost:5000')

    def connect_signals_slots(self):
        """
        Connect functions to UI elements

        :return: None
        """
        self.ui.action_quit.triggered.connect(self.close)
        self.ui.action_aboutApp.triggered.connect(self.about)
        self.ui.action_aboutQt.triggered.connect(self.about_qt)
        self.ui.pushButton_sendPing.clicked.connect(self.send_ping)
        self.ui.pushButton_am_mod.clicked.connect(self.send_am_mod)

    def about(self):
        """
        Show information about this GUI

        :return: None
        """
        QMessageBox.about(
            self,
            'About this application',
            '<p><b>VERY Simple JSON-RPC Client</b></p>'
            'Written in Python using <i>jsonrpcclient</i>.<br>'
            'Accompanying Server program written using <i>jsonrpcserver</i>.<br><br>'
            'This little GUI made in PyQt5 with Qt Designer.<br><br>'
            '(C) 2021 <a href="github.com/semprini96">semprini96</a>'
        )

    def about_qt(self):
        """
        Show information about Qt version

        :return: None
        """
        QMessageBox.aboutQt(self)

    def send_ping(self):
        """
        Send very simple ping to server and show response

        :return: None
        """
        response = self.client.send(Request('ping'))
        self.ui.label_response.setText('Server response: {}'.format(response.data.result))

    def send_am_mod(self):
        """
        Prepare data for AM modulation, send data to server and show response size

        :return: None
        """
        t = np.arange(0, 1, 1 / 44100)
        msg_signal = np.cos(2 * np.pi * 10 * t)
        car_signal = np.sin(2 * np.pi * 1000 * t)

        msg_signal = dump_numpy_to_json(msg_signal)
        car_signal = dump_numpy_to_json(car_signal)

        response = self.client.send(Request('am_mod', msg_signal=msg_signal, carrier_signal=car_signal))
        resp_data = dump_json_to_numpy(response.data.result)
        self.ui.label_am_mod_length.setText('Length = {}'.format(len(resp_data)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
