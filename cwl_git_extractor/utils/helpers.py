import os
import argparse
from ruamel import yaml


def load_yaml(imput_file):
    with open(imput_file, "r") as input_stream:
        data = yaml.round_trip_load(input_stream, preserve_quotes=True)
    return data


def normalize_args(args, skip_list=[]):
    normalized_args = {}
    for key, value in args.__dict__.items():
        if value and key not in skip_list:
            normalized_args[key] = os.path.normpath(os.path.join(os.getcwd(), value))
        else:
            normalized_args[key]=value
    return argparse.Namespace(**normalized_args)


def export_to_file (output_filename, data):
    with open(output_filename, 'w') as output_file:
        output_file.write(data)