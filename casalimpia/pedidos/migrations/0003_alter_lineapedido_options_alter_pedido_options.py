# Generated by Django 4.1.5 on 2023-03-27 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_alter_lineapedido_options_alter_pedido_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lineapedido',
            options={'ordering': ['id'], 'verbose_name': 'lineapedido', 'verbose_name_plural': 'lineaspedidos'},
        ),
        migrations.AlterModelOptions(
            name='pedido',
            options={'ordering': ['id'], 'verbose_name': 'pedido', 'verbose_name_plural': 'pedidos'},
        ),
    ]