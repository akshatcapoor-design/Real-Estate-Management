from connect import connect_db, save_data

def delete_property():
    try:
        prop_id = int(input("Enter property ID to delete: "))
    except ValueError:
        print("Property ID must be an integer.")
        return

    properties = connect_db()
    filtered_properties = [p for p in properties if p["id1"] != prop_id]

    if len(filtered_properties) == len(properties):
        print("Property not found.")
    else:
        if save_data(filtered_properties):
            print("Property deleted successfully.")
