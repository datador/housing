import csv

from sqlalchemy import delete

from app.db import Session
from app.models.hms import HMSRaw


def main():
    with Session() as session:
        with session.begin():
            session.execute(delete(HMSRaw))

    with Session() as session:
        with session.begin():
            # https://www.fasteignaskra.is/gogn/grunngogn-til-nidurhals/kaupskra-fasteigna/eigindalysing-kaupskrar
            # https://objectstorage.eu-frankfurt-1.oraclecloud.com/n/frs3o1zldvgn/b/public_data_for_download/o/kaupskra.csv # 20250325
            with open("app/data/kaupskra.csv", encoding="latin-1") as f:
                reader = csv.DictReader(f, delimiter=";")

                for row in reader:
                    lower_row = {k.lower(): v for k, v in row.items()}
                    house = HMSRaw(**lower_row)
                    session.add(house)


if __name__ == "__main__":
    main()
