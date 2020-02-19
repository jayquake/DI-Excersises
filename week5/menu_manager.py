class MenuManager:
    def __init__(self, resturant):
        self.menu = {}
        self.name = {}
        self.price = {}
        self.spice_level={A : not spicy,B:"a little spicy",C:"very spicy"}
        self.gluten_index = {}

        def add_item(name,price,spice,gluten):
            self.name = input(MenuManager.name("Name of your Dish"))
            self.price = input(MenuManager.price("How much is your Dish"))
            self.spice = input(MenuManager.spice_level("Spice Level"))
            self.gluten_index = input(MenuManager.gluten_index("Gluten"))
            self.menu.append(name,price,spice,gluten)
            add_item()

first_menu = MenuManager("jays_menu")
first_menu.add_item()