from wtforms import StringField, SelectField, SubmitField, IntegerField
from wtforms.fields.html5 import DateField
from db_dict.mammography import MammographyDict
from db_dict.common_dict import CommonDict
from schema_forms.form_utilities import BaseForm, SectionForm


class AbvsForm(BaseForm):
    fld_abvs_date = DateField("Date of examination of ABVS", default=None)
    fld_abvs_acc = StringField("Accession number of ABVS")
    fld_abvs_right_breast_lesion = SelectField("Location of lesion in right breast",
                                               choices=CommonDict.breast_location_choice)
    fld_abvs_right_breast_lesion_other = StringField("Other")
    fld_abvs_left_breast_lesion = SelectField("Location of lesion in left breast",
                                              choices=CommonDict.breast_location_choice)
    fld_abvs_left_breast_lesion_other = StringField("Other")
    fld_abvs_size = StringField("Size of lesion")
    fld_abvs_dist = StringField("Distance from Skin (cm)")
    fld_abvs_pect = StringField("Distance from Pectoralis Major (cm)")
    fld_abvs_diagnosis = SelectField("ABVS Diagnosis", choices=MammographyDict.abvs_diagnosis_choice)




class SonoMammoMassForm(SectionForm):
    def get_summary(self):
        return "fld-number: " + str(self.fld_number.data)
    fld_number = IntegerField("Mass number", default=1)
    fld_sono_mass_right_location = SelectField("Location of mass in right breast",
                                               choices=CommonDict.breast_location_choice)
    fld_sono_mass_right_location_other = StringField("Other")
    fld_sono_mass_left_location = SelectField("Location of mass in left breast",
                                              choices=CommonDict.breast_location_choice)
    fld_sono_mass_left_location_other = StringField("Other")
    fld_sono_location_clock = StringField("What is the clock position of mass?", default='enter position only')
    fld_sono_mass_shape = SelectField("Shape of mass", choices=MammographyDict.sono_mass_shape_choice)
    fld_sono_mass_shape_other = StringField("Other")
    fld_sono_mass_size = StringField("Mass Dimension in mm:")
    fld_sono_mass_margin = SelectField("Margin of mass", choices=MammographyDict.sono_mass_margin_choice)
    fld_sono_mass_margin_other = StringField("Other")
    fld_sono_mass_echo = SelectField("Echo pattern of mass", choices=MammographyDict.sono_mass_echo_choice)
    fld_sono_mass_echo_other = StringField("Other")

    submit_button = SubmitField('Submit Form')