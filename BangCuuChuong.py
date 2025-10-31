import tkinter as tk
from tkinter import messagebox

def App_tra_cuu_bang_cuu_chuong():
    try:
        so_bang = int(entry.get())
        if so_bang < 2 or so_bang > 9:
            messagebox.showerror("Lỗi", "Nhập số nguyên từ 2–9!")
            return
        Listbox.delete(0, 'end')
        for i in range(1, 11):
            Listbox.insert('end', f"{so_bang} x {i} = {so_bang * i}")
    except:
        messagebox.showerror("Lỗi", "Vui lòng nhập số nguyên hợp lệ!")

def xoa_het():
    entry.delete(0, 'end')
    Listbox.delete(0, 'end')


from tkinter import *
root = Tk()
root.title('Bảng Cửu Chương')
root.minsize(height=300, width=600)
Label(root, text='Ứng Dụng Hiện Bảng Cửu Chương',
fg='red', bg='yellow', font=('Arial', 16), width=50).grid(row=0, columnspan=4)
Listbox = Listbox(root, height=15, width=80)
Listbox.grid(row=1, columnspan=3)
thanhcuon = Scrollbar(root, orient=VERTICAL)
thanhcuon.grid(row=1, column=3, sticky='ns')
Listbox.config(yscrollcommand=thanhcuon.set)
thanhcuon.config(command=Listbox.yview)
Label(root, text='Bảng cửu chương:').grid(row=2, column=0, sticky='e', padx=5, pady=10)
number = StringVar()
entry = Entry(root, width=20, textvariable=number)
entry.grid(row=2, column=1, sticky='w')
nutbam = Frame(root)
nutbam.grid(row=3, column=1, pady=10)
Button(nutbam, text='Xóa', command=xoa_het).pack(side=LEFT, padx=5)
Button(nutbam, text='Tra cứu', command=App_tra_cuu_bang_cuu_chuong).pack(side=LEFT, padx=5)
Button(nutbam, text='Thoát', command=root.quit).pack(side=LEFT, padx=5)

root.mainloop()
