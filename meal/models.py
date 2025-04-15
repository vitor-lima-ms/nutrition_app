from django.db import models

# Create your models here.

class Meal(models.Model):
    meal_name = models.CharField(verbose_name="Nome da refeição", max_length=255)
    protein = models.DecimalField(verbose_name='Proteínas (g)', max_digits=5, decimal_places=2)
    carbs = models.DecimalField(verbose_name='Carboidratos (g)', max_digits=5, decimal_places=2)
    fat = models.DecimalField(verbose_name='Gorduras (g)', max_digits=5, decimal_places=2)
    calories = models.DecimalField(verbose_name='Calorias (kcal)', max_digits=5, decimal_places=2)
    water = models.DecimalField(verbose_name='Água (mL)', max_digits=5, decimal_places=2, default=0)
    datetime = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-datetime',)

    def __str__(self):
        return self.meal_name