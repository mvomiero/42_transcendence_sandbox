# Generated by Django 4.2.7 on 2023-11-14 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='dashboard_color',
            field=models.CharField(default='', max_length=20),
        ),
    ]
