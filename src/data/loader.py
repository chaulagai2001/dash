import pandas as pd 
import datetime as dt

class DataSchema:
    AMOUNT = "amount"
    CATEGORY = "category"
    DATE = "date"
    MONTH = "month"
    YEAR = "year"


def load_transaction_data(path:str) -> pd.DataFrame:
    #load the data from csv
    data = pd.read_csv(
        path, 
        dtype = {
            DataSchema.AMOUNT:float,
            DataSchema.CATEGORY:str
        },
        parse_dates=[DataSchema.DATE]              
    )
    data[DataSchema.YEAR]=data[DataSchema.DATE].dt.year.astype(str)
    data[DataSchema.MONTH]=data[DataSchema.DATE].dt.month.astype(str)
    print(data)
    return data