from pydantic import BaseModel
from typing import List

class StockPriceResult(BaseModel):
    stock_price: float
    stock_name: str 

class StockPriceResults(BaseModel):  # Moved outside of StockPriceResult
    stock_prices: List['StockPriceResult']   