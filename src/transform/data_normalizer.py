class DataNormalizer:

    def __init__(self, dataframe):
        self.df = dataframe

    def create_customers(self):

        return (
            self.df[["Customer ID", "Customer Name", "Segment"]]
            .drop_duplicates()
            .reset_index(drop=True)
        )

    def create_categories(self):

        categories = self.df[["Category"]].drop_duplicates().reset_index(drop=True)

        categories["category_id"] = categories.index + 1

        return categories

    def create_subcategories(self):

        return (
            self.df[["Category", "Sub-Category"]]
            .drop_duplicates()
            .reset_index(drop=True)
        )

    def create_products(self):

        return (
            self.df[["Product ID", "Product Name", "Sub-Category"]]
            .drop_duplicates()
            .reset_index(drop=True)
        )

    def create_locations(self):

        locations = (
            self.df[["Country", "State", "City", "Postal Code", "Region"]]
            .drop_duplicates()
            .reset_index(drop=True)
        )

        locations["location_id"] = locations.index + 1

        # Adiciona o location_id ao dataframe original
        self.df = self.df.merge(
            locations,
            on=["Country", "State", "City", "Postal Code", "Region"],
            how="left",
        )

        return locations

    def create_orders(self):

        return (
            self.df[
                [
                    "Order ID",
                    "Order Date",
                    "Ship Date",
                    "Ship Mode",
                    "Customer ID",
                    "location_id",
                ]
            ]
            .drop_duplicates()
            .reset_index(drop=True)
        )

    def create_order_items(self):

        items = self.df[
            ["Order ID", "Product ID", "Sales", "Quantity", "Discount", "Profit"]
        ].copy()

        items["item_id"] = range(1, len(items) + 1)

        return items

    def normalize(self):

        customers = self.create_customers()
        categories = self.create_categories()
        subcategories = self.create_subcategories()
        products = self.create_products()
        locations = self.create_locations()
        orders = self.create_orders()
        order_items = self.create_order_items()

        return {
            "customers": customers,
            "categories": categories,
            "subcategories": subcategories,
            "products": products,
            "locations": locations,
            "orders": orders,
            "order_items": order_items,
        }
