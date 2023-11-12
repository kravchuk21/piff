#!/usr/bin/env python3

import sys

def read_entire_file(file_path):
    with open(file_path, "r") as f:
        return f.read()

if __name__ == "__main__":
    program = sys.argv[0]
    if len(sys.argv) < 3:
        print(f"Usage: {program} <file1> <file2>")
        print(f"ERROR: no files to compare ")
        exit(1)
    lines1 = read_entire_file(sys.argv[1]).splitlines()
    lines2 = read_entire_file(sys.argv[2]).splitlines()
