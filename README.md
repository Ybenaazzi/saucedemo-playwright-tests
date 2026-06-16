# Фреймворк автоматизации тестирования SauceDemo

Это комплексный фреймворк автоматизации тестирования для приложения SauceDemo, созданный с использованием Python, Playwright и Pytest.

## Структура проекта

```
saucedemo_tests/
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── locators/
│   ├── __init__.py
│   └── saucedemo_locators.py
├── utils/
│   ├── __init__.py
│   ├── test_data.py
│   ├── driver_factory.py
│   └── logger.py
├── data/
│   └── __init__.py
├── reports/
│   └── __init__.py
├── tests/
│   └── test_saucedemo.py
├── config.py
├── conftest.py
├── run_tests.py
├── requirements.txt
└── README.md
```

## Инструкции по установке

1. Клонируйте репозиторий
2. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```
3. Установите браузеры Playwright:
   ```
   playwright install
   ```
   Или используйте наш скрипт запуска с флагом `--install-browsers`

## Запуск тестов

Для запуска всех тестов со стандартными настройками (Chromium, без графического интерфейса):
```
pytest --browser=chromium
```

Для запуска тестов с HTML отчетом:
```
pytest --browser=chromium --html=reports/test_report.html
```

Для запуска тестов в режиме с графическим интерфейсом:
```
pytest --browser=chromium --headed
```

Для запуска тестов параллельно:
```
pytest --browser=chromium -n auto
```

Для запуска с помощью скрипта тестирования:
```
python run_tests.py --install-browsers
```

## Конфигурация

Фреймворк использует файл конфигурации (`config.py`) и переменные окружения для управления настройками:

### Параметры конфигурации

- `BASE_URL`: Базовый URL тестируемого приложения (по умолчанию: https://www.saucedemo.com/)
- `REPORTS_DIR`: Директория для отчетов о тестах (по умолчанию: reports)
- `LOGS_DIR`: Директория для файлов журналов (по умолчанию: logs)

### Использование переменных окружения

Вы можете переопределить настройки конфигурации с помощью переменных окружения:

```bash
export BASE_URL="https://your-test-site.com"
pytest --browser=chromium
```

## Основные особенности

- Шаблон проектирования Page Object Model (POM)
- Поддержка кросс-браузерного тестирования (Chromium, Firefox, WebKit)
- Комплексное ведение журналов
- Управление тестовыми данными
- Возможность выполнения в headless/headed режимах
- Поддержка параллельного выполнения тестов
- Подробные HTML отчеты
- Гибкая конфигурация через файл конфигурации и переменные окружения

## Утилиты

- `test_data.py`: Централизованное управление тестовыми данными
- `driver_factory.py`: Утилиты управления браузером Playwright
- `logger.py`: Функциональность ведения журналов с выводом в файл и консоль
- `run_tests.py`: Скрипт запуска тестов с различными вариантами выполнения

## Особенности Playwright

- Возможности автоматического ожидания
- Надежный выбор элементов
- Перехват сети
- Эмуляция устройств
- Поддержка мобильного тестирования