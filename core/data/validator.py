from .market_data import MarketData


class MarketDataValidator:

    @staticmethod
    def validate(record: MarketData) -> None:

        if not record.symbol:
            raise ValueError("Símbolo não informado")

        if record.close <= 0:
            raise ValueError(
                f"Preço de fechamento inválido: {record.symbol}"
            )

        if record.high < record.low:
            raise ValueError(
                f"Máxima menor que mínima: {record.symbol}"
            )

        if record.high < record.open:
            raise ValueError(
                f"Máxima menor que abertura: {record.symbol}"
            )

        if record.high < record.close:
            raise ValueError(
                f"Máxima menor que fechamento: {record.symbol}"
            )

        if record.low > record.open:
            raise ValueError(
                f"Mínima maior que abertura: {record.symbol}"
            )

        if record.low > record.close:
            raise ValueError(
                f"Mínima maior que fechamento: {record.symbol}"
            )

        if record.quantity < 0:
            raise ValueError(
                f"Quantidade inválida: {record.symbol}"
            )

        if record.volume < 0:
            raise ValueError(
                f"Volume inválido: {record.symbol}"
            )
        