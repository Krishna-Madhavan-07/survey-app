# Generated by Django 2.2.5 on 2019-09-08 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='d3',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='d4a',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='d4b',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='d4c',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='d4d',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='d4e',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='d4f',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='d4g',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='d4h',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='d4i',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='d4j',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='d4k',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='d6',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='f4',
        ),
        migrations.AddField(
            model_name='survey',
            name='d3a',
            field=models.CharField(choices=[('0-No', '0-No'), ('1-Yes', '1-Yes'), ("9-Don't know", "9-Don't know")], default='1-Yes', max_length=128, verbose_name='d3a'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='survey',
            name='d3b',
            field=models.CharField(choices=[('0-No', '0-No'), ('1-Yes', '1-Yes'), ("9-Don't know", "9-Don't know")], default='1-Yes', max_length=128, verbose_name='d3b'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='survey',
            name='d3c',
            field=models.CharField(choices=[('0-No', '0-No'), ('1-Yes', '1-Yes'), ("9-Don't know", "9-Don't know")], default='1-Yes', max_length=128, verbose_name='d3c'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='survey',
            name='d3d',
            field=models.CharField(choices=[('0-No', '0-No'), ('1-Yes', '1-Yes'), ("9-Don't know", "9-Don't know")], default='1-Yes', max_length=128, verbose_name='d3d'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='survey',
            name='d3e',
            field=models.CharField(choices=[('0-No', '0-No'), ('1-Yes', '1-Yes'), ("9-Don't know", "9-Don't know")], default='1-Yes', max_length=128, verbose_name='d3e'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='survey',
            name='d3f',
            field=models.CharField(choices=[('0-No', '0-No'), ('1-Yes', '1-Yes'), ("9-Don't know", "9-Don't know")], default='1-Yes', max_length=128, verbose_name='d3f'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='survey',
            name='d3g',
            field=models.CharField(choices=[('0-No', '0-No'), ('1-Yes', '1-Yes'), ("9-Don't know", "9-Don't know")], default='1-Yes', max_length=128, verbose_name='d3g'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='survey',
            name='d3h',
            field=models.CharField(choices=[('0-No', '0-No'), ('1-Yes', '1-Yes'), ("9-Don't know", "9-Don't know")], default='1-Yes', max_length=128, verbose_name='d3h'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='survey',
            name='d3i',
            field=models.CharField(choices=[('0-No', '0-No'), ('1-Yes', '1-Yes'), ("9-Don't know", "9-Don't know")], default='1-Yes', max_length=128, verbose_name='d3i'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='survey',
            name='d3j',
            field=models.CharField(choices=[('0-No', '0-No'), ('1-Yes', '1-Yes'), ("9-Don't know", "9-Don't know")], default='1-Yes', max_length=128, verbose_name='d3j'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='survey',
            name='d3k',
            field=models.CharField(choices=[('0-No', '0-No'), ('1-Yes', '1-Yes'), ("9-Don't know", "9-Don't know")], default='1-Yes', max_length=128, verbose_name='d3k'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='survey',
            name='d4',
            field=models.CharField(choices=[('0-No', '0-No'), ('1-Yes', '1-Yes')], default='1-Yes', max_length=8, verbose_name='d4'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='survey',
            name='f4a',
            field=models.CharField(blank=True, choices=[('0-No', '0-No'), ('1-Yes', '1-Yes')], max_length=128, null=True, verbose_name='f4a'),
        ),
        migrations.AddField(
            model_name='survey',
            name='f4b',
            field=models.CharField(blank=True, choices=[('0-No', '0-No'), ('1-Yes', '1-Yes')], max_length=128, null=True, verbose_name='f4b'),
        ),
        migrations.AddField(
            model_name='survey',
            name='f4c',
            field=models.CharField(blank=True, choices=[('0-No', '0-No'), ('1-Yes', '1-Yes')], max_length=128, null=True, verbose_name='f4c'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='d2',
            field=models.CharField(choices=[('01-My vote matters', '01-My vote matters'), ('02-Voting is my right', '02-Voting is my right'), ('03-Voting is my duty', '03-Voting is my duty'), ('04-Because of enabling environment (free and fair) created by Election Commission', '04-Because of enabling environment (free and fair) created by Election Commission'), ('05-Because of accessible polling station', '05-Because of accessible polling station'), ('06-I got registered in electoral roll', '06-I got registered in electoral roll'), ('07-I got voter slip', '07-I got voter slip'), ('08-Candidate was good', '08-Candidate was good'), ('09-I voted for a political party', '09-I voted for a political party'), ('10-Cast vote due to threat or coercion', '10-Cast vote due to threat or coercion'), ('12-My family asked me to', '12-My family asked me to'), ('13-My friends asked me to', '13-My friends asked me to'), ('14-I had the option of NOTA', '14-I had the option of NOTA')], max_length=128, verbose_name='d2'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='d5',
            field=models.CharField(blank=True, choices=[('01-Long queue', '01-Long queue'), ('02-No separate queue for senior citizen', '02-No separate queue for senior citizen'), ('03-Lack of facilities including drinking water toilet and ramp', '03-Lack of facilities including drinking water toilet and ramp'), ('04-Coercion/ threat by political party', '04-Coercion/ threat by political party'), ('05-Difficulties in locating my polling station', '05-Difficulties in locating my polling station'), ('06-Difficulties in voting in absence of voter slip', '06-Difficulties in voting in absence of voter slip'), ('07-No guidance from polling personnel', '07-No guidance from polling personnel'), ('99-Others(please specify)', '99-Others(please specify)')], max_length=128, null=True, verbose_name='d5'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='d7',
            field=models.CharField(blank=True, choices=[('01-My name was not on the electoral roll', '01-My name was not on the electoral roll'), ('02-I was not in my consituency', '02-I was not in my consituency'), ('03-I did not have my electoral photo ID card(EPIC)', '03-I did not have my electoral photo ID card(EPIC)'), ('04-I did not know my polling station', '04-I did not know my polling station'), ('05-Polling station was at a distance (logistic problem)', '05-Polling station was at a distance (logistic problem)'), ('06-Long queue and I did not have time', '06-Long queue and I did not have time'), ('07-I felt insecure to go to the polling station', '07-I felt insecure to go to the polling station'), ('08-There was no candidate of my choice/liking', '08-There was no candidate of my choice/liking'), ('09-I just did not want to vote as nothing will change/ No faith in political system', '09-I just did not want to vote as nothing will change/ No faith in political system'), ("10-Voting in national or Assembly elections doesn't make a difference, I vote only in                   local election", "10-Voting in national or Assembly elections doesn't make a difference, I vote                   only in local election"), ('11-Polling station was not accessible', '11-Polling station was not accessible'), ('99-Others(please specify)', '99-Others(please specify)')], max_length=128, null=True, verbose_name='d7'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='f2',
            field=models.CharField(choices=[('1-Newspapers/magazines', '1-Newspapers/magazines'), ('2-TV advertisements and programmes', '2-TV advertisements and programmes'), ('3-Radio and FM channels', '3-Radio and FM channels'), ('4-Advertisements in cinemas', '4-Advertisements in cinemas'), ('5-Activity like Rallies, Prabhat Pheris, loudspeaker announcement', '5-Activity like Rallies, Prabhat Pheris, loudspeaker announcement'), ('6-Cultural/entertainments programmes', '6-Cultural/entertainments programmes'), ('7-Government offices circular', '7-Government offices circular'), ('8-Posters, hoardings and publicity materials', '8-Posters, hoardings and publicity materials'), ('9-NGO and Civil society Group', '9-NGO and Civil society Group'), ('10-Internet/ Social Media/Whatsapp', '10-Internet/ Social Media/Whatsapp'), ('11-SMS', '11-SMS'), ('12-Pledge letters/Sankalp patras through school students in the family', '12-Pledge letters/Sankalp patras through school students in the family'), ('13-At Polling Station', '13-At Polling Station'), ('99-Others (please specify)', '99-Others (please specify)')], max_length=128, verbose_name='f2'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='f3',
            field=models.CharField(choices=[('01-Date of voting and schedules', '01-Date of voting and schedules'), ('02-Voting is my right and duty', '02-Voting is my right and duty'), ('03-Cast vote as per choice and without taking any inducement', '03-Cast vote as per choice and without taking any inducement'), ('04-#GoRegister or Register', '04-#GoRegister or Register'), ('05-#GoVerify or Verify name in voter list', '05-#GoVerify or Verify name in voter list'), ('06-12 Identity documents allowed for Voting', '06-12 Identity documents allowed for Voting'), ('07-Facilities provided at polling station', '07-Facilities provided at polling station'), ('08-Priority voting for old and PwDs', '08-Priority voting for old and PwDs'), ('09-Voter helpline 1950 or Voter helpline app', '09-Voter helpline 1950 or Voter helpline app'), ('10-cVIGIL app related', '10-cVIGIL app related'), ('11-NVSP portal', '11-NVSP portal'), ('99-Others (please specify)', '99-Others (please specify)')], max_length=128, verbose_name='f3'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='f9',
            field=models.CharField(choices=[('0-None of the two', '0-None of the two'), ('1-Voter Helpline no 1950', '1-Voter Helpline no 1950'), ('2-Voter Helpline app only', '2-Voter Helpline app only'), ('3-Both of them', '3-Both of them')], max_length=128, verbose_name='f9'),
        ),
    ]
