from django.db import models

class Transaction(models.Model):
    TRANSACTION_TYPE = (('income','Доход'),
                        ('outcome','Расход'))
    name = models.CharField(max_length=100, verbose_name='Название', blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма')
    transaction_type = models.CharField(choices=TRANSACTION_TYPE, verbose_name='Тип операции')
    category = models.ForeignKey('Category',max_length=50, on_delete=models.PROTECT,null=True, blank=True,
                                 verbose_name='Категория')
    date = models.DateField(verbose_name='Дата операции')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = "Транзакция"
        verbose_name_plural = "Транзакции"
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} {self.created_at} '

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    color = models.CharField(
        max_length=20, default='primary', verbose_name='Цвет(Bootstrap)',
        help_text='primary, secondary, success, danger, warning, info, light, dark'
    )
    icon = models.CharField(
        max_length=50, default='bi-tag', verbose_name='Иконка (Bootstrap Icons)',
        help_text='Название иконки из https://icons.getbootstrap.com/'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
