import sys
import os
import urllib.request
from urllib.error import HTTPError
import shutil
import subprocess

BASE = "https://cfvod.kaltura.com/scf/hls/p/2323111/sp/0/serveFlavor/entryId/1_ozta4bof/v/11/ev/11/flavorId/1_copskb7d/name/a.mp4/seg-{}-v1-a1.ts?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9jZnZvZC5rYWx0dXJhLmNvbS9zY2YvaGxzL3AvMjMyMzExMS9zcC8wL3NlcnZlRmxhdm9yL2VudHJ5SWQvMV9venRhNGJvZi92LzExL2V2LzExL2ZsYXZvcklkLzFfY29wc2tiN2QvbmFtZS9hLm1wNC8qIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNjA4MTk3OTI5fX19XX0_&Signature=MMSKALT16V0JzjBpMY757ok7c78uEOdrw6UQABuvPZYkcZISexal~yk13Ba-0vaetWDDeUmbIJ694NiBHrQxGa0QUAsm5bBpdBi8geXEdJF8RHuMyMIEXAYjX9uXsvwd7adtZ4sbFWJ-4dOvyZD0ut4AxaFyqG9gx8pmtBujwoYl4y7TKECJ4Ty3cV-9fThaG0fC41xW4U2l-F8tvsibh1A16HHPPJkgw-TXU2Njy4mlu4Ht5eNC71hqe3eQDpLeEe~xqEB0ddfiRyDEC~kw8jgqH6LoVSxFRvSU3zvMyRKJEfdaTSSj~0exbObfQhloiHovz6J9OQhPNSk7VBizyQ__&Key-Pair-Id=APKAJT6QIWSKVYK3V34A"

MAX = 1000


def download():
    try:
        for i in range(1, MAX):
            urllib.request.urlretrieve(BASE.format(i+1), f"vid_{i}.ts")
            print(f"Downloaded clip {i}")
    except HTTPError:
        print("the download is finished")
        stitch(i)


def stitch(index):
    ts_filenames = [f"vid_{x}.ts" for x in range(1, index)]
    # open one ts_file from the list after another and append them to merged.ts
    with open("merged.ts", "wb") as merged:
        for ts_file in ts_filenames:
            with open(ts_file, "rb") as mergefile:
                shutil.copyfileobj(mergefile, merged)


def mydelete(index):
    # delete files
    for i in range(1, index):
        filename = f"{os.getcwd()}/vid_{i}.ts"
        if os.path.exists(filename):
            print(f"Removing {filename}")
            os.remove(filename)

def convert():
    infile = "merged.ts"
    outfile = "merged.mp4"
    subprocess.run(['ffmpeg', '-i', infile, outfile])

stitch(499)
convert()