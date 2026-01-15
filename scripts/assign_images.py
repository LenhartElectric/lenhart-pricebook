import json

# Load pricebook data
with open('data/pricebook.json', 'r') as f:
    data = json.load(f)

# Image mappings based on package names and categories
image_map = {
    # EV Charging
    'E CAR': 'images/packages/EV Charging/EV Outlet.webp',
    'TOTAL HOME CARE': 'images/packages/EV Charging/Emporia/Emporia 1.webp',

    # Ceiling Fans
    'CEILING FAN': 'images/packages/Fans and Fixtures/Libertor-96-living.webp',
    'FAN BOX': 'images/packages/Fans and Fixtures/retrofit fan box.webp',
    'FAN REMOTE': 'images/packages/Fans and Fixtures/Bulb-in-fan-2.webp',
    'FAN CONTROL': 'images/packages/Fans and Fixtures/Bulb-in-fan-2.webp',
    'FAN LIGHT CONTROL': 'images/packages/Fans and Fixtures/Bulb-in-fan-2.webp',
    'EXHAUST FAN': 'images/heroes/fixtures.webp',

    # Generators
    'GENERATOR': 'images/packages/Generators/generac-home-generator_guardian-20kw_7077_hero.webp',
    '14KW': 'images/packages/Generators/generac-home-generator_guardian-20kw_7077_hero.webp',
    '18KW': 'images/packages/Generators/generac-home-generator_guardian-20kw_7077_hero.webp',
    '22KW': 'images/packages/Generators/generac-home-generator_guardian-20kw_7077_hero.webp',
    '24KW': 'images/packages/Generators/generac-home-generator_guardian-20kw_7077_hero.webp',
    '26KW': 'images/packages/Generators/liquid cooled.webp',
    'MAINTENANCE': 'images/packages/Generators/generac-home-generator_guardian-20kw_7077_hero.webp',
    'TRANSFER SWITCH': 'images/packages/Generators/transfer switch.webp',

    # Hot Tub
    'HOT TUB': 'images/packages/Hot Tub/spa disconnect.webp',

    # Recessed Lighting
    'WAFER': 'images/packages/Recessed Lights/pivot wafer.webp',
    'RCAN': 'images/packages/Recessed Lights/baffle.webp',
    'RECESSED': 'images/packages/Recessed Lights/Living.webp',

    # LED Tape
    'TAPE LT': 'images/packages/Tape Lighting/kitchen.webp',
    'TAPE LIGHT': 'images/packages/Tape Lighting/kitchen.webp',

    # Outlets & Switches
    'USB OUTLET': 'images/packages/Outlets/brown night light outlet.webp',
    'SWITCH': 'images/packages/15amp duplex outlet.webp',
    'OUTLET': 'images/packages/15amp duplex outlet.webp',
    'DIMMER': 'images/packages/15amp duplex outlet.webp',
    'RECEPTACLE': 'images/packages/15amp duplex outlet.webp',

    # Exterior Outlets
    'OUTLET WP': 'images/packages/Outlets/Heavy Duty/post outlet.webp',
    'SOFFIT OUTLET': 'images/packages/Outlets/Heavy Duty/post outlet.webp',

    # Heavy Duty Circuits
    '240V 20A': 'images/packages/Outlets/Heavy Duty/40a 240v.webp',
    '240V 30A': 'images/packages/Outlets/Heavy Duty/40a 240v.webp',
    '240V 40A': 'images/packages/Outlets/Heavy Duty/40a 240v.webp',
    '240V 50A': 'images/packages/Outlets/Heavy Duty/50a 240v.webp',
    '240V 60A': 'images/packages/Outlets/Heavy Duty/50a 240v.webp',
    'RV 30A': 'images/packages/Outlets/Heavy Duty/30a rv box.webp',
    'RV 50A': 'images/packages/Outlets/Heavy Duty/50a RV box.webp',

    # HVAC
    'AIR CONDITIONER': 'images/packages/Outlets/Heavy Duty/40a 240v.webp',
    'SOFT STARTER': 'images/packages/Outlets/Heavy Duty/40a 240v.webp',

    # Panel Upgrades
    'PANEL': 'images/packages/Electrical Panels/Interior Panels/40 Space Main Panel/Interior Panel 1.webp',
    'SUB PANEL': 'images/packages/Electrical Panels/Interior Panels/24 Space Sub Panel/Sub Panel 1.webp',
    '400 AMP': 'images/packages/Electrical Panels/Interior Panels/40 Space Main Panel/40 space panel installed.webp',
    '200 AMP': 'images/packages/Electrical Panels/Interior Panels/40 Space Main Panel/Interior Panel 1.webp',

    # Surge Protection
    'SURGE': 'images/packages/Generators/GENERAC SURGE.webp',

    # Interior Lighting
    'PENDANT': 'images/packages/beautiful livingroom.webp',
    'FIXTURE': 'images/heroes/fixtures.webp',
    'LIGHT BOX': 'images/packages/Fans and Fixtures/retrofit fan box.webp',

    # Exterior Lighting
    'SOFFIT LIGHT': 'images/packages/pario lighting.webp',
    'FLOOD': 'images/packages/Security Lights/black security.webp',
    'COACH LT': 'images/packages/pario lighting.webp',
    'LANDSCAPE': 'images/packages/Landscape Lighting/landscape lighting kit.webp',

    # Bathrooms
    'EXHAUST COMBO': 'images/heroes/fixtures.webp',

    # GFCI
    'GFI': 'images/packages/Electrical Panels/dual function breaker.webp',
    'GFCI': 'images/packages/Electrical Panels/dual function breaker.webp',

    # Interlock / Portable Generator
    'INTERLOCK': 'images/packages/Interlock Kit/interlock installed.webp',
    'INLET': 'images/packages/Interlock Kit/Inlet box.webp',

    # Nest/Smart Home
    'RING': 'images/packages/Nest/Google_Nest_Product_Family.width-1200.format-webp.webp',
    'NEST': 'images/packages/Nest/Google_Nest_Product_Family.width-1200.format-webp.webp',
    'SMOKE': 'images/packages/Nest/smoke - carbon.webp',
    'CARBON': 'images/packages/Nest/smoke - carbon.webp',
    'THERMOSTAT': 'images/packages/Nest/thermostat.webp',
}

