# Generated by Django 3.0.3 on 2020-12-27 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0002_auto_20201227_1355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('department_desc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contract.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contract.Position')),
            ],
        ),
    ]