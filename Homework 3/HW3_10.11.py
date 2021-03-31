#  Luke Gilin 1216992

class FoodItem:
    def __init__(self, name="None", fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


if __name__ == '__main__':
    #  Get user inputs
    DefaultFood = FoodItem()

    FoodName = str(input())
    FoodFat = float(input())
    FoodCarbs = float(input())
    FoodProtein = float(input())
    FoodServings = float(input())

    # Call constructors

    MyFood = FoodItem(FoodName, FoodFat, FoodCarbs, FoodProtein)

    #  Print default constructor
    DefaultFood.print_info()
    print('Number of calories for {s:.2f} serving(s): {c:.2f}'.format(s=FoodServings, c=DefaultFood.get_calories(FoodServings)))
    print()
    #  Print MyFood info from class
    MyFood.print_info()
    #  Print Calories
    print('Number of calories for {s:.2f} serving(s): {c:.2f}'.format(s=FoodServings, c=MyFood.get_calories(FoodServings)))
