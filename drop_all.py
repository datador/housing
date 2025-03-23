from app.db import Model, engine
import app.models
Model.metadata.drop_all(engine)