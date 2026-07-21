from dataclasses import dataclass
import os


@dataclass
class ObservationConfig:
    timeout: int = int(os.getenv("OBSERVATION_TIMEOUT", "10"))
    dexscreener_base_url: str = os.getenv(
        "DEXSCREENER_BASE_URL",
        "https://api.dexscreener.com/latest"
    )
