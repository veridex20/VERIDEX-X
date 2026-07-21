from dataclasses import dataclass
from typing import Optional


@dataclass
class TokenObservation:
    chain: str
    dex: str
    pair_address: str
    base_token: str
    quote_token: str
    price_usd: Optional[float]
    liquidity_usd: Optional[float]
    volume_24h: Optional[float]
    fdv: Optional[float]
