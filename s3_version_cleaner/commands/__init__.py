import argparse
import logging

from s3_version_cleaner.commands.vaccum import vacuum

logging.basicConfig(level=logging.INFO)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", "-v", action="store_true")
    parser.add_argument("--quiet", "-q", action="store_true")
    parser.add_argument("--endpoint-url", dest="endpoint_url", type=str)
    subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

    vacuum_parser = subparsers.add_parser("vacuum")
    vacuum_parser.add_argument("--keep-last", dest="keep_last", required=True, type=int)
    vacuum_parser.add_argument("--bucket", type=str)
    vacuum_parser.add_argument("--object-key", dest="object_key", type=str)

    args = parser.parse_args()

    # Set the log level based on the command line arguments
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    elif args.quiet:
        logging.getLogger().setLevel(logging.ERROR)

    # Dispatch to the appropriate subcommand
    if args.subcommand == "vacuum":
        vacuum(
            keep_last=args.keep_last,
            endpoint_url=args.endpoint_url,
            bucket=args.bucket,
            object_key=args.object_key,
        )
    else:
        parser.print_usage()
