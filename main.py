from sqlalchemy import text, create_engine

from conf import config

# create database engine

engine = create_engine(
    f"postgresql+psycopg2://{config['database']['username']}:{config['database']['password']}@{config['database']['host']}:{config['database']['port']}/{config['database']['name']}",
    echo=True
)


def helloWorld():
    """Creates a self closing connection to the database after outputting 'Hello World'"""

    statement = "select 'Hello World'"
    with engine.connect() as conn:
        result = conn.execute(text(statement))
        print(result.all())


def main():
    helloWorld()
    return None


if __name__ == '__main__':
    main()
