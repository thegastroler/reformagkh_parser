import sqlite3


def input_data():
    """Функция ввода исходных данных."""
    while True:
        region = input(
            'Введите название региона, не указывая его тип, '
            'например: "Татарстан", "Владимирская", "Москва".\n'
            'Поле для ввода: '
        )
        print()
        city = input(
            'Введите название населенного пункта, например: "г. Калининград", '
            '"пгт. Прохоровка", "д. Крюково".\n'
            'Поле для ввода: '
        )
        print()
        street = input(
            'Введите название улицы, например: "ул. Лесная", "пр-кт. Победы", '
            '"пер. Дорожный".\n'
            'Поле для ввода: '
        )
        print()
        house = input(
            'Введите номер дома, например: "д. 144", "д. 6В, к. 3".\n'
            'Поле для ввода: '
        )
        print()
        address = ''
        params = (region, city, street, house)
        for i in params:
            if i:
                address += f'{i} '

        if not any([region, city, street, house, address]):
            pass
        else:
            conn = sqlite3.connect('reformagkh.db')
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO source (region, city, street, house, address)
                VALUES (?, ?, ?, ?, ?)
            """, (region, city, street, house, address))

            conn.commit()
            conn.close()


if __name__ == '__main__':
    input_data()
