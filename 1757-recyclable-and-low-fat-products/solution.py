import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    table = products[(products["low_fats"]== "Y") & (products["recyclable"]== "Y")]
    return table[["product_id"]]