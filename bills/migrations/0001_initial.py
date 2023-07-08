# Generated by Django 4.2.3 on 2023-07-08 03:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userProfile', '0005_rename_intended_value_category_planning_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('value', models.FloatField(default=0)),
                ('payment_day', models.DateField(default=django.utils.timezone.now)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='userProfile.category')),
            ],
        ),
        migrations.CreateModel(
            name='Payed_Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payed', models.DateField()),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bills.bill')),
            ],
        ),
    ]