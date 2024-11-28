# Generated by Django 5.0.6 on 2024-11-28 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0003_rename_technologies_used_project_skills_used'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='rank',
            field=models.PositiveIntegerField(choices=[(1, 'Rank 1 - Highest Priority'), (2, 'Rank 2'), (3, 'Rank 3'), (4, 'Rank 4'), (5, 'Rank 5 - Lowest Priority')], default=1),
        ),
    ]
