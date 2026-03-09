# Telegram-бот для продажи подписок Remnawave

Этот Telegram-бот предназначен для автоматизации продажи и управления подписками для панели **Remnawave**. Он интегрируется с API Remnawave для управления пользователями и подписками, а также использует различные платежные системы для приема платежей.

## ✨ Ключевые возможности

### Для пользователей:

- **Регистрация и выбор языка:** Поддержка русского и английского языков.
- **Просмотр подписки:** Пользователи могут видеть статус своей подписки, дату окончания и ссылку на конфигурацию.
- **Мои устройства:** Опциональный раздел для просмотра и отключения подключенных устройств (активируется через настройки).
- **Пробная подписка:** Система пробных подписок для новых пользователей (активируется вручную по кнопке).
- **Промокоды:** Возможность применять промокоды для получения скидок или бонусных дней.
- **Реферальная программа:** Пользователи могут приглашать друзей и получать за это бонусные дни подписки.
- **Оплата:** Поддержка оплаты через YooKassa, FreeKassa (REST API), Platega, SeverPay, CryptoPay и Telegram Stars.

### Для администраторов:

- **Защищенная админ-панель:** Доступ только для администраторов.
- **Статистика:** Просмотр статистики использования бота (общее количество пользователей, забаненные, активные подписки), недавние платежи и статус синхронизации с панелью.
- **Управление пользователями:** Блокировка/разблокировка пользователей, просмотр списка забаненных и детальной информации о пользователе.
- **Рассылка:** Отправка сообщений всем пользователям, пользователям с активной или истекшей подпиской.
- **Управление промокодами:** Создание и просмотр промокодов.
- **Синхронизация с панелью:** Ручной запуск синхронизации пользователей и подписок с панелью Remnawave.
- **Логи действий:** Просмотр логов всех действий пользователей.

## 🚀 Технологии

- **Python 3.12**
- **Aiogram 3.x:** Асинхронный фреймворк для Telegram ботов.
- **aiohttp:** Для запуска веб-сервера (вебхуки).
- **SQLAlchemy 2.x & asyncpg:** Асинхронная работа с базой данных PostgreSQL.
- **Alembic:** Миграции схемы базы данных.
- **YooKassa, FreeKassa API, Platega, SeverPay, aiocryptopay:** Интеграции с платежными системами.
- **Pydantic:** Для управления настройками из `.env` файла.
- **Docker & Docker Compose:** Для контейнеризации и развертывания.

## ⚙️ Установка и запуск

### Предварительные требования

- Установленные Docker и Docker Compose.
- Рабочая панель Remnawave.
- Токен Telegram-бота.
- Данные для подключения к платежным системам (YooKassa, CryptoPay и т.д.).

### Шаги установки

1.  **Клонируйте репозиторий:**

    ```bash
    git clone https://github.com/kavore/remnawave-tg-shop
    cd remnawave-tg-shop
    ```

