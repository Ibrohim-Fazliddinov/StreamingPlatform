# from django.contrib import admin
#
# from .models.model_content import Content, Category
#
#
# @admin.register(Content)
# class ContentAdmin(admin.ModelAdmin):
#     # Используется для определения столбцов, которые будут отображаться в списке объектов модели.
#     list_display = ('title', 'description', 'author_content')
#     # Удаляем определенное поле при создании записи
#     exclude = ('slug', 'pub_date_time')
#     # Добавляем фильтрацию
#     list_filter = ('pub_date_time',)
#     # Количество записей еа одной странице
#     list_per_page = 100
#     # Добовляем понель поиска для указанных полей
#     search_fields = ('title', 'description')
#     # Добовляем текст помощи для поисковой строки
#     search_help_text = '''Введите ключевые слова для поиска по названию и описанию.
#                           Используйте точные совпадения для лучших результатов.'''
#     filter_horizontal = ['categories_content']
#
#
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     search_fields = ('name',)
#     search_help_text = '''Введите ключевые слова для поиска по названию'''
