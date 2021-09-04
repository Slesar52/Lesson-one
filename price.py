def format_price(price):
    price = int(abs(price))
    return f'Цена: {price} руб.' 
print(format_price(input()))
