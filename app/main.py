from app.database import get_connection


def main():
    print("Hello from Python!")

    connection = get_connection()

    try:
        print("Connected to PostgreSQL!")
    finally:
        connection.close()


if __name__ == "__main__":
    main()