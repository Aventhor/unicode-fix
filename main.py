import tkinter
from tkinter import ttk
import functional as f
import webbrowser

class Main:
    def __init__(self, master):
        func = f.Functional()
        self.bc = ttk.Button(master, text='Сделать копию', command = func.createCopiesFiles)
        self.br = ttk.Button(master, text='Начать замену', command = func.confirmReplace)
        self.l = ttk.Label(master, text='Перед заменой файлов, сделайте копию!')
        self.lv = ttk.Label(master, text="ver. 0.8")
        self.lc = ttk.Label(master, text='by Aventhor', cursor='hand2', foreground='blue')
        self.lc.bind('<Button-1>', redirectToProfile)
        self.l.pack(padx=12, pady=12)
        self.bc.pack(padx=12, pady=12, ipadx=12, ipady=12)
        self.br.pack(padx=12, pady=12, ipadx=12, ipady=12)
        self.lv.pack(padx=12, side='right')
        self.lc.pack(padx=12, side='left')
    
def redirectToProfile(event):
    webbrowser.open_new(r"https://github.com/Aventhor/unicode-fix")
    

root = tkinter.Tk()
root.title('System Files Changer')
root.geometry('300x230')
root.resizable(False, False)
main = Main(root)
root.mainloop()