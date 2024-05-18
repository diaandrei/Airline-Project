import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AirplaneModule', '0001_initial'),
        ('CitiesModule', '0001_initial'),
        ('PassengersModule', '0001_initial'),
        ('StaffModule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_number', models.IntegerField()),
                ('date', models.DateField()),
                ('arrival_time', models.TimeField()),
                ('departure_time', models.TimeField()),
                ('airplane', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='AirplaneModule.airplane')),
                ('crew', models.ManyToManyField(to='StaffModule.staff')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='destination', to='CitiesModule.city')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='origin', to='CitiesModule.city')),
                ('passengers', models.ManyToManyField(to='PassengersModule.passenger')),
                ('stops', models.ManyToManyField(to='CitiesModule.city')),
            ],
        ),
    ]
