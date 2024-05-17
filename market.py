def iva(price, iva_percent=10):
    price += price*(iva_percent/100)
    return price
def discount(price, discount=10):
    price -= price*(discount/100)
    return price
shop_cart = {"Tomate": 2000, "Bolsas": 3000, "Cebolla": 6000}

if __name__ == "__main__":
    final_price = 0
    for product, price in shop_cart.items():
        final_price += discount(shop_cart[product])
    print(f"El precio de la canasta con los descuentos es de: {final_price}")
    print(f"El precio final con el IVA aplicado es de: {iva(final_price)}")