from pathlib import Path

from core.reference.asset_repository import AssetRepository


ASSETS_FILE = (
    Path(__file__).resolve().parent.parent
    / "core"
    / "reference"
    / "assets.csv"
)


def test_find_asset_by_symbol():

    repository = AssetRepository(ASSETS_FILE)

    asset = repository.find_by_symbol("VALE3")

    assert asset is not None
    assert asset.symbol == "VALE3"
    assert asset.asset_id is not None


def test_symbol_lookup_is_case_insensitive():

    repository = AssetRepository(ASSETS_FILE)

    asset = repository.find_by_symbol("vale3")

    assert asset is not None
    assert asset.symbol == "VALE3"


def test_unknown_symbol_returns_none():

    repository = AssetRepository(ASSETS_FILE)

    assert repository.find_by_symbol("XXXX99") is None
    