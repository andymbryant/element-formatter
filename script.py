import json
from uuid import uuid4

# Open element data as JSON file
# https: // github.com/Bowserinator/Periodic-Table-JSON/edit/master/PeriodicTableJSON.json
with open('data/elements.json') as f:
  element_data = json.load(f)['elements']

symbols = []
keys = []
element_data_formatted = {}

for el in element_data:
    symbol = el.get('symbol')
    key = symbol.lower()
    el_formatted = {
        # Add an ID in case these ever need to be tracked during iteration or render
        'id': str(uuid4())[:8],
        'symbol': symbol,
        'objKey': key,
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
    keys.append(key)
    element_data_formatted[key] = el_formatted

# Include keys, symbols, and formatted element data
output = {
    'keys': keys,
    'symbols': symbols,
    'elements': element_data_formatted
}
with open('data/out/elementData.json', 'w') as json_file:
    json.dump(output, json_file)
