import tkinter as tk
from tkinter import messagebox

def App_tra_cuu_bang_cuu_chuong():
    try:
        so_bang = int(entry.get()) #nhap so dau vao va  gan so nguyen
        if so_bang < 2 or so_bang > 9:
            messagebox.showerror("Lỗi", "Nhập số nguyên từ 2–9!") #hien thi thong bao loi
            return
        Listbox.delete(0, 'end') #xoa thong bao ket qua loi
        for i in range(1, 11):
            Listbox.insert('end', str(so_bang) +"x"+ str(i) +"="+ str(so_bang * i))
    except:
        messagebox.showerror("Lỗi", "Vui lòng nhập số nguyên hợp lệ!") #ngoai le truong hop con lai cua nhap so khong phai la so nguyen

def xoa_het():
    entry.delete(0, 'end')
    Listbox.delete(0, 'end')


from tkinter import * # import thư viện tkinter để xây dựng giao 
root = Tk() #tạo cửa sổ giao diện 
root.title('Bảng Cửu Chương') #đặt tiêu đề cho cửa sổ ứng dụng
root.minsize(height=300, width=600) #thiết lập kích thước tối thiểu cho cửa sổ (cao 300, rộng 600)
Label(root, text='Ứng Dụng Hiện Bảng Cửu Chương', 
fg='red', bg='yellow', font=('Arial', 16, 'bold'), width=50).grid(row=0, columnspan=4) # tạo nhãn tiêu đề, thiết lập phông chữ,cỡ chữ,kiểu chữ
Listbox = Listbox(root, height=15, width=80) #tạo hộp danh sách cao 15, rộng 80
Listbox.grid(row=1, columnspan=3) #vị trí đặt listbox ở hàng 1, trải dài qua 3 cột
thanhcuon = Scrollbar(root, orient=VERTICAL) #tạo thanh cuộn dọc 
thanhcuon.grid(row=1, column=3, sticky='ns') #đặt thanh cuộn ở dòng 1, cột 3, cuộn từ trên xuống(north-south)
Listbox.config(yscrollcommand=thanhcuon.set) #liên kết thanh cuộn với listbox
thanhcuon.config(command=Listbox.yview) #cấu hình thanh cuộn để điều chỉnh chế độ xem 
Label(root, text='Bảng cửu chương:').grid(row=2, column=0, sticky='e', padx=5, pady=10) #tạo nhãn bảng cửu chương, căn ở hàng 2,cột 0, lề phải(east),padx là khoảng cách theo chiều ngang, pady là kcach theo chiều dọc
number= StringVar() #là biến đặc biệt của tkinter dùng để lưu trữ và theo dõi giá trị chuỗi từ ô nhập,khi giá trị thay đổi thì các widget liên kết sẽ tự động cập nhập
entry= Entry(root, width=20, textvariable= number) #tạo ô nhập liệu đặt trong cửa sổ chính với rộng bằng 20 ký tự và liên kết với biến number
entry.grid (row=2, column=1, sticky='w') #vị trí đặt hàng 2,cột1, căn lề trái(west)
nutbam=Frame(root) #tạo 1 khung chứa các nút bấm
nutbam.grid(row=3,column=1,pady=10) #đặt khung vào hàng thứ 3,cột 1, căn khoảng cách dọc trên dưới là 10
Button(nutbam, text='Xóa',command=xoa_het).pack(side=LEFT,padx=5) #tạo nút Xóa liên kết hàm xoa_het , đặt vị trí bên trái, khoảng cách ngang 2 bên nút=5
Button(nutbam, text='Tra cứu', command=App_tra_cuu_bang_cuu_chuong).pack(side=LEFT,padx=5)
Button(nutbam,text='Thoát',command=root.quit).pack(side=LEFT,padx=5)

root.mainloop() #khởi tạo vòng lặp, mở cửa sổ chính và chờ tương tác từ người 
