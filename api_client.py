import requests

class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
    
    def create_advertisement(self, data):
        return requests.post(f"{self.base_url}/create", json=data)
    
    def get_advertisement(self, item_id):
        return requests.get(f"{self.base_url}/item/{item_id}")
    
    def get_seller_ads(self, seller_id):
        return requests.get(f"{self.base_url}/items/{seller_id}")
    
    def get_statistics(self, item_id):
        return requests.get(f"{self.base_url}/stat/{item_id}")
