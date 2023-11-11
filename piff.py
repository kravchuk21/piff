#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    program = sys.argv[0]
    if len(sys.argv) < 3:
        print(f"Usage: {program} <file1> <file2>")
        print(f"ERROR: no files to compare ")
        exit(1)
    file_path1 = sys.argv[1]
    file_path2 = sys.argv[2]
    print(f"File1: {file_path1}")
    print(f"File2: {file_path2}")
