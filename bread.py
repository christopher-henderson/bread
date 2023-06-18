class Gram(float):
    pass


class Calorie(float):
    pass


class NutritionalLabel:

    def __init__(self, serving_size: Gram, calories: Calorie, carbs: Gram, protein: Gram, fat: Gram, fiber: Gram):
        self.serving_size = serving_size
        self.calories = calories
        self.carbs = carbs
        self.protein = protein
        self.fat = fat
        self.fiber = fiber

    def macros(self, grams: Gram):
        percentage = grams / self.serving_size
        return Macros(calories=percentage * self.calories,
                      carbs=percentage * self.carbs,
                      protein=percentage * self.protein,
                      fat=percentage * self.fat,
                      fiber=percentage * self.fiber)


class Macros:

    def __init__(self, calories: Calorie, carbs: Gram, protein: Gram, fat: Gram, fiber: Gram):
        self.calories = calories
        self.carbs = carbs
        self.protein = protein
        self.fat = fat
        self.fiber = fiber

    def __add__(self, other):
        return Macros(calories=self.calories + other.calories,
                      carbs=self.carbs + other.carbs,
                      protein=self.protein + other.protein,
                      fat=self.fat + other.fat,
                      fiber=self.fiber + other.fiber)

    def __str__(self):
        return f'''\
    calories: {self.calories:.2f}
    carbs:    {self.carbs:.2f}
    protein:  {self.protein:.2f}
    fat:      {self.fat:.2f}
    fiber:    {self.fiber:.2f}'''


WholeWheatNutrition = NutritionalLabel(serving_size=Gram(38),
                                       calories=Calorie(140),
                                       carbs=Gram(27),
                                       protein=Gram(6),
                                       fat=Gram(0.5),
                                       fiber=Gram(5))

WhiteWheatNutrition = NutritionalLabel(serving_size=Gram(36),
                                       calories=Calorie(130),
                                       carbs=Gram(26),
                                       protein=Gram(5),
                                       fat=Gram(0.5),
                                       fiber=Gram(1))

StarterNutrition = WholeWheatNutrition


class Ingredient:
    def __init__(self, label: NutritionalLabel, grams: Gram):
        self.grams = grams
        self.label = label

    def macros(self):
        return self.label.macros(self.grams)


class WholeWheat(Ingredient):

    def __init__(self, grams: Gram):
        Ingredient.__init__(self, WholeWheatNutrition, grams)


class WhiteWheat(Ingredient):

    def __init__(self, grams: Gram):
        Ingredient.__init__(self, WhiteWheatNutrition, grams)


class Starter(Ingredient):

    def __init__(self, grams: Gram):
        Ingredient.__init__(self, StarterNutrition, grams)


class Sourdough:

    def __init__(self, starter: Starter, whole: WholeWheat, white: WhiteWheat):
        self.starter = starter
        self.whole = whole
        self.white = white

    def macros(self) -> Macros:
        return self.starter.macros() + self.whole.macros() + self.white.macros()

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.macros())
