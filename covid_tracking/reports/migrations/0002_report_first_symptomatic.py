import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='Report',
            name='first_symptomatic',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]