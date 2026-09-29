from connect import connect_db

def view_properties():
    properties = connect_db()

    print("\nAll Properties:")
    print("ID | Title | Location | Price | Bedrooms | Bathrooms | Area")
    print("-" * 65)

    if not properties:
        print("No properties found.")
        return

    for p in properties:
        print(f"{p['id1']} | {p['title']} | {p['location']} | ${p['price']:,.2f} | {p['bedrooms']} | {p['bathrooms']} | {p['area']} sq ft")
