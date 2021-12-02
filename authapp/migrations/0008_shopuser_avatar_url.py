from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('authapp', '0007_shopuserprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuser',
            name='avatar_url',
            field=models.CharField(blank=True, max_length=128, null=True)
        ),
    ]