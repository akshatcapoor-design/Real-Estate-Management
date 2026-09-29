from connect import connect_db

def search_properties():
    keyword = input("Enter search keyword (location/title): ").strip().lower()

    if not keyword:
        print("Search keyword cannot be empty.")
        return

    properties = connect_db()
    matches = [
        p for p in properties
        if keyword in p["title"].lower() or keyword in p["location"].lower()
    ]

    print("\nSearch Results:")
    if not matches:
        print("No properties match your keyword.")
        return

    for p in matches:
        print(f"ID: {p['id1']}, Title: {p['title']}, Location: {p['location']}, Price: ${p['price']:,.2f}, Bedrooms: {p['bedrooms']}, Bathrooms: {p['bathrooms']}, Area: {p['area']} sq ft")
