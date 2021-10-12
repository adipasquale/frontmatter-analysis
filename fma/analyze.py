import pandas as pd
import os
from pathlib import Path
import frontmatter
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="path containing .md files")
    args = parser.parse_args()
    data = [frontmatter.load(path).metadata for path in Path(args.path).glob('*.md')]
    df = pd.DataFrame(data)
    with pd.option_context('display.width', 100):
        print(df.describe().transpose())
