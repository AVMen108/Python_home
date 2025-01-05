is_year_leap = 2020
if (is_year_leap % 4 == 0 and is_year_leap % 100 != 0) or (is_year_leap % 400 == 0):
    print(True)
else:
    print(False)

print(is_year_leap)






