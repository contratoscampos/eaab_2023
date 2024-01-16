import pandas as pd
from utils.model_dolar import foo


def return_df():
    """
    :return:
    """
    df = pd.read_excel("data/Base_dolar.xlsx")
    foo()
    return df


def final_model():
    """
    :return:
    """
    print("Acá estaria el modelo.")
