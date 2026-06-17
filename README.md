# Фреймворк автоматизации тестирования SauceDemo

Это комплексный фреймворк автоматизации тестирования для приложения SauceDemo, созданный с использованием Python, Playwright и Pytest.

## Структура проекта

```
saucedemo_tests/
├── __init__.py
├── config.py                 # Configuration management with environment variables
├── conftest.py               # Pytest fixtures and configuration
├── pyproject.toml            # Build system and project metadata
├── requirements.txt          # Python dependencies (Playwright, pytest, etc.)
├── .env.example             # Environment variables template
├── .gitignore               # Git ignore patterns
├── README.md                # Project documentation (in Russian)
├── run_tests.py             # Test execution script with multiple options
├── verify_setup.py          # Verification script for basic functionality
├── .github/                 # GitHub configuration
│   └── workflows/           # GitHub Actions workflows
│       └── saucedemo_tests.yml  # SauceDemo tests workflow configuration
├── pages/                   # Page Object Model implementation
│   ├── __init__.py          # Exposes all page classes
│   ├── base_page.py         # Base page with common methods
│   ├── login_page.py        # SauceDemo login page object
│   ├── inventory_page.py    # SauceDemo inventory page object
│   ├── products_page.py     # SauceDemo products page object
│   ├── cart_page.py         # SauceDemo cart page object
│   └── checkout_page.py     # SauceDemo checkout page object
├── locators/                # Element locators centralized management
│   ├── __init__.py          # Exposes SauceDemoLocators
│   └── saucedemo_locators.py # All SauceDemo page element locators
├── utils/                   # Utility classes and data
│   ├── __init__.py          # Exposes utilities
│   ├── test_data.py         # Test data and credentials management
│   ├── driver_factory.py    # Playwright browser management utilities
│   └── logger.py            # Logging functionality
├── data/                    # Test data files (empty directory placeholder)
│   └── __init__.py
├── reports/                 # HTML test reports output (empty directory placeholder)
│   └── __init__.py
├── logs/                    # Runtime logs output (empty directory placeholder)
│   └── __init__.py
├── screenshots/             # Screenshot output (empty directory placeholder)
│   └── __init__.py
├── .pytest_cache/           # Pytest cache directory
├── saucedemo_env/           # Python virtual environment
└── tests/                   # Test cases
    └── test_saucedemo.py    # Main test file with multiple test scenarios
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
