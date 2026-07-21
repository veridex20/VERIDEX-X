import httpx


class DexScreenerClient:
    """Client for fetching live market data from DexScreener."""

    BASE_URL = "https://api.dexscreener.com/latest"

    async def health_check(self) -> bool:
        """Check if the DexScreener API is reachable."""
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(f"{self.BASE_URL}/dex/search?q=solana")
            return response.status_code == 200
