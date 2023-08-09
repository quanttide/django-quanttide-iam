from django.db import models


class Education(models.Model):
    school = models.CharField(max_length=255, verbose_name='学校')
    college = models.CharField(max_length=255, verbose_name='学院')
    department = models.CharField(max_length=255, verbose_name='系')
    major = models.CharField(max_length=255, verbose_name='专业')
    degree = models.CharField(max_length=16, verbose_name='学历')
    start_year = models.IntegerField(verbose_name='入学年份')
    end_year = models.IntegerField(verbose_name='毕业年份')

    class Meta:
        verbose_name = '教育经历'
        verbose_name_plural = '教育经历'
