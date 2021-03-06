# Generated by Django 3.1 on 2020-08-20 18:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boast', models.BooleanField(choices=[(True, 'Boast'), (False, 'Roast')], default=False)),
                ('post_content', models.CharField(max_length=140)),
                ('up_votes', models.IntegerField()),
                ('down_votes', models.IntegerField()),
                ('time_stamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
