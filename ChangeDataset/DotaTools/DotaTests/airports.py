import os

path = 'DOTA-v2.0_train'
first_airport = None
i = 0
airports = 0

for file in os.listdir(path):
    with open(os.path.join(path,file)) as f:
        df = f.read()
        if df != '':
            name = df.split(' ')[8]
        if name == 'airport':
            airports += 1
            file_id = file.split('.')[0][1:]
            if first_airport is None or first_airport > int(file_id):
                first_airport = int(file_id)
            #print(f'{file_id} {name}')
    i+=1


print(f'First Airport {first_airport}')
print(f'Airports number = {airports}')