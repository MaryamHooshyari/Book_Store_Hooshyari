# Generated by Django 3.2.6 on 2021-09-02 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customer_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=50)),
                ('town', models.CharField(blank=True, max_length=50, null=True)),
                ('street', models.CharField(max_length=50)),
                ('postal_code', models.IntegerField(blank=True, null=True)),
                ('details', models.CharField(max_length=200)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='accounts.customer')),
            ],
            options={
                'verbose_name': 'آدرس',
                'verbose_name_plural': 'آدرس ها',
            },
        ),
    ]
