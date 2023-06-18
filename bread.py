class Gram(int):
	pass


class Calorie(int):
	pass


class Nutrition:

	SERVING_SIZE: Gram = 1

	CALORIES:Calorie   = 0
	CARBS: Gram        = 0
	PROTEIN: Gram      = 0
	FAT: Gram          = 0
	FIBER: Gram        = 0

	def __init__(self, grams: Gram):
		percentage = grams / self.SERVING_SIZE
		self.calories = percentage * self.CALORIES
		self.carbs = percentage * self.CARBS
		self.protein = percentage * self.PROTEIN
		self.fat = percentage * self.FAT
		self.fiber = percentage * self.FIBER

	def __add__(self, other):
		total = Nutrition(0)
		total.calories = self.calories + other.calories
		total.carbs = self.carbs + other.carbs
		total.protein = self.protein + other.protein
		total.fat = self.fat + other.fat
		total.fiber = self.fiber + other.fiber
		return total

	def __str__(self):
		return f'''\
calories: {self.calories:.2f}
carbs:    {self.carbs:.2f}
protein:  {self.protein:.2f}
fat:      {self.fat:.2f}
fiber:    {self.fiber:.2f}'''


class WholeWheat(Nutrition):

	SERVING_SIZE: Calorie = 38

	CALORIES: Gram        = 140
	CARBS: Gram           = 27
	PROTEIN: Gram         = 6
	FAT: Gram             = 0.5
	FIBER: Gram           = 5


class WhiteWheat(Nutrition):

	SERVING_SIZE: Calorie = 36

	CALORIES: Gram        = 130
	CARBS: Gram           = 26
	PROTEIN: Gram         = 5
	FAT:Gram              = 0.5
	FIBER: Gram           = 1

class Starter(WholeWheat):
	pass


class Sourdough:

	def __init__(self, starter: Starter, whole: WholeWheat, white: WhiteWheat):
		self.starter = starter
		self.whole = whole
		self.white = white

	def nutrition(self) -> Nutrition:
		return self.starter + self.whole + self.white

	def __repr__(self):
		return str(self)

	def __str__(self):
		return str(self.nutrition())
