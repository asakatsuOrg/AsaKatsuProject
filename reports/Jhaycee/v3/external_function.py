import configparser
import csv
from dataUpdate import *

config = configparser.ConfigParser()
config.read("config.ini")

sale = config["SALE_EN"]["path"]


def order_phone_number():
    with open(sale, encoding="UTF8") as f:
        reader = csv.reader(f)
        order_number = []
        phone_number = []
        telephone_number = []
        for item in reader:
            if item[1] not in order_number:
                phone_number.append(f"E{item[0]}")
                order_number.append(item[1])
                telephone_number.append(item[0][1:])
        return order_number, phone_number, telephone_number


def order_number():
    order_num = order_phone_number()
    return order_num[0]


def phone_number():
    phone_num = order_phone_number()
    return phone_num[1]


def telephone_number():
    telephone_no = order_phone_number()
    return telephone_no[2]


def is_recorded():
    phone_num = phone_number()
    personal_info = []
    for numbers in phone_num:
        personal_info.append(select_item(numbers))
    return personal_info


if __name__ == "__main__":
    print(telephone_number())
    # check_record(sale, db)
