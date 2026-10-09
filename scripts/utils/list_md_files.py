import os
import glob
import re

md_files = glob.glob('**/*.md', recursive=True)
print(f"Total markdown files found: {len(md_files)}")
for f in sorted(md_files):
    print(" -", f)
