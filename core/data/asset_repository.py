#core\data\asset_repository.py

import csv
from pathlib import Path
from typing import Optional
from uuid import UUID

from .asset import Asset, AssetType
from .asset_symbol import AssetSymbol


class AssetRepository:

    def __init__(self, filename: str):
        self._assets: dict[UUID, Asset] = {}
        self._symbols: dict[str, list[AssetSymbol]] = {}

        self._load(filename)

    def _load(self, filename: str) -> None:

        path = Path(filename)

        with path.open(
            "r",
            encoding="utf-8-sig",
            newline=""
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                asset_id = UUID(row["asset_id"])

                asset = Asset(
                    asset_id=asset_id,
                    asset_type=AssetType(
                        row["asset_type"].strip()
                    ),
                    name=row["name"].strip(),
                    isin=row["isin"].strip() or None
                )

                self._assets[asset_id] = asset

                symbol = AssetSymbol(
                    asset_id=asset_id,
                    symbol=row["symbol"].strip(),
                    valid_from=self._parse_date(
                        row["valid_from"]
                    ),
                    valid_to=self._parse_date(
                        row["valid_to"]
                    )
                )

                self._symbols.setdefault(
                    symbol.symbol,
                    []
                ).append(symbol)

    @staticmethod
    def _parse_date(value: str):
        value = value.strip()

        if not value:
            return None

        from datetime import date

        return date.fromisoformat(value)

    def get(self, asset_id: UUID) -> Optional[Asset]:
        return self._assets.get(asset_id)

    def find_by_symbol(
        self,
        symbol: str,
        reference_date
    ) -> Optional[Asset]:

        symbols = self._symbols.get(
            symbol.strip(),
            []
        )

        for item in symbols:

            if item.valid_from > reference_date:
                continue

            if (
                item.valid_to is not None
                and reference_date > item.valid_to
            ):
                continue

            return self._assets.get(item.asset_id)

        return None

    def all(self) -> list[Asset]:
        return list(self._assets.values())
    