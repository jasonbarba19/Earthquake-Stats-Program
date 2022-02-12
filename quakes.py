# Name: Jason Barba
# Instructor: Workman
# Section: 11
# Project 5

from quakeFuncs import *

def main():
   quake_list = read_quakes_from_file("quakes.txt")
   option = "s"
   while option == "s" or option == "f" or option == "n" or option == "q":
      print()
      print("Earthquakes:\n------------")
      if option != "f":
         for quake in quake_list:
            print(quake)
         print()
         print("Options: \n  (s)ort\n  (f)ilter\n  (n)ew quakes\n  (q)uit")
         print()
      else:
         for quake in filter_list:
            print(quake)
         print()
         print("Options: \n  (s)ort\n  (f)ilter\n  (n)ew quakes\n  (q)uit")
         print()
      option = input("Choice: ").lower()
      if option == "s":
         sort_option = input("Sort by (m)agnitude, (t)ime, (l)ongitude, or l(a)titude? ").lower()
         if sort_option == "m":
            quake_list.sort(reverse=True)
         elif sort_option == "t":
            quake_list.sort(key=attrgetter("time"), reverse=True)
         elif sort_option == "l":
            quake_list.sort(key=attrgetter("longitude"))
         elif sort_option == "a":
            quake_list.sort(key=attrgetter("latitude"))
         else:
            pass
      elif option == "f":
         filter_option = input("Filter by (m)agnitude or (p)lace? ").lower()
         if filter_option == "m":
            lb = float(input("Lower bound: "))
            ub = float(input("Upper bound: "))
            filter_list = filter_by_mag(quake_list, lb, ub)
         elif filter_option == "p":
            place = input("Search for what string? ").lower()
            filter_list = filter_by_place(quake_list, place)
      elif option == "n":
         new_count = 0
         features = get_json('http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson')
         f = features["features"]
         for feature in f:
            new_quake = quake_from_feature(feature)
            if new_quake not in quake_list:
               new_count += 1
               quake_list.append(new_quake)
         if new_count > 0:
            print("\nNew quakes found!!!")
      elif option == "q":
         final_file = update_text(quake_list, "quakes.txt")
         quit()



if __name__ == "__main__":
   main()