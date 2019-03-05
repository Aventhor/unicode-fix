import os
import shutil
import platform
from tkinter import messagebox

class Functional:

    sysFiles = ['C_1251.NLS', 'C_1252.NLS']
    desktopPath = os.path.join(os.environ["USERPROFILE"], "Desktop\\")

    def getPath(self):
        bit = platform.architecture()[0]
        if(bit == '32bit'):
            winPath = os.environ['WINDIR'] + "\\Sysnative\\"
        elif(bit == '64bit'):
            winPath = os.environ['WINDIR'] + "\\SYSWOW64\\"
        return winPath

    def createCopiesFiles(self):
        copiesDirectory = os.path.join(self.desktopPath, 'system-copies')
        success = True
        if not os.path.exists(copiesDirectory):
            os.makedirs(copiesDirectory)
            print("Directory was created: " + copiesDirectory)
        for i in self.sysFiles:
            try:
                shutil.copy(self.getPath() + i, copiesDirectory)
                print('File {0} was copied in {1}'.format(i, copiesDirectory))
            except FileNotFoundError:
                messagebox.showerror('Ошибка', 'Файл {0} не найден!'.format(i))
                print('File {0} not found in {1}'.format(i, self.getPath()))
                success = False
        if success:
            messagebox.showinfo('Уведомление', 'Копии файлов успешно созданы!')

    def confirmReplace(self):
        box = messagebox.askquestion('Подтверждение', 'Будет произведена замена системных файлов. Продолжить?', icon='warning')
        if box == 'yes':
            self.replaceFiles()


    def replaceFiles(self):
        temp = os.path.join(self.desktopPath, 'temp\\')
        try: 
            os.makedirs(temp)
            print('Temporary directory is created: ' + temp)
        except FileExistsError:
            print('Directory {0} already exist!'.format(temp))

        shutil.move(self.getPath() + self.sysFiles[0], temp)
        subject = temp + self.sysFiles[0]
        print('File {0} was moved in {1} directory'.format(self.sysFiles[0] ,temp))

        shutil.move(self.getPath() + self.sysFiles[1], temp + 'C_1252.bak')
        print('File {0} was moved in {1} directory as C_1252.bak'.format(self.sysFiles[1], temp))

        shutil.copy(subject, temp + self.sysFiles[1])
        copy = temp + self.sysFiles[1]
        print('Copy of {0} was created as {1} in {2}'.format(self.sysFiles[0], self.sysFiles[1], temp))

        try: 
            shutil.move(subject, self.getPath() + self.sysFiles[0])
            print("File {0} was moved in {1} directory from {2}".format(self.sysFiles[0], self.getPath(), temp))
            shutil.move(temp + self.sysFiles[1], self.getPath() + self.sysFiles[1])
            print("File {0} was moved in {1} directory from {2}".format(self.sysFiles[1], self.getPath(), temp))
        except PermissionError:
            messagebox.showerror('Ошибка', 'Нет доступа!')