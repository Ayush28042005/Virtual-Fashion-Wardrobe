import random

class OutfitGenerator:
    def __init__(self, wardrobe):
        self.wardrobe = wardrobe        # Reference to the Wardrobe object

    def generate_outfit(self):
        shirts = self.wardrobe.get_items_by_type("shirt")
        jeans = self.wardrobe.get_items_by_type("jeans")
        jackets = self.wardrobe.get_items_by_type("jacket")

        if not shirts or not jeans:
            print("❌ Need at least one shirt and one jeans to generate outfit!")
            return None

        shirt = random.choice(shirts)
        jean = random.choice(jeans)
        jacket = random.choice(jackets) if jackets else None

        print("\n👗 === Outfit Suggestion === 👗")
        print(f"  {shirt.get_info()}")
        print(f"  {jean.get_info()}")
        if jacket:
            print(f"  {jacket.get_info()}")
        else:
            print("  🧥 No jacket available")

        return {
            "shirt_id": shirt.item_id,
            "jeans_id": jean.item_id,
            "jacket_id": jacket.item_id if jacket else None
        }

    def __str__(self):
        return "👗 Outfit Generator"
    