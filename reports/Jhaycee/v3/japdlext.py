import os
import wget
import csv
import datetime
from shutil import copyfile
from configparser import ConfigParser

conf = ConfigParser()
conf.read("config.ini")

temp_loc = conf['SALE_JN']['temp']
r_path = conf['SALE_JN']['r_path']
url = conf['SITELINK']['jn_site_link']

cur = os.getcwd()
today = datetime.date.today()
time = datetime.datetime.now()
t_now = time.strftime("%H%M%S")
now = today.strftime("%Y%m%d")

def dl_csv():
    if os.path.isfile(temp_loc):
        os.remove(temp_loc)

    wget.download(url, temp_loc)
    copyfile(f"{temp_loc}", f"{r_path}/order_finished/{now}{t_now}_order.csv")
    #dup = wget.download(url, f"{now}{t_now}_order.csv")

def modify_csv():
    with open(temp_loc, encoding="UTF8", newline="\n") as file:
        with open(f"{r_path}{now}{t_now}_orderwc.csv", "a",encoding="UTF8", newline="\n") as f:
            r = csv.reader(file)
            w = csv.writer(f)
            for row in r:
                row[0] = row[0].replace("+63", "0").replace(" ","").replace("-","").replace("+81","0").strip()
                row[1] = f"wcpf{row[1]}"
                w.writerow(row)
                

def dl_link_jn():
    dl_csv()
    modify_csv()


"""    with open("copy.csv", encoding="UTF8") as copy:
        c = csv.reader(copy)
        for i in c:"""
if __name__ == "__main__":
    dl_csv()
    modify_csv()