from django.db import models

RECEIPE_THEME = [
    (
        "Occasion",
        (
            ("su", "Dimanche soir"),
            ("ch", "Noël"),
            ("sv", "Saint Valentin"),
            ("ea", "Pâques"),
            ("ch", "Chandeleur"),
            ("rm", "Ramadan"),
            ("hl", "Halloween"),
        ),
    ),
    (
        "Localisation",
        (
            ("it", "Italien"),
            ("us", "Américain"),
            ("jp", "Japonnais"),
            ("eu", "Européen"),
            ("as", "Asiatique"),
            ("sa", "Sud-Américain"),
            ("fr", "Français"),
            ("mx", "Mexicain"),
            ("en", "Anglais"),
            ("bx", "Belgique"),
            ("gk", "Grecque"),
            ("mg", "Maghrebin"),
            ("pt", "Portugais"),
            ("in", "Indien"),
            ("af", "Africain"),
        ),
    ),
    (
        "Autres",
        (
            ("co", "Comfort"),
            ("re", "Recevoir"),
            ("bq", "Barbecue"),
            ("sp", "A la soupe !"),
            ("cl", "Classiques"),
            ("ck", "Cocktails"),
            ("sm", "Smoothie"),
            ("zw", "Zéro-déchet"),
        ),
    ),
]
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
    type_ingr = models.CharField(
        verbose_name="Type", max_length=3, choices=TypeChoice.choices, default=TypeChoice.OTHERS
    )
    nutriscore = models.CharField(
        max_length=1,
        choices=[("a", "A"), ("b", "B"), ("c", "C"), ("d", "D"), ("e", "E")],
        default="a",
    )
    season = models.CharField(max_length=3, choices=SEASON, default="any")
    image = models.ImageField(blank=True)
    
    def __str__(self):
        return self.name


class Regime(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


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
    type_receipe = models.CharField(
        max_length=3, choices=TypeChoice.choices, default=TypeChoice.COURSE
    )
    theme = models.CharField(max_length=2, choices=RECEIPE_THEME)
    source = models.CharField(max_length=200, blank=True)
    time = models.DecimalField(verbose_name="Temps de préparation", max_digits=5, decimal_places=1)
    difficulty = models.CharField(
        max_length=2, choices=DifficultyChoice.choices, default=DifficultyChoice.NORMAL
    )
    regimes = models.ManyToManyField(Regime)
    image = models.ImageField(blank=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
