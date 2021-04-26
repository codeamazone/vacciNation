from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


p = Path(__file__).parent / 'data/germany_vaccinations_by_state.tsv'
print(p.exists())

vacc_by_state = pd.read_csv(p, sep='\t')
print(vacc_by_state.head())

# Get total vaccinations in Berlin
for row in vacc_by_state.iterrows():
    pos = row[0]
    data = row[1]
    if data[0] == 'DE-BE':
        print(f'Total vaccinations in Berlin: {data[1]}')

# Get Berlin dataset
# vacc_berlin = vacc_by_state[vacc_by_state['code'] == 'DE-BE']
# print(vacc_berlin)

states = ['Baden-Württhemberg', 'Bayern', 'Berlin', 'Brandenburg', 'Bremen', 'Hamburg', 'Hessen', 'Mecklenburg-Vorp.',
          'Niedersachsen', 'Nordrhein-Westf.', 'Rheinland-Pfalz', 'Saarland', 'Sachsen', 'Sachsen-Anhalt', 'Schleswig-Holstein', 'Thüringen']
vacc_by_state['states'] = states

vacc_by_state.plot(x='states', kind='bar')
plt.xlabel('Bundesländer')
plt.ylabel('Impfungen')
plt.xticks(rotation=25, ha='right', size='small')
plt.show()
