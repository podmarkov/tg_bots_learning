def word_mul(number: int, word: str) -> str:
    string = word.capitalize()
    return string * number


print(word_mul(3, 'hello'))

from typing import Literal

user: dict[literal['name'] | literal['second_name'] | literal['username'], str] = {}

user['age'] = 18


class User:
    def __init__(self, user_id, name, age, email):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.email = email

def get_user_info(user: User) -> str:
    return f'''Возраст пользователя {user.name}: {user.age},
    адрес электронной почты: {user.email}'''

user_1 : User = User(1, 'John Doe', 25, 'john.doe@example.com')

from dataclasses import dataclass
@dataclass

class User1:
    user_id: int
    name: str
    age: int
    email: str



@dataclass
class DatabaseConfig:
    db_host: str
    db_user: str
    db_password: str
    database: str

@dataclass
class TgBot:
    token: str
    admin_ids: list[int]

@dataclass


class Config:
    tg_bot: TgBot
    db: DatabaseConfig

config = Config(tg_bot=TgBot(token=BOT_TOKEN,
                             admin_ids=ADMIN_IDS),
                db=DatabaseConfig(db_host=DB_HOST,
                                  db_user=DB_USER,
                                  db_password=DB_PASSWORD,
                                  database=DATABASE))