class RoutingTable:
    def __init__(self):
        self.table = {}  # Структура {id: name}
        self.reverse_table = {}  # Структура {name: id}

    def add_user(self, user_id, name):
        """Добавление нового пользователя в таблицу маршрутизации."""
        if name in self.reverse_table:
            raise ValueError("Name already exists")
        self.table[user_id] = name
        self.reverse_table[name] = user_id

    def get_name_by_id(self, user_id):
        """Получить имя пользователя по его id."""
        return self.table.get(user_id)

    def get_id_by_name(self, name):
        """Получить id пользователя по его имени."""
        return self.reverse_table.get(name)

    def remove_user(self, user_id):
        """Удаление пользователя из таблицы маршрутизации."""
        if user_id in self.table:
            name = self.table.pop(user_id)
            self.reverse_table.pop(name, None)