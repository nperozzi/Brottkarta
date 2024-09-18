import folium

def add_crime_marker(crime, map):
    popup = folium.Popup(f'<div style="max-width: 500px; max-height: 200px; overflow: auto; padding: 10px; box-sizing: border-box">'
                         f'<p><b>Date:</b> {crime.date}</p>'
                         f'<h6><b>{crime.headline}</b></h6>'
                         f'<p>{crime.content_formatted}</p>'
                         f'</div>', max_width = 500)
    tooltip = folium.Tooltip(f'<div style="width: 300px; height: 200px; overflow: hidden; padding: 10px; box-sizing: border-box">'
                         f'<p>Date: {crime.date}</p>'
                         f'<p><i>{crime.title_type}</i></p>'
                         f'<h10>{crime.headline}</h10>'
                         f'<p>{crime.content_teaser}</p>'
                         f'</div>')

    folium.Marker(location = [crime.lat, crime.lng], popup = popup, tooltip = tooltip).add_to(map)

def get_map(area_lat, area_lng, zoom):
    return folium.Map(location=[area_lat, area_lng], zoom_start = zoom)

