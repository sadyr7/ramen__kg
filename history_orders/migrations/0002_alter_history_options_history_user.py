# Generated by Django 4.2.3 on 2023-07-25 08:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('history_orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='history',
            options={'verbose_name': 'История', 'verbose_name_plural': 'Истории'},
        ),
        migrations.AddField(
            model_name='history',
            name='user',
            field=models.ForeignKey(default=1, on_delete=models.Model, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]