from django.db import models
from django.utils.translation import gettext_lazy as _


class Payment(models.Model):
    """
    Модель для управления платежами в системе подписок.

    Атрибуты:
        amount (DecimalField): Сумма платежа.
        payment_options (CharField): Способ оплаты, выбранный пользователем.
        subscription (OneToOneField): Связь с моделью подписки, указывающая, за какую подписку был произведён платёж.
        status (CharField): Статус платежа, который может быть в ожидании, завершён или не выполнен.
        transaction_id (CharField): Уникальный идентификатор транзакции, используемый для отслеживания платежей.
        created_at (DateTimeField): Время создания записи о платеже.
        updated_at (DateTimeField): Время последнего обновления записи о платеже.
    """

    class PaymentMethod(models.TextChoices):
        """
        Класс для описания возможных методов оплаты.

        Значения:
            PAYPAL (str): Оплата через PayPal.
            STRIPE (str): Оплата через Stripe.
            PAYME (str): Оплата через PayMe.
        """
        PAYPAL = 'PP', _('paypal')
        STRIPE = 'ST', _('stripe')
        PAYME = 'PM', _('payme')

    class Status(models.TextChoices):
        """
        Класс для описания статусов платежа.

        Значения:
            PENDING (str): Платёж в ожидании.
            COMPLETED (str): Платёж завершён.
            FAILED (str): Платёж не выполнен.
        """
        PENDING = 'P', _('Ожидание')
        COMPLETED = 'C', _('Завершено')
        FAILED = 'F', _('Не выполнено')

    amount = models.DecimalField(
        _("Сумма"),
        max_digits=10,
        decimal_places=2
    )
    payment_options = models.CharField(
        _("Способ оплаты"),
        max_length=50,
        choices=PaymentMethod.choices
    )
    # subscription = models.OneToOneField(
    #     "app.Subscription",
    #     verbose_name=_("Подписка"),
    #     on_delete=models.CASCADE
    # )
    status = models.CharField(
        _("Статус"),
        max_length=2,
        choices=Status.choices,
        default=Status.PENDING
    )
    transaction_id = models.CharField(
        _("ID Транзакции"),
        max_length=50,
        unique=True,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        _("Дата создания"),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        _("Дата обновления"),
        auto_now=True
    )

    class Meta:
        """
        Класс для мета-информации о модели Payment.

        Атрибуты:
            ordering (tuple): Определяет порядок сортировки записей — по убыванию времени создания.
            verbose_name (str): Название модели в единственном числе на русском.
            verbose_name_plural (str): Название модели во множественном числе на русском.
        """
        ordering = ("-created_at",)
        verbose_name = _("Платёж")
        verbose_name_plural = _("Платежи")

    def __str__(self):
        """
        Возвращает строковое представление объекта платежа.

        Возвращает:
            str: Транзакционный ID и сумму платежа.
        """
        return f"{self.transaction_id} - {self.amount}"
