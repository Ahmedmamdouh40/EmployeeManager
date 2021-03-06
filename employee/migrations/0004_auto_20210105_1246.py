# Generated by Django 3.0.3 on 2021-01-05 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20210105_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AlterField(
            model_name='employee',
            name='date_of_birth',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_number',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='employee',
            name='full_name',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default=None, max_length=1),
        ),
        migrations.AlterField(
            model_name='employee',
            name='has_medical',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='employee',
            name='hire_date',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='employee',
            name='id_number',
            field=models.CharField(default=None, max_length=14),
        ),
        migrations.AlterField(
            model_name='employee',
            name='id_type',
            field=models.CharField(choices=[('NATIONAL', 'National'), ('PASSPORT', 'Passport')], default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='employee',
            name='is_insured',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='employee',
            name='leave_balance',
            field=models.IntegerField(default=21),
        ),
        migrations.AlterField(
            model_name='employee',
            name='mobile_number',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AlterField(
            model_name='employee',
            name='nationality',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='place_of_birth',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AlterField(
            model_name='employee',
            name='social_status',
            field=models.CharField(choices=[('SINGLE', 'Single'), ('MARRIED', 'Married')], default=None, max_length=10),
        ),
    ]
