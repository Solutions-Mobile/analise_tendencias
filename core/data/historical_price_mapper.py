from core.data.b3_raw_record import B3RawRecord
from core.data.historical_price import HistoricalPrice
from core.data.asset_symbol import AssetSymbol


class HistoricalPriceMapper:

    @staticmethod
    def map(
        record: B3RawRecord,
        asset: AssetSymbol
    ) -> HistoricalPrice:

        if record.date is None:
            raise ValueError("Cotação sem data")

        return HistoricalPrice(
            asset_id=asset.asset_id,
            date=record.date,
            open=record.open,
            high=record.high,
            low=record.low,
            close=record.close,
            average=record.average,
            trades=record.trades,
            quantity=record.quantity,
            volume=record.volume
        )
    