import tkinter as tk #Khai báo thư viện tkinter
from tkinter import messagebox #Từ tkinter tạo hộp thoại thông báo lỗi kết quả

def App_tra_cuu_bang_cuu_chuong(): # Hàm phép tính
    try:
        so_bang = int(entry.get()) #Nhập số đầu vào và gán tên so_bang
        if so_bang < 2 or so_bang > 9:
            messagebox.showerror("Lỗi", "Nhập số nguyên từ 2–9!")
            return
        Listbox.delete(0, 'end') # Xóa thông báo kết quả lỗi
        for i in range(1, 11): #Tạo dãy vòng lặp số bị nhân từ 1 tới 10
            Listbox.insert('end', f"{so_bang} x {i} = {so_bang * i}") # Điền công thức nhân vào khung kết quả
    except:# Trường hợp còn lại của nhập số không phải là số nguyên
        messagebox.showerror("Lỗi", "Vui lòng nhập số nguyên hợp lệ!") 

def xoa_het(): # Hàm xóa kết quả cũ
    entry.delete(0, 'end') # Xóa dòng hiển thị ở ô nhập liệu
    Listbox.delete(0, 'end') # Xóa dòng hiển thị ở khung kết quả


from tkinter import *
root = Tk()
root.title('Bảng Cửu Chương')
root.minsize(height=300, width=600)
Label(root, text='Ứng Dụng Hiện Bảng Cửu Chương',
fg='red', bg='yellow', font=('Arial', 16), width=50).grid(row=0, columnspan=4)
Listbox = Listbox(root, height=15, width=80)
Listbox.grid(row=1, columnspan=3)
scrollbar = Scrollbar(root, orient=VERTICAL)
scrollbar.grid(row=1, column=3, sticky='ns')
Listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=Listbox.yview)
Label(root, text='Bảng cửu chương:').grid(row=2, column=0, sticky='e', padx=5, pady=10)
number = StringVar()
entry = Entry(root, width=20, textvariable=number)
entry.grid(row=2, column=1, sticky='w')
button_frame = Frame(root)
button_frame.grid(row=3, column=1, pady=10)
Button(button_frame, text='Xóa', command=xoa_het).pack(side=LEFT, padx=5)
Button(button_frame, text='Tra cứu', command=App_tra_cuu_bang_cuu_chuong).pack(side=LEFT, padx=5)
Button(button_frame, text='Thoát', command=root.quit).pack(side=LEFT, padx=5)

root.mainloop()
