class MyName:
    """Клас для роботи з іменами користувачів"""

    total_names = 0  # Class Variable

    def __init__(self, name=None) -> None:
        """Конструктор класу"""

        if name is None:
            name = self.anonymous_user().name

        # Перевірка: тільки літери
        if not name.isalpha():
            raise ValueError("Ім'я може містити лише літери!")

        # Завжди з великої літери
        self.name = name.capitalize()

        MyName.total_names += 1
        self.my_id = MyName.total_names

    # ---------- PROPERTIES ----------

    @property
    def whoami(self) -> str:
        return f"My name is {self.name}"

    @property
    def my_email(self) -> str:
        return self.create_email()

    @property
    def full_name(self) -> str:
        return f"User #{self.my_id}: {self.name} ({self.my_email})"

    # ---------- METHODS ----------

    def create_email(self, domain="itcollege.lviv.ua") -> str:
        return f"{self.name}@{domain}"

    def name_length(self) -> int:
        return len(self.name)

    def save_to_file(self, filename="users.txt") -> None:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(self.full_name + "\n")

    # ---------- CLASS / STATIC ----------

    @classmethod
    def anonymous_user(cls):
        return cls("Anonymous")

    @staticmethod
    def say_hello(message="Hello to everyone!") -> str:
        return f"You say: {message}"


print("Розпочинаємо створювати об'єкти!")

# 🔹 ДОДАНО твоє ім'я
names = ("Bohdan", "Marta", "Alina", None)

all_names = {name: MyName(name) for name in names}

for name, me in all_names.items():
    print(f"""{">*<"*20}
Object: {me}
Name / ID: {me.name} / {me.my_id}
Who am I: {me.whoami}
Email: {me.my_email}
Full info: {me.full_name}
Name length: {me.name_length()}
Say hello: {me.say_hello("Привіт усім!")}
Total names (class): {MyName.total_names}
{"<*>"*20}""")

    me.save_to_file()

print(f"Завершено. Створено об'єктів: {MyName.total_names}")
