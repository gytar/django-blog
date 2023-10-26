from django.contrib import admin
from .models import Receipe, Ingredient, Regime

@admin.register(Receipe)
class ReceipeAdmin(admin.ModelAdmin):
    filter_horizontal = ["ingredients", "regimes"]
    fieldsets = [
        (
            None,
            {
                "fields": [
                    "name",
                    "pub_date",
                    ("difficulty", "time"),
                    ("theme", "type_receipe"),
                    "ingredients",
                    "regimes",
                    "description",
                ],
            },
        ),
        (
            "Advanced options", 
            {"classes": ["collapse"], "fields": ["image", "source"]}
        ),
    ]


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass


@admin.register(Regime)
class RegimeAdmin(admin.ModelAdmin):
    pass
