# Generated by Django 4.2.3 on 2023-08-21 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Default', '0005_remove_userprofile_purchases_remove_userprofile_user_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='order',
        ),
        migrations.AlterField(
            model_name='details',
            name='Email',
            field=models.CharField(max_length=100),
        ),
    ]
