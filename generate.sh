#!/bin/bash
cd src

# generate the settings_definition.json from SettingsDefinition in SeedSigner
python3 seedsigner/src/seedsigner/models/settings_definition.py

# parse the json and generate the static index.html
python3 parse_settings_json.py

mv index.html ../docs/.
