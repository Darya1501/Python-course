# Стоимость доставки

def cost_of_delivery(count):
    return 100 + (count - 1) * 50
    
count_of_goods = int(input())

print(cost_of_delivery(count_of_goods))
