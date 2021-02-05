import json

# Open element data as JSON file
# https: // github.com/Bowserinator/Periodic-Table-JSON/edit/master/PeriodicTableJSON.json
with open('data/elements.json') as f:
  element_data = json.load(f)['elements']

symbols = []
keys = []
element_data_formatted = {}

for el in element_data:
    symbol = el.get('symbol')
    el_formatted = {
        'symbol': symbol,
        'name': el.get('name'),
        'atomicMass': el.get('atomic_mass'),
        'xpos': el.get('xpos'),
        'ypos': el.get('ypos'),
        'period': el.get('period'),
        'density': el.get('density')
    }
    # Store the unformatted symbol
    symbols.append(symbol)
    # Store the formatted key
    el_key = symbol.lower()
    keys.append(el_key)
    element_data_formatted[el_key] = el_formatted

# Include keys, symbols, and formatted element data
output = {
    'keys': keys,
    'symbols': symbols,
    'elements': element_data_formatted
}
with open('data/out/elementData.json', 'w') as json_file:
    json.dump(output, json_file)
