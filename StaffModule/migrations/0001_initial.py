from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_number', models.IntegerField()),
                ('surname', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
                ('rating', models.CharField(choices=[('a', 'A'), ('b', 'B'), ('c', 'C')], max_length=10)),
                ('is_pilot', models.BooleanField(default=False)),
            ],
        ),
    ]
