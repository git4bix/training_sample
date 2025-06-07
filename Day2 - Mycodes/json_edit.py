#import json
"""
data = [
        {'Name': 'Alice', 'Age': 30, 'Occupation': 'Engineer'},
        {'Name': 'Bob', 'Age': 25, 'Occupation': 'Designer'},
        ]

with open('people.json', 'w') as file:
        json.dump(data, file, indent=4)
"""
from xml.etree.ElementTree import indent

"""
data = {
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}

with open('people.json', 'w') as file:
        json.dump(data, file, indent=4)

"""

import json
with open('people.json', 'r') as file:
        data = json.load(file)

print(type(data))