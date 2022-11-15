from jschon import create_catalog, JSON, JSONSchema, URI, LocalSource
import pathlib
import pprint
import sys

# Loads the schemas in jschon and validates the file passed on the command line.
# Example: 
#  > python3 -m venv .venv
#  > . .venv/bin/activate
#  > pip install -r requirements.txt
#  > python validate.py example.tree

mydir = pathlib.Path(__file__).parent 

catalog = create_catalog('2020-12')
# Any call to a schema in our namespace gets mapped to the Schema folder from the local system
catalog.add_uri_source(URI('https://my.domain.com/rev00/'), LocalSource(mydir, suffix='.schema.json'))

tree_schema = catalog.get_schema(URI('https://my.domain.com/rev00/tree'))
data = JSON.loadf(mydir / sys.argv[1])

result = tree_schema.evaluate(data)
if result.valid:
    pprint.pp(result.output('flag'))
else:
    pprint.pp(result.output('basic'))
