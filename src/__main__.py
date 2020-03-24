# Importing 3rd party classes
# from flask import Flask, request, Response, jsonify
# Importing custom functions
import src.utils.log
import src.utils.parser as parser

def main():
    # Initialize logger
    logger = src.utils.log.setup_custom_logger('root')

    # Welcome
    logger.debug('Welcome to the classifier app')

    # Parse arguments
    config = parser.arg_parser()
    # config = {"path": "."}

    logger.info("You said: " + config['text'])

# Entrypoint
if __name__ == '__main__':
    main()