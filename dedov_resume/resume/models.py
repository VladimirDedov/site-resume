from django.db import models


class User(models.Model):
    '''Модель описания пользователя'''
    name = models.CharField(max_length=255, verbose_name='ФИО')
    email = models.EmailField(max_length=30, verbose_name='E-mail')
    phone = models.CharField(max_length=15, verbose_name='Телефон')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    wats_up_number = models.CharField(max_length=15, blank=True, verbose_name='Ватсап')
    telegram_number = models.CharField(max_length=15, blank=True, verbose_name='Телеграм')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d', verbose_name='Фото')
    published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Education(models.Model):
    '''Образование'''
    user = models.ForeignKey('User', related_name="education", on_delete=models.CASCADE, null=True,
                             verbose_name="Пользователь")
    school_name = models.CharField(max_length=255, verbose_name='Наименование')
    description = models.TextField(verbose_name="Описание")
    specialization = models.CharField(max_length=255, verbose_name="Специальность")
    years = models.CharField(max_length=50, verbose_name='Года учебы')
    sertifity = models.BooleanField(default=False)

    def __str__(self):
        return self.school_name

    class Meta:
        verbose_name = "Образование"
        verbose_name_plural = "Образования"

class Skills(models.Model):
    '''Умения для правой панели'''
    user = models.ForeignKey('User', related_name='skills', on_delete=models.CASCADE, null=True,
                             verbose_name="Пользователь")
    skill_name = models.CharField(max_length=255, verbose_name='Умение')
    skill_value = models.PositiveSmallIntegerField(default=0, verbose_name='Уровень скила')
    tooltip = models.TextField(default='', verbose_name='ToolTip')
    skill_level = models.CharField(max_length=100, verbose_name='Уровень владения', default='Expert')

    def __str__(self):
        return self.skill_name

    class Meta:
        verbose_name = "Умения"
        verbose_name_plural = "Умения"

class JobSkills(models.Model):
    '''Обязанности по работе'''
    description_job = models.CharField(max_length=255, verbose_name='Обязанность')

    def __str__(self):
        return self.description_job
    class Meta:
        verbose_name = "Обязанность на работе"
        verbose_name_plural = "Обязанности на работе"


class Experience(models.Model):
    '''Описание опыта работы'''
    user = models.ForeignKey('User', related_name="experience", on_delete=models.CASCADE, null=True,
                             verbose_name="Пользователь")
    name_organization = models.CharField(max_length=255, verbose_name='Организация')
    position = models.CharField(max_length=100, verbose_name='Должность')
    years = models.CharField(max_length=50, verbose_name='Года работы')
    description = models.TextField(verbose_name="Описание")
    job_skill = models.ManyToManyField(JobSkills, related_name='job_skill', verbose_name='Выполняемые работы')

    def __str__(self):
        return self.name_organization

    class Meta:
        verbose_name = "Опыт работы"
        verbose_name_plural = "Опыт работы"

class Language(models.Model):
    '''Описание владения языками'''
    name_language = models.CharField(max_length=255, verbose_name='Язык')
    level = models.CharField(max_length=255, verbose_name='Уровень владения')

    class Meta:
        verbose_name = "Языки"
        verbose_name_plural = "Языки"