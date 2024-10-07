class ItemsService:

    items = [
        {"id": 1, "name": "Item One", "price": 10.99},
        {"id": 2, "name": "Item Two", "price": 15.49},
        {"id": 3, "name": "Item Three", "price": 7.99}
    ]

    def get_all_items(self):
        return {"status": "success", "data": self.items}