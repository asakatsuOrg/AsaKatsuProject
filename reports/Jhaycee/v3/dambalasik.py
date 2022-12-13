# from tkinter import *
# from external_function import saleCsv, is_recorded

# root = Tk()
# scrollbar = Scrollbar(root)
# scrollbar.pack( side = RIGHT, fill = Y )

# mylist = Listbox(root, yscrollcommand = scrollbar.set )

# sale = saleCsv()
# records = is_recorded()

# # for items in sale.items():
# #    mylist.insert(END, items[1][0])
# for items in records:
#    lbl = Label(root, text=items)
#    lbl.pack()

# mylist.pack( side = LEFT, fill = BOTH )
# scrollbar.config( command = mylist.yview )
# mylist.configure(width=100)

#mainloop()




# import tkinter as tk
# from tkinter.scrolledtext import ScrolledText
# from external_function import saleCsv

# root = tk.Tk()

# text = ScrolledText(root, state='disable')
# text.pack(fill='both', expand=True)

# frame = tk.Frame(text)
# text.window_create('1.0', window=frame)

# records = saleCsv()


# for x, number in enumerate(records):
#       l = tk.Label(frame, text=f"{number}", font=20, pady=4)
#       l.grid(row=x, column=0, sticky='w')
#       #  l = tk.Label(frame, text=number, bg='green')
#       #  l.grid(row=number, column=1, sticky='we')
    
# root.mainloop() 




# import tkinter as tk
# from tkinter.scrolledtext import ScrolledText

# root = tk.Tk()

# text = ScrolledText(root)
# text.pack(fill='both', expand=True)

# frame = tk.Frame(text)
# text.window_create('1.0', window=frame)

# for number in range(30):
#     l = tk.Label(frame, text='Input:', bg='red')
#     l.grid(row=number, column=0, sticky='we')
#     l = tk.Label(frame, text=number, bg='green')
#     l.grid(row=number, column=1, sticky='we')
    
# root.mainloop() 


import tkinter as tk
from tkinter import ttk, END, messagebox
from external_function import *
from external_function_jn import *
from dataUpdate import *

class main_window:
   def __init__(self):
      root = tk.Tk()
      root.title("DAMBALASIK 住所確認 v3.2")
      width_of_window = 1000
      height_of_window = 800
      screen_width = root.winfo_screenwidth()
      screen_height = root.winfo_screenheight()
      x_coordinate = (screen_width/2)-(width_of_window/2)
      y_coordinate = (screen_height/2)-(height_of_window/2)
      root.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
      root.config(background="powder blue")



      frame = ttk.Frame(root)
      frame.pack(padx=20,pady=(150,10))

      # root.overrideredirect(1)



      # lbl = ttk.Label(root, text="V3", background="powder blue", foreground="blue", font=("Inter", 20))
      # lbl.place(x=400, y=20)


      # CSV database
      def click():
         # variables phone number and order number
         clear()
         order_no = order_number()
         phone_no = phone_number()
         telephone_no = telephone_number()
         personal_info = is_recorded()
         # insert look ups in list box 1 by 1
         for x, infos in enumerate(personal_info):
            if infos is None:
               if select_item(telephone_no[x]):
                  Listbox.insert(END, order_no[x])
                  Listbox.itemconfig(x, bg="SeaGreen1")
               else:
                  Listbox.insert(END, order_no[x])
            else:
               Listbox.insert(END, f'{order_no[x]} {infos[2]} {infos[3]} {infos[4]} {infos[5]} {infos[6]}')

            if x % 2 == 0:
               Listbox.itemconfig(x, bg='lavender')

            if phone_no.count(phone_no[x]) > 1:
               Listbox.itemconfig(x, bg="salmon")
            

      def update_database():
         clear_db()
         update_db()
         messagebox.showinfo("UPDATE STATUS", "Update Done!!")
               

      def jap():
         clear()
         order_no = order_number_jn()
         phone_no = phone_number_jn()
         telephone_no = telephone_number_jn()
         personal_info = is_recorded_jn()
         # insert look ups in list box 1 by 1
         for x, infos in enumerate(personal_info):
            if infos is None:
               if select_item(telephone_no[x]):
                  Listbox.insert(END, order_no[x])
                  Listbox.itemconfig(x, bg="SeaGreen1")
               else:
                  Listbox.insert(END, order_no[x])
            else:
               Listbox.insert(END, f'{order_no[x]} {infos[2]} {infos[3]} {infos[4]} {infos[5]} {infos[6]}')

            if x % 2 == 0:
               Listbox.itemconfig(x, bg='lavender')

            if phone_no.count(phone_no[x]) > 1:
               Listbox.itemconfig(x, bg="salmon")


      def clear():
         #Listbox.itemconfig(1, bg='red')
         Listbox.delete(0, END)

      def under_maintenance():
         messagebox.showwarning("HEY! ", "THIS FEATURE IS NOT YET AVAILABLE")


      # info_lbl = tk.Label(root, text="""
      #                   LAST UPDATE [DB]:   xx/xx/xx
      #                   LAST UPDATE [CSV]:  xx/xx/xx
      #                   """, background="powder blue")
      # info_lbl.place(x=750,y=10)

      btn_update = tk.Button(root, text="UPDATE DB",width=10,relief="ridge" ,command=update_database)
      btn_update.place(x=880, y=100)

      btn_download = tk.Button(root, text="DOWNLOAD",width=10,relief="ridge", command=under_maintenance)
      btn_download.place(x=30, y=750)

      btn_english = tk.Button(root, text="ENGLISH",width=10,relief="ridge" ,command=click)
      btn_english.place(x=130, y=750)

      btn_download_jn = tk.Button(root, text="DOWNLOAD",width=10,relief="ridge", command=under_maintenance)
      btn_download_jn.place(x=780, y=750)

      btn_jap = tk.Button(root, text="JAPANESE",width=10,relief="ridge", command=jap)
      btn_jap.place(x=880,y=750)

      btn_clear = tk.Button(root, text="CLEAR",width=10, relief="ridge", command=clear)
      btn_clear.place(x=480,y=750)

      lists = tk.StringVar(value="")

      # 各種ウィジェットの作成
      Listbox = tk.Listbox(frame, height=30, width=100, font=25, background="azure", activestyle='none', selectforeground='black', selectbackground='sky blue')

      # スクロールバーの作成
      scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=Listbox.yview)

      # スクロールバーをListboxに反映
      Listbox["yscrollcommand"] = scrollbar.set

      # 各種ウィジェットの設置
      Listbox.grid(row=0, column=0, pady=10, padx=10)
      scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

      root.resizable(False,False)
      root.mainloop()

if __name__ == '__main__':
   main_window()