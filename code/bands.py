headline = input('Headline: ')
band = input('Band: ')
bands = []

while band:
    bands.append(band)
    band = input('Band: ')

bands.sort()

print(headline)
for b in bands:
    print(b)
