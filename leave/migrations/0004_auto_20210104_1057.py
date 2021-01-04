# Generated by Django 3.0.3 on 2021-01-04 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0003_auto_20201230_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeleave',
            name='leave_status',
            field=models.CharField(choices=[('WAITING', 'Waiting'), ('APPROAVED', 'Approaved'), ('REJECTED', 'Rejected')], default='WAITING', max_length=25),
        ),
    ]
