import argparse
from concurrent.futures import ThreadPoolExecutor

from base.job import job


def main(path):
    # Load file from doc and convert it to page
    with ThreadPoolExecutor(max_workers=5) as executor:
        result = executor.map(job, [])
    for r in result:
        print(r)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help="doc path")
    args = parser.parse_args()
    if not args.path:
        raise "missing doc path"
    main(args.path)
