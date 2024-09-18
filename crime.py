from dates import convert_to_date

class Crime:
    def __init__(self, id, date, title_type, title_location, headline, description, content, content_formatted, content_teaser, location_string,
                 location_string_2, date_human, lat, lng, viewport_northeast_lat, viewport_northeast_lng, viewport_southwest_lat, viewport_southwest_lng,
                 administrative_area_level_1, administrative_area_level_2, image, image_far, external_source_link, permalink):
        self.id = id
        self.date = convert_to_date(date)
        self.title_type = title_type
        self.title_location = title_location
        self.headline = headline
        self.description = description
        self.content = content
        self.content_formatted = content_formatted
        self.content_teaser = content_teaser
        self.location_string = location_string
        self.location_string_2 = location_string_2
        self.date_human = date_human
        self.lat = lat
        self.lng = lng
        self.viewport_northeast_lat = viewport_northeast_lat
        self.viewport_northeast_lng = viewport_northeast_lng
        self.viewport_southwest_lat = viewport_southwest_lat
        self.viewport_southwest_lng = viewport_southwest_lng
        self.administrative_area_level_1 = administrative_area_level_1
        self.administrative_area_level_2 = administrative_area_level_2
        self.image = image
        self.image_far = image_far
        self.external_source_link = external_source_link
        self.permalink = permalink

    def __str__(self):
        return f"{self.title_type}"

    def to_dict(self):
            return {
                "id": self.id,
                "date": str(self.date),
                "title_type": self.title_type,
                "title_location": self.title_location,
                "headline": self.headline,
                "description": self.description,
                "content": self.content,
                "content_formatted": self.content_formatted,
                "content_teaser": self.content_teaser,
                "location_string": self.location_string,
                "location_string_2": self.location_string_2,
                "date_human": self.date_human,
                "lat": self.lat,
                "lng": self.lng,
                "viewport_northeast_lat": self.viewport_northeast_lat,
                "viewport_northeast_lng": self.viewport_northeast_lng,
                "viewport_southwest_lat": self.viewport_southwest_lat,
                "viewport_southwest_lng": self.viewport_southwest_lng,
                "administrative_area_level_1": self.administrative_area_level_1,
                "administrative_area_level_2": self.administrative_area_level_2,
                "image": self.image,
                "image_far": self.image_far,
                "external_source_link": self.external_source_link,
                "permalink": self.permalink
            }
