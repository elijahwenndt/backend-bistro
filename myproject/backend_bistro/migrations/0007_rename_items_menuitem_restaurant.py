# Generated by Django 4.1.3 on 2022-11-14 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend_bistro', '0006_rename_name_category_title_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='items',
            new_name='restaurant',
        ),
    ]