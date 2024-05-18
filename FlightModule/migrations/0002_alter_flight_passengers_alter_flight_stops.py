from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CitiesModule', '0001_initial'),
        ('FlightModule', '0001_initial'),
        ('PassengersModule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='passengers',
            field=models.ManyToManyField(blank=True, to='PassengersModule.passenger'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='stops',
            field=models.ManyToManyField(blank=True, to='CitiesModule.city'),
        ),
    ]
