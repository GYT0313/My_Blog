# Generated by Django 2.0.5 on 2018-05-18 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PictureOfArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='article/')),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(blank=True, max_length=50, verbose_name='类别'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='article',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='发表时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100, verbose_name='文章名称'),
        ),
    ]