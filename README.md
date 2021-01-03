# cura-temp-tower-script

This script is based on the script written by Okke Formsma here https://github.com/okke-formsma/cura-temp-tower-script
I have modified the regex to find negative X and Y values for my Delata Printer.
Some more smal improvements are in progress,...

Renamed the .py file to TempTowerMM.py (for the mm version)

Copy TempTower.py into your cura directory like the following;

C:\Program Files\Ultimaker Cura 4.8\plugins\PostProcessingPlugin\scripts

This script is based on some variations I found on Thingiverse.

Four settings are available;

1. Start Height
2. Start Temperature
3. Height Increment
4. Temperature Increment

So, if you have a tower with a base layer 1.5mm thick and goes down from 260* (base) to 220* (top) in steps of 5* every 10mm, set:

* Start height: 1.5 mm
* Start Temperature 260 *C
* Height Increment 10.0 mm
* Temperature Increment -5 *C
