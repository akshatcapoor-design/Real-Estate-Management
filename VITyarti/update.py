from connect import connect_db, save_data

def update_property():
    try:
        prop_id = int(input("Enter property ID to update: "))
    except ValueError:
        print("Property ID must be an integer.")
        return

    properties = connect_db()
    target_prop = None

    for p in properties:
        if p["id1"] == prop_id:
            target_prop = p
            break

    if not target_prop:
        print("Property not found.")
        return

    print("Enter new details (leave blank to keep current value):")
    title = input("New title: ").strip()
    location = input("New location: ").strip()
    price_input = input("New price: ").strip()
    bedrooms_input = input("New number of bedrooms: ").strip()
    bathrooms_input = input("New number of bathrooms: ").strip()
    area_input = input("New area in square feet: ").strip()

    try:
        if title:
            target_prop["title"] = title
        if location:
            target_prop["location"] = location
        if price_input:
            target_prop["price"] = float(price_input)
        if bedrooms_input:
            target_prop["bedrooms"] = int(bedrooms_input)
        if bathrooms_input:
            target_prop["bathrooms"] = int(bathrooms_input)
        if area_input:
            target_prop["area"] = float(area_input)

        if save_data(properties):
            print("Property updated successfully.")
    except ValueError:
        print("Invalid numerical input during update. Changes aborted.")
