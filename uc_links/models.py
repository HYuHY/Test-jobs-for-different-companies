from django.db import models
from django.core.validators import RegexValidator

class Person(models.Model):
    """Имя и фамилия пользователя"""
    first_name = models.CharField(
        validators=[RegexValidator(regex='^[^\W\d_]+(-[^\W\d_]+)?$', message='Text symbols and -, without digits')], 
        max_length=50
        )
    last_name = models.CharField(
        validators=[RegexValidator(regex='^[^\W\d_]+(-[^\W\d_]+)?$', message='Text symbols and -, without digits')],
        max_length=150, 
        unique=True
        )
    date_added = models.DateTimeField(
        "upload date",
        auto_now_add=True
        )
    
    def __str__(self):
        """Простое текстовое представление модели"""
        return "%s %s" % (self.last_name, self.first_name)



class Cards(models.Model):
    """Номера карт пользователей"""
    person = models.ForeignKey(
        Person, 
        on_delete=models.CASCADE,
        null=True
        )
    card_number = models.CharField(
        validators=[RegexValidator(regex='\d{4}', message='Length has to be 4 numeric symbols')],
        max_length = 4,
        unique=True
        )
    
    def __str__(self):
        """Простое текстовое представление модели"""
        return self.card_number



