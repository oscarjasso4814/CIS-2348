
class FoodItem:

    def __init__(self, item_name = 'None', amount_fat = 0, amount_carbs = 0, amount_protein = 0):
        self.name = item_name
        self.fat = amount_fat
        self.carbs = amount_carbs
        self.protein = amount_protein

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
        return calories

    def print_info(self):
        print(f'Nutritional information per serving of {self.name}:')
        print(f'   Fat: {self.fat:.2f} g')
        print(f'   Carbohydrates: {self.carbs:.2f} g')
        print(f'   Protein: {self.protein:.2f} g')


if __name__ == "__main__":
    item_name = input()

    amount_fat = float(input())
    amount_carbs = float(input())
    amount_protein = float(input())
    num_servings = float(input())

    food_item = FoodItem()
    food_item.print_info()
    print(f'Number of calories for {num_servings:.2f} serving(s): {food_item.get_calories(1.0):.2f}')

    print()

    food_item_2 = FoodItem(item_name, amount_fat, amount_carbs, amount_protein)

    food_item_2.print_info()
    print(f'Number of calories for {num_servings:.2f} serving(s): {food_item_2.get_calories(num_servings):.2f}')