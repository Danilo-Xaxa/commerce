# Generated by Django 3.2.9 on 2022-03-11 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auction_bid_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='auction',
        ),
        migrations.RemoveField(
            model_name='bid',
            name='user',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='auction',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.DeleteModel(
            name='Auction',
        ),
        migrations.DeleteModel(
            name='Bid',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]