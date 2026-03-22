# Telegram Booking Bot

## Описание

Telegram-бот для записи клиентов на услуги (салон, барбершоп, мастер, врач и т.д.)

## Функционал

* Выбор услуги
* Выбор даты
* Выбор времени
* Ввод имени
* Кнопка отправки номера телефона
* Подтверждение заявки
* Отправка заявки администратору

## Технологии

* Python 3
* aiogram 3
* FSM (Finite State Machine)

## Запуск

```bash
git clone <your_repo>
cd booking-bot

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

Создать `.env`:

```
BOT_TOKEN=your_token
ADMIN_ID=your_id
```

Запуск:

```bash
python main.py
```

## Применение

Подходит для:

* салонов красоты
* барбершопов
* клиник
* репетиторов

## Демо

Напишите боту в Telegram и попробуйте записаться.

## Контакты

Готов разработать подобного бота под ваш бизнес.
