import pandas as pd

# Load the CSV
df = pd.read_csv("../commuter/DepartureDestinationTrip.csv")

# Function to adapt for delivery person
def adapt_for_delivery(df):
    df_new = df.copy()

    # Weekday rows only
    weekdays = df_new['days'] == 'weekdays'

    # Remove workplace time
    df_new.loc[weekdays, 'workplace'] = 0

    # Increase errands probability during all weekdays
    df_new.loc[weekdays, 'errands'] = df_new.loc[weekdays, 'errands'] * 3

    # Increase home slightly to balance the day
    df_new.loc[weekdays, 'home'] = df_new.loc[weekdays, 'home'] * 1.2

    return df_new

# Adapt the CSV
df_delivery = adapt_for_delivery(df)

# Save to new CSV
df_delivery.to_csv("DepartureDestinationTrip.csv", index=False)
