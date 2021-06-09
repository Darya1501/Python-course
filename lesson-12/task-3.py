# Стоимость доставки

def cost_of_delivery(count):
    cost = 100
    while count > 1:
        cost += 50
        count -= 1
    
    return cost
    
count_of_goods = int(input())

print(cost_of_delivery(count_of_goods))