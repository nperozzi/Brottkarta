# Brottsplatskartan sketch

## Final project requirements:
* There must be a 'main()' funciton in `project.py`
* 3 or more additional funcitons in `project.py`
* 3 or more unit tests for different functions to execute with `pytest`. The tests should be in `test_project.py`
* Video
* README.md over 500 words and multiple paragraphs
    * what your project is
    * what each of the files you wrote for the project contains and does
    * debated certain design choices, explaining why you made them


Workflow:
1. Get area filter from argument
1. Get from and to dates for filtering
1. Get all new events
1. Get filtered data set to display
1. Create map
1. Add markers
1. Save map


1. Plot Stockholm and filter boxes and a button called "plot"
1. Retrive data
    * retrive data based on filter parameters
    * request library
    * [brottsplatskartan´s API](https://brottsplatskartan.se/sida/api)
    * Retrive based ona search box? (potential to use reg exp)
1. Store Data
    * store data in a JSON file
1. Plot Data
    * folium library
    * plot crime data based on filter parameters


# Notes:
Class `crime_data_retriver`
    * `retrieve_data(self)` uses "pagination"
    * [ONGOING] "Incremental Data Fetching" and "Catching"(store data localy)
