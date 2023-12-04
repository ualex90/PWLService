# Generated by Django 4.2.7 on 2023-12-04 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Payment date')),
                ('payment_amount', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Payment amount')),
                ('payment_method', models.CharField(choices=[('transfer', 'Transfer'), ('cash', 'Cash')], default='transfer', max_length=8, verbose_name='Payment Method')),
            ],
            options={
                'verbose_name': 'Платеж',
                'verbose_name_plural': 'Платежи',
            },
        ),
        migrations.CreateModel(
            name='StripeSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Create date')),
                ('payment_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Payment amount')),
                ('session_url', models.CharField(blank=True, max_length=400, null=True, verbose_name='Session URL')),
            ],
        ),
    ]
