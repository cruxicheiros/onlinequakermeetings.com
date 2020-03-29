#!/bin/sh
echo "Installing the required modules"

pip install -r requirements.txt
sudo apt-get install moreutils

echo "Commencing the freezening!"

python freezer.py

echo "Freezening complete!"

echo "Minifying HTML"

for f in ./application/build/*.html ; do
    echo " - Minifying $f"
    htmlmin "$f" | sponge "$f"
done

echo "html minified"