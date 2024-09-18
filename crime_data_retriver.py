import requests
import json
import re
from crime import Crime


class CrimeDataRetriver:
    def __init__(self, url):
        self.url = url
        self.json_file = f"events.json"
        self.data = self._get_saved_data()


    def __str__(self):
        return "\n".join(str(crime) for crime in self.data)     #NOTE: "string comprehension" is happening here.

    def _get_saved_data(self):                                  # Fills up self.data with the data already exisitng in the json file
        with open(self.json_file, "r") as file:
            try:
                data = json.load(file)
                return [Crime(**crime) for crime in data]       #NOTE: `**` is "unpacking" the calues from the json file.
            except (FileNotFoundError, json.JSONDecodeError):
                return []

    def _save_data(self):
        crime_dicts = [crime.to_dict() for crime in self.data]

        with open(self.json_file, "w") as file:
            json.dump(crime_dicts, file, ensure_ascii = False, indent = 4)

    def get_new_events(self, area):
        page = 1
        per_page = 100                                          #NOTE: API supports max 500 results per page
        max_page = 10
        new_events = []                                         #list of Crime objects
        event_found = False

        while page <= max_page and not event_found:
            response = requests.get(f"{self.url}?limit={per_page}&page={page}") #&area={area}
            if response.status_code == 200:
                data = response.json()
                for event in data["data"]:
                    if any(crime.id == event["id"] for crime in self.data):
                        event_found = True
                    else:
                        new_events.append(self._create_crime_object(event))

                if new_events:
                    self.data.extend(new_events)
                    print(f"Fetched {len(new_events)} new events.")
                else:
                    print("No new events to fetch.")

            else:
                print(f"Error: Request status code {response.status_code}")
                break

            if self._check_pages(page, data):
                page += 1
            else:
                break

        self._save_data()

    def get_filtered_data(self, from_date, to_date, area):
        filtered_data = []

        for crime in self.data:
            if from_date <= crime.date <= to_date and area == crime.administrative_area_level_1:
                filtered_data.append(crime)

        return filtered_data

    def _create_crime_object(self, event):
        id = event["id"]
        date = self._clean_date(event["pubdate_iso8601"])
        title_type = event["title_type"]
        title_location = event["title_location"]
        headline = event["headline"]
        description = event["description"]
        content = event["content"]
        content_formatted = event["content_formatted"]
        content_teaser = event["content_teaser"]
        location_string = event["location_string"]
        location_string_2 = event["location_string_2"]
        date_human = event["date_human"]
        lat = event["lat"]
        lng = event["lng"]
        viewport_northeast_lat = event["viewport_northeast_lat"]
        viewport_northeast_lng = event["viewport_northeast_lng"]
        viewport_southwest_lat = event["viewport_southwest_lat"]
        viewport_southwest_lng = event["viewport_southwest_lng"]
        administrative_area_level_1 = event["administrative_area_level_1"]
        administrative_area_level_2 = event["administrative_area_level_2"]
        image = event["image"]
        image_far = event["image_far"]
        external_source_link = event["external_source_link"]
        permalink = event["permalink"]
        return Crime(id, date, title_type, title_location, headline, description, content, content_formatted, content_teaser, location_string,
                 location_string_2, date_human, lat, lng, viewport_northeast_lat, viewport_northeast_lng, viewport_southwest_lat, viewport_southwest_lng,
                 administrative_area_level_1, administrative_area_level_2, image, image_far, external_source_link, permalink)

    def _clean_date(self, str):
        pattern = r"^(\d{4}-\d{2}-\d{2})"
        match = re.search(pattern, str)
        if match:
            date_str = match.group(1)
        return date_str

    def _check_pages(self, page, data):
        last_page = self._get_last_page(data)
        return page < last_page

    def _get_last_page(self, data):
        try:
            last_page = int(data["links"]["last_page"])
        except KeyError:
            print("Error retriving last_page.")
            return 1
        return last_page
