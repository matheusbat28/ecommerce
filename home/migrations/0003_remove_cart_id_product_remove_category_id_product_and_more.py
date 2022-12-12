# Generated by Django 4.1.4 on 2022-12-11 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_carrinho_cart_alter_cart_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='id_Product',
        ),
        migrations.RemoveField(
            model_name='category',
            name='id_Product',
        ),
        migrations.AlterField(
            model_name='product',
            name='id_image',
            field=models.ManyToManyField(db_column='id_imagens', to='home.image', verbose_name='image'),
        ),
        migrations.AddField(
            model_name='cart',
            name='id_product',
            field=models.ManyToManyField(db_column='id_product', to='home.product', verbose_name='product'),
        ),
        migrations.AddField(
            model_name='category',
            name='id_product',
            field=models.ManyToManyField(db_column='id_product', to='home.product', verbose_name='product'),
        ),
    ]
