# Generated by Django 5.0.6 on 2024-11-28 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0002_remove_project_technologies_used_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='technologies_used',
            new_name='skills_used',
        ),
    ]