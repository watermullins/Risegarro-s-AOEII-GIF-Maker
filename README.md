# Risegarro's AOEII GIF Maker

## Setup
* install python
* download unitgifmaker.py

## Extract PNGs from SLDs
* locate target SLD file in c:\SteamLibrary\steamapps\common\AoE2DE\resources\_common\drs\graphics
* drag into WAIFor's SLD Extractor hosted by Greg Stein https://ageofnotes.com/sld-extractor-online-aoe2/
* download extacted files
* unzip folder

## Generate the GIFs
* place the PNGs in a folder called frames in the script's directory (see directory map below)
* running the script will place the 16 generated GIFs in the parent directory

### Directory Structure
```map
gif/
├── unitgifmaker.py
├── frames/
│   ├── frame01.png
│   ├── frame02.png
│   └── ...
└── unitgifmaker_0.gif
