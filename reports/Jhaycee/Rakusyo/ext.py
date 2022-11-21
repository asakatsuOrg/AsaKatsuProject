import re
"""def validate(inp):
    if inp:
        try:
            float(inp)
        except ValueError:
            return False
    return True
"""
"""def validate(inp):
    if re.search(r"\d", inp) or inp == "":
        return True
    else:
        return False
"""

def validate(inp):
    if re.search(r"[0-9]", inp) or inp == "":
        print("True")
        return True
    else:
        print("False")
        return False
