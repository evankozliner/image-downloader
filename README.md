# image-downloader

* This repo is intended to be used with the [ISIC archive metadata](https://isic-archive.com/). 

It's mostly meant for my personal use, but if you're interested in using it you'll need to do the following:
1. Download the ISIC metadata off the above website, run the `python parse_metadata.py` script to combine all of the metadata into a single CSV file (you can see mine in `metadata.csv`)
2. Run `python build_dataset.py` to create a final dataset CSV (`data.csv`) with a 60/40 benign malignant split
3. Finally from the location you want to download the images to run `python download_images.py` to download the images from the ISIC archive 

[instance AMI matrix](https://aws.amazon.com/amazon-linux-ami/instance-type-matrix/)

