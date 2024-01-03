#!/bin/sh
echo installing modules
pip3 install openfoodfacts microdot evdev

echo Updating autorun.sh
cp ./autolaunch/autorun.sh /opt

echo Enabling autorun.sh
chmod +x /opt/autorun.sh

echo Enabling launch.sh
chmod +x launch.sh

echo #########################
echo Reboot to apply changes !
echo #########################