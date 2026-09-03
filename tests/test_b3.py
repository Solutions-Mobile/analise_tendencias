from datetime import date
from pathlib import Path

from core.data.b3_parser import B3Parser
from core.data.asset_repository import AssetRepository


BASE_DIR = Path(__file__).resolve().parent.parent

COTAHIST_LINE = (
    "012016122902VALE3       010VALE        ON      N1   R$  "
    "000000000266800000000026850000000002550000000000258600"
    "000000025680000000002568000000000256913268000000000004"
    "778000000000012359083500000000000000009999123100000010"
    "000000000000BRVALEACNOR0192"
)

ASSETS_FILE = BASE_DIR / "core" / "reference" / "assets.csv"


def test_b3_parser():

    record = B3Parser.parse_line(
        COTAHIST_LINE
    )

    assert record is not None

    assert record.date == date(2016, 12, 29)
    assert record.bdi_code == 2
    assert record.symbol == "VALE3"
    assert record.market_type == 10
    assert record.name == "VALE"
    assert record.specification == "ON      N1"
    assert record.currency == "R$"

    assert record.open == 26.68
    assert record.high == 26.85
    assert record.low == 25.50
    assert record.average == 25.86
    assert record.close == 25.68
    assert record.bid == 25.68
    assert record.ask == 25.69

    assert record.trades == 13268
    assert record.quantity == 4778000
    assert record.volume == 123590835

    assert record.isin == "BRVALEACNOR0"
    assert record.quotation_factor == 1

def test_ignore_header():

    line = "00COTAHIST.2003BOVESPA"

    assert B3Parser.parse_line(line) is None


def test_ignore_trailer():

    line = "99COTAHIST.2003BOVESPA"

    assert B3Parser.parse_line(line) is None


def test_invalid_record():

    line = "012003021202VALE3"

    try:
        B3Parser.parse_line(line)
        assert False
    except ValueError as error:
        assert "Registro B3 inválido" in str(error)


def test_asset_repository():

    repository = AssetRepository(
        str(ASSETS_FILE)
    )

    asset = repository.find_by_symbol(
        "VALE3",
        date(2003, 2, 12)
    )

    assert asset is not None
    assert asset.asset_type.value == "STOCK"
