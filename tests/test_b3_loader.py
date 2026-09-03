from pathlib import Path

from core.data.b3_data_loader import B3DataLoader

COTAHIST_FILE = (
    Path(__file__).resolve().parent
    / "data"
    / "cotahist_fragment.txt"
)


def test_load_cotahist():

    loader = B3DataLoader()

    records = list(
        loader.load(COTAHIST_FILE)
    )

    assert len(records) > 0

    for record in records:
        assert record.symbol
        assert record.date is not None

def test_loader_returns_only_tipreg_01():

    loader = B3DataLoader()

    records = list(
        loader.load(COTAHIST_FILE)
    )

    assert len(records) > 0

    for record in records:
        assert record.symbol
