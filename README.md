Автотесты для приложения Stellar Burgers

1. В файле conftest.py описано:
* фикстура для открытия браузера и перехода на сайт приложения Stellar Burgers
* фикстура авторизации под пользователем

2. В файле test_registration.py проверяю:
* Успешная регистрация нового пользователя
* Ошибку для неправильного пароля

3. В файле test_authorization.py проверяю:
* Авторизацию по кнопке "Войти в аккаунт" на главной странице
* Авторизацию по кнопке "Личный кабинет" на главной странице
* Переход в личный кабинет
* Авторизацию по кнопке в форме регистрации
* Авторизацию по кнопке в форме восстановления пароля

4. В файле test_account_page.py проверяю:
* Переход на главную страницу через кнопку "Конструктор"
* Переход на главную страницу через логотип "Stellar Burgers"

5. В файле test_logout.py проверяю:
* Выход из аккаунта

6. В файле test_section_construction.py проверяю:
* Переход в раздел "Начинки"
* Переход в раздел "Соусы"
* Переход в раздел "Булки"