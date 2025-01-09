import pandas as pd

# Create a simple DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emily"],
    "Age": [25, 30, 35, 40, 45],
}


def get_data():
    return pd.DataFrame(data)


print(get_data())
