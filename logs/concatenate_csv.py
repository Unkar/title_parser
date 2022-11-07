import os
import glob


os.chdir("logs")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
print(all_filenames)

#combine all files in the list
for i in all_filenames:
    with open(i, 'r') as f:
        with open("combined_csv.csv", "a") as f1:
            for line in f:
                f1.write(line)