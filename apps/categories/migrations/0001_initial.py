# Generated by Django 3.1.8 on 2021-05-03 09:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('budgets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Nazwa kategorii')),
                ('finance_type', models.CharField(choices=[('Przychód', 'Income'), ('Wydatek', 'Outcome')], default='Przychód', max_length=20, verbose_name='Typ kategorii')),
                ('budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='budgets.budget')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
