import os


class DatabaseUri:
    type = 'postgresql'
    name = "trivia_dev"
    host = 'localhost'
    port = 5432
    username = os.getenv('DATABASE_USERNAME')
    password = os.getenv('DATABASE_PASSWORD')

    def __str__(self):
        return f"{self.type}://{self.username}:{self.password}@{self.host}:{self.port}/{self.name}"
