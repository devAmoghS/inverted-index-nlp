from inverted_index.Index import index

# TOP10 Dire straits
index.add('Industrial Disease')
index.add('Private Investigations')
index.add('So Far Away')
index.add('Twisting by the Pool')
index.add('Skateaway')
index.add('Walk of Life')
index.add('Romeo and Juliet')
index.add('Tunnel of Love')
index.add('Money for Nothing')
index.add('Sultans of Swing')

# TOP10 Led Zeppelin
index.add('Stairway To Heaven')
index.add('Kashmir')
index.add('Achilles Last Stand')
index.add('Whole Lotta Love')
index.add('Immigrant Song')
index.add('Black Dog')
index.add('When The Levee Breaks')
index.add('Since I\'ve Been Lovin\' You')
index.add('Since I\'ve Been Loving You')
index.add('Over the Hills and Far Away')
index.add('Dazed and Confused')

# Let's make some queries:

print(index.lookup('loves'))
# ['Tunnel of Love', 'Whole Lotta Love', "Since I've Been Loving You"]

print(index.lookup('loved'))
# ['Tunnel of Love', 'Whole Lotta Love', "Since I've Been Loving You"]

print(index.lookup('daze'))
# ['Dazed and Confused']

print(index.lookup('confusion'))
# ['Dazed and Confused']
