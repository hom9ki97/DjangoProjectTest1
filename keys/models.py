from django.db import models
from django.core.validators import RegexValidator


class UserData(models.Model):
    first_name = models.CharField(max_length=25, verbose_name='Имя')
    last_name = models.CharField(max_length=25, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Почта', unique=True)
    card_number = models.CharField(max_length=19,
                                   validators=[RegexValidator(regex=r'^(\d{4}\s?){4}$',
                                                              message="Номер карты должен быть в формате 'XXXX XXXX XXXX XXXX'")],
                                   verbose_name='Номер карты')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-created_at']


    def mask_card_number(self):
        if self.card_number:
            return f'**** **** **** {self.card_number[-4:]}'
        return ''

class UserKeys(models.Model):
    user = models.OneToOneField(UserData, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='keys')
    public_key = models.TextField(verbose_name='Публичный ключ')
    private_key = models.TextField(verbose_name='Приватный ключ', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Ключи'
        verbose_name_plural = 'Ключи'
