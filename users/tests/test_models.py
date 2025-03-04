import pytest
from users.models import User
from django.utils import timezone
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError


@pytest.mark.django_db
class TestUserModule:
    def test_create_user(self):
        """
        Тест проверяет, что пользователь может быть успешно создан с правильными значениями полей.
        Проверяются username, email и правильность установки пароля.
        """
        user = User.objects.create_user(username='testuser', email='test@test.com', password='rfvtgbhn')
        assert user.username == 'testuser'
        assert user.email == 'test@test.com'
        assert user.check_password('rfvtgbhn')

    def test_create_superuser(self):
        """
        Тест проверяет, что суперпользователь может быть создан и имеет флаг is_staff.
        """
        user = User.objects.create_superuser(username='testsuperuser', email='testsuperuser@super.com', password='rfvtgbhn')
        assert user.is_staff

    def test_unique_username_and_email(self):
        """
        Тест проверяет, что нельзя создать пользователя с дублирующимся username и email.
        Ожидается исключение при попытке создать пользователя с уже существующими данными.
        """
        User.objects.create_user(username='uniqueuser', email='unique@test.com', password='rfvtgbyhn')
        with pytest.raises(ValidationError) as err:
            User.objects.create_user(username='uniqueuser', email='unique@test.com', password='rfvtgbyhn')

    def test_user_role(self):
        """
        Тест проверяет, что пользователь может быть создан с определенной ролью (например, CONTENT_MAKER).
        """
        user = User.objects.create_user(username='uniqueuser', email='unique@test.com', password='rfvtgbyhn', user_role=User.Role.CONTENT_MAKER)
        assert user.user_role == User.Role.CONTENT_MAKER

    def test_last_login(self):
        """
        Тест проверяет, что поле last_login обновляется после успешной аутентификации пользователя.
        Первоначальная проверка поля не требуется, так как last_login автоматически обновляется при аутентификации.
        """
        user = User.objects.create_user(username='uniqueuser', email='unique@test.com', password='rfvtgbyhn')
        user = authenticate(username='uniqueuser', password='rfvtgbyhn')
        assert user.last_login is not None
        assert user.last_login <= timezone.now()

    def test_created_at(self):
        """
        Тест проверяет, что поле created_at устанавливается автоматически при создании пользователя
        и соответствует текущему времени с погрешностью в несколько секунд.
        """
        user = User.objects.create_user(username='uniqueuser', email='unique@test.com', password='rfvtgbyhn')
        assert abs(timezone.now() - user.created_at).seconds < 5
