from app.imports.import_hms import main as load_hms
from app.imports.import_products import main as load_product

load_product()
load_hms()