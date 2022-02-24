# Developers

## Overview
The SettingsQR Generator pulls the `SettingsDefinition` class from the main SeedSigner repo and outputs the settings options as json. A python script in this repo then reads that settings json in and injects the settings data into a Jinja2 template that renders the final static `index.html`.


## Set up a local copy of this repo
To make deeper changes to the SettingsQR Generator, you'll want to clone the repo with the `--recursive` option so that it includes the nested SeedSigner core repo as well:
```
git clone --recursive https://github.com/kdmukai/seedsigner-settings-generator.git
```

<details>
    <summary>Note: If you don't include `--recursive`...</summary>
    You'll need to make two follow-up calls:

    ```
    git submodule init
    git submodule update --remote
    ```
</details>

You should now have a complete copy of this repo AND the SeedSigner repo in your `src/` subdir.


## Local dev environment
We rely on a python script that uses a Jinja2 template to generate the static `index.html`. So you'll need to set up a new python3 `virtualenv` (plenty of python3 virtualenv guides you can follow) and install the Jinja2 dependencies:
```
pip install -r requirements.txt
```


## Updating changes from `SettingsDefinition` in the SeedSigner repo
Any time a change is made in `SettingsDefinition` in SeedSigner, you'll need to regenerate the SettingsQR Generator's `index.html` in order to see the latest settings options changes.


## Targeting the SeedSigner submodule to your own repo or branch
If you're changing the settings options in your own SeedSigner fork/branch, you'll need to make sure that `.gitmodules` in this project's root dir is pointing to your repo and your target branch. Just change the `url` and `branch` as needed:
```
[submodule "src/seedsigner"]
	path = src/seedsigner
	url = https://github.com/kdmukai/seedsigner.git
	branch = settings_definition
```

Once your changes are made, you need to tell `git` to pull the new repo or branch:
```
git submodule update --remote
```

And then any time there are further changes in the `SettingsDefinition` in your target fork/branch, you'll need to repeat the above `update` call to pull in those changes.


## Generate updated `index.html`
With your target `SettingsDefinition` and your virtualenv set up, you can now just run:
```
./generate.sh
```

The script tells `SettingsDefinition` to extract itself to json and then calls the `src/parse_settings_json.py` python script to read the settings in and generate the final static `index.html` that gets written to the `docs/` dir.

*Note: why are the static web files in the `docs/` subdir (a better place would be something like a `www/` subdir). A limitation in Github Pages only lets us host the static website from either the repo root or from a hard-coded `docs/` subdir.*
