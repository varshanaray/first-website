# Generated by Django 3.1.5 on 2021-01-17 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='Enter your email', max_length=254)),
                ('password', models.CharField(help_text='Enter your password', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='NoteBk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter the title of this notebook', max_length=200)),
                ('description', models.CharField(help_text='Enter a brief description of this notebook', max_length=800)),
                ('login', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='notebooks.login')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter the title of your entry', max_length=200)),
                ('date', models.DateTimeField(auto_now=True)),
                ('entry', models.CharField(help_text='Type in your entry here', max_length=6000)),
                ('journal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='notebooks.notebk')),
            ],
        ),
    ]
