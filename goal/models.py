from django.db import models

# Create your models here.

class Goal(models.Model):
    protein_goal = models.DecimalField(verbose_name='Proteínas (g)', max_digits=7, decimal_places=2)
    carbs_goal = models.DecimalField(verbose_name='Carboidratos (g)', max_digits=7, decimal_places=2)
    fat_goal = models.DecimalField(verbose_name='Gorduras (g)', max_digits=7, decimal_places=2)
    calories_goal = models.DecimalField(verbose_name='Calorias (kcal)', max_digits=7, decimal_places=2)
    water_goal = models.DecimalField(verbose_name='Água (mL)', max_digits=7, decimal_places=2)