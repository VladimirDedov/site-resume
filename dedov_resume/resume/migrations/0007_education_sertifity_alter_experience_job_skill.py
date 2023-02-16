# Generated by Django 4.1.6 on 2023-02-15 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_experience_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='sertifity',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='experience',
            name='job_skill',
            field=models.ManyToManyField(related_name='job_skill', to='resume.jobskills', verbose_name='Выполняемые работы'),
        ),
    ]