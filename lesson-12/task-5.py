# Звездная дата

def star_date(string):
    result = False
    
    date = string.split('.')
    
    day = int(date[0])
    month = int(date[1])
    year = int(date[2]) % 100
    
    if day * month == year:
        result = True
        
    return result
    
date = input()

print(star_date(date))