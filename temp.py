# coding: utf-8



from pyautocad import Autocad, APoint, aDouble
from tkinter import Tk, filedialog, messagebox, Radiobutton, StringVar
from tkinter.ttk import Label, Button, Style, Frame

# acad = Autocad(create_if_not_exists=True)
# doc = acad.ActiveDocument



def radioD():
    def ok_clic():
        win.destroy()
    win = Tk()
    st =  Style()
    st.configure('frameStyle.TFrame', borderwidth=2, relief='solid')
    win.title('tracePtLas')
    win.geometry('250x200+820+270')
    win.resizable(False, False)
    v = StringVar()
    v.set('2D')
    lab = Label(win, text='Choose dimensions').pack(pady=5)
    fram  = Frame(win, style='frameStyle.TFrame')
    fram.pack(padx=10, pady=10)
    r1 = Radiobutton(fram, text="2D", variable=v, value="2D")
    r1.pack(pady=5)
    r2 = Radiobutton(fram, text="3D", variable=v, value="3D")
    r2.pack(pady=5)
    Button(win, text="Ok", command=ok_clic).pack(pady=10)
    win.bind('<Escape>', lambda e: win.destroy())
    win.mainloop()
    return v.get()    
# import time
# print(radioD())
# doc.SaveAs('c:/Data/Python/test.dwg')
# acad.doc.Open('./dwg/Lambert93.dwg')
# doc.SendCommand('(vla-open (vla-get-documents (vlax-get-acad-object)) "c:/Data/Python/tracePtLas/dwg/Lambert93.dwg")\n')
# time.sleep(3)
# doc.SendCommand('(vla-activate (vla-item (vla-get-documents (vlax-get-acad-object)) "Lambert93.dwg"))\n')
# time.sleep(1)
# acad = Autocad()
# doc = acad.ActiveDocument
# acad.prompt('tracePtLas connected\n')
# doc.close()
# acad.prompt('tracePtLas connected\n')
print(int((1000 / 33) / 100))