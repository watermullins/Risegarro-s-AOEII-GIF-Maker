![gif](https://github.com/watermullins/Risegarro-s-AOEII-GIF-Maker/blob/main/gifs/knight_walk_2.gif)![gif](https://github.com/watermullins/Risegarro-s-AOEII-GIF-Maker/blob/main/gifs/cavalier_walk_2.gif)![gif](https://github.com/watermullins/Risegarro-s-AOEII-GIF-Maker/blob/main/gifs/paladin_walk_2.gif)
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
* place the extracted PNGs in a folder called frames in the script's directory (see directory map below)
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
```

#### Credit
This project was started from a script by Risegarro, one of the aoe wiki admins.
