#!/usr/bin/python
"""
Dropcloud!
----------------
A simple script that keeps Dropbox and iCloud in sync.

Written by Steve Gattuso
steve@stevegattuso.me
"""
import os

ICLOUD_PATH = os.path.join(os.getenv("HOME"), "Library/Mobile Documents")
DROPBOX_PATH = os.path.join(os.getenv("HOME"), "Dropbox/iCloud")
IGNORED_FILES = [".DS_Store"]

def check_dropbox_init():
    """
    Returns True/False depending on whether or not ~/Dropbox/iCloud exists.
    """
    return os.path.isdir(DROPBOX_PATH)

def list_documents():
    """
    Scans ~/Library/Mobile Documents for documents to sync
    with dropbox
    """
    # Loop through each app in the iCloud folder
    apps = os.listdir(ICLOUD_PATH)
    docs = {}
    for dirname in apps:
        # If it's not a directory skip it
        if not os.path.isdir(os.path.join(ICLOUD_PATH, dirname)):
            continue
        # If it doesn't have a Documents folder skip it
        if not os.path.isdir(os.path.join(ICLOUD_PATH, dirname, "Documents")):
            continue

        for filename in os.listdir(os.path.join(ICLOUD_PATH, dirname, "Documents")):
            docs[filename] = os.path.join(ICLOUD_PATH, dirname, "Documents", filename)

    return docs

if __name__ == "__main__":
    # See if we've created the folder
    if not check_dropbox_init():
        os.mkdir(DROPBOX_PATH)

    docs = list_documents()
    # Sync iCloud -> Dropbox
    for doc in docs:
        # If they're not already symlinked
        if os.path.exists(os.path.join(DROPBOX_PATH, doc)):
            continue
        # Ignore the files we don't care about
        if doc in IGNORED_FILES:
            continue

        os.symlink(docs[doc], os.path.join(DROPBOX_PATH, doc))
        print("Symlinking %s" % doc)

    # Delete symlinks that aren't needed anymore
    links = os.listdir(DROPBOX_PATH)
    for link in links:
        if link not in docs:
            # Make sure it's not a directory or something
            if os.path.isdir(os.path.join(DROPBOX_PATH, link)):
                continue

            # Remove the lint!
            os.remove(os.path.join(DROPBOX_PATH, link))
            print("Removing %s" % link)
