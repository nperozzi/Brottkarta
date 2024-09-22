# Crime Map Sweden
#### Video Demo:  [https://youtu.be/HXNZ30L0zuM?si=9Wl_Q2efgHga_6S7](https://youtu.be/HXNZ30L0zuM?si=9Wl_Q2efgHga_6S7)
#### Description:
Crime Map Sweden generates a map of the crimes reported in an area of Sweden during a given time.

The program requests the user for an area and "from" and "to" dates. Subsequently, it updates a JSON file that saves all past crime events reported in Sweden. The data is retrieved from the [brottsplatskartan.se](https://brottsplatskartan.se/) API. Then, the data is filtered by area and date and displayed in a map of the area that is saved as an HTML file.

## Files content
### project.py
This file contains the `main()` function and the functions related to the request of user input.
#### `main()` workflow:
1. The user enters the area to query as a command line argument.
1. Evaluate if the number of command line arguments is valid.
1. Evaluate if the area provided is valid.
1. Request the "from_date" and the "to_date"
1. Evaluate if the from_date and to_date are valid.
1. Update the crime data in the JSON file.
1. Filter the crime data
1. Create a map focusing on the area to query
1. Create markers for each of the crimes filtered.
1. Save the map as an HTML file in a folder called "output"

#### `evaluate_argument(arg_list)`:
Validates if the number of command line arguments is correct. If it is not accurate, it exits the program.

#### `evaluate_area(input_area)`:
Validates if the area to query exists in the list of areas. If not, it raises a `ValueError`.

#### `get_input_date(promt)`:
Prompts the user for a date in the YYYY-MM-DD format. If the format is not correct or if the date is in the future, it re-prompts.

#### `get_area_coordinates(name)`:
Returns a tuple with the latitude and longitude of the area to query. If the area does not exist, it returns `None`.

### crime_data_retriver.py
This file contains a class that retrieves the API´s data. The `CrimeDataRetriver` class, stores the following attributes and methods:
* `url`: Base URL to make API queries.
* `json_file`: JSON file´s name
* `data`: list of stored crimes.

#### `get_new_events(self)`:
Retrieves every crime event until it finds one that is already stored in `data`. Then, it saves those events in `data`.

This method uses a "pagination" design pattern, where the `request.get()` method is called in a loop for the next page. Note that the function has a limit on the number of pages that it can retrieve to prevent overloading the API.

Once the loop is broken, the new crime events are saved in the JSON file.

#### `get_filtered_data(self, from_date, to_date, area)`:
Gets a list of the crimes filtered by `area`, `from_date`, and `to_date`.

#### `_create_crime_object(self, event)`:
Converts the elements of the JSON file into attributes of a `crime` object.

#### `_clean_date(self, str)`:
Retrieves the date that the crime occurred but in YYYY-MM-DD format.

#### `_check_pages(self, page, data)`:
Check if the current page is the last.

#### `_get_last_page(self, data)`:
Gets the last page from the API query.

#### `_get_saved_data(self)`:
Gets the crime´s data from the JSON file to the data list.

#### `_save_data(self)`:
Saves the new crime objects into the JSON file.

### crime.py
Contains the `Crime` class.

#### `to_dict(self)`:
Converts the object into a dictionary.

### dates.py
This file contains the methods that do date manipulation. It does this by using the `datetime` library.

#### `convert_to_date(date_str)`:
Converts a string into a date object with the YYYY-MM-DD format.

#### `get_today()`:
Gets today´s date with the YYYY-MM-DD format.

### areas.py
This file contains the class `Area` with its attributes
* `name`: name of the area
* `lat`: latitude
* `lng`: longitude

#### `create_areas_list()`:
Creates a list of Area objects that align with the areas in the API.

### map.py
This file contains the methods that handle the map and markers. It does this by using the `folium` library.

#### `add_crime_marker(crime, map)`:
Creates a marker on the map. The marker is positioned in the corresponding latitude and longitude, it displays a summary of the crime (tooltip) when hovering the pinter over it and it displays more information when clicking on the marker (popup).

#### `get_map`:
Creates a map and centers on the area being queried.

### events.json:
Stores all the crime events that have been retrived from the API.

## Decisions and choices:
A lot of choices have been made to use the tools and concepts learned in the course even though there might be better ways of solving them. Here are some examples:
* The area to query is entered as a command line argument and the from and to dates are prompt to the user as in the terminal. These inputs from the user could have been displayed as filters with drop-down lists on the HTML map itself.
* The crime data is converted into crime objects and loaded into the JSON file, then the crime data is complemented with new crime events from the API, which are converted into crime objects. Then all the crime objects are converted into dictionaries and saved into the JSON file. Maybe it would have been easier to just work with each crime event as dictionaries and save them as dictionaries in the JSON file. The crime object was a good excuse to use OOP.
