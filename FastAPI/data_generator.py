import pandas as pd
from faker import Faker
import random

fake = Faker()

num_records = 500000

unique_locations = set()
while len(unique_locations) < 100:
    unique_locations.add(fake.city())

unique_locations = list(unique_locations)

ids = []
names = []
locations = []

for i in range(num_records):
    ids.append(i + 1)
    names.append(fake.name())
    locations.append(random.choice(unique_locations))

df = pd.DataFrame({
    'ID': ids,
    'Candidate Name': names,
    'Location': locations
})

df.to_csv('candidates.csv', index=False)

print(f'Excel of {num_records} generated!')












