from fastapi import FastAPI
from operations.schemas import Trade
from typing import List

app = FastAPI(
    title= 'My FastAPI App'
)

fake_trades = [
    {'id': 1, 'user_id': 1, 'kek': 'W'},
    {'id': 2, 'user_id': 1, 'kek': 'W'},
    {'id': 3, 'user_id': 1, 'kek': 'W'},
    {'id': 4, 'user_id': 1, 'kek': 'W'},
    {'id': 5, 'user_id': 1, 'kek': 'W'},

]


@app.get('/trades', response_model=List[Trade])
def get_trades(limit: int = 1, offset: int = 1):
    return fake_trades[offset:][:limit]

@app.post('/trades')
def add_trades(trades: List[Trade]):
    fake_trades.extend(trades)
    return {'status': 200, 'data': fake_trades}


