#core\data\instrument_classifier.py

from .asset import AssetType
from .b3_raw_record import B3RawRecord


class InstrumentClassifier:

    STOCK_SPECIFICATIONS = {
        "ON",
        "PN",
        "PNA",
        "PNB",
        "PNC",
        "PND",
        "PNE",
        "OR",
    }

    @classmethod
    def classify(cls, record: B3RawRecord) -> AssetType:

        if record.market_type not in {10, 20}:
            return AssetType.UNKNOWN

        if record.bdi_code == 12:
            return AssetType.FII

        if record.specification == "BDR":
            return AssetType.BDR

        symbol = record.symbol.strip()

        if symbol.endswith(("34", "39")):
            return AssetType.BDR

        if record.specification in cls.STOCK_SPECIFICATIONS:
            return AssetType.STOCK

        if symbol.endswith("11"):
            return AssetType.UNKNOWN

        return AssetType.UNKNOWN

    