'''
Name: Adam Huybers, Ana Sckaff Santos Lazaro, Hriday Bedi
Program: Business Information Technology
Course: ADEV-3005 Programming in Python
Created: 2022-11-22
Updated: 2022-11-24
TODO - All web scraping operations.
Final Project
@version 1.0.3
'''
from html.parser import HTMLParser
import urllib.request


class WeatherScraper(HTMLParser):
  """Scrapes date from the Environment Canada website and returns a dictionary of the data."""

  def __init__(self):
    """ Init function."""
    HTMLParser.__init__(self)
    self.weather = dict()
    self.temperatures = dict()
    self.stack = list()
    self.items = 0
    self.columns = 0
    self.date = ""

  def handle_starttag(self, tag, attrs):
    """ Adds the tag to the stack when we enter a tag element. """
    try:
      self.stack.append(tag)
      if tag == "td":
        self.columns += 1

    except Exception as e:
      print("Error handling start tags:", e)


  def handle_endtag(self, tag):
    """ Removes the tag from the stack when we exit a tag element. """
    try:
      if tag == "tr":
        self.columns = 0
        self.items = 0

      # Loops through to check entire stack for the tag we are exiting out of.
      while self.stack:
        try:
          item = self.stack.pop()
          if item == tag:
            break

        except Exception as e:
          print("Error handling end tags:", e)

    except Exception as e:
      print("Error handling end tags:", e)


  def handle_data(self, data):
    """ Handles the data from the website. """
    try:
      if self.stack[-5:] == ["tbody", "tr", "th", "abbr", "a"] or self.stack[-4:] == ["tbody", "tr", "th", "abbr"]:
        if data.isdigit():
          self.date = data

      if self.stack[-3:] == ["tbody", "tr", "td"] or self.stack[-2:] == ["td", "a"] and self.columns <= 3:

        # Remove the "E" and "M" values from the data.
        if data == "M" or data == "\xa0":
          data = "N/A"
        elif data == "E":
          return

        # By tracking our column count, we can determine which dictionary key to insert the data into.
        if self.items == 0:
          self.temperatures["Max"] = data
          self.items += 1

        elif self.items == 1:
          self.temperatures["Min"] = data
          self.items += 1

        elif self.items == 2:
          self.temperatures["Mean"] = data
          self.items += 1

          if not self.date in self.weather.keys():
            self.weather[self.date] = self.temperatures
            self.temperatures = dict()

    except Exception as e:
      print("Error handling data:", e)

  def get_url(self, year, month):
    """ Retrieves the url used in database operations to collect data. """
    try:
      url_string = "https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840&EndYear=2018&Day=1&"
      month_string = f"&Month={str(month)}"
      year_string = f"Year={str(year)}"
      returned_url = url_string + month_string + year_string
      return returned_url

    except Exception as e:
      print("Error retreiving url:", e)

  def data_dump(self):
        """ Returns the weather as a dictionary. """
        try:
            temp_weather = self.weather
            self.weather = dict()
            return temp_weather

        except Exception as e:
            print("Error exoporting data:", e)


output = WeatherScraper()

with urllib.request.urlopen('https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840&EndYear=2018&Day=1&Year=1996&Month=5') as response:
    html = str(response.read())

output.feed(html)
print(output.data_dump())