for f in *.png; do convert $f -crop 64x64+0+0 -interpolate nearest -filter point -resize 50% resized/$f; done
