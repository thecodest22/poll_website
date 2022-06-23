from django.db import models


class Question(models.Model):
    # Тут прописываем поля класса модели, т.е. задаем ей свойства.
    # Каждый тип модели говорит Джанго, какой там тип данных.
    # Имена этих переменных будут использованы БД как имена столбцов, если не указан арг, как в "pub_date" ниже.

    question_text = models.CharField(max_length=200)  # Задаем максимальную длину цифро-буквенного поля
    pub_date = models.DateTimeField('date published')  # Поле для даты и времени, необязательный арг - имя поля


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # Это поле отношений, т.е. связи между моделями.
                                                                      # ПОКА ХЗ ЧТО ЭТО
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)  # Числовое поле с нулем по дефолту
