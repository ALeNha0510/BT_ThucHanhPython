from tkinter import *
from tkinter import messagebox, LEFT

task_list = []
count = 1

def inputErorr():
    if enterTaskField.get() == "":
        messagebox.showerror("input Error!!")
        return 0
    return 1

def clear_taskNumberFiled():
    taskNumberField.delete(0.0, END)


def clear_taskField():
    enterTaskField.delete(0, END)


def insertTask():
    global count
    value = inputErorr()

    if value == 0:
        return
    
    content = enterTaskField.get()+ "\n"

    task_list.append(content)

    TextArea.insert('end -1 chars', "[ " + str(count) + " ]" + content)

    count += 1

    clear_taskField()

def delete():
    global count
    
    if len(task_list) == 0:
        messagebox.showerror("No task")
        return
    
    number = taskNumberField.get(1.0, END)

    if number == "\n":
        messagebox.showerror("input error!!")
        return
    else:
        task_no = int(number)

    clear_taskNumberFiled()
    task_list.pop(task_no - 1)
    count -= 1
    TextArea.delete(1.0, END)

    for i in range(len(task_list)):
        TextArea.insert('end -1 char', "[ " + str(i+1) + " ]" + task_list[i])

if __name__ == "__main__":
    gui = Tk()

    gui.configure(background="light green")
    gui.title("ToDo App")
    gui.geometry("250x300")
    enterTask = Label(gui, text="Enter your Task", bg="light green")

    enterTaskField = Entry(gui)

    submit = Button(gui, text="Submit", fg="black", bg="red", command=insertTask)

    TextArea = Text(gui, height=5, width=25, font="lucida 13")

    taskNumber = Label(gui, text="Delete Task Number", bg="blue")

    taskNumberField = Text(gui, height=1, width=2, font="lucida 13")

    Delete = Button(gui, text="Delete", fg="black", bg="red", command=delete)

    Exit = Button(gui, text="Exit", fg="black", bg="red", command=exit)

    enterTask.grid(row=0, column=2)
    enterTaskField.grid(row=1, column=2, ipadx=50)
    submit.grid(row=2, column=2)
    TextArea.grid(row=3, column=2, padx=10, sticky=W)
    taskNumber.grid(row=4, column=2, pady=5)
    taskNumberField.grid(row=5, column=2)

    Delete.grid(row=6, column=2, pady=5)
    Exit.grid(row=7, column=2)

    gui.mainloop()