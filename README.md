# tg_bot_open_cv_ffmpeg
Telegram bot for face recognition in photos and converting voice messages to .wav format

 *Оглавление:*
 - [Описание](#Описание)
 - [Технологии](#Технологии)
 - [Алгоритм работы](#Алгоритмработы)
 - [Запуск проекта](#Запускпроекта)
 - [Автор](#Автор)


### Описание
Telegram бот для распознавания лиц на фотографиях и преобразования голосовых сообщений в формат .wav

### Технологии
aiogram, ffmpeg, OpenCV

<div id='Алгоритмработы'/>
 
### Алгоритм работы 
- Распознавание голосовых сообщений: отправляем голосовое сообщение, получаем сконвертированный файл.
- Распознование лиц на фотографиях: отправляем боту фотографию, в ответ получаем сообщение с количеством распознанных лиц. 
Если на фотографии распознаны лица, то мы ее сохраняем в файловую систему, иначе удаляем.

### Команды
- /start - Приветствие, появляется при первом старте бота
- /help - Повторяет сообщение при первом старте бота
- /test - Отвечает тестовым сообщением

<div id='Алгоритмработы'/>
 
### Запуск проекта 

Клонируйте репозиторий и перейдите в него в командной строке:

```
git clone git@github.com:Oleg5511/tg_bot_open_cv_ffmpeg.git
cd tg_bot_open_cv_ffmpeg
```

Установите зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Создайте файл .env и укажите токен вашего бота. Пример есть в .env_example.

### Автор
Над проектом работал:<br/>
[Oleg5511](https://github.com/Oleg5511)<br/>