import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


# Load animal data
animals_data = load_data('animals_data.json')


def serialize_animal(animal):
    """Converts one animal object into an HTML list item."""
    output = ""

    output += '<li class="cards__item">\n'

    if "name" in animal:
        output += f'    <div class="card__title">{animal["name"]}</div>\n'

    output += '    <p class="card__text">\n'

    if "characteristics" in animal and "diet" in animal["characteristics"]:
        output += f"<strong>Diet:</strong> {animal['characteristics']['diet']}<br/>\n"

    if "locations" in animal and len(animal["locations"]) > 0:
        output += f"<strong>Location:</strong> {animal['locations'][0]}<br/>\n"

    if "characteristics" in animal and "type" in animal["characteristics"]:
        output += f"<strong>Type:</strong> {animal['characteristics']['type']}<br/>\n"

    output += '</p>\n'
    output += '</li>\n'

    return output


# Build output string instead of printing
output = ""

for animal in animals_data:
    output += serialize_animal(animal)

# Read HTML template
with open("animals_template.html", "r") as file:
    html_template = file.read()

# Replace placeholder with data
html_content = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

# Write new HTML file
with open("animals.html", "w") as file:
    file.write(html_content)
