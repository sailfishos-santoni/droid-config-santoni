# These and other macros are documented in ../droid-configs-device/droid-configs.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device santoni
%define vendor xiaomi

%define vendor_pretty Xiaomi
%define device_pretty Redmi 4X

# Community HW adaptations need this
%define community_adaptation 1

# Pixel ratio 1.0 was originally jolla phone with 245ppi, and the devices
# should roughly have their ppi compared to that. Large displays can use
# bigger ratio if seen fit. Values are with 0.25 increments.
%define pixel_ratio 1.0

%include droid-configs-device/droid-configs.inc
%include patterns/patterns-sailfish-device-adaptation-santoni.inc
%include patterns/patterns-sailfish-device-configuration-santoni.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

