# Generated by Django 5.1.1 on 2024-09-24 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_alter_notes_priority_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='priority_level',
            field=models.CharField(choices=[('1', 'Low'), ('2', 'Medium'), ('3', 'High')], default='3', max_length=10),
        ),
    ]
