# Generated by Django 5.1.3 on 2024-11-20 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_nome_areas_nome_rename_email_usuario_email_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Areas',
            new_name='Area',
        ),
        migrations.RenameModel(
            old_name='Cursos',
            new_name='Curso',
        ),
    ]