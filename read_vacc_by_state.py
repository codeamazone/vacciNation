from pathlib import Path
import pandas as pd


p = Path(__file__).parent / 'src/germany_vaccinations_by_state.tsv'
print(p.exists())

vacc_by_state = pd.read_csv(p, sep='\t')

# Get total vaccinations in Berlin
for row in vacc_by_state.iterrows():
    pos = row[0]
    data = row[1]
    if data[0] == 'DE-BE':
        print(f'Total vaccinations in Berlin: {data[1]}')

# Get Berlin dataset
vacc_berlin = vacc_by_state[vacc_by_state['code'] == 'DE-BE']
print(vacc_berlin)
