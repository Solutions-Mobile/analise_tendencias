from pathlib import Path

from core.data.historical_price_loader import HistoricalPriceLoader
from core.reference.asset_repository import AssetRepository


COTAHIST_FILE = (
    Path(__file__).resolve().parent
    / "data"
    / "cotahist_fragment.txt"
)

ASSETS_FILE = (
    Path(__file__).resolve().parent.parent
    / "core"
    / "reference"
    / "assets.csv"
)


def test_load_historical_prices():

    repository = AssetRepository(ASSETS_FILE)
    loader = HistoricalPriceLoader(repository)

    prices = list(
        loader.load(COTAHIST_FILE)
    )

    assert len(prices) > 0

    for price in prices:
        assert price.asset_id is not None
        assert price.date is not None
        assert price.close >= 0
        