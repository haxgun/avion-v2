## 🔩 Необходимые компоненты
- Python 3.11.4
- Pipenv
- VSCode or Pycharm

```bash
git clone https://github.com/MAGICXcmd/avion-v2.git
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

## 🛍️ Пакеты используемые в Backend
```
cryptography==41.0.3
└── cffi [required: >=1.12, installed: 1.15.1]
    └── pycparser [required: Any, installed: 2.21]
django-cors-headers==4.2.0
└── Django [required: >=3.2, installed: 4.2.3]
    ├── asgiref [required: >=3.6.0,<4, installed: 3.7.2]
    ├── sqlparse [required: >=0.3.1, installed: 0.4.4]
    └── tzdata [required: Any, installed: 2023.3]
django-ninja-jwt==5.2.5
├── Django [required: >=2.1, installed: 4.2.3]
│   ├── asgiref [required: >=3.6.0,<4, installed: 3.7.2]
│   ├── sqlparse [required: >=0.3.1, installed: 0.4.4]
│   └── tzdata [required: Any, installed: 2023.3]
├── django-ninja-extra [required: >=0.14.2, installed: 0.19.1]
│   ├── asgiref [required: Any, installed: 3.7.2]
│   ├── contextlib2 [required: Any, installed: 21.6.0]
│   ├── Django [required: >=2.2, installed: 4.2.3]
│   │   ├── asgiref [required: >=3.6.0,<4, installed: 3.7.2]
│   │   ├── sqlparse [required: >=0.3.1, installed: 0.4.4]
│   │   └── tzdata [required: Any, installed: 2023.3]
│   ├── django-ninja [required: ==0.22.2, installed: 0.22.2]
│   │   ├── Django [required: >=2.2, installed: 4.2.3]
│   │   │   ├── asgiref [required: >=3.6.0,<4, installed: 3.7.2]
│   │   │   ├── sqlparse [required: >=0.3.1, installed: 0.4.4]
│   │   │   └── tzdata [required: Any, installed: 2023.3]
│   │   └── pydantic [required: >=1.6,<2.0.0, installed: 1.10.12]
│   │       └── typing-extensions [required: >=4.2.0, installed: 4.7.1]
│   └── injector [required: >=0.19.0, installed: 0.21.0]
├── pyjwt [required: >=1.7.1,<3, installed: 2.8.0]
└── pyjwt [required: Any, installed: 2.8.0]
email-validator==2.0.0.post2
├── dnspython [required: >=2.0.0, installed: 2.4.1]
└── idna [required: >=2.0.0, installed: 3.4]
python-dotenv==1.0.0
pytz==2023.3
six==1.16.0
uvicorn==0.23.2
├── click [required: >=7.0, installed: 8.1.6]
│   └── colorama [required: Any, installed: 0.4.6]
└── h11 [required: >=0.8, installed: 0.14.0]
whitenoise==6.5.0
```