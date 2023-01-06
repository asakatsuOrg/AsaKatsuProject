import configparser
import csv
from dataUpdate import *

config = configparser.ConfigParser()
config.read('config.ini')

salej = config['SALE_JN']['path']

def order_phone_number_jn():
    with open(salej, encoding='UTF8') as f:
        reader = csv.reader(f)
        order_number = []
        phone_number = []
        telephone_number = []
        for item in reader:
            if item[1] not in order_number:
                phone_number.append(f"J{item[0]}")
                order_number.append(item[1])
                telephone_number.append(item[0][1:])
        return order_number, phone_number, telephone_number

def order_number_jn():
    order_num = order_phone_number_jn()
    return order_num[0]
    
def phone_number_jn():
    phone_num = order_phone_number_jn()
    return phone_num[1]
    
def telephone_number_jn():
    telephone_no = order_phone_number_jn()
    return telephone_no[2]

def is_recorded_jn():
    phone_num = phone_number_jn()
    personal_info = []
    for numbers in phone_num:
        personal_info.append(select_item(numbers))
    return personal_info


if __name__ == "__main__":
    print(telephone_number_jn())
    #check_record(sale, db)