# Default placeholder for packages without matching images
placeholder = 'images/logo.webp'

def find_image(pkg_name, category):
    """Find the best matching image for a package"""
    name_upper = pkg_name.upper()

    # Try specific matches first (longer patterns first)
    for pattern in sorted(image_map.keys(), key=len, reverse=True):
        if pattern in name_upper:
            return image_map[pattern]

    # Category-based defaults
    category_defaults = {
        'EV Charging': 'images/packages/EV Charging/EV Outlet.webp',
        'Ceiling Fans': 'images/packages/Fans and Fixtures/Libertor-96-living.webp',
        'Home Generators': 'images/packages/Generators/generac-home-generator_guardian-20kw_7077_hero.webp',
        'Hot Tub Circuits': 'images/packages/Hot Tub/spa disconnect.webp',
        'Recessed Lighting': 'images/packages/Recessed Lights/Living.webp',
        'LED Tape Lighting': 'images/packages/Tape Lighting/kitchen.webp',
        'Outlets & Switches': 'images/packages/15amp duplex outlet.webp',
        'Exterior Outlets': 'images/packages/Outlets/Heavy Duty/post outlet.webp',
        'Heavy Duty Circuits': 'images/packages/Outlets/Heavy Duty/40a 240v.webp',
        'HVAC Circuits': 'images/packages/Outlets/Heavy Duty/40a 240v.webp',
        'Panel Upgrades': 'images/packages/Electrical Panels/Interior Panels/40 Space Main Panel/Interior Panel 1.webp',
        'Surge Protection': 'images/packages/Generators/GENERAC SURGE.webp',
        'Interior Lighting': 'images/heroes/fixtures.webp',
        'Exterior Lighting': 'images/packages/pario lighting.webp',
        'Bathrooms': 'images/heroes/fixtures.webp',
        'GFCI Protection': 'images/packages/Electrical Panels/dual function breaker.webp',
        'Portable Generator': 'images/packages/Interlock Kit/interlock installed.webp',
    }

    if category in category_defaults:
        return category_defaults[category]

    return placeholder

# Assign images to all packages
assigned = 0
for cat in data['categories']:
    for pkg in cat['packages']:
        if not pkg.get('image'):
            img = find_image(pkg['displayName'], cat['name'])
            pkg['image'] = img
            assigned += 1

# Save updated data
with open('data/pricebook.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Assigned images to {assigned} packages")
