import glob
import os
import sys


def print_usage():
    print("Usage:")
    print("  markdown-sitegen <DIRECTORY>: generate website from markdown in directory")


def cli_entry_point():
    if len(sys.argv) == 2:
        gen_dir = sys.argv[1]
        if os.path.exists(gen_dir) and os.path.isdir(gen_dir):
            files_to_render = []
            for root, dirs, files in os.walk(gen_dir):
                for filename in files:
                    if filename.lower().endswith('.md'):
                        files_to_render.append(filename)
            print(files_to_render, len(files_to_render))
        else:
            print("Error: not a directory - %s" % gen_dir)
    else:
        print_usage()
