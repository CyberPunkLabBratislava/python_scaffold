import argparse
import logging
logger = logging.getLogger('root')

def arg_parser():
    # Defaults
    config = {}
    config["port"] = 5000
    config["host"] = "127.0.0.1"
    config["path"] = "."
    config["text"] = "You didn't say anything..."
    # Parsing
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--text", help="Say something")
    args = parser.parse_args()
    if args.text:
        config["text"] = args.text
        logger.debug("You said something!")
    return config