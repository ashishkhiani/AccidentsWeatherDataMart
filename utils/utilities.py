def is_null_or_empty(item):
    if item is None or item.strip() == '':
        return True

    return False


def is_estimated(item):
    if item == 'E':
        return True

    return False


def is_missing_or_unavailable(item):
    if item == 'M' or item == 'NA':
        return True

    return False


def parse_ottawa_location(street_string):
    parsed_streets = []
    if '@' in street_string:
        parsed_streets = street_string.split('@')
        parsed_streets[1] = parsed_streets[1].lstrip()
        parsed_streets.append(None)
    else:
        temp_parsed_streets = street_string.split("btwn")
        parsed_intersection = temp_parsed_streets[1].split('&')
        parsed_streets.append(temp_parsed_streets[0])
        parsed_streets = parsed_streets + parsed_intersection
        parsed_streets[1] = parsed_streets[1].lstrip()
        parsed_streets[2] = parsed_streets[2].lstrip()
    
    return parsed_streets


ENVIRONMENT = (
    'unknown',
    'clear',
    'rain',
    'snow',
    'freezing rain',
    'drifting snow',
    'strong wind',
    'fog, mist, smoke, dust',
    'other'
)


VISIBILITY = (
    'unknown',
    'daylight',
    'daylight, artificial',
    'dawn',
    'dawn, artificial',
    'dusk',
    'dusk, artificial',
    'dark',
    'dark, artificial',
    'other'
)


ROAD_SURFACE = (
    'unknown',
    'dry',
    'ice',
    'loose snow',
    'packed snow',
    'slush',
    'wet',
    'mud',
    'loose sand or gravel',
    'spilled liquid',
    'other'
)


TRAFFIC_CONTROL = (
    'traffic signal',
    'stop sign',
    'yield sign',
    'pedestrian crossover',
    'school bus',
    'traffic gate',
    'traffic controller',
    'no control',
    'roundabout',
    'other'
)

COLLISION_CLASSIFICATION = (
    'fatal',
    'non-fatal',
    'p.d. only'
)

IMPACT_TYPE = (
    'approaching',
    'angle',
    'cyclist collisions'
    'pedestrian collisions'
    'rear end',
    'sideswipe',
    'turning movement',
    'smv unattended vehicle',
    'smv other',
    'other'
)
