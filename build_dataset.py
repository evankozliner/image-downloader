import pandas as pd
from parse_metadata import METADATA_NAME

FINAL_DATASET_NAME = 'data.csv'

# We're getting all the malignant images because they're in short supply, and an equal number of benign
# images with the caveat that we'll take benign images from older patients first because they're in
# shorter supply. 
def main():
    metadata = pd.read_csv(METADATA_NAME)
    malignants = metadata[metadata['benign_malignant'] == 1]
    benigns = metadata[metadata['benign_malignant'] == 0]

    # we want a 60/40 split of benign/malignant, this just solves for the num of benigns we're including
    total_imgs = 5.0 / 2.0 * len(malignants)
    num_ben = int(0.6 * total_imgs)

    benigns_sample = benigns.sample(n = num_ben)
    shuffled_dataset = pd.concat([benigns_sample, malignants]).sample(frac=1, random_state = 1)

    shuffled_dataset.to_csv(FINAL_DATASET_NAME)

if __name__ == '__main__':
    main()
