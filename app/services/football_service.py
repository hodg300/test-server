from app.base_models import Player, HistoryShuffle
from app.services.firebase_service import FirebaseService


class FootballService:

    def __init__(self):
        self.firebase_service = FirebaseService()


    def add_player(self, player: Player):
        return self.firebase_service.save_data_to_firestore("test-collection", player.name, player.model_dump())

    def get_all_players(self):
        return self.firebase_service.fetch_all_docs_from_firestore("players")

    def get_last_selected_players(self):
        return self.firebase_service.fetch_data_from_firestore("last_selected_players", "JASLDP12DKPX")


    def save_last_selected_players(self, players):
        return self.firebase_service.save_data_to_firestore("last_selected_players", "JASLDP12DKPX", players)

    def save_history_shuffle(self, history_shuffle: HistoryShuffle):
        return self.firebase_service.save_data_to_firestore("history_shuffles", str(history_shuffle.date), history_shuffle.model_dump())

    def get_all_history_shuffles(self, limit=10):
        return self.firebase_service.fetch_all_docs_from_firestore("history_shuffles", limit)