2.  **Создайте и настройте файл `.env`:**
    Скопируйте `env.example` в `.env` и заполните своими данными.

    ```bash
    cp .env.example .env
    nano .env
    ```

    ### 📝 Описание всех переменных окружения

    Все параметры конфигурации заданы в файле `.env`. Ниже представлены таблицы с описанием каждой из настроек бота.

    <details>
    <summary><b>1. Основные настройки Telegram и бота</b></summary>

    | Переменная                   | Описание                                         | Примеры / Значения          |
    | ---------------------------- | ------------------------------------------------ | --------------------------- |
    | `BOT_TOKEN`                  | Токен Telegram-бота от @BotFather                | `1234567890:ABC-DEF...`     |
    | `ADMIN_IDS`                  | ID администраторов в Telegram через запятую      | `123456,789012`             |
    | `DEFAULT_LANGUAGE`           | Язык по умолчанию для новых пользователей        | `ru` или `en`               |
    | `SUPPORT_LINK`               | Ссылка на поддержку (отображается пользователям) | `https://t.me/support`      |
    | `SERVER_STATUS_URL`          | Ссылка на страницу статуса серверов              | `https://status.domain.com` |
    | `TERMS_OF_SERVICE_URL`       | Ссылка на условия использования                  | `https://domain.com/tos`    |
    | `SUBSCRIPTION_MINI_APP_URL`  | URL Mini App для показа подписки                 | `https://t.me/bot/app`      |
    | `START_COMMAND_DESCRIPTION`  | Описание команды /start                          |                             |
    | `MY_DEVICES_SECTION_ENABLED` | Включить раздел "Мои устройства"                 | `True` или `False`          |
    | `USER_HWID_DEVICE_LIMIT`     | Дефолтный лимит устройств (0 = безлимит)         | `0`                         |

    </details>

    <details>
    <summary><b>2. Настройки базы данных</b></summary>

    | Переменная          | Описание                             | Примеры / Значения     |
    | ------------------- | ------------------------------------ | ---------------------- |
    | `DATABASE_USER`     | Имя пользователя базы данных         | `postgres`             |
    | `DATABASE_PASSWORD` | Пароль базы данных                   | `postgres`             |
    | `DATABASE_HOST`     | Имя хоста или контейнера базы данных | `remnawave-tg-shop-db` |
    | `DATABASE_PORT`     | Порт базы данных                     | `5432`                 |
    | `DATABASE_DB`       | Имя базы данных                      | `postgres`             |

    </details>

    <details>
    <summary><b>3. Обязательная подписка на канал</b></summary>

    | Переменная                          | Описание                                    | Примеры / Значения     |
    | ----------------------------------- | ------------------------------------------- | ---------------------- |
    | `REQUIRED_CHANNEL_SUBSCRIBE_TO_USE` | Включить обязательную подписку на канал     | `True` или `False`     |
    | `REQUIRED_CHANNEL_ID`               | Telegram ID канала                          | `-100123456789`        |
    | `REQUIRED_CHANNEL_LINK`             | Публичная ссылка (или приглашение) на канал | `https://t.me/channel` |

    </details>

    <details>
    <summary><b>4. Серверные настройки и Webhooks</b></summary>

    | Переменная                | Описание                                      | Примеры / Значения            |
    | ------------------------- | --------------------------------------------- | ----------------------------- |
    | `WEBHOOK_BASE_URL`        | Базовый URL для Telegram вебхуков и платежей  | `https://webhooks.domain.com` |
    | `TELEGRAM_WEBHOOK_PATH`   | Относительный путь для Telegram-вебхука       | `/webhook/telegram`           |
    | `TELEGRAM_WEBHOOK_SECRET` | Секретный токен для проверки Telegram вебхука | `my_secret_token_123`         |
    | `WEB_SERVER_HOST`         | IP-адрес для прослушивания веб-сервером бота  | `0.0.0.0`                     |
    | `WEB_SERVER_PORT`         | Порт для прослушивания веб-сервером бота      | `8080`                        |

    </details>

    <details>
    <summary><b>5. Настройки платежных систем</b></summary>

    Включение и выключение:
    | Переменная | Описание |
    | --- | --- |
    | `PAYMENT_METHODS_ORDER` | Порядок платежек, например: `severpay,yookassa,cryptopay,freekassa,platega,stars` |
    | `YOOKASSA_ENABLED` | Включить YooKassa (`True`/`False`) |
    | `FREEKASSA_ENABLED` | Включить FreeKassa (`True`/`False`) |
    | `STARS_ENABLED` | Включить Telegram Stars (`True`/`False`) |
    | `CRYPTOPAY_ENABLED` | Включить CryptoPay (`True`/`False`) |
    | `PLATEGA_ENABLED` | Включить Platega (`True`/`False`) |
    | `SEVERPAY_ENABLED` | Включить SeverPay (`True`/`False`) |

    Детальные настройки конкретных платежек:

    YooKassa:
    | Переменная | Описание |
    | --- | --- |
    | `YOOKASSA_SHOP_ID` | ID магазина |
    | `YOOKASSA_SECRET_KEY` | Секретный ключ API |
    | `YOOKASSA_RETURN_URL` | Ссылка, куда вернется пользователь после оплаты |
    | `YOOKASSA_DEFAULT_RECEIPT_EMAIL`| Эл. почта по умолчанию для чеков |
    | `YOOKASSA_VAT_CODE` | Код НДС (например 1) |
    | `YOOKASSA_AUTOPAYMENTS_ENABLED`| Включить автоплатежи (`True`/`False`) |
    | `YOOKASSA_AUTOPAYMENTS_REQUIRE_CARD_BINDING`| Обязывать сохранять карту (`True`/`False`) |

    Налоговая (самозанятые):
    | Переменная | Описание |
    | --- | --- |
    | `NALOGO_INN` | ИНН для nalog.ru |
    | `NALOGO_PASSWORD` | Пароль для nalog.ru |
    | `NALOGO_RECEIPT_NAME_SUBSCRIPTION`| Шаблон для чека, например: `subscription {months} months` |
    | `NALOGO_RECEIPT_NAME_TRAFFIC` | Шаблон для чека, например: `traffic package {gb} GB` |

    FreeKassa, CryptoBot, Platega, SeverPay — см. ключи `FREEKASSA_*`, `CRYPTOPAY_*`, `PLATEGA_*`, `SEVERPAY_*` с аналогичным смыслом API-доступов.
    `STARS_PROVIDER_TOKEN` — Оставить пустым для Telegram Stars (XTR) или указать токен провайдера.
    </details>

    <details>
    <summary><b>6. Настройки подписок и тарифов</b></summary>

    Периоды:
    На каждый период (`1_MONTH`, `3_MONTHS`, `6_MONTHS`, `12_MONTHS`) есть переменные:
    - `*_ENABLED` (Включает продажу периода: `True`/`False`)
    - `RUB_PRICE_*` (Цена в рублях)
    - `STARS_PRICE_*` (Цена в Stars, 0 = недоступно/бесплатно)

    Трафик пакеты:
    | Переменная | Описание | Примеры / Значения |
    | --- | --- | --- |
    | `TRAFFIC_PACKAGES` | Покупка чистого трафика, формат ГБ:ЦЕНА | `10:199,50:799` |
    | `STARS_TRAFFIC_PACKAGES` | Трафик-пакеты в Stars | `10:2500` |
    | `DISCOUNT_PROMO_PAYMENT_TIMEOUT_MINUTES` | Удержание временного слота промокода до отмены | `10` |
    </details>

    <details>
    <summary><b>7. Взаимодействие с Remnawave-панелью</b></summary>

    | Переменная                 | Описание                                       |
    | -------------------------- | ---------------------------------------------- |
    | `PANEL_API_URL`            | URL API вашей панели Remnawave                 |
    | `PANEL_API_KEY`            | API ключ для доступа к панели                  |
    | `PANEL_WEBHOOK_SECRET`     | Секретный ключ для проверки вебхуков от панели |
    | `USER_TRAFFIC_LIMIT_GB`    | Общий лимит трафика для юзеров (0 = безлимит)  |
    | `USER_TRAFFIC_STRATEGY`    | Стратегия сброса (`NO_RESET`, `WEEK`, `MONTH`) |
    | `USER_SQUAD_UUIDS`         | ID отрядов для пользователей                   |
    | `USER_EXTERNAL_SQUAD_UUID` | UUID внешнего отряда Remnawave                 |

    </details>

    <details>
    <summary><b>8. Настройки триал-периода</b></summary>

    | Переменная               | Описание                        | Примеры / Значения |
    | ------------------------ | ------------------------------- | ------------------ |
    | `TRIAL_ENABLED`          | Включить пробный период         | `True` или `False` |
    | `TRIAL_DURATION_DAYS`    | Дней триала                     | `5`                |
    | `TRIAL_TRAFFIC_LIMIT_GB` | Лимит трафика ГБ (0 = безлимит) | `0`                |
    | `TRIAL_TRAFFIC_STRATEGY` | Сброс триального трафика        | `NO_RESET`         |

    </details>

    <details>
    <summary><b>9. Реферальная программа и уведомления</b></summary>

    Система рефералов:
    | Переменная | Описание |
    | --- | --- |
    | `REFERRAL_ENABLED` | Включить систему рефералов (`True`/`False`) |
    | `REFERRAL_ONE_BONUS_PER_REFEREE`| Выдавать бонус только за первую оплату друга |
    | `LEGACY_REFS` | Разрешать использовать старые реф-ссылки (`true`/`false`) |
    | `REFERRAL_BONUS_DAYS_*` | Бонусы пригласителю (для 1/3/6/12 мес) |
    | `REFEREE_BONUS_DAYS_*` | Бонусы приглашенному (для 1/3/6/12 мес) |

    Внутри-системные уведомления юзерам об истечении:
    - `SUBSCRIPTION_NOTIFICATIONS_ENABLED`: Разрешить нотификации
    - `SUBSCRIPTION_NOTIFY_ON_EXPIRE`: Писать при истечении
    - `SUBSCRIPTION_NOTIFY_AFTER_EXPIRE`: Писать после истечения
    - `SUBSCRIPTION_NOTIFY_DAYS_BEFORE`: За сколько дней (например `3`) писать об окончании.
    </details>

    <details>
    <summary><b>10. Настройки логирования / Админ-уведомлений / Прочее</b></summary>

    | Переменная                                                                                                   | Описание                                                        |
    | ------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------- |
    | `LOGS_PAGE_SIZE`                                                                                             | Размер страницы в админ-логах бота                              |
    | `LOG_LEVEL`                                                                                                  | Глобальный уровень логов (`DEBUG`, `INFO`...)                   |
    | `LOG_STORE_MESSAGE_CONTENT`                                                                                  | Хранить содержимое сообщений в БД (`True`/`False`)              |
    | `LOG_STORE_RAW_UPDATES`                                                                                      | Хранить RAW telegram update (`True`/`False`)                    |
    | `LOG_EXPORT_INCLUDE_SENSITIVE`                                                                               | Включать ли сырые данные в CSV (`True`/`False`)                 |
    | `LOG_ADMIN_HIDE`                                                                                             | Скрывать админов из списка логов в интерфейсе                   |
    | `LOG_CHAT_ID`                                                                                                | Telegram чат для админ-уведомлений                              |
    | `LOG_THREAD_ID`                                                                                              | Telegram тред (сообщение) для уведомлений                       |
    | `LOG_NEW_USERS`, `LOG_PAYMENTS`, `LOG_PROMO_ACTIVATIONS`, `LOG_TRIAL_ACTIVATIONS`, `LOG_SUSPICIOUS_ACTIVITY` | Выключатели конкретных типов админ-уведомлений (`True`/`False`) |
    | `CRYPT4_ENABLED`, `CRYPT4_REDIRECT_URL`                                                                      | Шифрование happ crypt4 (Обычно не нужно менять)                 |
    | `INLINE_*_THUMBNAIL_URL`                                                                                     | Иконки миниатюр в инлайн-режиме (Не менять без необходимости)   |

    </details>

