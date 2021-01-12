from decimal import Decimal
from jinja2 import Markup


def format_power(val):
    if val is None:
        res = ""
    elif val >= 50e6:
        res = "{:,.0f}&nbsp;MW".format(val / Decimal(1e6))
    elif val >= 1e6:
        res = "{:.2f}&nbsp;MW".format(val / Decimal(1e6))
    else:
        res = "{:.0f}&nbsp;kW".format(val / Decimal(1e3))
    return Markup(res)


def format_length(val):
    if val is None:
        res = ""
    elif val >= 1000:
        res = "{:,.0f}&nbsp;km".format(val / Decimal(1e3))
    else:
        res = "{:,.0f}&nbsp;m".format(val)
    return Markup(res)


def format_voltage(val):
    if val is None:
        res = ""
    elif val >= 1000:
        res = "{:,.0f}&nbsp;kV".format(val / Decimal(1e3))
    else:
        res = "{:,.0f}&nbsp;V".format(val)
    return Markup(res)


def format_percent(val):
    if val is None:
        res = ""
    else:
        res = "{:,.1f}%".format(val * 100)
    return Markup(res)


def osm_link(osm_id, geom_type):
    url = "https://www.openstreetmap.org/"
    if osm_id < 0:
        osm_id = -osm_id
        url += "relation"
    elif geom_type == "ST_Point":
        url += "node"
    else:
        url += "way"
    return url + "/" + str(osm_id)


THE_COUNTRY_NAMES = {"United States", "United Kingdom", "Netherlands", "Bahamas",
                     "Canary Islands", "British Virgin Islands", "Azores", "Cayman Islands"}


def country_name(name, cap=False):
    if name in THE_COUNTRY_NAMES:
        if cap:
            return "The " + name
        else:
            return "the " + name
    return name
