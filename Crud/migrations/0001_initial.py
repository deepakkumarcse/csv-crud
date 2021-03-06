# Generated by Django 3.2.2 on 2021-05-12 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name field you need to fill.', max_length=100, verbose_name='Name')),
                ('email', models.EmailField(help_text='Email field you need to fill.', max_length=100, verbose_name='Email')),
                ('phone', models.CharField(help_text='Phone Number field you need to fill.', max_length=100, verbose_name='Phone Number')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
