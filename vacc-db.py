import sqlalchemy as db
import pandas as pd
from pathlib import Path

# Define paths to data sources
p1 = Path(__file__).parent / 'data/germany_vaccinations_by_state.tsv'
p2 = Path(__file__).parent / 'data/germany_deliveries_timeseries_v2.tsv'
p3 = Path(__file__).parent / 'data/germany_vaccinations_timeseries_v2.tsv'

# read data and create dataframes
vacc_by_state = pd.read_csv(p1, sep='\t')
deliveries = pd.read_csv(p2, sep='\t')
timeseries = pd.read_csv(p3, sep='\t')

# create sqlite database named vacciNation and connect to database
engine = db.create_engine('sqlite:///vacciNation.db', echo=True)
sqlite_connection = engine.connect()
# create tables in db corresponding to the dataframes
sqlite_table1 = 'vacc_by_state'
vacc_by_state.to_sql(sqlite_table1, sqlite_connection, if_exists='replace')

sqlite_table2 = 'deliveries'
deliveries.to_sql(sqlite_table2, sqlite_connection, if_exists='replace')

sqlite_table3 = 'timeseries'
timeseries.to_sql(sqlite_table3, sqlite_connection, if_exists='replace')

# close the db connection
sqlite_connection.close()


# @TODO:
# write class to read and handle the data,
# visualize data with matplotlib
# vaccination of risk group, daily comparison -> create new table
# Vergleich Bundesländer (immer tagesaktuell?)
# Abgleich Gesamtzahl Länder und Deutschland (Datum tagesaktuell? ->
# Aktuelles Datum mit datetime importieren -> gemeinsamer key der neu kreierten Tabelle)
