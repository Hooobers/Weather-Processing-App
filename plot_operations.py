'''
Name: Adam Huybers, Ana Sckaff Santos Lazaro, Hriday Bedi
Program: Business Information Technology
Course: ADEV-3005 Programming in Python
Created: 2022-11-29
Updated: 2022-12-15
TODO - All plotting operations.
Final Project
@version 1.0.6
'''

import matplotlib.pyplot as plt
from datetime import datetime


class PlotOperations:
    """ Plots temperature data in multiple ways."""
    
    def box_plot(self, weather, start_year, end_year):
        """ Creates a box plot for display purposes. """
        try:
          # Verify that there is data.  
          if (len(weather) > 0):

            fig, ax = plt.subplots()
            fig.canvas.set_window_title(f"Python Weather Application: {start_year}-{end_year}")
            ax.set_title(f"Monthly Temperature Range From: {start_year} to {end_year}")
            plt.ylabel('Temps')
            plt.xlabel('Month')

            # Data for months will be stored in lists.
            # Create lists for each month.
            january = []
            february = []
            march = []
            april = []
            may = []
            june = []
            july = []
            august = []
            september = []
            october = []
            november = []
            december = []

            for row in weather:
                """ Loops through the data via month. """
                try:
                    if (row["avg_temp"] != "N/A"):
                        month = int(row["sample_date"][5:7].replace("-",""))
                        # Use a switch?
                        if (month == 1): 
                            january.append(row["avg_temp"])
                        elif (month == 2):
                            february.append(row["avg_temp"])
                        elif (month == 3):
                            march.append(row["avg_temp"])
                        elif (month == 4):
                            april.append(row["avg_temp"])
                        elif (month == 5):
                            may.append(row["avg_temp"])
                        elif (month == 6):
                            june.append(row["avg_temp"])
                        elif (month == 7):
                            july.append(row["avg_temp"])
                        elif (month == 8):
                            august.append(row["avg_temp"])
                        elif (month == 9):
                            september.append(row["avg_temp"])
                        elif (month == 10):
                            october.append(row["avg_temp"])
                        elif (month == 11):
                            november.append(row["avg_temp"])
                        else:
                            december.append(row["avg_temp"])

                except Exception as e:
                    print("Error handling end tags:", e)

            # The data is populated in a list (of lists), and then plotted.
            data = [january, february, march, april, may, june, july, august, september, october, november, december]
            plt.boxplot(data)
            plt.show()

        except Exception as e:
            print("Error:", e)

    def line_plot(self, weather, year, month):
        """ Creates a box plot for display purposes. """
        try:
            # Verify that there is data.
            if (len(weather) > 0):
                # Format data into a DateTime object.
                format = dates.DateFormatter('%d')
                datetime_object = datetime.strptime(year+ "-" + month, "%Y-%m")

                # Plotting framework.
                fig, axis = plt.subplots()
                fig.canvas.set_window_title(f"Python Weather Application: {datetime_object.strftime('%B, %Y')}")
                axis.xaxis.set_major_formatter(format)
                axis.set_title(f"Daily Temperatures: {datetime_object.strftime('%B, %Y')}")
                plt.ylabel('Temps')
                plt.xlabel('Day')

                mean_temps = []
                dates = []
                previous_temp = ""

                # Data collection.
                for row in weather:
                    """ Loops through the data and creates lists. """
                    try:
                        avg_temp = row["avg_temp"]
                        dates.append(row["sample_date"])

                        if (avg_temp != "N/A"):
                          mean_temps.append(avg_temp)
                          previous_temp = avg_temp
                        else:
                          mean_temps.append(previous_temp)

                    except Exception as e:
                      print("Error:", e)

            # The data is plotted.
            plt.plot(dates, mean_temps)
            plt.show()

        except Exception as e:
            print("Error:", e)