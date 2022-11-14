# Generated by Django 4.1.3 on 2022-11-14 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend_bistro', '0004_ingredients_menuitem_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='backend_bistro.category'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='cuisine_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cuisine', to='backend_bistro.cuisine'),
        ),
    ]
