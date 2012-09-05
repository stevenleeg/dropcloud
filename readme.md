# Dropcloud

A simple python script to sync iCloud and Dropbox. Still a work in progress, but it does the job.

![Dropcloud](http://i.imgur.com/jkDJZ.png)

## How does it work?
Essentially it scans the iCloud storage on your Mac (~/Library/iCloud/) for documents. If it finds things that need to be synced, it creates a symlink in the iCloud folder of your Dropbox.

## What needs to be done
 * More testing
 * Create a listener for changes of files in the iCloud directory
