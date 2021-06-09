# Количество дней в месяце

def count_of_days(month):
    count = 0
    
    if month == 2:
        count = 28
    elif month < 8:
        count = 30 + month % 2
    else:
        count = 31 - month % 2

    return count
  
month = int(input())
print(count_of_days(month))