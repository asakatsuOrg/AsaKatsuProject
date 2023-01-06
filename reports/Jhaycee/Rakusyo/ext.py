import csv

def validate(inp):
    if inp:
        try:
            float(inp)
        except ValueError:
            return False
    return True

def find_num(inpt):
    with open("customer_rec.csv", encoding="UTF8") as file:
        r = csv.DictReader(file)
        for num in r:
            if num["phone"] == inpt:
                return num["name"], num["postal"], num["address"]