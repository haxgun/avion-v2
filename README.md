<p></p>
<p align="center">
  <img width="300" src="docs/media/AvionBanner.png#gh-light-mode-only"/>
  <img width="300" src="docs/media/AvionBannerInverted.png#gh-dark-mode-only"/>
</p>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11.4-informational.svg">
  <img src="https://img.shields.io/badge/Django-4.2.3-informational.svg">
  <img src="https://img.shields.io/badge/Django--ninja-0.22.2-informational.svg">
  <a href="https://github.com/haxgun/avion-v2/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/haxgun/avion-v2">
  </a>
</p>

---

**[avion](https://avion.space/) это простой, интуитивно понятный ToDo-менеджер.**

Наш подход основан на идее гуманности — мы делаем приложение дружелюбным и естественным.
Мы верим, что использование приложения должно быть приятным и легким, как естественное общение.
Мы хотим, чтобы Вы ощущали гармонию в каждом взаимодействии с нашим приложением.

> **⚠️ IMPORTANT NOTE:** Этот репозиторий находится в стадии интенсивной разработки.

<br/>

## ⚡️ Начало

**Необходимые компоненты:**
- Python 3.11.4
- Pipenv
- VSCode or Pycharm

```bash
git clone https://github.com/haxgun/avion-v2.git
cd avion-v2

# Установите необходимые пакеты
pipenv install

# Перейдите в папку backend и настройте .env
cd backend
nano .env

# Проведите миграции и запустите сервер
pipenv run migrate
pipenv run server

# По-умолчанию, документация к API доступна до адресу 127.0.0.1:8000/api/docs
```

### В .env необходимо добавить следующее
```env
DEBUG= # true или false
SECRET_KEY='' # необходимо вставить свой секретный ключ
DB_NAME='' # название базы данных
```

> **Если необходимо создать суперпользователя**
> ```bash
> pipenv run createsuperuser
> ```
