# hpe3par-cinder-id-parser

Introduction:

This is a small python code snippet to translate cinder volume ID into virtual volume as seen in hpe3par. It is useful while debugging Cinder volume issues while using HPE3PAR backend Cinder driver. Using this utility a user can see the corresponding virtual volume in HPE3PAR storage system.

Usage:

Copy this python utility (hpe3par-cinder-id-parser.py) on a system with python runtime installed.
naviage to the loaction you have saved this file: hpe3par-cinder-id-parser.py.
On the command prompt ($) execute:

$python hpe3par-cinder-id-parser.py

This tool converts Cinder Volume ID ($cinder list) to HPE3PARVirtual Volume Name ($showvv).
Enter Cinder Volume ID: 5308f37c-6142-4824-9433-9ae69fc99246
Mapping HPE3PAR Virtual Volume Name: osv-UwjzfGFCSCSUM5rmn8mSRg
