#! /usr/bin/env python3
import sys
import argparse
from git import Repo
from cwl_git_extractor.utils.helpers import normalize_args, export_to_file


def get_parser():
    parser = argparse.ArgumentParser(description='CWL Git Extractor', add_help=True)
    parser.add_argument("-r", "--repo",     help="Path to Git repository", required=True)
    parser.add_argument("-f", "--file",     help="Relative path to the cwl file", required=True)
    parser.add_argument("-s", "--sha",      help="SHA hash of git commit",        required=True)
    parser.add_argument("-o", "--output",   help="Output file name",              default="workflow.cwl")
    return parser


def main(argsl=None):
    if argsl is None:
        argsl = sys.argv[1:]
    args,_ = get_parser().parse_known_args(argsl)
    args = normalize_args(args, ["file", "sha"])
    args.file = args.file.lstrip("/")

    repository = Repo(args.repo)
    file_content = repository.git.show('{}:{}'.format(args.sha, args.file))
    export_to_file(args.output, file_content)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))