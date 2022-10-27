# Generated by Django 3.2.5 on 2022-10-27 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0003_pessoa_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contatos', to='pessoa.pessoa'),
        ),
    ]
