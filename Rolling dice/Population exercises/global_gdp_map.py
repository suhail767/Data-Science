import json
from country_codes import get_country_code
from pygal.maps.world import World
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS


filename = "global_gdp_data.json"
with open(filename) as f:
    gdp_data = json.load(f)

    # Build a dictionary of country code and gdp
cc_gdp = {}
for gdp_dict in gdp_data:
    if gdp_dict['Year'] == '2014':
        country_name = gdp_dict['Country Name']
        gdp_country = int(float(gdp_dict['Value']))
        code = get_country_code(country_name)

        if code:
            cc_gdp[code] = gdp_country

# Categorising countries into 3 groups by their GDP
gdp_1, gdp_2, gdp_3 = {}, {}, {}

for cc, gdp in cc_gdp.items():
    if gdp < 5*(10**9):
        gdp_1[cc] = gdp
    elif gdp < 5*(10**10):
        gdp_2[cc] = gdp
    else:
        gdp_3[cc] = gdp


# Printing the number of countries in each GDP category
print(len(gdp_1), len(gdp_2), len(gdp_3))

# Plotting the GDP global map
wm_style = RS("#336699", base_style=LCS)
wm = World(style=wm_style)
wm.title = "Global GDP in 2014, by Country"
wm.add('0-5bn', gdp_1)
wm.add('5-50bn', gdp_2)
wm.add('>50bn', gdp_3)

wm.render_to_file('global_gdp.svg')
