# SeedSigner SettingsQR Generator


## Quick Start
The SettingsQR Generator is just a bunch of static files that you can run in two different ways:

* Access the online hosted version at https://kdmukai.github.io/seedsigner-settings-generator/
* Or download the files yourself and run it in a completely offline web browser

### Download and run offline
If you prefer the offline method, get a local copy of this github repo by clicking on the green "code" button.

* If you have `git` installed, you can `git clone https://github.com/kdmukai/seedsigner-settings-generator.git`
* Or you can choose the "Download Zip" option

At this point you can disconnect your computer from the internet (or transfer the project files over to your air-gapped computer).

To run the SettingsQR Generator, just double-click on docs/index.html.


---

## Developers

If you need to update the SettingsQR Generator with settings changes in your SeedSigner branch, you'll need to make sure that the `.gitmodules` is pointing to the right repo and target branch:
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
