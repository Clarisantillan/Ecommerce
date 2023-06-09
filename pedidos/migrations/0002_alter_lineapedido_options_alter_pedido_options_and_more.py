# Generated by Django 4.1.5 on 2023-03-27 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lineapedido',
            options={'ordering': ['id'], 'verbose_name': 'Línea Pedido', 'verbose_name_plural': 'Líneas Pedidos'},
        ),
        migrations.AlterModelOptions(
            name='pedido',
            options={'ordering': ['id'], 'verbose_name': 'Pedido', 'verbose_name_plural': 'Pedidos'},
        ),
        migrations.RenameField(
            model_name='lineapedido',
            old_name='pedido_id',
            new_name='pedido',
        ),
        migrations.RenameField(
            model_name='lineapedido',
            old_name='producto_id',
            new_name='producto',
        ),
    ]
