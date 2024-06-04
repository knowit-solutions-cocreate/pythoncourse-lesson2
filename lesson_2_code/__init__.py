from lesson_2_code import db

import argparse


def cli():
    """Command line interface to `lesson_2_code`."""
    parser = argparse.ArgumentParser()
    sub_parsers = parser.add_subparsers(required=True, dest='sub_parser')

    db_parser = sub_parsers.add_parser('db')

    db_parser.add_argument('action', choices=['create', 'populate'])

    args = parser.parse_args()
    if args.sub_parser == 'db':
        if args.action == 'create':
            db.create()
        elif args.action == 'populate':
            db.populate()
