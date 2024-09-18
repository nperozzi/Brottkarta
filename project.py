import sys
from datetime import datetime
import dates
import areas
import map
import crime_data_retriver

areas_list = areas.create_areas_list()                                             #NOTE: global variable

def main():
    #Enter area to filter
    evaluate_argument(sys.argv)
    evaluate_area(sys.argv[1])
    area = sys.argv[1]

    #Enter from and to date:
    from_date = get_input_date(f"Enter \"from\" date as YYYY-MM-DD: ")
    to_date = get_input_date(f"Enter \"to\" date as YYYY-MM-DD: ")          #TODO: Should not allow for dates in the future or before the from_date
    if to_date < from_date:
        raise ValueError(f"The to_date cannot be a date before the from_date")

    api_url = "https://brottsplatskartan.se/api/events/"
    retriever = crime_data_retriver.CrimeDataRetriver(api_url)
    retriever.get_new_events(area)

    data_set = retriever.get_filtered_data(from_date, to_date, area)

    area_lat, area_lng = get_area_lat(area)
    zoom = 12
    area_map = map.get_map(area_lat, area_lng, zoom)
    for crime in data_set:
        map.add_crime_marker(crime, area_map)                                   ##TODO: The crime makers should be categorize by color.

    area_map.save(f"output/crime_map_{sys.argv[1]}-{dates.get_today()}.html")

#_____________________________________________

def evaluate_argument(arg_list):
    if len(arg_list) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif len(arg_list) < 2:
        print("Too few command-line arguments")
        sys.exit(1)

def evaluate_area(input_area):
    if not any(area.name == input_area for area in areas_list):
        raise ValueError("The area requested is not valid")
    return input_area

def get_input_date(prompt):
    while True:
        try:
            input_str = input(prompt)
            input_date = datetime.strptime(input_str, "%Y-%m-%d").date()
            if input_date > dates.get_today():
                raise ValueError
            return input_date
        except ValueError:
            print("Invalid date format. Please enter the date as YYYY-MM-DD.")

def get_area_lat(name):
    area = next((area for area in areas_list if area.name == name), None)
    return (area.lat, area.lng) if area else None

if __name__ == "__main__":
    main()



