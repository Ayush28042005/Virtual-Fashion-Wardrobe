import json
from clothing_item import Shirt, Jeans, Jacket

class Wardrobe:
    def __init__(self, filename="data.json"):
        self.filename = filename
        self.items = []                 # List of all ClothingItem objects
        self.favourite_outfits = []     # List of saved favourite outfits
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                for item in data.get("items", []):
                    if item["type"] == "shirt":
                        self.items.append(Shirt.from_dict(item))
                    elif item["type"] == "jeans":
                        self.items.append(Jeans.from_dict(item))
                    elif item["type"] == "jacket":
                        self.items.append(Jacket.from_dict(item))
                self.favourite_outfits = data.get("favourite_outfits", [])
        except (FileNotFoundError, json.JSONDecodeError):
            self.items = []
            self.favourite_outfits = []

    def save_data(self):
        with open(self.filename, "w") as f:
            json.dump({
                "items": [item.to_dict() for item in self.items],
                "favourite_outfits": self.favourite_outfits
            }, f, indent=4)

    def add_item(self, item):
        for i in self.items:
            if i.item_id == item.item_id:
                print(f"❌ Item ID '{item.item_id}' already exists!")
                return
        self.items.append(item)
        self.save_data()
        print(f"✅ {item.name} added to wardrobe!")

    def get_items_by_type(self, item_type):
        return [i for i in self.items if i.to_dict()["type"] == item_type]

    def view_wardrobe(self):
        if not self.items:
            print("❌ Your wardrobe is empty!")
            return
        shirts = self.get_items_by_type("shirt")
        jeans = self.get_items_by_type("jeans")
        jackets = self.get_items_by_type("jacket")
        print("\n=== Your Wardrobe ===")
        print(f"\n👕 Shirts ({len(shirts)}):")
        for s in shirts:
            print(f"   {s.get_info()}")
        print(f"\n👖 Jeans ({len(jeans)}):")
        for j in jeans:
            print(f"   {j.get_info()}")
        print(f"\n🧥 Jackets ({len(jackets)}):")
        for j in jackets:
            print(f"   {j.get_info()}")

    def save_favourite(self, outfit):
        if outfit:
            self.favourite_outfits.append(outfit)
            self.save_data()
            print("❤️ Outfit saved to favourites!")

    def view_favourites(self):
        if not self.favourite_outfits:
            print("❌ No favourite outfits saved!")
            return
        print("\n=== Favourite Outfits ===")
        for i, outfit in enumerate(self.favourite_outfits, 1):
            shirt = self._get_item_by_id(outfit["shirt_id"])
            jean = self._get_item_by_id(outfit["jeans_id"])
            jacket = self._get_item_by_id(outfit["jacket_id"]) if outfit["jacket_id"] else None
            print(f"\n❤️ Outfit {i}:")
            print(f"   {shirt.get_info() if shirt else 'Shirt not found'}")
            print(f"   {jean.get_info() if jean else 'Jeans not found'}")
            print(f"   {jacket.get_info() if jacket else 'No jacket'}")

    def _get_item_by_id(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                return item
        return None
    