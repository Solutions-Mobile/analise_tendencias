from pathlib import Path

from core.data.b3_parser import B3Parser

COTAHIST_FILE = (
    Path(__file__).resolve().parent
    / "data"
    / "cotahist_fragment.txt"
)

def test_parse_all_records():

    records = []

    with COTAHIST_FILE.open(
        "r",
        encoding="latin-1"
    ) as file:

        for line in file:

            line = line.rstrip("\r\n")

            if not line:
                continue

            if line[0:2] != "01":
                continue

            record = B3Parser.parse_line(line)

            assert record is not None
            records.append(record)

    assert len(records) > 0

    for record in records:

        assert record.symbol
        assert record.date is not None

        assert record.open >= 0
        assert record.high >= 0
        assert record.low >= 0
        assert record.average >= 0
        assert record.close >= 0

        assert record.trades >= 0
        assert record.quantity >= 0
        assert record.volume >= 0

def test_price_consistency():

    with COTAHIST_FILE.open(
        "r",
        encoding="latin-1"
    ) as file:

        for line in file:

            line = line.rstrip("\r\n")

            if not line.startswith("01"):
                continue

            record = B3Parser.parse_line(line)

            assert record.low <= record.high

            assert record.low <= record.average <= record.high

            assert record.low <= record.close <= record.high

def test_record_length():

    with COTAHIST_FILE.open(
        "r",
        encoding="latin-1"
    ) as file:

        for line in file:

            line = line.rstrip("\r\n")

            if not line.startswith("01"):
                continue

            assert len(line) == 245

            