3.  **Запустите контейнеры:**

    ```bash
    docker compose up -d
    ```

    Эта команда скачает образ и запустит сервис в фоновом режиме.

4.  **Настройка вебхуков (Обязательно):**
    Вебхуки являются **обязательным** компонентом для работы бота, так как они используются для получения уведомлений от платежных систем (YooKassa, FreeKassa, CryptoPay, Platega, SeverPay) и панели Remnawave.

    Вам понадобится обратный прокси (например, Nginx) для обработки HTTPS-трафика и перенаправления запросов на контейнер с ботом.

    **Пути для перенаправления:**
    - `https://<ваш_домен>/webhook/yookassa` → `http://remnawave-tg-shop:<WEB_SERVER_PORT>/webhook/yookassa`
    - `https://<ваш_домен>/webhook/freekassa` → `http://remnawave-tg-shop:<WEB_SERVER_PORT>/webhook/freekassa`
    - `https://<ваш_домен>/webhook/platega` → `http://remnawave-tg-shop:<WEB_SERVER_PORT>/webhook/platega`
    - `https://<ваш_домен>/webhook/severpay` → `http://remnawave-tg-shop:<WEB_SERVER_PORT>/webhook/severpay`
    - `https://<ваш_домен>/webhook/cryptopay` → `http://remnawave-tg-shop:<WEB_SERVER_PORT>/webhook/cryptopay`
    - `https://<ваш_домен>/webhook/panel` → `http://remnawave-tg-shop:<WEB_SERVER_PORT>/webhook/panel`
    - **Для Telegram:** Бот автоматически установит вебхук, если в `.env` указан `WEBHOOK_BASE_URL`. Путь берётся из `TELEGRAM_WEBHOOK_PATH` (по умолчанию `https://<ваш_домен>/webhook/telegram`).

    Где `remnawave-tg-shop` — это имя сервиса из `docker-compose.yml`, а `<WEB_SERVER_PORT>` — порт, указанный в `.env`.

