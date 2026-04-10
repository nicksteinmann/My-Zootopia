import json


def load_data(file_path):
    """ Loads a JSON file """
    try:
        with open(file_path, "r") as handle:
            return json.load(handle)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []


def serialize_animal(animal):
    """Converts one animal object into an HTML list item."""
    output = []

    output.append('<li class="cards__item">')

    if "name" in animal:
        output.append(f'    <div class="card__title">{animal["name"]}</div>')

    output.append('    <p class="card__text">')

    if "characteristics" in animal and "diet" in animal["characteristics"]:
        output.append(f"<strong>Diet:</strong> {animal['characteristics']['diet']}<br/>")

    if "locations" in animal and len(animal["locations"]) > 0:
        output.append(f"<strong>Location:</strong> {animal['locations'][0]}<br/>")

    if "characteristics" in animal and "type" in animal["characteristics"]:
        output.append(f"<strong>Type:</strong> {animal['characteristics']['type']}<br/>")

    output.append('</p>')
    output.append('</li>')

    return "\n".join(output)


def main():
    # Load animal data
    animals_data = load_data('animals_data.json')

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


if __name__ == "__main__":
    main()
