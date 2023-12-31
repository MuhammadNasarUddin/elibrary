# Generated by Django 5.0 on 2023-12-29 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Default', '0008_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='Category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='Main_Cat',
            new_name='main_cat',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='Status',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='Main_Cat',
            new_name='main_cat',
        ),
        migrations.RenameField(
            model_name='details',
            old_name='Book',
            new_name='book',
        ),
        migrations.RenameField(
            model_name='details',
            old_name='Status',
            new_name='status',
        ),
        migrations.AlterModelTable(
            name='author',
            table='author',
        ),
        migrations.AlterModelTable(
            name='book',
            table='book',
        ),
        migrations.AlterModelTable(
            name='category',
            table='category',
        ),
        migrations.AlterModelTable(
            name='contact',
            table='contact',
        ),
        migrations.AlterModelTable(
            name='details',
            table='details',
        ),
        migrations.AlterModelTable(
            name='main_cat',
            table='main_cat',
        ),
        migrations.AlterModelTable(
            name='slider',
            table='slider',
        ),
        migrations.AlterModelTable(
            name='status',
            table='status',
        ),
        migrations.AlterModelTable(
            name='testimonials',
            table='testimonials',
        ),
    ]
