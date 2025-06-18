import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:

    if len(orders) == 0:
       return pd.DataFrame([], columns=['customer_number'])

    df = orders.groupby("customer_number").count().reset_index().sort_values(by=['order_number'],ascending=False)

    return pd.DataFrame([df.iloc[0]['customer_number']], columns=['customer_number'])