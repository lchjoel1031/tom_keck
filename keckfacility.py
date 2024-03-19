from crispy_forms.layout import Layout
from django import forms
from tom_observations.facility import BaseRoboticObservationFacility, BaseRoboticObservationForm


#SITES = {
#    'Keck': {
#        'sitecode': 'Keck',
#        'latitude': 19.8238,
#        'longitude': -155.46905,
#        'elevation': 4215
#    }
#}

#class KeckFacilityForm(BaseRoboticObservationForm):
#    exposure_time = forms.IntegerField()
#    exposure_count = forms.IntegerField()
#
#    def layout(self):
#        return Layout(
#            'exposure_time',
#            'exposure_count'
#
#            )

KECK_TOO_INSTRUMENT_CHOICES=[
    ('HIRES','HIRES'),
    ('MOSFIRE','MOSFIRE'),
    ('LRIS','LRIS'),
    ('KPF','KPF'),
    ('OSIRIS','OSIRIS'),
    ('DEIMOS','DEIMOS'),
    ('ESI','ESI'),
    ('KCWI','KCWI'),
    ('NIRES','NIRES'),
    ('NIRC2','NIRC2'),
    ('NIRSPEC','NIRSPEC'),
]


KECK_IMAGING_INSTRUMENT_CHOICES=[
    ('MOSFIRE', 'MOSFIRE'),
    ('LRIS', 'LRIS'),
    ('OSIRIS','OSIRIS'),
    ('DEIMOS','DEIMOS'),
    ('ESI','ESI'),
    ('KCWI','KCWI'),
    ('NIRC2','NIRC2'),
]

KECK_SPECTROSCOPY_INSTRUMENT_CHOICES=[
    ('HIRES','HIRES'),
    ('MOSFIRE', 'MOSFIRE'),
    ('LRIS', 'LRIS'),
    ('KPF', 'KPF'),
    ('OSIRIS','OSIRIS'),
    ('DEIMOS','DEIMOS'),
    ('ESI','ESI'),
    ('KCWI','KCWI'),
    ('NIRES','NIRES'),
    ('NIRC2','NIRC2'),
    ('NIRSPEC','NIRSPEC'),
]

class KeckToOObservationForm(BaseRoboticObservationForm):
    program_id = forms.CharField()
    date = forms.CharField()
    instrument = forms.ChoiceField(
        required=True,
        choices=KECK_TOO_INSTRUMENT_CHOICES,
        )
    start_time = forms.CharField()
    interrupt_type = forms.ChoiceField(
        required=True,
        choices=[('Institution','Institution'),('Partner','Partner')]
    )


class KeckImagingObservationForm(BaseRoboticObservationForm):
    ob_name = forms.CharField()
    program_id = forms.CharField()
    instrument = forms.ChoiceField(
        required=True,
        choices=KECK_IMAGING_INSTRUMENT_CHOICES,
        )
    exposure_time = forms.IntegerField()
    repeat = forms.IntegerField()
    ob_type = forms.ChoiceField(
        required=True,
        choices=[('Normal','Classical'),('ToO','Target of opportunity')]
    )

    def layout(self):
        return Layout(
            'ob_name',
            'program_id',
            'instrument',
            'exposure_time',
            'repeat',
            'ob_type',
        )

class KeckSpectroscopyObservationForm(BaseRoboticObservationForm):
    ob_name = forms.CharField()
    program_id = forms.CharField()
    instrument = forms.ChoiceField(
        required=True,
        choices=KECK_SPECTROSCOPY_INSTRUMENT_CHOICES,
        )
    exposure_time = forms.IntegerField()
    repeat = forms.IntegerField()
    ob_type = forms.ChoiceField(
        required=True,
        choices=[('Normal','Classical'),('ToO','Target of opportunity')]
    )
    def layout(self):
        return Layout(
            'ob_name',
            'program_id',
            'instrument',
            'exposure_time',
            'repeat',
            'ob_type',
        )

class KeckFacility(BaseRoboticObservationFacility):
    name = 'Keck'
#    observation_types = [('OBSERVATION', 'Custom Observation')]
    observation_forms = {
        'ToO':KeckToOObservationForm,
        'Imaging': KeckImagingObservationForm,
        'Spectroscopy' : KeckSpectroscopyObservationForm,
    }

    SITES = {
        'Keck': {
            'latitude': 19.8238,
            'longitude': -155.46905,
            'elevation': 4215,
            }
        }

    def data_products(self, observation_id, product_id=None):
       return []

    def get_form(self, observation_type):
        return self.observation_forms.get(observation_type, KeckToOObservationForm)
#       return KeckFacilityForm

    def get_observation_status(self, observation_id):
        return ['IN_PROGRESS']

    def get_observation_url(self, observation_id):
        return ''

    def get_observing_sites(self):
        return {}

    def get_terminal_observing_states(self):
        return ['IN_PROGRESS', 'COMPLETED']

    def submit_observation(self, observation_payload):

        print(observation_payload)
        return [1]

    def validate_observation(self, observation_payload):
        pass

    def get_observing_sites(self):
        return self.SITES
