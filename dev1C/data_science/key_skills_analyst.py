
import pandas as pd

df = pd.read_csv('dev1C_vacancies.csv')
df_skills = df['skills']
df['published_at'] = df['published_at'].apply(lambda x: int(str(x)[:4]))
years = df['published_at'].unique()
all_skills = {}
for year in years:
    all_skills[year] = []

for index, row in df.iterrows():
    skills = str(row['skills']).split('\n')
    year = int(str(row['published_at'])[:4])
    if skills[0] != 'nan':
        all_skills[year].extend(skills)

year_frequency = dict()
for year in all_skills.keys():
    year_frequency[year] = dict()

for year in all_skills.keys():
    for skill in all_skills[year]:
        try:
            skill = str(skill).replace('\r', '')
            year_frequency[year][skill] += 1
        except:
            year_frequency[year][skill] = 1

# noinspection PyTypeChecker
for year in year_frequency.keys():
    year_frequency[year] = dict(sorted(year_frequency[year].items(), key=lambda x: x[1], reverse=True))
    year_frequency[year] = list(year_frequency[year].keys())[:10]
print('Год, Наиболее высокочастотные навыки')
for year in year_frequency.keys():
    if len(year_frequency[year]) > 0:
        print(f'{year}, {year_frequency[year]}')




