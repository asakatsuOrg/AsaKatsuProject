import os
import wget
import csv
import datetime
import configparser
from shutil import copyfile

config = configparser.ConfigParser()
config.read('config.ini')

site_link = config['SITELINK']['en_site_link']

cur = os.getcwd()
today = datetime.date.today()
time = datetime.datetime.now()
t_now = time.strftime("%H%M%S")
now = today.strftime("%Y%m%d")

config = configparser.ConfigParser()
config.read('config.ini')

salej = config['SALE_JN']['path']

def dl_csv():
    if os.path.isfile(f"{cur}/plugins/temp.csv"):
        os.remove(f"{cur}/plugins/temp.csv")

    wget.download(site_link, f"{cur}/plugins/temp.csv")
    copyfile(f"{cur}/plugins/temp.csv", f"{cur}/order_finished/{now}{t_now}_order.csv")
    #dup = wget.download(site_link, f"{now}{t_now}_order.csv")

def modify_csv():
    with open(f"{cur}/plugins/temp.csv", encoding="UTF8", newline="\n") as file:
        with open(f"{now}{t_now}_orderwc.csv", "a",encoding="UTF8", newline="\n") as f:
            r = csv.reader(file)
            w = csv.writer(f)
            for row in r:
                row[0] = row[0].replace("+63", "0").replace(" ","").replace("-","").replace("+81","0").strip()
                row[1] = f"wc{row[1]}"
                w.writerow(row)

def dl_link_EN():
    dl_csv()
    modify_csv()


"""    with open("copy.csv", encoding="UTF8") as copy:
        c = csv.reader(copy)
        for i in c:"""
if __name__ == "__main__":
    dl_csv()
    modify_csv()

