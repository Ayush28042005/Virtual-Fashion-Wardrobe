# Virtual Fashion Wardrobe

A Python-based command-line application that acts as your personal digital wardrobe. Add clothing items, generate random outfit suggestions, and save your favourite combinations — all stored persistently in a JSON file.

---

## Features

- Add shirts with size and fabric details
- Add jeans with waist size and fit type
- Add jackets with type and waterproof status
- View full wardrobe organized by category
- Generate random outfit suggestions
- Save favourite outfit combinations
- View all saved favourite outfits
- Live clothing count in menu header
- Persistent storage using JSON

---

## Class Hierarchy

```
ClothingItem (Parent)
    │
    ├── Shirt   → size, fabric
    ├── Jeans   → waist_size, fit_type
    └── Jacket  → jacket_type, waterproof

Wardrobe          → manages all clothing items and favourites
OutfitGenerator   → generates random outfit suggestions
```

---

## OOP Concepts Used

| Concept | Where Used |
|---|---|
| **Inheritance** | Shirt, Jeans, Jacket inherit from ClothingItem |
| **Polymorphism** | `get_info()` returns different output per clothing type |
| **Encapsulation** | Item details stored inside class attributes |
| **Composition** | OutfitGenerator contains Wardrobe; Wardrobe contains ClothingItems |
| **Private Methods** | `_get_item_by_id()` is private to Wardrobe class |

---

## Project Structure

```
Virtual-Fashion-Wardrobe/
│
├── clothing_item.py      → ClothingItem, Shirt, Jeans, Jacket classes
├── outfit_generator.py   → OutfitGenerator class
├── wardrobe.py           → Wardrobe manager class
├── main.py               → Entry point and menu
└── data.json             → Persistent JSON storage
```

---

## How To Run

```bash
python main.py
```

No external libraries required.

---

## Menu Options

```
=== Virtual Fashion Wardrobe ===
👕 Shirts: 2  👖 Jeans: 1  🧥 Jackets: 1
1. Add Shirt
2. Add Jeans
3. Add Jacket
4. View Wardrobe
5. Generate Outfit Suggestion
6. Save Favourite Outfit
7. View Favourite Outfits
8. Exit
```

---

## Future Upgrades

- Color matching algorithm
- Weather-based outfit recommendations
- AI outfit suggestions
- Outfit calendar planner
- Style tags and filters

---

## Author

**Ayush Saini**

