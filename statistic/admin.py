# from django.contrib import admin
#
# from statistic.models import Statistic
#
#
# @admin.register(Statistic)
# class StatisticAdmin(admin.ModelAdmin):
#     list_display = ('content', 'author', 'number_of_likes',
#                     'number_of_dislikes', 'number_of_comments', 'number_of_views')
#     list_filter = ('number_of_likes', 'number_of_dislikes', 'number_of_comments', 'number_of_views')
#     list_per_page = 100
#     search_fields = ('content', 'author')
#     search_help_text = '''Введите ключевые слова для поиска по названию и автору.
#                             Используйте точные совпадения для лучших результатов.'''
#
