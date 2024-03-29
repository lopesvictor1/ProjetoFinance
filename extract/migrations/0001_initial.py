# Generated by Django 4.2.3 on 2023-07-07 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userProfile', '0004_rename_bill_account_rename_icone_account_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inputs_outputs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('type', models.CharField(choices=[('E', 'Entrada'), ('S', 'Saída')], max_length=1)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='userProfile.account')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='userProfile.category')),
            ],
        ),
    ]
