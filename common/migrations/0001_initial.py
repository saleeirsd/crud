# Generated by Django 4.1.6 on 2023-02-13 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.BigIntegerField()),
                ('gender', models.CharField(max_length=15)),
                ('password', models.CharField(default='', max_length=20)),
                ('status', models.CharField(default='active', max_length=20)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.BigIntegerField()),
                ('gender', models.CharField(max_length=15)),
                ('user_name', models.IntegerField(default=0)),
                ('password', models.CharField(default='', max_length=40)),
                ('company_name', models.CharField(max_length=30)),
                ('holder_name', models.CharField(max_length=30)),
                ('ifsc', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('account_number', models.BigIntegerField()),
                ('pic', models.ImageField(upload_to='seller/')),
                ('status', models.CharField(default='pending', max_length=20)),
            ],
            options={
                'db_table': 'seller',
            },
        ),
    ]
