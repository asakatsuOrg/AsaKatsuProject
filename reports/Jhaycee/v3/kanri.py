from tkinter import *
from tkinter import messagebox

class Kanri:
    def __init__(self):
        root = Toplevel()
        root.title("管理画面")
        width_of_window = 300
        height_of_window = 150
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_coordinate = (screen_width/2)-(width_of_window/2)
        y_coordinate = (screen_height/2)-(height_of_window/2)
        root.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))





        root.resizable(0,0)
        root.mainloop()

class Login:
    def __init__(self):
        root = Toplevel()
        root.title("Login")
        width_of_window = 300
        height_of_window = 150
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_coordinate = (screen_width/2)-(width_of_window/2)
        y_coordinate = (screen_height/2)-(height_of_window/2)
        root.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))


        def credentials():
            admin_user = "jhaycee"
            admin_pass = "pogi"
            user = login_txt.get("1.0", END).strip()
            print(user)
            # if user == admin_user:
            #     root.destroy()
            # else:
            #     messagebox.showerror("WRONG COMBINATION", "WRONG USER OR PASSWORD")


        login_lbl = Label(root, text="User")
        login_lbl.place(x=50, y=50)

        pwd_lbl = Label(root, text="Pw")
        pwd_lbl.place(x=50, y=80)

        login_txt = Text(root, width=20, height=1)
        login_txt.place(x=100, y=52)

        pwd_txt = Text(root, width=20, height=1)
        pwd_txt.place(x=100, y=82)

        login_button = Button(root, text="Login", command=credentials)
        login_button.place(x=140, y=115)



        root.resizable(0,0)
        root.mainloop()

if __name__ == "__main__":
    Login()