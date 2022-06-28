import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    # Тут прописываем поля класса модели, т.е. задаем ей свойства.
    # Каждый тип модели говорит Джанго, какой там тип данных.
    # Имена этих переменных будут использованы БД как имена столбцов, если не указан арг, как в "pub_date" ниже.

    question_text = models.CharField(max_length=200)  # Задаем максимальную длину цифро-буквенного поля
    pub_date = models.DateTimeField('date published')  # Поле для даты и времени, необязательный арг - имя поля
    # objects = models.Manager()
    def __str__(self):
        return self.question_text

    def was_published_recently(self) -> bool:
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # Это поле отношений, т.е. связи между моделями.
                                                                      # ПОКА ХЗ ЧТО ЭТО
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)  # Числовое поле с нулем по дефолту

    def __str__(self):
        return self.choice_text
