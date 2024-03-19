To spin up a Keck TOM, first install TOMtoolkit following the instructions on:

https://tom-toolkit.readthedocs.io/en/stable/introduction/getting_started.html

After that, copy the keckfacility.py to mytom/mytom/ and put it along with the settings.py. Then modify the settings.py to incorporate Keck into observation facility:

TOM_FACILITY_CLASSES = [
    'tom_observations.facilities.lco.LCOFacility',
    'tom_observations.facilities.gemini.GEMFacility',
    'tom_observations.facilities.soar.SOARFacility',
    'tom_swift.swift.SwiftFacility',
    'mytom.keckfacility.KeckFacility',
]

as well as adding Keck observer's log in credentials in:

FACILITIES = {
    'LCO': {
        'portal_url': 'https://observe.lco.global',
        'api_key': '',
    },
    'Keck':{
        'Keck_USERNAME': 'username@keck.hawaii.edu',
        'Keck_PASSWORD': 'keckpassword',
    },
}

