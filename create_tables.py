from sql_data.db import Base, engine
from sql_data.Models.movies import *
from sql_data.Models.conversations import *


def main():
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    main()