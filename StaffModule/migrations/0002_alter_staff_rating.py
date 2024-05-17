from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StaffModule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='rating',
            field=models.CharField(blank=True, choices=[('a', 'A'), ('b', 'B'), ('c', 'C')], max_length=10),
        ),
    ]
