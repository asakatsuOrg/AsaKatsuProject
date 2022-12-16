"""
# DAY 56 OF THE 100 DAYS OF CODE CHALLENGE
THIS IS A BLOCK COMMENT.
This is a simple script of creating a directory from a CSV file containing list of 100 Most Streamed
music containing artist names and their songs.

Writing commments per line to make sure that I understand how each line works aka how the program runs.
Corrections are most welcome!
"""

import csv, os, time

with open("100MostStreamedSongs.csv") as file:       # library/module is imported for functions
  reader = csv.DictReader(file)                      # DictReader reads the assigned csv file (created an object as a dictionary) and assigns it to variable 'reader'

  print("BUILDING DIRECTORY...")
  print()
  for row in reader:                                 # for every row in variable reader (the csv file)
    dir = os.listdir()                               # the os function creates a directory list and assigns it to variable 'dir'
    artist = row["Artist(s)"].title()                # row Artists in reader is assigned to variable
    song = row["Song"]                               # row Song in reader is assigned to variable
    print(f"ADDING {artist}, '{song}'")              # outputs ADDING artist_name, 'song_name' into the terminal
    time.sleep(1)                                    # the delay on the terminal before another line from the above command gets printed
    if artist not in dir:                            # if artist is not yet in directory,
      os.mkdir(artist)                               # a new folder with the artists's name gets created
    path = os.path.join(f"{artist}/", song)          # .join() creates an understandable location of the file and assigned to 'path'
    f = open(path, "w")                              # opens a file indicated in the path and writes a file indicated with the 'w'
    f.close()                                        # closes the opened file to make sure it won't be affected by another operation (?)

