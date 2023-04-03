# Python JSON Parser

# Import dependencies ==========================================================
import json
from ISIS3_Enums import ISIS_DAGS
import ISIS3_Mods

# Declare variables ============================================================
JSON_DATA = ''

# Declare functions ============================================================
"""
Function    : read_file
Description : Opens and reads a given file using the Python JSON parser/handler.
Inputs      : filename (string)
              - String representation of file name to be opened, including ext
Outputs     : json_data (returned)
              - Returns JSON object containing file data.
"""
def read_file(filename):
    file = open(filename)

    data = json.load(file)

    file.close()

    JSON_DATA = data
    return data


"""
Function    : parse_data
Description : Parses read JSON data into lists.
Inputs      : data ( dict )
              - Dictionary representation of a JSON file
Outputs     : parsed_data (list)
              - Parsed list of data / recipes.
"""
def parse_data(data):
    parsed_data = []

    # For recipe in file
    for key in data:
        if( isinstance(data[key], dict) ):
            recipeName = key
            recipe = []
            recipe.append(recipeName)

            # For module in recipe
            for keytwo in data[ recipeName ]:
                if( isinstance(data[recipeName][keytwo], dict) ):

                    # For module name in module
                    for keythree in data[recipeName][keytwo]:
                        module = getattr(ISIS_DAGS, keythree.replace('.', '_') ).value
                        new_dag = getattr(ISIS3_Mods, keythree.replace('.','_'))

                        # For variable in module name
                        for keyfour in data[recipeName][keytwo][keythree]:
                            value =  data[recipeName][keytwo][keythree][keyfour]
                            setattr(new_dag, keyfour, value)

                        recipe.append( (module, new_dag) )

            parsed_data.append( recipe )

    # Returns a list of lists, where each sublist is a complete recipe
    return( parsed_data )

data = read_file('example_recipes.json')
parse_data(data)
