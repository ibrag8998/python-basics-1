# ТЗ - Техническое Задание

Телеграм бот, который отвечает на следующие виды сообщений.

/convert 100 usd to rub

> 100 usd = 7000 rub

/convert usd to rub

> 1 usd = 70 rub

/convert 1000000 rub to btc

> 1000000 rub = 0.6 btc

/priceof rub

> 1 rub = 0.014 usd

/priceof btc

> 1 btc = 48000 usd

/start
/help

> Добрый день. Вот список команд: ...

## Реализация

Для работы с телеграм бот апи можно пользоваться чем угодно.
Но есть очень простая библиотека: https://github.com/eternnoir/pyTelegramBotAPI.

Для конвертации валют: https://exchangerate.host/#/docs.

Для работы с криптовалютами: https://coinmarketcap.com/.
Можно парсить, можно использовать апи.
