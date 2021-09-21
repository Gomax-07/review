# Generated by Django 3.2.7 on 2021-09-21 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='status',
            field=models.IntegerField(blank=True, choices=[(1, 'Too poor'), (2, 'Poor'), (3, 'Try'), (4, 'Somewhat good'), (5, 'Neutral'), (6, 'Somewhat good'), (7, 'Good'), (8, 'Too good'), (9, 'Near perfect'), (10, 'Excellent')], default='5', help_text='Project Ratings(Out of 10)'),
        ),
    ]
