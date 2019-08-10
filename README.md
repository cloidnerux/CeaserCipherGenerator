# CeaserCipherGenerator

A script to generate ceasar like cipher text and a printable cipher card

Ceasar cipher work by shifting the letters a certain amount, also called ROTX. If X is 4 A becomes E, B becomes F, Z becomes D and so on. 
To make this shift easier one can build a shift disk. These are two disk ontop of each other, both with the alphabet. You can turn one disk a certain amount to the other to achieve the desired shift and can now translate between them.

This script uses this idea and expands a little on it. Instead of using just uppercase letters from A - Z an arbitrary selection of letters can be used. Further a scramble algorithm is in place, so the second "disk" is not only shifted, but the letters are randomly assigned, so the code gets a little bit "stronger". You can disable this scrambling when youjust want to shift the letters.

cipher.py is the scirpt to run. It will read the text in "normal_text.txt" and will cipher it using the settings made. It will generate a PDF with the encryption disk you can print, cut-out and make your cipher-disk. It also generates the scrambled text as a text-file and also a PDF with field below each letter to allow for easier decryption.

This is not a save cipher but rather intended for gifts and challenges, geo-chaching or education.
