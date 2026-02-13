# loose_coupling.py
from abc import ABC, abstractmethod


class Database(ABC):

    @abstractmethod
    def connect(self):
        pass


class MySQLDatabase(Database):
    def connect(self):
        return "Connected to MySQL"


class PostgreSQLDatabase(Database):
    def connect(self):
        return "Connected to PostgreSQL"


class Application:
    def __init__(self, database: Database):
        self.database = database

    def start(self):
        print(self.database.connect())


if __name__ == "__main__":
    mysql = MySQLDatabase()
    app = Application(mysql)
    app.start()

    postgres = PostgreSQLDatabase()
    app = Application(postgres)
    app.start()
