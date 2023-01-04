from tkinter import *
from tkinter import ttk, messagebox
from ext import *
import csv
import textwrap
from pygetwindow import getAllTitles, getWindowsWithTitle
from PIL import Image
import pyautogui


class MainWindow:
    def __init__(self):
        window = Tk()
        window.geometry("1440x1024")
        window.configure(bg = "#FFFFFF")

        #PhotoImage
        canvas_bg_loc = PhotoImage(file=f"./frame0/image_1.png")
        jushotouroku_btn_img = PhotoImage(file=f"./frame0/button_8.png")
        annaisho_btn_img = PhotoImage(file=f"./frame0/button_7.png")
        chuumon_btn_img = PhotoImage(file=f"./frame0/button_6.png")
        uriageshokai_btn_img = PhotoImage(file=f"./frame0/button_5.png")
        chuumonrireki_btn_img = PhotoImage(file=f"./frame0/button_4.png")
        tanaoroshi_btn_img = PhotoImage(file=f"./frame0/button_3.png")
        nyuushukko_btn_img = PhotoImage(file=f"./frame0/button_2.png")
        torikeshi_btn_img = PhotoImage(file=f"./frame0/button_1.png")

        #Canvas
        canvas = Canvas(window,height = 1024,width = 1440,relief = "ridge")
        canvas.place(x = 0, y = 0)
        canvas_bg = canvas.create_image(720, 512, image = canvas_bg_loc)

        #Label
        canvas.create_text(178,68,anchor="nw",text="楽商 JVer",fill="#FFFFFF",font=("Inter SemiBold", 96 * -1))
        canvas.create_rectangle(100, 203, 1338, 205,fill="#FFFFFF")

        #Buttons
        jushotouroku_btn = Button(window, image=jushotouroku_btn_img, command = RecordWindow, relief="flat")
        jushotouroku_btn.place(x=102,y=247,width=618,height=78)

        annaisho_btn = Button(window, image = annaisho_btn_img, command = AnnaishoWindow, relief="flat")
        annaisho_btn.place(x=102, y=367, width=618, height=78)

        chuumon_btn = Button(window, image = chuumon_btn_img, command = ChuumonWindow, relief="flat")
        chuumon_btn.place(x=102, y=487, width=618, height=78)

        uriageshokai_btn = Button(window, image = uriageshokai_btn_img, command = UriageshokaiWindow, relief="flat")
        uriageshokai_btn.place(x=102, y=607, width=618, height=78)
        
        chuumonrireki_btn = Button(window, image = chuumonrireki_btn_img, command = ChuumonrirekiWindow, relief = "flat")
        chuumonrireki_btn.place(x=728, y=247, width=618, height=78)

        tanaoroshi_btn = Button(window, image= tanaoroshi_btn_img, command = TanaoroshiWindow, relief = "flat")
        tanaoroshi_btn.place(x=728, y=367, width=618, height=78)      

        nyuushukko_btn = Button(window, image= nyuushukko_btn_img, command = NyuushukkoWindow, relief = "flat")
        nyuushukko_btn.place(x=728, y=487, width=618, height=78)  

        torikeshi_btn = Button(window, image = torikeshi_btn_img, command = lambda: window.destroy(), relief = "flat")
        torikeshi_btn.place(x=728, y=608,width=618,height=78)

        window.resizable(0,0)
        window.mainloop()

