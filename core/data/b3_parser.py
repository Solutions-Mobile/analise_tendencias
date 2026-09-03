#core\data\b3_parser.py
from datetime import date
from typing import Optional

from .b3_raw_record import B3RawRecord


class B3Parser:

    @staticmethod
    def _text(value: str) -> str:
        return value.strip()

    @staticmethod
    def _integer(value: str) -> int:
        value = value.strip()

        if not value:
            return 0

        return int(value)

    @staticmethod
    def _price(value: str) -> float:
        value = value.strip()

        if not value:
            return 0.0

        return int(value) / 100

    @staticmethod
    def _decimal(value: str, decimals: int) -> float:
        value = value.strip()

        if not value:
            return 0.0

        return int(value) / (10 ** decimals)

    @staticmethod
    def _date(value: str) -> Optional[date]:
        value = value.strip()

        if not value or value == "00000000":
            return None

        return date(
            int(value[0:4]),
            int(value[4:6]),
            int(value[6:8])
        )

    @classmethod
    def parse_line(cls, line: str) -> Optional[B3RawRecord]:

        if not line:
            return None

        record_type = line[0:2]

        if record_type != "01":
            return None

        if len(line) < 245:
            raise ValueError(
                f"Registro B3 inválido: tamanho={len(line)}"
            )

        return B3RawRecord(
            date=cls._date(line[2:10]),
            bdi_code=cls._integer(line[10:12]),
            symbol=cls._text(line[12:24]),
            market_type=cls._integer(line[24:27]),
            name=cls._text(line[27:39]),
            specification=cls._text(line[39:49]),
            currency=cls._text(line[52:56]),

            open=cls._price(line[56:69]),
            high=cls._price(line[69:82]),
            low=cls._price(line[82:95]),
            average=cls._price(line[95:108]),
            close=cls._price(line[108:121]),
            bid=cls._price(line[121:134]),
            ask=cls._price(line[134:147]),

            trades=cls._integer(line[147:152]),
            quantity=cls._integer(line[152:170]),
            volume=cls._price(line[170:188]),

            exercise_price=cls._price(line[188:201]),
            exercise_indicator=cls._integer(line[201:202]),
            expiration_date=cls._date(line[202:210]),

            quotation_factor=cls._integer(line[210:217]),
            exercise_points=cls._decimal(
                line[217:230],
                6
            ),

            isin=cls._text(line[230:242]),
            distribution_number=cls._integer(line[242:245])
        )

    @classmethod
    def parse_file(cls, filename: str) -> list[B3RawRecord]:

        records = []

        with open(
            filename,
            "r",
            encoding="latin-1"
        ) as file:

            for line in file:
                record = cls.parse_line(
                    line.rstrip("\r\n")
                )

                if record is not None:
                    records.append(record)

        return records
    