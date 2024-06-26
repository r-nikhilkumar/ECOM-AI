# Generated by Django 5.0.4 on 2024-04-20 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_catagory_item_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='Dyn_price_strat',
            field=models.CharField(choices=[('Dynamic Bundling', 0), ('Dynamic Markdowns', 1), ('Personalized Pricing', 2), ('Discounting', 3)], default='Personalized Pricing', max_length=30),
        ),
        migrations.AddField(
            model_name='item',
            name='comp_price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='eco_ind',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='price_elas',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='profitability',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='revenue',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='seasonality',
            field=models.CharField(choices=[('Low', 0), ('Medium', 1), ('High', 2)], default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='sentiment',
            field=models.CharField(choices=[('Negative', -1), ('Neutral', 0), ('Positive', 1)], default='Neutral', max_length=10),
        ),
        migrations.AddField(
            model_name='user',
            name='purchase_history',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='flag',
            field=models.CharField(choices=[('Inactive', 0), ('New', 1), ('Regular', 2), ('Premium', 3)], default='New', max_length=10),
        ),
    ]
