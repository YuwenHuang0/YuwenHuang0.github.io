# Leaflet cluster map of talk locations
#
# Run this from the repo root. It scrapes the location YAML field from each
# .md file in _talks/, geolocates it with geopy/Nominatim, and uses the getorg
# library to output data, HTML, and Javascript for a standalone cluster map
# in talkmap/.
import glob
import sys
import time

import frontmatter
import getorg
from geopy import Nominatim

TIMEOUT = 10  # seconds per geocoding request
RATE_LIMIT_SECONDS = 1.1  # Nominatim usage policy: max 1 request/second

geocoder = Nominatim(user_agent="yuwenhuang0.github.io talkmap")
location_dict = {}
failures = []

for file in sorted(glob.glob("_talks/*.md")):
    data = frontmatter.load(file).to_dict()
    if 'location' not in data:
        continue

    title = data['title'].strip()
    venue = data['venue'].strip()
    location = data['location'].strip()
    # "(virtual)" and similar suffixes confuse the geocoder
    query = location.replace("(virtual)", "").strip()
    description = f"{title}<br />{venue}; {location}"

    try:
        result = geocoder.geocode(query, timeout=TIMEOUT)
    except Exception as ex:
        print(f"Error: geocode raised on input {query}: {type(ex).__name__}: {ex}")
        failures.append(query)
        continue
    finally:
        time.sleep(RATE_LIMIT_SECONDS)

    if result is None:
        print(f"Warning: no geocode result for {query}")
        failures.append(query)
        continue

    location_dict[description] = result
    print(description, "->", result)

if not location_dict:
    # Nothing geocoded (e.g. Nominatim unreachable). Keep the existing map
    # rather than overwriting it with an empty one.
    print("No locations geocoded; leaving existing talkmap/ untouched.")
    sys.exit(1)

getorg.orgmap.output_html_cluster_map(location_dict, folder_name="talkmap", hashed_usernames=False)
print(f"Map written: {len(location_dict)} located, {len(failures)} failed ({failures})")
