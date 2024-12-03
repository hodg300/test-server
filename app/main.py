from fastapi import FastAPI
from fastapi import status
from fastapi.responses import JSONResponse

from app.base_models import User2, Player, HistoryShuffle
from app.services.football_service import FootballService
from app.services.greet_service import GreetService

app = FastAPI()
football_service = FootballService()


@app.get("/")
def route():
    return {"hello": "world2"}


@app.post('/add-player')
def add_player(player: Player):
    return football_service.add_player(player=player)


@app.get('/all-players')
def get_all_players():
    return football_service.get_all_players()


@app.get('/last-selected-players')
def get_last_selected_players():
    return football_service.get_last_selected_players()


@app.post('/save-last-selected-players')
def save_last_selected_players(players: dict):
    return football_service.save_last_selected_players(players=players)


@app.post('/save-history-shuffle')
def save_history_shuffle(history_shuffle: HistoryShuffle):
    return football_service.save_history_shuffle(history_shuffle)


@app.get('/all-history-shuffles')
def save_history_shuffle(limit=10):
    return football_service.get_all_history_shuffles(limit)