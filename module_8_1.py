def add_everything_up(a, b):
    try:
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return round(a + b, 3)
        else:
            return str(a) + str(b)
    except TypeError:
        return str(a) + str(b)

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))