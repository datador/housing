import csv
from sqlalchemy import select, delete
from app.db import Session, Model, engine
from app.models.hms import HMS

def main():
    with Session() as session:
        with session.begin():
            session.execute(delete(HMS))

    with Session() as session:
        with session.begin():
            with open('app/data/kaupskra.csv', encoding='utf-8') as f:
                reader = csv.DictReader(f)

                for row in reader:
                    house = HMS(**row)
                    session.add(house)

if __name__ == '__main__':
    main()