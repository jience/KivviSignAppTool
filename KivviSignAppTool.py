import os
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PyQt5.QtCore import QThread, pyqtSignal
from ui_signapp import Ui_Form


class SignThread(QThread):
    _signal = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent=None)
        self.cmd = []

    def setCmd(self, cmd):
        self.cmd = cmd

    def run(self):
        os.chdir('source')
        si = subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        p = subprocess.Popen(self.cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, startupinfo=si)
        os.chdir('../')
        while True:
            line = p.stdout.readline().decode()
            if line is None or line == '':
                break
            self._signal.emit(str(line))


class SignApp(QWidget, Ui_Form):
    def __init__(self):
        super(SignApp, self).__init__()
        self.setupUi(self)
        self.lineEdit_certPath.setText(os.path.abspath(r'source/app_kivvi.der'))
        self.lineEdit_keyPath.setText(os.path.abspath(r'source/app_kivvi_privkey.pk8'))
        try:
            self.pushButton_apkPath.clicked.connect(self.btn_apkPath_Clicked)
            self.pushButton_certPath.clicked.connect(self.btn_certPath_Clicked)
            self.pushButton_keyPath.clicked.connect(self.btn_keyPath_Clicked)
            self.pushButton_signedApkPath.clicked.connect(self.btn_SignedApkPath_Clicked)
            self.pushButton_sign.clicked.connect(self.btn_sign_Clicked)
            self.pushButton_cleanLog.clicked.connect(self.btn_clean_log_clicked)
            self.signend = SignThread()
            self.signend._signal.connect(self.print_log)
        except Exception as e:
            print(e)

    def btn_sign_Clicked(self):
        try:
            apkPath = self.lineEdit_apkPath.text()
            certPath = self.lineEdit_certPath.text()
            keyPath = self.lineEdit_keyPath.text()
            signedApkPath = self.lineEdit_signedApkPath.text()

            apk_file_name = os.path.basename(apkPath)
            signed_apk_file_name = os.path.splitext(apk_file_name)[0] + '-signed.apk'
            java_home = r'jdk\bin\java.exe'
            java_path = r'jdk\bin'

            args = [java_home, '-jar', 'kivvi_sign.jar', certPath, keyPath, apkPath,
                   signedApkPath + '\\' + signed_apk_file_name, java_path]
            self.signend.setCmd(args)
            self.signend.start()

        except Exception as e:
            print(e)

    def btn_clean_log_clicked(self):
        self.textBrowser_log.setText("")

    def print_log(self, log):
        self.textBrowser_log.append(log)

    def btn_apkPath_Clicked(self):
        filename, filetype = QFileDialog.getOpenFileName(self, "Select Apk File", "./", "APK Files (*.apk)")
        if filename:
            self.lineEdit_apkPath.setText(filename)

    def btn_certPath_Clicked(self):
        filename, filetype = QFileDialog.getOpenFileName(self, "Select Cert File", "./", "Cert Files (*.der)")
        if filename:
            self.lineEdit_certPath.setText(filename)

    def btn_keyPath_Clicked(self):
        filename, filetype = QFileDialog.getOpenFileName(self, "Select Key File", "./", "Key Files (*.pk8);;DER "
                                                                                        "Files (*.der)")
        if filename:
            self.lineEdit_keyPath.setText(filename)

    def btn_SignedApkPath_Clicked(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Signed Apk Path", "./")
        if directory:
            self.lineEdit_signedApkPath.setText(directory)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    mainwindow = SignApp()
    mainwindow.setWindowTitle("KivviSignAppToolV1.1")
    mainwindow.show()
    sys.exit(app.exec_())
