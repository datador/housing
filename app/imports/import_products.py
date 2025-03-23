import csv
from app.db import Session
from app.models.product import Product
from sqlalchemy import delete

def main():
    with Session() as session:
        with session.begin():
            session.execute(delete(Product))


    with Session() as session:
        with session.begin():
            with open('app/data/products.csv') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    row['year'] = int(row['year'])
                    product = Product(**row)
                    session.add(product)


if __name__ == '__main__':
    main()
