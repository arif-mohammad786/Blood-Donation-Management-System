# Generated by Django 2.2.14 on 2020-09-10 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='donarmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=70)),
                ('bgroup', models.CharField(choices=[('A+', 'A-'), ('B+', 'B-'), ('AB+', 'AB-'), ('o+', 'o-')], default='A+', max_length=70)),
                ('address', models.TextField()),
            ],
        ),
    ]
