import csv
from datetime import date
from pathlib import Path
from uuid import UUID

from core.data.asset_symbol import AssetSymbol


class AssetRepository:

    def __init__(self, filename: str | Path):
        self._filename = Path(filename)
        self._assets: dict[str, AssetSymbol] = {}
        self._load()

    @staticmethod
    def _date(value: str) -> date | None:
        value = value.strip()

        if not value:
            return None

        return date.fromisoformat(value)

    def _load(self) -> None:
        with self._filename.open(
            "r",
            encoding="utf-8-sig",
            newline=""
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:
                symbol = row["symbol"].strip().upper()

                self._assets[symbol] = AssetSymbol(
                    asset_id=UUID(row["asset_id"]),
                    symbol=symbol,
                    valid_from=self._date(row["valid_from"]),
                    valid_to=self._date(row["valid_to"])
                )

    def find_by_symbol(
            self,
            symbol: str
        ) -> AssetSymbol | None:

            return self._assets.get(
                symbol.strip().upper()
            )

    def find_by_symbol_and_date(
            self,
            symbol: str,
            reference_date: date
        ) -> AssetSymbol | None:

            asset = self.find_by_symbol(symbol)

            if asset is None:
                return None

            if reference_date < asset.valid_from:
                return None

            if (
                asset.valid_to is not None
                and reference_date > asset.valid_to
            ):
                return None

            return asset