import tkinter as tk

root = tk.Tk()
root.title("Login")
root.geometry("600x400")

in_name = tk.StringVar()
in_pass = tk.StringVar()


#Tạo hàm nhận Tên và pass nhập vào và in ra màn hình
def submit():
    name = in_name.get()
    password = in_pass.get()

    print(f"Tên của bạn là: {name}")
    print(f"Mật khâu của bạn là: {password}")

    in_name.set("")
    in_pass.set("")

#Tạo một dòng tiêu đề : sử dụng widget Label
name_label = tk.Label(root, text = 'Tên tài khoản', font=('calibre',10, 'bold'))

name_entry = tk.Entry(root,textvariable = in_name, font=('calibre',10,'normal'))
  
pass_label = tk.Label(root, text='Mật khẩu', font=('calibre', 10, 'bold'), )

pass_entry = tk.Entry(root, textvariable = in_pass, font=('calibre', 10, 'normal'), show='*')

btn_submit = tk.Button(root, text='OK', command=submit, activebackground='red')

name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
pass_label.grid(row=1, column=0)
pass_entry.grid(row=1, column=1)
btn_submit.grid(row=2, column=1)


root.mainloop()
