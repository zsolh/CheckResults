import os
import glob
import re

def get_files_matching_pattern(directory, pattern):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    matching_files = [f for f in files if re.match(pattern, f)]
    
    return matching_files


if __name__ == '__main__':
    directory = 'Log'
    pattern = '^.*csv$'
    #pattern = '.*'
    csv_files = get_files_matching_pattern(directory, pattern)
    print("csv files: ")
    print(csv_files)
