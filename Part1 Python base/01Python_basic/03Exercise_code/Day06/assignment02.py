list_year = [year for year in range(1970, 2051)
             if (year % 4 == 0 and year % 100 != 0)
             or (year % 400 == 0)]
print(list_year)
