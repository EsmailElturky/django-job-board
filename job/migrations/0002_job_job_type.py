# Generated by Django 4.0.6 on 2022-07-16 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Full Time', 'Part Time'), ('Part Time', 'Full Time')], default=1, max_length=15),
            preserve_default=False,
        ),
    ]
