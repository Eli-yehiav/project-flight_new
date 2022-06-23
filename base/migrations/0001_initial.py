# Generated by Django 4.0.4 on 2022-06-23 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='airline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Airline_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
                ('credit_card_number', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Flights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_time', models.DateTimeField()),
                ('landing_time', models.DateTimeField()),
                ('airline_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.airline')),
                ('country_origin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origin', to='base.countries')),
                ('destination_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.countries')),
            ],
        ),
        migrations.CreateModel(
            name='UserRoles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('Password', models.IntegerField(default=0)),
                ('email', models.CharField(max_length=50)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.userroles')),
            ],
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customers_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.customers')),
                ('Flights_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.flights')),
            ],
        ),
        migrations.AddField(
            model_name='customers',
            name='Users_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.users'),
        ),
        migrations.AddField(
            model_name='airline',
            name='User_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.users'),
        ),
        migrations.AddField(
            model_name='airline',
            name='country_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.countries'),
        ),
        migrations.CreateModel(
            name='Administor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('Users_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.users')),
            ],
        ),
    ]
