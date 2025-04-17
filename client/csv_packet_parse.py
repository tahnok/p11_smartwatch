import csv
import io
import sys
from pathlib import Path

import client


def main():
    p = Path(sys.argv[1])
    assert p.exists(), "input file not found"
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    with p.open() as f:
        reader = csv.DictReader(f)
        for r in reader:
            if r["Source"].startswith("Google"):
                source = "phone"
            else:
                source = "watch"

            p = client.hex_to_packet(r["Value"])

            writer.writerow(
                [
                    r["No."],
                    source,
                    repr(p.command),
                    repr(p.subCommand),
                    p.dataType,
                    p.data.hex(),
                ]
            )

    print(output.getvalue())


if __name__ == "__main__":
    main()
