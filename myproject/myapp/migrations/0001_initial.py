# Generated by Django 2.2.5 on 2022-04-18 15:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('unit', models.CharField(choices=[('ลูก', 'ลูก'), ('กก.', 'กิโลกรัม'), ('ชิ้น', 'ชิ้น')], default='ชิ้น', max_length=5)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('image', models.ImageField(upload_to='myimages')),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('postcode', models.CharField(max_length=5)),
                ('email', models.EmailField(max_length=254)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Item')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Profile')),
            ],
        ),
    ]