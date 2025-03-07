# Generated by Django 5.1.2 on 2025-02-21 02:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Салбарын нэр')),
                ('location', models.CharField(max_length=255, verbose_name='Салбарын байршил')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Хэрэглэгчийн нэр')),
                ('phone', models.CharField(max_length=20, verbose_name='Утасны дугаар')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Цахим шуудан')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Албан тушаалын нэр')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Үйлчилгээний төрөл')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Үйлчилгээний нэр')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Үнэ')),
                ('duration', models.IntegerField(verbose_name='Үргэлжлэх хугацаа (минут)')),
                ('service_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.servicetype', verbose_name='Үйлчилгээний төрөл')),
            ],
        ),
        migrations.CreateModel(
            name='TimeOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Огноо')),
                ('time', models.TimeField(verbose_name='Цаг')),
                ('status', models.CharField(choices=[('pending', 'Хүлээгдэж буй'), ('confirmed', 'Баталгаажсан'), ('cancelled', 'Цуцлагдсан')], default='pending', max_length=20, verbose_name='Төлөв')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.branch', verbose_name='Салбар')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customer', verbose_name='Хэрэглэгч')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.service', verbose_name='Үйлчилгээ')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type', models.CharField(choices=[('cash', 'Бэлэн'), ('card', 'Карт'), ('online', 'Онлайн')], max_length=50, verbose_name='Төлбөрийн төрөл')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Төлбөрийн дүн')),
                ('payment_date', models.DateTimeField(auto_now_add=True, verbose_name='Төлбөрийн огноо')),
                ('time_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.timeorder', verbose_name='Цаг захиалга')),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Овог')),
                ('last_name', models.CharField(max_length=255, verbose_name='Нэр')),
                ('phone', models.CharField(max_length=20, verbose_name='Утасны дугаар')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.branch', verbose_name='Салбар')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.role', verbose_name='Албан тушаал')),
            ],
        ),
        migrations.AddField(
            model_name='timeorder',
            name='worker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.worker', verbose_name='Ажилтан'),
        ),
    ]