5.  **Просмотр логов:**

    ```bash
    docker compose logs -f remnawave-tg-shop
    ```

    > 💡 Если включена проверка подписки (`REQUIRED_CHANNEL_SUBSCRIBE_TO_USE=true`), добавьте бота администратором в канал из `REQUIRED_CHANNEL_ID`. Пользователь увидит кнопку «Проверить подписку», и после успешного подтверждения доступ продолжится.

### Миграции БД (Alembic)

- При запуске `python main.py` миграции применяются автоматически до `head`.
- Для ручного запуска используйте:

```bash
alembic upgrade head
```

## Подробная инструкция для развертывания на сервере с панелью Remnawave

### 1. Клонирование репозитория

```bash
git clone https://github.com/kavore/remnawave-tg-shop && cd remnawave-tg-shop
```

### 2. Настройка переменных окружения

```bash
cp .env.example .env && nano .env
```

Обязательно ознакомьтесь с таблицами конфигураций выше, чтобы правильно настроить бота.

**Основные поля для заполнения:**

- `BOT_TOKEN` - токен телеграмм бота, например, `234567890:ABC-DEF...`
- `ADMIN_IDS` - TG ID администраторов, например, `12345678,98765432`
- `WEBHOOK_BASE_URL` - Обязательно. Базовый URL для вебхуков, например `https://webhook.domain.com`
- `PANEL_API_URL` - URL API вашей панели Remnawave (например, `http://remnawave:3000/api` или `https://panel.domain.com/api`)
- `PANEL_API_KEY` - API ключ для доступа к панели (генерируется из UI-интерфейса панели)
- `PANEL_WEBHOOK_SECRET` - Секретный ключ для проверки вебхуков от панели (берётся из `.env` самой панели)

