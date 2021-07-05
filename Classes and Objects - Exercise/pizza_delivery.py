class PizzaDelivery:
    
    def __init__(self, name: str, price: float, ingredients: dict) -> None:
        self.name = name
        self.price = price
        self.ingredients = dict(ingredients)
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, price_per_ingredient: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        if not ingredient in self.ingredients:
            self.ingredients[ingredient] = quantity
            self.price += price_per_ingredient * quantity
        else:
            self.ingredients[ingredient] += quantity
            self.price += price_per_ingredient * quantity

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_ingredient: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        if not ingredient in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        if  self.ingredients[ingredient] - quantity < 0:
            return f"Please check again the desired quantity of {ingredient}!"
        self.price -= quantity * price_per_ingredient
        self.ingredients[ingredient] -= quantity
    def make_order(self):
        self.ordered = True
        unpacking_ingredients = (', '.join([f'{i}: {q}' for i, q in self.ingredients.items()]))
        return f"You've ordered pizza {self.name} prepared with {unpacking_ingredients} and the price will be {self.price}lv."



margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))
