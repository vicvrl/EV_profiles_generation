import pandas as pd

# Load original CSV
df = pd.read_csv("../commuter/DepartureDestinationTrip.csv")

def adapt_for_unemployed(df):
    df_new = df.copy()

    # Weekdays: unemployed stays mostly at home
    weekdays = df_new['days'] == 'weekdays'

    # Remove workplace entirely
    df_new.loc[weekdays, 'workplace'] = 0

    # Strong increase of home probability
    df_new.loc[weekdays, 'home'] *= 2.0   # strong weight for home

    # Slight increase in leisure + errands
    df_new.loc[weekdays, 'errands'] *= 1.2
    df_new.loc[weekdays, 'leisure'] *= 1.3
    df_new.loc[weekdays, 'shopping'] *= 1.1

    # Weekend: more leisure
    weekend = df_new['days'] == 'weekend'
    df_new.loc[weekend, 'home'] *= 1.5
    df_new.loc[weekend, 'workplace'] = 0
    df_new.loc[weekend, 'leisure'] *= 1.4
    df_new.loc[weekend, 'errands'] *= 1.1

    # Return modified dataset without normalization
    return df_new

# Apply transformation
df_unemployed = adapt_for_unemployed(df)

# Save
df_unemployed.to_csv("DepartureDestinationTrip.csv", index=False)