### 3. Настройка Reverse Proxy (Nginx)

Перейдите в директорию конфигурации Nginx панели Remnawave:

```bash
cd /opt/remnawave/nginx && nano nginx.conf
```

Добавьте в `nginx.conf` следующую конфигурацию:

```nginx
upstream remnawave-tg-shop {
    server remnawave-tg-shop:8080;
}

map $http_upgrade $connection_upgrade {
    default upgrade;
    "" close;
}

server {
    server_name webhook.domain.com; # Домен для отправки Webhook'ов
    listen 443 ssl;
    http2 on;

    ssl_certificate "/etc/nginx/ssl/webhook_fullchain.pem";
    ssl_certificate_key "/etc/nginx/ssl/webhook_privkey.key";
    ssl_trusted_certificate "/etc/nginx/ssl/webhook_fullchain.pem";

    proxy_http_version 1.1;
    proxy_set_header Host $host;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection $connection_upgrade;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header X-Forwarded-Host $host;
    proxy_set_header X-Forwarded-Port $server_port;
    proxy_send_timeout 60s;
    proxy_read_timeout 60s;
    proxy_intercept_errors on;
    error_page 400 404 500 502 @redirect;

    location / {
        proxy_pass http://remnawave-tg-shop$request_uri;
    }

    location @redirect {
        return 404;
    }
}
```

### 4. Выпуск SSL-сертификата для домена webhook

Убедитесь, что установлены необходимые компоненты, а также откройте 80 порт:

```bash
sudo apt-get install cron socat
curl https://get.acme.sh | sh -s email=EMAIL && source ~/.bashrc
ufw allow 80/tcp && ufw reload
```

