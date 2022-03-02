import external_lib
import sys
import os
from dotenv import load_dotenv
import pandas as pd
import numpy as np


def hello_world():
    print("hello")
    print("world")


def crash_me():
    x = [1, 2, 3]
    i = 5
    print(x[i])


def crash_me_harder():
    df = pd.DataFrame(
        {
            "A": 1.0,
            "B": pd.Timestamp("20130102"),
            "C": pd.Series(1, index=list(range(4)), dtype="float32"),
            "D": np.array([3] * 4, dtype="int32"),
            "E": pd.Categorical(["test", "train", "test", "train"]),
            "F": "foo",
        }
    )
    print(df.iloc["A"])


def use_env():
    load_dotenv(os.environ.get("ENV_PATH"))
    for var in ["USERNAME", "PASSWORD", "BUCKET"]:
        print(f"{var}: {os.environ.get(var)}")


if __name__ == "__main__":
    hello_world()
    # external_lib.fizz_buzz(int(sys.argv[1]))
    # crash_me()
    # crash_me_harder()
    # use_env()
