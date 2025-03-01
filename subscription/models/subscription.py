# from django.db import models
# from django.utils.translation import gettext_lazy as _
# from django.contrib.auth import get_user_model
# from datetime import timedelta
# from django.utils import timezone
#
# User = get_user_model()
#
#
# class Subscription(models.Model):
#     """
#     Модель подписки пользователя на тарифные планы.
#     """
#
#     class Plan(models.TextChoices):
#         """
#         Доступные тарифные планы.
#         """
#         BASIC = 'BASE', _('Базовая')
#         PREMIUM = 'PREM', _('Премиум')
#
#     user = models.ForeignKey(
#         to=User,
#         verbose_name=_("Пользователь"),
#         on_delete=models.CASCADE
#     )
#     plan = models.CharField(
#         _("Тарифный план"),
#         max_length=5,
#         choices=Plan.choices,
#         default=Plan.BASIC
#     )
#     start_date = models.DateTimeField(
#         _("Дата начала"),
#         auto_now_add=True
#     )
#     end_date = models.DateTimeField(
#         _("Дата окончания"),
#         null=True,
#         blank=True
#     )
#
#     class Meta:
#         verbose_name = _("Подписка")
#         verbose_name_plural = _("Подписки")
#
#     def save(self, *args, **kwargs):
#         """
#         Сохраняет объект подписки, устанавливая дату окончания для премиум-плана.
#         Если план премиум и дата окончания не установлена, то она устанавливается на 45 дней
#         позже даты начала подписки.
#         """
#         if self.plan == self.Plan.PREMIUM and not self.end_date:
#             self.end_date = self.start_date + timedelta(days=45)
#         if self.plan == self.Plan.BASIC:
#             self.end_date = None
#         super().save(*args, **kwargs)
#
#     def is_active(self):
#         """
#         Проверяет, активна ли подписка. Если истекла, переводит на базовый план.
#         """
#         # после будем делать через celery
#         if self.end_date and self.end_date <= timezone.now():
#             self.plan = self.Plan.BASIC
#             self.end_date = None
#             self.save()
#             return False
#         return True
#
#     def __str__(self):
#         """
#         Возвращает строковое представление подписки.
#         """
#         return f"{self.user} - {self.get_plan_display()}"