Выпустите сертификат:

```bash
acme.sh --set-default-ca --server letsencrypt
acme.sh --issue --standalone -d 'webhook.domain.com' \
  --key-file /opt/remnawave/nginx/webhook_privkey.key \
  --fullchain-file /opt/remnawave/nginx/webhook_fullchain.pem
```

### 5. Добавление сертификатов в Docker Compose Nginx

Отредактируйте `docker-compose.yml` панели Nginx:

```bash
cd /opt/remnawave/nginx && nano docker-compose.yml
```

Добавьте две строки в секцию `volumes`:

```yaml
services:
  remnawave-nginx:
    image: nginx:1.26
    container_name: remnawave-nginx
    hostname: remnawave-nginx
    volumes:
      - ./nginx.conf:/etc/nginx/conf.d/default.conf:ro
      - ./fullchain.pem:/etc/nginx/ssl/fullchain.pem:ro
      - ./privkey.key:/etc/nginx/ssl/privkey.key:ro
      - ./subdomain_fullchain.pem:/etc/nginx/ssl/subdomain_fullchain.pem:ro
      - ./subdomain_privkey.key:/etc/nginx/ssl/subdomain_privkey.key:ro
      - ./webhook_fullchain.pem:/etc/nginx/ssl/webhook_fullchain.pem:ro # Добавьте эту строку
      - ./webhook_privkey.key:/etc/nginx/ssl/webhook_privkey.key:ro # Добавьте эту строку
    restart: always
    ports:
      - "0.0.0.0:443:443"
    networks:
      - remnawave-network

networks:
  remnawave-network:
    name: remnawave-network
    driver: bridge
    external: true
```

### 6. Запуск бота и перезапуск Nginx

Запустите бота:

```bash
cd /root/remnawave-tg-shop && docker compose up -d && docker compose logs -f -t
```

Перезапустите Nginx:

```bash
cd /opt/remnawave/nginx && docker compose down && docker compose up -d && docker compose logs -f -t
```

## 🐳 Docker

Файлы `Dockerfile` и `docker-compose.yml` уже настроены для сборки и запуска проекта. `docker-compose.yml` использует готовый образ с GitHub Container Registry, но вы можете раскомментировать `build: .` для локальной сборки.

Для автоматической публикации образов настроены GitHub Actions (`.github/workflows`). По умолчанию образы пушатся в GitHub Container Registry и Docker Hub. Добавьте в Secrets репозитория значения `DOCKERHUB_USERNAME` и `DOCKERHUB_TOKEN` (персональный access token или пароль для Docker Hub), чтобы загрузка в Docker Hub работала корректно.

## 📁 Структура проекта

```
.
├── bot/
│   ├── filters/          # Пользовательские фильтры Aiogram
│   ├── handlers/         # Обработчики сообщений и колбэков
│   ├── keyboards/        # Клавиатуры
│   ├── middlewares/      # Промежуточные слои (i18n, проверка бана)
│   ├── services/         # Бизнес-логика (платежи, API панели)
│   ├── states/           # Состояния FSM
│   └── main_bot.py       # Основная логика бота
├── config/
│   └── settings.py       # Настройки Pydantic
├── db/
│   ├── dal/              # Слой доступа к данным (DAL)
│   ├── database_setup.py # Настройка БД
│   └── models.py         # Модели SQLAlchemy
├── locales/              # Файлы локализации (ru, en)
├── .env.example          # Пример файла с переменными окружения
├── Dockerfile            # Инструкции для сборки Docker-образа
├── docker-compose.yml    # Файл для оркестрации контейнеров
├── requirements.txt      # Зависимости Python
└── main.py               # Точка входа в приложение
```

## 🔮 Планы на будущее

- Расширенные типы промокодов (например, скидки в процентах).

## ❤️ Поддержка

- Карты РФ и зарубежные: [Tribute](https://t.me/tribute/app?startapp=dqdg)
- Crypto: `USDT TRC-20 TT3SqBbfU4vYm6SUwUVNZsy278m2xbM4GE`
