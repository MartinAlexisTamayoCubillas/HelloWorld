def calculate_discount(price, customer_type):
    if customer_type == 'regular':
        discount = price * 0.05
    elif customer_type == 'premium':
        discount = price * 0.1
    elif customer_type == 'vip':
        discount = price * 0.2
    else
        discount = 0

final_price = price - discount
return final_price