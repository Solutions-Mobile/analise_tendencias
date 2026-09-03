from collections import defaultdict
from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from core.data.historical_price_loader import HistoricalPriceLoader
from core.reference.asset_repository import AssetRepository


COTAHIST_FILE = (
    BASE_DIR / "tests" / "data" / "cotahist_fragment.txt"
)

ASSETS_FILE = (
    BASE_DIR / "core" / "reference" / "assets.csv"
)


def main():

    repository = AssetRepository(ASSETS_FILE)
    loader = HistoricalPriceLoader(repository)

    prices = list(loader.load(COTAHIST_FILE))

    assets = defaultdict(list)

    for price in prices:
        assets[price.asset_id].append(price)

    print(f"Total de registros: {len(prices)}")
    print(f"Total de ativos:    {len(assets)}")
    print()

    print(
        f"{'Ativo':36} "
        f"{'Pregões':>8} "
        f"{'Início':>12} "
        f"{'Fim':>12} "
        f"{'Fech. Inicial':>15} "
        f"{'Fech. Final':>14}"
    )

    print("-" * 105)

    for asset_id, series in sorted(assets.items()):

        series.sort(key=lambda price: price.date)

        first = series[0]
        last = series[-1]

        print(
            f"{str(asset_id):36} "
            f"{len(series):8} "
            f"{first.date:%Y-%m-%d} "
            f"{last.date:%Y-%m-%d} "
            f"{first.close:15.2f} "
            f"{last.close:14.2f}"
        )


if __name__ == "__main__":
    main()
    