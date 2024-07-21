import os
import sys
import glob
import re

def main():
    args = sys.argv[1:]
    directory = 'Log'
    #pattern = '^.*csv$'
    #pattern = args[0]
    patterns = args
    #pattern = '.*'
    csv_files = get_files_matching_pattern(directory, patterns)
    print("csv files: ")
    print(csv_files)


def get_files_matching_pattern(directory, patterns):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    #matching_files = [f for f in files if re.match(pattern, f)]
    matching_files = [f for f in files if all(re.match(pattern, f) for pattern in patterns)]
    
    return matching_files


if __name__ == '__main__':
    main()