class RecordWindow:
    def __init__(self):
        window = Toplevel()
        window.title("Record")
        canvas = Canvas(window, width=800,height=600, background="Black")
        canvas.grid(column=0,row=0)

        def clear_txt():
            phone_txbox.delete(0, END)  
            customername_txbox.delete(0, END)
            postal_txbox.delete(0, END)
            address1_txbox.delete(0, END)
            address2_txbox.delete(0, END)
            address3_txbox.delete(0, END)
            incharge_txbox.delete(0, END)
            doubleaddress_txbox.delete(0, END)

        #validate the entry
        reg = window.register(validate)
        
        #PhotoImage
        canvas_bg_img = PhotoImage(file = "./record/image_1.png")
        submit_btn_image = PhotoImage(file="./record/btn.png")
        clear_btn_image = PhotoImage(file="./record/clear.png")

        #Canvas
        canvas_bg = canvas.create_image(720, 512, image = canvas_bg_img)

        #Label
        canvas.create_rectangle(51,92,697,93,fill="#FFFFFF",outline="")
        canvas.create_text(56, 26, anchor="nw", text="住所登録", fill="#FFFFFF", font=("Inter SemiBold", 36 * -1))
        canvas.create_text(56, 117, anchor="nw",text="Phone Number", fill="#FFFFFF", font=("Inter", 24 * -1))
        canvas.create_text(56,162,anchor="nw",text="Customer Name",fill="#FFFFFF",font=("Inter", 24 * -1))
        canvas.create_text(56,204,anchor="nw",text="Postal Code",fill="#FFFFFF",font=("Inter", 24 * -1))
        canvas.create_text(56, 246,anchor="nw",text="Address 1",fill="#FFFFFF",font=("Inter", 24 * -1))
        canvas.create_text(56,289,anchor="nw",text="Address 2",fill="#FFFFFF",font=("Inter", 24 * -1))
        canvas.create_text(56,329,anchor="nw",text="Address 3",fill="#FFFFFF",font=("Inter", 24 * -1))
        canvas.create_text(56,414,anchor="nw",text="Double Address",fill="#FFFFFF",font=("Inter", 24 * -1))
        canvas.create_text(56,456,anchor="nw",text="In Charge",fill="#FFFFFF",font=("Inter", 24 * -1))

        

        #Textbox
        phone_txbox = Entry(canvas,validate='key',validatecommand=(reg, '%P'),bg="#FFF3FB",fg="#000716",font='Inter 16 bold')
        phone_txbox.place(x=296,y=112,width=396,height=31)

        customername_txbox = Entry(canvas,bd=0,bg="#FFF3FB",fg="#000716",font='Inter 16 bold',highlightthickness=0)
        customername_txbox.place(x=296,y=154,width=396,height=31)

        postal_txbox = Entry(canvas,bd=0,bg="#FFF3FB",fg="#000716",font='Inter 16 bold',highlightthickness=0)
        postal_txbox.place(x=296,y=196,width=102,height=31)

        address1_txbox = Entry(canvas,bd=0,bg="#FFF3FB",fg="#000716",font='Inter 16 bold',highlightthickness=0)
        address1_txbox.place(x=296,y=238,width=396,height=31)

        address2_txbox = Entry(canvas,bd=0,bg="#FFF3FB",fg="#000716",font='Inter 16 bold',highlightthickness=0)
        address2_txbox.place(x=296,y=280,width=396,height=31)

        address3_txbox = Entry(canvas,bd=0,bg="#FFF3FB",fg="#000716",font='Inter 16 bold',highlightthickness=0)
        address3_txbox.place(x=296,y=322,width=396,height=31)

        doubleaddress_txbox = Entry(canvas,bd=0,bg="#FFF3FB",fg="#000716",font='Inter 16 bold',highlightthickness=0)
        doubleaddress_txbox.place(x=296,y=406,width=396,height=31)

        incharge_txbox = Entry(canvas,bd=0,bg="#FFF3FB",fg="#000716",font='Inter 16 bold',highlightthickness=0)
        incharge_txbox.place(x=296,y=448,width=396,height=31)

        submit_btn = Button(canvas,image=submit_btn_image,command=lambda: print("submit"),relief="flat")
        submit_btn.place(x=410,y=523,width=125,height=34)

        clear_btn = Button(canvas,image=clear_btn_image,command=clear_txt,relief="flat")
        clear_btn.place(x=265,y=523,width=125,height=34)
        
        window.resizable(0,0)
        window.mainloop()

