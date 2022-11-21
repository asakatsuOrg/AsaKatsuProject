from tkinter import *


def clear_txt():
        phone_txbox.insert("awdawdwd")
        customername_txbox.delete(0, END)

leaf = Tk()
leaf.title("record")
leaf_canvas = Canvas(leaf, width=800,height=600, background="Black")
leaf_canvas.grid(column=0,row=0)

bg = PhotoImage(file = "./record/assets/image_1.png")
leaf_canvas_bg = leaf_canvas.create_image(
    720,
    512,
    image = bg
)

leaf_canvas.create_text(
    56.0,
    26.0,
    anchor="nw",
    text="住所登録",
    fill="#FFFFFF",
    font=("Inter SemiBold", 36 * -1)
)

leaf_canvas.create_rectangle(
    51, #x
    92, #y
    697, #width
    93, # base on y. y+val = tickness of line
    fill="#FFFFFF",
    outline=""
)

leaf_canvas.create_text(
    56,
    117,
    anchor="nw",
    text="Phone Number",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

leaf_canvas.create_text(
    56,
    162,
    anchor="nw",
    text="Customer Name",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

leaf_canvas.create_text(
    56,
    204,
    anchor="nw",
    text="Postal Code",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

leaf_canvas.create_text(
    56,
    246,
    anchor="nw",
    text="Address 1",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

leaf_canvas.create_text(
    56,
    289,
    anchor="nw",
    text="Address 2",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

leaf_canvas.create_text(
    56,
    329,
    anchor="nw",
    text="Address 3",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

leaf_canvas.create_text(
    56,
    414,
    anchor="nw",
    text="Double Address",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

leaf_canvas.create_text(
    56,
    456,
    anchor="nw",
    text="In Charge",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)


phone_txbox = Entry(
    bd=0,
    bg="#FFF3FB",
    fg="#000716",
    font='Inter 16 bold',
    highlightthickness=0
)

phone_txbox.place(
    x=296,
    y=112,
    width=396,
    height=31
)

customername_txbox = Entry(
    leaf_canvas,
    bd=0,
    bg="#FFF3FB",
    fg="#000716",
    font='Inter 16 bold',
    highlightthickness=0
)

customername_txbox.place(
    x=296,
    y=154,
    width=396,
    height=31
)

postal_txbox = Entry(
    leaf_canvas,
    bd=0,
    bg="#FFF3FB",
    fg="#000716",
    font='Inter 16 bold',
    highlightthickness=0
)

postal_txbox.place(
    x=296,
    y=196,
    width=102,
    height=31
)

address1_txbox = Entry(
    leaf_canvas,
    bd=0,
    bg="#FFF3FB",
    fg="#000716",
    font='Inter 16 bold',
    highlightthickness=0
)

address1_txbox.place(
    x=296,
    y=238,
    width=396,
    height=31
)

address2_txbox = Entry(
    leaf_canvas,
    bd=0,
    bg="#FFF3FB",
    fg="#000716",
    font='Inter 16 bold',
    highlightthickness=0
)

address2_txbox.place(
    x=296,
    y=280,
    width=396,
    height=31
)

address3_txbox = Entry(
    leaf_canvas,
    bd=0,
    bg="#FFF3FB",
    fg="#000716",
    font='Inter 16 bold',
    highlightthickness=0
)

address3_txbox.place(
    x=296,
    y=322,
    width=396,
    height=31
)

doubleaddress_txbox = Entry(
    leaf_canvas,
    bd=0,
    bg="#FFF3FB",
    fg="#000716",
    font='Inter 16 bold',
    highlightthickness=0
)

doubleaddress_txbox.place(
    x=296,
    y=406,
    width=396,
    height=31
)

incharge_txbox = Entry(
    leaf_canvas,
    bd=0,
    bg="#FFF3FB",
    fg="#000716",
    font='Inter 16 bold',
    highlightthickness=0
)

incharge_txbox.place(
    x=296,
    y=448,
    width=396,
    height=31
)

submit_btn_image = PhotoImage(file="./record/assets/btn.png")
submit_btn = Button(
    leaf_canvas,
    image=submit_btn_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("submit"),
    relief="flat"
)

submit_btn.place(
    x=410,
    y=523,
    width=125,
    height=34
)

clear_btn_image = PhotoImage(file="./record/assets/clear.png")
clear_btn = Button(
    leaf_canvas,
    image=clear_btn_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: clear_txt,
    relief="flat"
)

clear_btn.place(
    x=265,
    y=523,
    width=125,
    height=34
)


leaf.resizable(False,False)
leaf.mainloop()