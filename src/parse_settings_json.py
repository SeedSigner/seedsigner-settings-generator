import json
from jinja2 import Template



print("Generating static index.html")

# Load the settings_definition.json
with open("settings_definition.json", 'r') as json_file:
    settings_json = json.load(json_file)

# Load the Jinja2 template
with open("index.jinja", 'r') as template_file:
    template = Template(template_file.read())

# Prep the template data from settings_json
template_data = {
    "settings_entries": [],
}

for entry in settings_json.get("settings_entries"):
    print(entry["attr_name"])
    if entry["visibility"] == "hidden":
        print(f"""Skipping hidden setting '{entry["attr_name"]}'""")
        continue
    if entry.get("abbreviated_name"):
        entry["attr_name"] = entry["abbreviated_name"]
    template_data["settings_entries"].append(entry)



# Render the final static index.html
final_html = template.render(template_data)
with open("index.html", 'w') as html_file:
    html_file.write(final_html)
