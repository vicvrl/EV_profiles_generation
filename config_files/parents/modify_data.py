import pandas as pd

# Load the CSV
df = pd.read_csv("../commuter/DepartureDestinationTrip.csv")

# Function to adapt for parents
def adapt_for_parents(df):
    df_new = df.copy()

    # Weekday rows only
    weekdays = df_new['days'] == 'weekdays'

    # Define morning and afternoon escort times (in hours)
    morning_hours = [7, 7.5, 8, 8.5]     # e.g., school drop-off
    afternoon_hours = [15, 15.5, 16, 16.5, 17, 17.5]  # e.g., school pick-up

    # Apply escort for these times
    df_new.loc[weekdays & df_new['time'].isin(morning_hours + afternoon_hours), 'escort'] = 0.05

    # Increase shopping probability slightly for all weekdays
    df_new.loc[weekdays, 'shopping'] = df_new.loc[weekdays, 'shopping'] * 1.5

    return df_new

# Adapt the CSV
df_parents = adapt_for_parents(df)

# Save to new CSV
df_parents.to_csv("DepartureDestinationTrip.csv", index=False)

