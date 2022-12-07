#!python

import argparse
import os.path
import json
import hexflower.parser as Parser


def parse_args():
    parser = argparse.ArgumentParser(description="")

    parser.add_argument("-c", "--config", required=True, type=str,
                        help="Path to the hex-flower configuration JSON file")
    parser.add_argument("-s", "--steps", required=True, type=int,
                        help="Number of navigation steps to take in the hex-flower")
    parser.add_argument("-i", "--start", required=False, type=int,
                        help="Override the starting hex number from the configuration file")
    parser.add_argument("-v", "--verbose", required=False, action='store_true')

    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    if args.steps <= 0:
        raise ValueError("The number of steps to take must be positive")
    if not os.path.isfile(args.config):
        raise FileNotFoundError(
            f"The config file '{args.config}' cannot be found")

    with (open(args.config)) as config_data:
        json_config = json.load(config_data)
        flower_config = Parser.parse_config(json_config, args.verbose)

        print(f"{flower_config.description}\n")

        # Traversing the flower
        current_hex = flower_config.get_starting_hex()
        print(current_hex)

        for i in range(1, args.steps):
            current_hex = flower_config.navigate(current_hex)
            print(f"{i}. {current_hex}")


if __name__ == "__main__":
    main()
