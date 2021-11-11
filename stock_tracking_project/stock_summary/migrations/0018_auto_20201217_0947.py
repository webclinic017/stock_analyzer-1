# Generated by Django 3.1.3 on 2020-12-17 08:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock_summary', '0017_auto_20201214_0950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='i_owned',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='i_watching',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='q_shares_owned',
        ),
        migrations.CreateModel(
            name='UserStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_added', models.DateField(auto_now_add=True)),
                ('i_watching', models.BooleanField()),
                ('i_owned', models.BooleanField()),
                ('q_shares_owned', models.DecimalField(decimal_places=6, max_digits=9)),
                ('a_share_price_bought', models.DecimalField(decimal_places=3, max_digits=8)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock_summary.stock')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'stock')},
            },
        ),
    ]