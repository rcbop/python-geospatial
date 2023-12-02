#!/usr/bin/env bash
curl -X POST \
    -F "image=@//home/rcbop/git/python-geospatial/S2L2A_2022-06-09.tiff" \
    -F "resolution=100" http://127.0.0.1:8000/image/thumbnail \
    --output thumbnail.png