class AnnaishoWindow:
    def __init__(self):
        window = Toplevel()
        window.title("Product Info")
        window.geometry("850x842")
        window.configure(bg = "#FFFFFF")

        canvas = Canvas(window,background = "#FFFFFF",height = 842,width = 850,relief = "ridge")
        canvas.place(x = 0, y = 0)

        #Rectangles
        canvas.create_rectangle(318.0,258.0,552.0,308.0,fill="#C9DBFF",outline="")
        canvas.create_rectangle(318.0,322.0,552.0,372.0,fill="#C9DBFF",outline="")
        canvas.create_rectangle(318.0,386.0,552.0,436.0,fill="#C9DBFF",outline="")
        canvas.create_rectangle(317.0,450.0,552.0,500.0,fill="#C9DBFF",outline="")
        canvas.create_rectangle(318.0,514.0,552.0,564.0,fill="#C9DBFF",outline="")
        canvas.create_rectangle(48.0,586.0,552.0,657.0,fill="#C9DBFF",outline="")
        #canvas.create_rectangle(48.0,479.0,298.0,564.0,fill="#C9DBFF",outline="")
        canvas.create_rectangle(48.0,677.0,552.0,748.0,fill="#C9DBFF",outline="")
        canvas.create_rectangle(621.0,0.0,850.0,842.0,fill="#D9D9D9",outline="")
        canvas.create_rectangle(48.0,211.0,298.0,461.0,fill="#FFFFFF",outline="")

        #PhotoImage
        canvas_bg_img = PhotoImage(file="./productinfo/image_1.png")
        canvas_bg = canvas.create_image(735,421,image = canvas_bg_img)
        entry_image_1 = PhotoImage(file="./productinfo/entry_1.png")
        entry_bg_1 = canvas.create_image(480.5,283.0,image=entry_image_1)
        entry_image_2 = PhotoImage(file="./productinfo/entry_2.png")
        entry_bg_2 = canvas.create_image(298.0,621.0,image=entry_image_2)
        entry_image_3 = PhotoImage(file="./productinfo/entry_3.png")
        entry_bg_3 = canvas.create_image(298.0,713.0,image=entry_image_3)
        button_image_1 = PhotoImage(file="./productinfo/button_1.png")

        def reactivate(e):
            item_code.delete(0, END)
            item_code.config(insertontime=600)
            product_name.config(text = "")
            retail_price.config(text = "")
            retail_price_zeikomi.config(text = "")
            half_case.config(text = "")
            half_case_zeikomi.config(text = "")
            case_price.config(text = "")
            case_price_zeikomi.config(text = "")
            jan_bara.config(text = "")
            jan_case.config(text = "")

        def find_item(event):
            item_code.config(insertontime=0)
            with open("products.csv", encoding="UTF8") as file:
                r = csv.reader(file)
                item = item_code.get()
                for item_info in r:
                    if item_info[0].strip() == item:
                        wrapped_item_info = textwrap.fill(item_info[2], 18)
                        #canvas.create_text(66,485,anchor="nw",text=wrapped_item_info,font=("Inter Bold", 20 * -1))
                        product_name.config(text = wrapped_item_info)
                        retail_price.config(text = f"¥{item_info[27]}")
                        retail_price_zeikomi.config(text = f"税込み \n¥{round(float(item_info[27]) * 1.08)}")
                        half_case.config(text = f"¥{item_info[28]}")
                        half_case_zeikomi.config(text = f"税込み \n¥{round(float(item_info[28]) * 1.08)}")
                        case_price.config(text = f"¥{item_info[29]}")
                        case_price_zeikomi.config(text = f"¥税込み \n¥{round(float(item_info[29]) * 1.08)}")
                        jan_bara.config(text = item_info[19])
                        jan_case.config(text = item_info[78])
                        """product_name.config(text = wrapped_item_info)
                        retail_price.config(text = f"¥{item_info[2]}")
                        retail_price_zeikomi.config(text = f"税込み \n¥{round(float(item_info[2]) * 1.08)}")
                        half_case.config(text = f"¥{item_info[3]}")
                        half_case_zeikomi.config(text = f"税込み \n¥{round(float(item_info[3]) * 1.08)}")
                        case_price.config(text = f"¥{item_info[4]}")
                        case_price_zeikomi.config(text = f"¥税込み \n¥{round(float(item_info[4]) * 1.08)}")"""


        def print_save():
            path = f"./record/{item_code.get()}.png"
            titles = getAllTitles()

            active_windows = getWindowsWithTitle("Product Info")[0]
            left, top = active_windows.topleft
            right, bottom = active_windows.bottomright

            pyautogui.screenshot(path)
            im = Image.open(path)
            im = im.crop((left+10, top+35,right-239,bottom-10))
            im.save(path)
            im.show(path)
            item_code.configure(insertontime=1)
        #Label
        canvas.create_text(313, 37,anchor="center",text="AKABANE BUSSAN CO., LTD.",font=("Inter", 20 * -1))
        canvas.create_text(313, 57,anchor="center",text="赤羽物産有限会社",font=("Inter", 20 * -1))
        canvas.create_text(48,91,anchor="nw",text="Address: 115-0051 東京都北区浮間\nTel: 03-5914-3735",font=("Inter", 12 * -1))
        canvas.create_text(392,94,anchor="nw",text="https://akabanebussan.com\nhttps://philippinefoods.co.jp",font=("Inter", 12 * -1))
        canvas.create_text(113,151,anchor="nw",text="Product Information",font=("Inter", 48 * -1))
        canvas.create_text(329,270,anchor="nw",text="Item Code:",font=("Inter", 15 * -1))
        canvas.create_text(329,327,anchor="nw",text="Retail 小売 :",font=("Inter", 15 * -1))
        canvas.create_text(331,391,anchor="nw",text="Half ハーフ :",font=("Inter", 15 * -1))
        canvas.create_text(329,455,anchor="nw",text="Case ケース :",font=("Inter", 15 * -1))
        canvas.create_text(329,519,anchor="nw",text="Jan Code バラ :\n\nJan Code ケース:",font=("Inter", 12 * -1))


        #LookUps
        product_name = Label(window, text="",anchor="center", background="#FFFFFF", font=("Arial", 15, "bold"),padx=10, pady=10)
        product_name.place(x=75,y=480)
        retail_price = Label(window, text="", background="#C9DBFF", font=("Arial", 20, "bold"), fg="Red")
        retail_price.place(x=420,y=327)
        retail_price_zeikomi = Label(window, text="", background="#C9DBFF", font=("Arial", 8), fg="Red")
        retail_price_zeikomi.place(x=500,y=332)
        half_case = Label(window, text="", background="#C9DBFF", font=("Arial", 20, "bold"), fg="Red")
        half_case.place(x=420,y=391)
        half_case_zeikomi = Label(window, text="", background="#C9DBFF", font=("Arial", 8), fg="Red")
        half_case_zeikomi.place(x=500,y=396)
        case_price = Label(window, text="", background="#C9DBFF", font=("Arial", 20, "bold"), fg="Red")
        case_price.place(x=420,y=455)
        case_price_zeikomi = Label(window, text="", background="#C9DBFF", font=("Arial", 8), fg="Red")
        case_price_zeikomi.place(x=500,y=460)
        jan_bara = Label(window, text="", background="#C9DBFF", font=("Arial", 10, "bold"), fg="Black")
        jan_bara.place(x=425,y=515)
        jan_case = Label(window, text="", background="#C9DBFF", font=("Arial", 10, "bold"), fg="Black")
        jan_case.place(x=425,y=537)
        

        #TextBox
        item_code = Entry(canvas,bd=0,bg="#C9DBFF",fg="Red", font=("Arial", 20, "bold"))
        item_code.place(x=425,y=263.0,width=119.0,height=38.0)
        item_code.bind("<Return>", find_item)

        entry_2 = Entry(canvas,bd=0,bg="#C9DBFF",fg="#000716")
        entry_2.place(x=61.0,y=594.0,width=474.0,height=52.0)

        entry_3 = Entry(canvas,bd=0,bg="#C9DBFF",fg="#000716")
        entry_3.place(x=61.0,y=686.0,width=474.0,height=52.0)
        
        #Button
        button_1 = Button(canvas,image=button_image_1,borderwidth=0,command=print_save,relief="flat")
        button_1.place(x=668.0,y=24.0,width=136.0,height=29.0)
        
        window.bind('<Escape>', lambda e: reactivate(e))
        #window.resizable(False, False)
        window.mainloop()


