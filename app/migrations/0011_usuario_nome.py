# Generated by Django 5.1.3 on 2024-12-06 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_usuario_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='nome',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
    ]