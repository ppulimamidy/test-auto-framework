from pydantic import BaseModel
from typing import List

class LoginResult(BaseModel):
    login_result: str

class LoginResults(BaseModel):  # Moved outside of StockPriceResult
    login_results: List['LoginResult']   