import random

def generate_seller_id():
    """Генерирует уникальный sellerId в диапазоне 111111-999999"""
    return random.randint(111111, 999999)

def generate_test_data():
    """Генерирует тестовые данные для объявлений"""
    return {
        "sellerId": generate_seller_id(),
        "title": f"Test Title {random.randint(1, 1000)}",
        "description": "Test Description",
        "price": random.randint(100, 10000)
    }
