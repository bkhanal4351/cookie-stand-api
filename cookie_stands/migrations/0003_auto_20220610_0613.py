# Generated by Django 3.2.7 on 2022-06-10 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookie_stands', '0002_cookiestand_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cookiestand',
            old_name='tags',
            new_name='hourly_sales',
        ),
        migrations.RenameField(
            model_name='cookiestand',
            old_name='name',
            new_name='location',
        ),
        migrations.AddField(
            model_name='cookiestand',
            name='average_cookies_per_sale',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='cookiestand',
            name='maximum_customers_per_hour',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cookiestand',
            name='minimum_customers_per_hour',
            field=models.IntegerField(default=0),
        ),
    ]
