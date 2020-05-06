# Generated by Django 3.0.5 on 2020-04-29 19:43

from django.db import migrations, models
import profiles.validators


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_add_contact_person_hospital_profile"),
    ]

    operations = [
        migrations.RemoveField(model_name="donorprofile", name="report",),
        migrations.AddField(
            model_name="donorprofile",
            name="date_last_tested_negative",
            field=models.DateField(
                blank=True,
                null=True,
                verbose_name="Date Last COVID19 Negative Test Report",
            ),
        ),
        migrations.AddField(
            model_name="donorprofile",
            name="igg_report",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="igg_donor_reports",
                validators=[profiles.validators.validate_file_extension],
                verbose_name="Immunoglobulin G (IgG) Test Report",
            ),
        ),
        migrations.AddField(
            model_name="donorprofile",
            name="last_covid_report",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="last_donor_reports",
                validators=[profiles.validators.validate_file_extension],
                verbose_name="Last COVID19 Negative Test Report",
            ),
        ),
    ]
