all_wares = {
    "amd_processor": {
        "name": "AMD Ryzen 9 5900X Processor",
        "price": 5590.0,
        "number_in_stock": 50,
        "ratings": [4.5, 4.0, 5.0, 5.0, 4.5, 3.0],
        "description": "All the cores and threads you'll need!",
    },
    "playstation_5": {
        "name": "PlayStation 5",
        "price": 5999.0,
        "number_in_stock": 0,
        "ratings": [5.0, 5.0, 4.5, 2.0, 5.0, 4.5, 4.0],
        "description": "Next generation console, never in stock!",
    },
    "hdmi_cable": {
        "name": "Belkin Ultra High Speed HDMI Cable - 2m",
        "price": 349.0,
        "number_in_stock": 3,
        "ratings": [5.0, 5.0, 4.5, 5.0, 5.0, 5.0],
        "description": "A high speed overprices HDMI cable!",
    }
}

shopping_cart = {}


def add_number_of_ware_to_shopping_cart(ware_key, ware, shopping_cart, number_of_ware=1):
    if number_of_ware <= all_wares[ware]['number_in_stock']:
        shopping_cart[ware] = number_of_ware
        print(f"{number_of_ware} instance(s) of "
              f"{ware_key} were added to the shopping cart.")

    if number_of_ware > all_wares[ware]['number_in_stock'] > 0:
        shopping_cart[ware] = all_wares[ware]['number_in_stock']
        print(f"Only {all_wares[ware]['number_in_stock']} instance(s) "
              f"of {ware_key} were in stock. These were added to the shopping cart.")

    if all_wares[ware]['number_in_stock'] <= 0:
        print(f"{ware_key} is not in stock and could not be added to the shopping cart.")


add_number_of_ware_to_shopping_cart(all_wares["amd_processor"]['name'], "amd_processor", shopping_cart)
add_number_of_ware_to_shopping_cart(all_wares["hdmi_cable"]['name'], "hdmi_cable", shopping_cart, 4)
add_number_of_ware_to_shopping_cart(all_wares["playstation_5"]['name'], "playstation_5", shopping_cart, 2)
print()
print(f"The shoppping cart:\n{shopping_cart}")