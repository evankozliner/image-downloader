require 'json'
require 'csv'

DATA_FILE = 'metadata.csv'

# You can download the metadata on the ISIC website https://isic-archive.com/#images

# move all images into same directory, then run the script :)
# `mv */* .`

CSV.open(DATA_FILE, 'wb') do |csv|
  csv << ['id', 'malignant', 'age', 'sex', 'name']

  `ls ISIC-images`.split('\n').select {|f|
    f.include? 'json'
  }.map { |f|
    metadata = JSON.parse File.read(f)
    male_female = metadata['meta']['clinical']['sex'] == 'female' ? 0 : 1
  
    csv << [metadata['_id'], 
            metadata['meta']['clinical']['malignant'], 
            metadata['meta']['clinical']['age_approx'], 
            male_female,
            metadata['name']]
  }
end
