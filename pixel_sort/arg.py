
import pathlib
import argparse

def get_args():
    arg = argparse.ArgumentParser()
    arg.add_argument("-i", "--image", required=True)

    return arg
