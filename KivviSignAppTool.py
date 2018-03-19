import os
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from ui_signapp import Ui_Form


class SignApp(QWidget, Ui_Form):

    def __init__(self):
        super(SignApp, self).__init__()
        self.setupUi(self)
        try:
            self.pushButton_apkPath.clicked.connect(self.btn_apkPath_Clicked)
            self.pushButton_certPath.clicked.connect(self.btn_certPath_Clicked)
            self.pushButton_keyPath.clicked.connect(self.btn_keyPath_Clicked)
            self.pushButton_signedApkPath.clicked.connect(self.btn_SignedApkPath_Clicked)
            self.pushButton_sign.clicked.connect(self.btn_sign_Clicked)
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

            args = ['java', '-jar', 'kivvi_sign.jar', certPath, keyPath, apkPath,
                   signedApkPath + '\\' + signed_apk_file_name]
            os.chdir('source')
            p = subprocess.Popen(args, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            os.chdir('../')

            self.textBrowser_log.setText("")
            for line in p.stdout.readlines():
                self.textBrowser_log.append(line.decode())

        except Exception as e:
            print(e)

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
    mainwindow.setWindowTitle("KivviSignAppToolV1.0")
    mainwindow.show()
    sys.exit(app.exec_())
