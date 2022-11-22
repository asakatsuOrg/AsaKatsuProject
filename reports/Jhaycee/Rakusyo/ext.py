def validate(inp):
    if inp:
        try:
            float(inp)
        except ValueError:
            return False
    return True