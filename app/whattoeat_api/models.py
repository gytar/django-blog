from django.db import models

RECEIPE_THEME = [(),]
SEASON = [
    ("win", "Hiver"), 
    ("fal", "Automne"), 
    ("spr", "Printemps"), 
    ("sum", "Eté"),
    ("any", "Toutes"),
]


class Ingredient(models.Model):
    # Enums
    class TypeChoice(models.TextChoices):
        FRUIT = "fru", "Fruit"
        VEGGIE = "veg", "Légume"
        LEGUME = "leg", "Légumineuse"
        CARNE = "car", "Simili-carne"
        SAUCE = "sau", "Sauce"
        DAIRY = "dai", "Simili laitier"
        STARCH = "sta", "Féculent"
        CEREAL = "cer", "Céréale"
        FLOUR = "flo", "Farine"
        HELPERS = "hel", "Aides culinaires"
        SWEET = "swe", "Sucré"
        OTHERS = "oth", "Autres"
    
    
    name = models.CharField()
    type_ingr = models.CharField(name="Type", max_length=3, choices=TypeChoice.choices, default=TypeChoice.OTHERS)
    nutriscore = models.CharField(max_length=1, choices=[("a", "A"), ("b", "B"), ("c", "C"), ("d", "D"), ("e", "E")], default="a")
    season = models.CharField(max_length=3, choices=SEASON, default="any")
    image = models.ImageField()


class Regime(models.Model):
    name = models.CharField(max_length=50)


class Receipe(models.Model):
    class TypeChoice(models.TextChoices):
        APERITIF = "ape", "Apéritif"
        STARTER = "sta", "Entrée"
        COURSE = "cou", "Plat"
        DESSERT = "des", "Déssert"
    class DifficultyChoice(models.TextChoices):
        VERY_EASY = "ve", "Très facile"
        EASY = "ee", "Facile"
        NORMAL = "nn", "Normal"
        HARD = "hh", "Difficile"
        VERY_HARD = "vh", "Très difficile"
        
    name = models.CharField()
    pub_date = models.DateTimeField()
    ingredients = models.ManyToManyField(Ingredient)
    type_receipe = models.CharField(name="Type", max_length=3, choices=TypeChoice.choices, default=TypeChoice.COURSE)
    theme = models.CharField()
    source = models.CharField(max_length=200)
    time = models.DecimalField(name="Temps de préparation", max_digits=5, decimal_places=1)
    difficulty = models.CharField(max_length=2, choices=DifficultyChoice.choices, default=DifficultyChoice.NORMAL)
    regimes = models.ManyToManyField(Regime)
    image = models.ImageField()
    description = models.TextField()
