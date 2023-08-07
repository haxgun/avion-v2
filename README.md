<p></p>
<p align="center">
	<img width="300" src="docs/media/AvionBanner.png#gh-light-mode-only"/>
	<img width="300" src="docs/media/AvionBannerInverted.png#gh-dark-mode-only"/>
</p>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11.4-informational.svg">
  <img src="https://img.shields.io/badge/Django-4.2.3-informational.svg">
  <img src="https://img.shields.io/badge/Django--ninja-0.22.2-informational.svg">
  <a href="https://github.com/MAGICXcmd/avion/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/MAGICXcmd/avion-v2">
  </a>
</p>
<h2></h2>

**avion** - это простой, интуитивно понятный ToDo-менеджер.
Наш подход основан на идее гуманности — мы делаем приложение дружелюбным и естественным.
Мы верим, что использование приложения должно быть приятным и легким, как естественное общение.
Мы хотим, чтобы Вы ощущали гармонию в каждом взаимодействии с нашим приложением.

> **Warning**
> 
> Приложение находится в разработке.

<h2 align="center">🐍 Чтобы начать</h2>

```
git clone https://github.com/MAGICXcmd/avion-v2.git
cd avion-v2
python -m pip install pipenv
pipenv install
cd backend
nano .env
pipenv run migrate
pipenv run server
```

### В .env необходимо добавить следующее
```
DEBUG= # true или false
SECRET_KEY='' # необходимо вставить свой секретный ключ
DB_NAME='' # название базы данных
```

> **Если необходимо создать суперпользователя**
> ```
> pipenv run createsuperuser
> ```
