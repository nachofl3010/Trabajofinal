# Generated by Django 4.1.4 on 2023-01-08 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tournaments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('GS', 'GS'), ('M1000', 'M1000'), ('ATP500', 'ATP500'), ('ATP250', 'ATP250')], max_length=50)),
            ],
        ),
    ]