# Generated by Django 2.1.3 on 2019-09-28 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_book_current_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(default='', max_length=50)),
            ],
        ),
    ]