# Generated by Django 4.1.7 on 2023-02-22 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_remove_menuitem_children_menuitem_children'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='children',
            field=models.ManyToManyField(null=True, to='mainapp.menuitem'),
        ),
    ]
