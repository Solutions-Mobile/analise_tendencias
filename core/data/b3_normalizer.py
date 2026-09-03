#core\data\b3_normalizer.py
from .asset import Asset
from .b3_raw_record import B3RawRecord
from .market_data import MarketData


class B3Normalizer:

    @staticmethod
    def normalize(
        record: B3RawRecord,
        asset: Asset
    ) -> MarketData:

        if record.date is None:
            raise ValueError(
                f"Registro sem data: {record.symbol}"
            )

        return MarketData(
            date=record.date,
            symbol=record.symbol,
            market_type=record.market_type,
            bdi_code=record.bdi_code,

            name=record.name,
            specification=record.specification,
            currency=record.currency,
            isin=asset.isin or record.isin,

            open=record.open,
            high=record.high,
            low=record.low,
            average=record.average,
            close=record.close,
            bid=record.bid,
            ask=record.ask,

            trades=record.trades,
            quantity=record.quantity,
            volume=record.volume,

            quotation_factor=record.quotation_factor,

            exercise_price=record.exercise_price,
            exercise_indicator=record.exercise_indicator,
            expiration_date=record.expiration_date,
            exercise_points=record.exercise_points,
            distribution_number=record.distribution_number
        )