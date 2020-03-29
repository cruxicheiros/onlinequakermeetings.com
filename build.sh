#!/bin/sh
echo "Installing the required modules"

pip install -r requirements.txt
sudo apt-get install moreutils

echo "Commencing the freezening!"

python freezer.py

echo "Freezening complete!"

echo "Minifying HTML"

FILES="$(find ./application/build/ -type f -name '*.html')"

for f in $FILES ; do
    echo " - Minifying $f"
    htmlmin "$f" | sponge "$f"
done

echo "html minified"