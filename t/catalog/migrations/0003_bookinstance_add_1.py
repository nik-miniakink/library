# Generated by Django 3.0.2 on 2020-01-17 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_remove_bookinstance_add_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='add_1',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
