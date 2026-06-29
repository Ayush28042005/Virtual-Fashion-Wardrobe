class ClothingItem:
    def __init__(self, item_id, name, color, brand):
        self.item_id = item_id          # Unique ID for item
        self.name = name                # Name of the item
        self.color = color              # Color of the item
        self.brand = brand              # Brand name

    def get_info(self):
        return f"[{self.item_id}] {self.name} | Color: {self.color} | Brand: {self.brand}"

    def to_dict(self):
        return {
            "item_id": self.item_id,
            "name": self.name,
            "color": self.color,
            "brand": self.brand
        }

    def __str__(self):
        return self.get_info()


class Shirt(ClothingItem):
    def __init__(self, item_id, name, color, brand, size, fabric):
        super().__init__(item_id, name, color, brand)
        self.size = size                # S, M, L, XL
        self.fabric = fabric            # Cotton, Polyester etc.

    def get_info(self):
        return f"👕 Shirt: {self.name} | Color: {self.color} | Brand: {self.brand} | Size: {self.size} | Fabric: {self.fabric}"

    def to_dict(self):
        data = super().to_dict()
        data["size"] = self.size
        data["fabric"] = self.fabric
        data["type"] = "shirt"
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(data["item_id"], data["name"], data["color"],
                   data["brand"], data["size"], data["fabric"])


class Jeans(ClothingItem):
    def __init__(self, item_id, name, color, brand, waist_size, fit_type):
        super().__init__(item_id, name, color, brand)
        self.waist_size = waist_size    # e.g. 30, 32, 34
        self.fit_type = fit_type        # Slim, Regular, Loose

    def get_info(self):
        return f"👖 Jeans: {self.name} | Color: {self.color} | Brand: {self.brand} | Waist: {self.waist_size} | Fit: {self.fit_type}"

    def to_dict(self):
        data = super().to_dict()
        data["waist_size"] = self.waist_size
        data["fit_type"] = self.fit_type
        data["type"] = "jeans"
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(data["item_id"], data["name"], data["color"],
                   data["brand"], data["waist_size"], data["fit_type"])


class Jacket(ClothingItem):
    def __init__(self, item_id, name, color, brand, jacket_type, waterproof):
        super().__init__(item_id, name, color, brand)
        self.jacket_type = jacket_type      # Denim, Leather, Hoodie etc.
        self.waterproof = waterproof        # True or False

    def get_info(self):
        wp = "Yes" if self.waterproof else "No"
        return f"🧥 Jacket: {self.name} | Color: {self.color} | Brand: {self.brand} | Type: {self.jacket_type} | Waterproof: {wp}"

    def to_dict(self):
        data = super().to_dict()
        data["jacket_type"] = self.jacket_type
        data["waterproof"] = self.waterproof
        data["type"] = "jacket"
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(data["item_id"], data["name"], data["color"],
                   data["brand"], data["jacket_type"], data["waterproof"])