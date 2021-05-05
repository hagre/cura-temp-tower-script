# cura-temp-tower-script

# Milimeter

This script is based on the script written by Okke Formsma here https://github.com/okke-formsma/cura-temp-tower-script .

I have modified the regex to find negative X and Y values for my Delata Printer.
Some more smal improvements are in progress,...

Renamed the .py file to TempTowerMM.py (for the mm version)

Copy TempTower.py into your cura directory like the following;

C:\Program Files\Ultimaker Cura <version>\plugins\PostProcessingPlugin\scripts

This script is based on some variations I found on Thingiverse.

Five settings are available;

1. Start Height
2. Start Temperature
3. Height Increment
4. Temperature Increment
5. Debug Output 1 or 0 (On or Off - default)

for Example:
So, if you have a tower with a base layer 1.5mm thick and goes down from 260* (base) to 220* (top) in steps of 5* every 10mm, set:

* Start height: 1.5 mm
* Start Temperature 260 °C
* Height Increment 10.0 mm
* Temperature Increment -5 °C


I am using this https://www.thingiverse.com/thing:4149643 temp tower (PLA) with the following settings:
* Start height: 1.1 mm (including -> The first layer with the calculated temp)
* Start Temperature 190 °C
* Height Increment 10.0 mm
* Temperature Increment 5 °C
* Debug 0





# AND LAYER

This additional script is inspired by the script https://github.com/Haruko/cura-temp-tower-script modified by Haruko (fork of the orginal script) and the already included script https://github.com/Ultimaker/Cura/blob/master/plugins/PostProcessingPlugin/scripts/DisplayFilenameAndLayerOnLCD.py .

Renamed the .py file to TempTowerLayer.py (for the Layer version)

Five settings are available;

1. Start Layer
2. Layer Increment
3. Start Temperature
4. Temperature Increment
5. Debug Output
