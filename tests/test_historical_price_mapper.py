from datetime import date
from pathlib import Path

from core.data.b3_data_loader import B3DataLoader
from core.data.historical_price_mapper import HistoricalPriceMapper
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


def test_map_record_to_historical_price():

    loader = B3DataLoader()
    repository = AssetRepository(ASSETS_FILE)

    record = next(
        record
        for record in loader.load(COTAHIST_FILE)
        if record.symbol == "VALE3"
    )

    asset = repository.find_by_symbol_and_date(
        record.symbol,
        record.date
    )

    assert asset is not None

    price = HistoricalPriceMapper.map(
        record,
        asset
    )

    assert price.asset_id == asset.asset_id
    assert price.date == record.date
    assert price.open == record.open
    assert price.high == record.high
    assert price.low == record.low
    assert price.close == record.close
    assert price.average == record.average
    assert price.trades == record.trades
    assert price.quantity == record.quantity
    assert price.volume == record.volume
        