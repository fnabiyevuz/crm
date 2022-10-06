# Generated by Django 3.1.7 on 2021-05-31 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_remove_order_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='phone',
        ),
        migrations.AddField(
            model_name='order',
            name='card',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]