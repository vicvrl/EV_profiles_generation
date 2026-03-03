import pandas as pd

# Load the CSV
df = pd.read_csv("../commuter/DepartureDestinationTrip.csv")


# Function to adapt for remote workers
def adapt_for_remote(df):
    df_new = df.copy()

    # Weekday rows only
    weekdays = df_new['days'] == 'weekdays'

    # Reduce workplace time (e.g., 70% reduction)
    df_new.loc[weekdays, 'workplace'] = df_new.loc[weekdays, 'workplace'] * 0.3

    # Increase home time (e.g., 50% increase)
    df_new.loc[weekdays, 'home'] = df_new.loc[weekdays, 'home'] * 1.5

    return df_new


# Adapt the CSV
df_remote = adapt_for_remote(df)

# Save to new CSV
df_remote.to_csv("DepartureDestinationTrip.csv", index=False)
