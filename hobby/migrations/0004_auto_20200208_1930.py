# Generated by Django 2.0 on 2020-02-08 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hobby', '0003_post_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cifra',
            field=models.CharField(default='Cifra indisponível até o momento.', max_length=2000),
        ),
        migrations.AddField(
            model_name='post',
            name='creditos',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]