# Generated by Django 3.2.3 on 2021-05-29 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kiosk', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_mode',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Card', 'Card')], default='green', max_length=50),
        ),
    ]
