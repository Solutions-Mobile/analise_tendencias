from pathlib import Path
from typing import Iterator

from core.data.b3_data_loader import B3DataLoader
from core.data.historical_price import HistoricalPrice
from core.data.historical_price_mapper import HistoricalPriceMapper
from core.reference.asset_repository import AssetRepository


class HistoricalPriceLoader:

    def __init__(
        self,
        asset_repository: AssetRepository
    ):
        self._asset_repository = asset_repository
        self._b3_loader = B3DataLoader()

    def load(
        self,
        filename: str | Path
    ) -> Iterator[HistoricalPrice]:

        for record in self._b3_loader.load(filename):

            asset = (
                self._asset_repository
                .find_by_symbol_and_date(
                    record.symbol,
                    record.date
                )
            )

            if asset is None:
                continue

            yield HistoricalPriceMapper.map(
                record,
                asset
            )
            