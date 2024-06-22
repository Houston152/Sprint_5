from selenium.webdriver.common.by import By


class Locators:
    # Главная страница
    ACCAUNT_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")  # Кнопка "Личный кабинет"
    ENTER_ACCAUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")  # Кнопка "Войти в аккаунт"
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[contains(text(),'Конструктор')]")  # Кнопка "Конструктор"
    ORDERS_BUTTON = (By.XPATH, ".//p[contains(text(),'Лента Заказов')]")  # Кнопка "Лента заказов"
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")  # Логотип
    MENU_INGRIDIENTS = (By.XPATH, "//div[contains(@class, 'BurgerIngredients_ingredients__menuContainer')]")  # Меню ингредиентов
    FILLING = (By.XPATH, "//img[contains(@alt, 'Биокотлета из марсианской Магнолии')]")  # Элемент начинки
    SAUCE = (By.XPATH, "//img[contains(@alt, 'Соус традиционный галактический')]")  # Элемент соуса
    BUN = (By.XPATH, "//img[contains(@alt, 'Флюоресцентная булка R2-D3')]")  # Элемент булки
    FILLING_SECTION = (By.XPATH, "//span[contains(text(),'Начинки')]/parent::div")  # Раздел с начинками
    SAUCE_SECTION = (By.XPATH, "//span[contains(text(),'Соусы')]/parent::div")  # Раздел с соусами
    BUN_SECTION = (By.XPATH, "//span[contains(text(),'Булки')]/parent::div")  # Раздел с булками

    # Страница авторизации
    AUTHORIZATION_PANEL = (By.XPATH, "//form[contains(@class, 'Auth_form')]")  # Панель авторизации
    EMAIL_FIELD = (By.XPATH, "//input[@name='name']")  # Поле ввода "Email"
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']")  # Поле ввода "Пароль"
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")  # Кнопка "Войти"
    REGISTRATION_PAGE_BUTTON = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")  # Кнопка перехода на страницу регистрации
    RECOVERY_BUTTON = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")  # Кнопка "Восстановить пароль"

    # Страница регистрации
    REGISTRATION_HEADER = (By.XPATH, "//h2[contains(text(),'Регистрация')]")  # Заголовок 'Регистрация'
    REGISTRATION_NAME_FIELD = (By.XPATH, "//fieldset[1]//input")  # Поле "Имя"
    REGISTRATION_EMAIL_FIELD = (By.XPATH, "//fieldset[2]//input")  # Поле "Email"
    REGISTRATION_PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")  # Поле "Пароль"
    REGISTRATION_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")  # Кнопка "Зарегистрироваться"
    REGISTRATION_LOGIN_BUTTON = (By.XPATH, "//a[contains(text(),'Войти')]")  # Кнопка "Войти"
    INVALID_PASSWORD = (By.XPATH, "//p[@class='input__error text_type_main-default']")  # Текст "Некорректный пароль"

    # Страница профиля
    PROFILE_NAME_FIELD = (By.XPATH, "//input[@name='Name']")  # Поле "Имя"
    PROFILE_EMAIL_FIELD = (By.XPATH, "//input[@type='text' and @name='name']")  # Поле "Email"
    PROFILE_EXIT_BUTTON = (By.XPATH, "//button[contains(@class, 'Account_button')]")  # Кнопка "Выход"
