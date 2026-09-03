from datetime import date
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


def test_series_has_no_duplicate_asset_date():

    repository = AssetRepository(ASSETS_FILE)
    loader = HistoricalPriceLoader(repository)

    prices = list(loader.load(COTAHIST_FILE))

    keys = [
        (price.asset_id, price.date)
        for price in prices
    ]

    assert len(keys) == len(set(keys))


def test_series_dates_are_valid():

    repository = AssetRepository(ASSETS_FILE)
    loader = HistoricalPriceLoader(repository)

    prices = list(loader.load(COTAHIST_FILE))

    for price in prices:
        assert isinstance(price.date, date)


def test_series_has_valid_ohlc():

    repository = AssetRepository(ASSETS_FILE)
    loader = HistoricalPriceLoader(repository)

    prices = list(loader.load(COTAHIST_FILE))

    for price in prices:
        assert price.low <= price.high
        assert price.low <= price.open <= price.high
        assert price.low <= price.close <= price.high
        