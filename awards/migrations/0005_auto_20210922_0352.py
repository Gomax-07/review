# Generated by Django 3.2.7 on 2021-09-22 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0004_auto_20210922_0350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='detail',
        ),
        migrations.AddField(
            model_name='detail',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='awards.project'),
        ),
    ]
