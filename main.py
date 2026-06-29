from wardrobe import Wardrobe
from clothing_item import Shirt, Jeans, Jacket
from outfit_generator import OutfitGenerator

def main():
    wardrobe = Wardrobe()
    generator = OutfitGenerator(wardrobe)

    while True:
        print("\n=== Virtual Fashion Wardrobe ===")
        print(f"    👕 Shirts: {len(wardrobe.get_items_by_type('shirt'))}  "
              f"👖 Jeans: {len(wardrobe.get_items_by_type('jeans'))}  "
              f"🧥 Jackets: {len(wardrobe.get_items_by_type('jacket'))}")
        print("1. Add Shirt")
        print("2. Add Jeans")
        print("3. Add Jacket")
        print("4. View Wardrobe")
        print("5. Generate Outfit Suggestion")
        print("6. Save Favourite Outfit")
        print("7. View Favourite Outfits")
        print("8. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            item_id = input("Enter shirt ID (e.g. SH001): ").strip()
            name = input("Enter shirt name: ").strip()
            color = input("Enter color: ").strip()
            brand = input("Enter brand: ").strip()
            size = input("Enter size (S/M/L/XL): ").strip().upper()
            fabric = input("Enter fabric (Cotton/Polyester/Linen): ").strip()
            shirt = Shirt(item_id, name, color, brand, size, fabric)
            wardrobe.add_item(shirt)

        elif choice == "2":
            item_id = input("Enter jeans ID (e.g. JN001): ").strip()
            name = input("Enter jeans name: ").strip()
            color = input("Enter color: ").strip()
            brand = input("Enter brand: ").strip()
            try:
                waist_size = int(input("Enter waist size (e.g. 30/32/34): ").strip())
            except ValueError:
                print("❌ Invalid waist size!")
                continue
            fit_type = input("Enter fit type (Slim/Regular/Loose): ").strip()
            jeans = Jeans(item_id, name, color, brand, waist_size, fit_type)
            wardrobe.add_item(jeans)

        elif choice == "3":
            item_id = input("Enter jacket ID (e.g. JK001): ").strip()
            name = input("Enter jacket name: ").strip()
            color = input("Enter color: ").strip()
            brand = input("Enter brand: ").strip()
            jacket_type = input("Enter jacket type (Denim/Leather/Hoodie): ").strip()
            waterproof_input = input("Is it waterproof? (yes/no): ").strip().lower()
            waterproof = waterproof_input == "yes"
            jacket = Jacket(item_id, name, color, brand, jacket_type, waterproof)
            wardrobe.add_item(jacket)

        elif choice == "4":
            wardrobe.view_wardrobe()

        elif choice == "5":
            last_outfit = generator.generate_outfit()

        elif choice == "6":
            try:
                wardrobe.save_favourite(last_outfit)
            except UnboundLocalError:
                print("❌ Generate an outfit first before saving!")

        elif choice == "7":
            wardrobe.view_favourites()

        elif choice == "8":
            print(" Goodbye! Stay stylish! 👗✨")
            break

        else:
            print("❌ Invalid choice! Please enter 1-8.")

if __name__ == "__main__":
    main()