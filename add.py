from connect import connect_db, save_data


def add_property():
    try:
        id1 = int(input("Enter ID of the property: "))
        title = input("Enter property title: ").strip()
        location = input("Enter location: ").strip()
        price = float(input("Enter price: "))
        bedrooms = int(input("Enter number of bedrooms: "))
        bathrooms = int(input("Enter number of bathrooms: "))
        area = float(input("Enter area in square feet: "))
    except ValueError:
        print("Invalid input. Please make sure numerical fields contain numbers.")
        return

    properties = connect_db()
    if any(p["id1"] == id1 for p in properties):
        print(f"A property with ID {id1} already exists.")
        return

    new_property = {
        "id1": id1,
        "title": title,
        "location": location,
        "price": price,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "area": area
    }

    properties.append(new_property)
    if save_data(properties):
        print("Property added successfully.")

