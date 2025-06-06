# Generated by Django 5.2 on 2025-04-15 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('protein_goal', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Proteína (g)')),
                ('carbs_goal', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Carboidratos (g)')),
                ('fat_goal', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Gordura (g)')),
                ('calories_goal', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Calorias (kcal)')),
                ('water_goal', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Água (mL)')),
            ],
        ),
    ]
