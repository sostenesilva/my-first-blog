# Generated by Django 2.0 on 2020-02-08 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hobby', '0004_auto_20200208_1930'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='letra',
        ),
        migrations.AlterField(
            model_name='post',
            name='cifra',
            field=models.TextField(default='Cifra indisponível até o momento.', max_length=2000),
        ),
        migrations.AlterField(
            model_name='post',
            name='creditos',
            field=models.TextField(default='Créditos:', max_length=2000),
        ),
    ]
