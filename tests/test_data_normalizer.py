from src.extract.csv_extractor import CSVExtractor
from src.transform.data_normalizer import DataNormalizer


def get_normalizer():

    extractor = CSVExtractor(
        "data/raw/Sample - Superstore.csv",
        encoding="latin-1"
    )

    df = extractor.extract()

    return DataNormalizer(df)


def test_create_customers():

    normalizer = get_normalizer()

    customers = normalizer.create_customers()

    assert len(customers) > 0


def test_create_categories():

    normalizer = get_normalizer()

    categories = normalizer.create_categories()

    assert "category_id" in categories.columns


def test_create_locations():

    normalizer = get_normalizer()

    locations = normalizer.create_locations()

    assert "location_id" in locations.columns


def test_create_products():

    normalizer = get_normalizer()

    products = normalizer.create_products()

    assert len(products) > 0


def test_create_orders():

    normalizer = get_normalizer()

    normalizer.create_locations()

    orders = normalizer.create_orders()

    assert "location_id" in orders.columns


def test_create_order_items():

    normalizer = get_normalizer()

    items = normalizer.create_order_items()

    assert "item_id" in items.columns