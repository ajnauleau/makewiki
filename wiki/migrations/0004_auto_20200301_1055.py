# Generated by Django 2.2.7 on 2020-03-01 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0003_page_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.CharField(blank=True, help_text='Unique URL path to access this page. Generated by the system.', max_length=600),
        ),
    ]
