from .dexscreener import DexScreenerClient


class ObservationService:
    """Coordinates market observations."""

    def __init__(self):
        self.client = DexScreenerClient()

    async def health(self):
        return await self.client.health_check()
