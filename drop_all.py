from app.db import Model, engine

Model.metadata.drop_all(engine)
