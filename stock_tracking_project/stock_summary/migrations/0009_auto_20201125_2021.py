# Generated by Django 3.1.3 on 2020-11-25 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_summary', '0008_auto_20201125_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockwatch',
            name='stock',
        ),
        migrations.AddField(
            model_name='stock',
            name='i_owned',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='i_watching',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='StockOwned',
        ),
        migrations.DeleteModel(
            name='StockWatch',
        ),
    ]