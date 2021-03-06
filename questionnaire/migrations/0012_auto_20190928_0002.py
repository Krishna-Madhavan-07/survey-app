# Generated by Django 2.2.5 on 2019-09-28 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0011_survey_d3'),
    ]

    operations = [
        migrations.AddField(
            model_name='familydetails',
            name='age',
            field=models.IntegerField(default=0, verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='e2',
            field=models.CharField(blank=True, choices=[('0-18th Birthday', '0-18th Birthday'), ('1-1st January', '1-1st January'), ("99-Don't Know", "99-Don't Know")], max_length=128, null=True, verbose_name='e2'),
        ),
    ]
