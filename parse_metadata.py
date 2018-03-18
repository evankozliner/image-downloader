import os
import csv
import json

METADATA_PATH = 'ISIC-images/'
METADATA_NAME = 'metadata.csv'

def main():
    with open(METADATA_NAME, 'w+') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'name', 'benign_malignant', 'age', 'sex', 'shape_x', 'shape_y'])
        for metadata_filename in os.listdir(METADATA_PATH):
            if not 'json' in metadata_filename: 
                continue

            metadata_path = METADATA_PATH + metadata_filename
            with open(metadata_path, 'r') as f:
                metadata = json.loads(f.read())

            meta = metadata['meta']
            aquisition = meta['acquisition']
            clinical = meta['clinical']
            writer.writerow([
                    metadata['_id'],
                    metadata['name'],
                    0 if clinical['benign_malignant'] == 'benign' else 1,
                    clinical['age_approx'],
                    clinical['sex'],
                    aquisition['pixelsX'],
                    aquisition['pixelsY']
                    ])
            
if __name__ == '__main__':
    main()
