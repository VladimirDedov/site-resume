# Generated by Django 4.1.6 on 2023-02-15 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0007_education_sertifity_alter_experience_job_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='years',
            field=models.CharField(max_length=50, verbose_name='Года учебы'),
        ),
    ]
