import pandas as pd
import multiprocessing
import os
import urllib2
from multiprocessing.dummy import Pool as ThreadsPool

from functools import partial
from build_dataset import FINAL_DATASET_NAME

ISIC_ENDPOINT = 'https://isic-archive.com/api/v1/image/{}/download'
OUTPUT_M = '~/images/malignant'
OUTPUT_B = '~/images/benign'
OUT_PATH = '~/out/{}/{}'

def main():
    metadata = pd.read_csv(FINAL_DATASET_NAME)
    ids = metadata['id'][0:5]
    malignancy = metadata['benign_malignant'][0:5]

    partial_save = partial(download_image)
    pool = ThreadsPool(4)
    pool.map(partial_save, zip(ids, malignancy))
    pool.close()
    pool.join()

def download_image(datum):
    img_id, benign_mal = datum
    print ISIC_ENDPOINT.format(img_id)
    img = urllib2.urlopen(ISIC_ENDPOINT.format(img_id))
    subdir = 'benign' if benign_mal == 0  else 'malignant'

    with open(OUT_PATH.format(subdir, img_id), 'w') as f:
        f.write(img.read())

if __name__ == "__main__":
    main()
