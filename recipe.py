from review import Review

class Recipe:

    _all = []

    def __init__(self, name):
        self._name = name
        Recipe._all.append(self)

    @property
    def name(self):
        return self._name

    @classmethod
    def all(cls):
        return cls._all

    def reviews(self):
        return [review for review in Review.all() if review.recipe == self]

    def avg_rating(self):
        recipe_ratings = [review.rating for review in self.reviews()]
        if len(recipe_ratings) > 0:
            return (sum(recipe_ratings)/len(recipe_ratings))

    @classmethod
    def top_three(cls):
        ratings_dict = {recipe : recipe.avg_rating() for recipe in cls.all() if type(recipe.avg_rating()) == float}
        sorted_list = []
        for rating in ratings_dict:
            if len(sorted_list) < 3:
                sorted_list.append(rating)
        return sorted_list

    @classmethod
    def bottom_three(cls):
        ratings_dict = {recipe : recipe.avg_rating() for recipe in cls.all() if type(recipe.avg_rating()) == float}
        sorted_list = sorted(ratings_dict, key = ratings_dict.get, reverse = False)[:3]

        return sorted_list

    def top_five_reviews(self):
        reviews_dict = {review: review.rating for review in self.reviews()}
        return sorted(reviews_dict, key = reviews_dict.get)[:5]