class ChuumonWindow:
    def __init__(self):
        window = Toplevel()
        window.title("Orders")
        window.geometry("1080x800")
        canvas = Canvas(window,height = 800,width = 1080,relief = "ridge")
        canvas.place(x = 0, y = 0)

        def check(event):
            entry = phone_num_txt.get()
            res = find_num(entry)
            if not res == None:
                name, postal, address = res
                cust_name_show.config(text=name.upper())
                cust_add_show.config(text=f"{postal} {address}".upper())
            else:
                messagebox.showerror("Error!", "No Record!", parent=window)
            

        #Entry
        phone_num_txt = Entry(window, width=15, font=("Arial", 10))
        phone_num_txt.place(x=130, y=23)
        phone_num_txt.bind("<Return>", check)

        #Label
        phone_num = Label(window, text="Phone Number: ")
        phone_num.place(x=20, y=20)
        cust_name = Label(window, text="Customer Name: ")
        cust_name.place(x=20, y=50)
        cust_add = Label(window, text="Address: ")
        cust_add.place(x=20, y=70)
        cust_name_show = Label(window, text="")
        cust_name_show.place(x=130, y=50)
        cust_add_show = Label(window,text="")
        cust_add_show.place(x=130, y=70)
        canvas.create_line(20, 120, 1060, 120)
    
        

        window.resizable(False,False)
        window.mainloop()

class UriageshokaiWindow:
    ...

class ChuumonrirekiWindow:
    ...

class TanaoroshiWindow:
    ...

class NyuushukkoWindow:
    ...

if __name__ == "__main__":
    main = MainWindow()