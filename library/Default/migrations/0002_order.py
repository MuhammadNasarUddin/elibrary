# Generated by Django 4.2.3 on 2023-08-17 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Default', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/')),
                ('b_name', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=13)),
            ],
        ),
    ]
