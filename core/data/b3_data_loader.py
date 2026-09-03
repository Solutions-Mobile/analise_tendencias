from pathlib import Path
from typing import Iterator

from core.data.b3_parser import B3Parser
from core.data.b3_raw_record import B3RawRecord


class B3DataLoader:

    def load(
        self,
        filename: str | Path
    ) -> Iterator[B3RawRecord]:

        path = Path(filename)

        with path.open(
            "r",
            encoding="latin-1"
        ) as file:

            for line_number, line in enumerate(
                file,
                start=1
            ):

                line = line.rstrip("\r\n")

                if not line:
                    continue

                if not line.startswith("01"):
                    continue

                try:
                    record = B3Parser.parse_line(line)

                except Exception as error:
                    raise ValueError(
                        f"Erro no registro B3: "
                        f"linha={line_number}"
                    ) from error

                if record is not None:
                    yield record
                    