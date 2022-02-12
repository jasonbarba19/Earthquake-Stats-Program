# Name: Jason Barba
# Instructor: Workman
# Section: 11
# Project 5

from urllib.request import *
from json import *
from datetime import *
from operator import *
from math import *

class Earthquake:
   def __init__(self, place, mag, longitude, latitude, time):
      #place -> string, mag -> float, long -> float, lat -> float, time -> int
      self.place = place
      self.mag = mag
      self.longitude = longitude
      self.latitude = latitude
      self.time = time

   def __eq__(self, other):
      return self.place == other.place and isclose(self.mag, other.mag) and isclose(self.longitude, other.longitude) and isclose(self.latitude, other.latitude) and self.time == other.time

   def __repr__(self):
      return str(self.mag) + " " + str(self.longitude) + " " + str(self.latitude) + " " + str(self.time) + " " + str(self.place)
      # match order in quakes.txt
      # when done, save quakes to file, open quakes and write quakes to file, file.write -> call __repr__
   def __str__(self):
      return "(%.2f) %40s at %s (%.3f, %.3f)" % (self.mag, self.place, time_to_str(self.time), self.longitude, self.latitude)

   def __lt__(self, other):
      return self.mag < other.mag

def read_quakes_from_file(filename):
   location = ""
   data_list = []
   file = open(filename, "r")
   for line in file:
      data = line.split()
      for i in range(4, len(data)):
         location += data[i]
         location += " "
      location = location.strip()
      quake = Earthquake(location, float(data[0]), float(data[1]), float(data[2]), int(data[3]))
      data_list.append(quake)
      location = ""
   return data_list

def filter_by_mag(quakes, low, high):
   return [quake for quake in quakes if quake.mag >= low and quake.mag <= high]
     
def filter_by_place(quakes, word):
   return [quake for quake in quakes if quake.place.lower().find(word) != -1]

def quake_from_feature(f):
   return Earthquake(f["properties"]["place"], f["properties"]["mag"], f["geometry"]["coordinates"][0], f["geometry"]["coordinates"][1], int(f["properties"]["time"])//1000)

def get_json(url):
   with urlopen(url) as response:
      html = response.read()
   htmlstr = html.decode("utf-8")
   return loads(htmlstr)

def time_to_str(time):
   return datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')    

def update_text(quakes, text):
   file = open(text, "r+")
   file.truncate(0)
   for quake in quakes:
      file.write(repr(quake))
      file.write("\n")
   return file



   
