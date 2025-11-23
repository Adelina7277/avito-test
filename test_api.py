import pytest
import requests
from api_client import ApiClient
from helpers import generate_seller_id

BASE_URL = "https://qa-internship.avito.com"

class TestAdvertisementsAPI:
    @pytest.fixture
    def api_client(self):
        return ApiClient(BASE_URL)
    
    @pytest.fixture
    def seller_id(self):
        return generate_seller_id()
    
    def test_create_advertisement_success(self, api_client, seller_id):
        """TC-001: Успешное создание объявления"""
        data = {
            "sellerId": seller_id,
            "title": "Test Advertisement",
            "description": "Test Description",
            "price": 1000
        }
        
        response = api_client.create_advertisement(data)
        
        assert response.status_code == 200
        assert "item_id" in response.json()
        assert response.json()["title"] == data["title"]
    
    def test_get_advertisement_by_id(self, api_client, seller_id):
        """TC-002: Получение объявления по ID"""
        # Сначала создаем объявление
        data = {
            "sellerId": seller_id,
            "title": "Test Ad",
            "description": "Test Desc",
            "price": 500
        }
        create_response = api_client.create_advertisement(data)
        item_id = create_response.json()["item_id"]
        
        # Затем получаем его по ID
        get_response = api_client.get_advertisement(item_id)
        
        assert get_response.status_code == 200
        assert get_response.json()["item_id"] == item_id
