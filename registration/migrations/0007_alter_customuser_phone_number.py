# Generated by Django 4.2.3 on 2023-07-22 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_alter_customuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(blank=True, default=1, max_length=25, unique=True),
            preserve_default=False,
        ),
    ]