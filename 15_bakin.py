import random
import string

def generate_random_email():
    """
    Генерирует случайный email адрес в формате <name>@<domain>.<tld>.

    Возвращает:
    str: Случайный email адрес.
    """
    # Генерация случайного имени (случайная строка длиной от 5 до 10 символов)
    name_length = random.randint(5, 10)
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=name_length))

    # Генерация случайного домена (случайная строка длиной от 5 до 10 символов)
    domain_length = random.randint(5, 10)
    domain = ''.join(random.choices(string.ascii_lowercase + string.digits, k=domain_length))

    # Выбор случайного домена верхнего уровня (TLD) из списка
    tlds = ['.com', '.net', '.org', '.info', '.biz', '.io', '.xyz']
    tld = random.choice(tlds)

    # Сборка email адреса в формате <name>@<domain>.<tld>
    email = f"{name}@{domain}{tld}"

    return email

# Пример использования функции для генерации email адреса
if __name__ == "__main__":
    random_email = generate_random_email()
    print("Случайный email адрес:", random_email)
