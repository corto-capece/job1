product_name = "PC"
product_price = 150
product_quantity = 3

print(
    "*** PRODUITS ***\n"
    f"Nom      : {product_name}\n"
    f"Prix     : {product_price}\n"
    f"Quantité : {product_quantity}\n"
)

user_quantity = int(input("Quelle quantité ? "))
new_product_quantity = product_quantity - user_quantity
product_price_inflation = product_price * 1.1

print(
    "*** PRODUITS ***\n"
    f"Nom                  : {product_name}\n"
    f"Prix après inflation : {product_price_inflation}\n"
    f"Nouvelle quantité    : {new_product_quantity}\n"
)