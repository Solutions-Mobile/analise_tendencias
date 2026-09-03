#core\data\asset.py

from dataclasses import dataclass
from enum import Enum
from typing import Optional
from uuid import UUID


class AssetType(Enum):
    STOCK = "STOCK"
    BDR = "BDR"
    ETF = "ETF"
    FII = "FII"
    UNKNOWN = "UNKNOWN"


@dataclass(frozen=True)
class Asset:
    asset_id: UUID
    asset_type: AssetType
    name: str
    isin: Optional[str]
    