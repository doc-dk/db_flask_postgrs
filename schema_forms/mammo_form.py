from wtforms import StringField, TextAreaField, IntegerField, SelectField, FormField, SubmitField
from wtforms.fields.html5 import DateField
from db_dict.mammography import MammographyDict
from db_dict.common_dict import CommonDict
from schema_forms.form_utilities import BaseForm, SectionForm
from schema_forms.usg import AbvsForm


class MammoMassForm(SectionForm):
    def get_summary(self):
        return "fld-number: " + str(self.fld_number.data)

    fld_number = IntegerField("Mass number", default=1)
    fld_loc_right_breast = SelectField("Location of mass in Right Breast",
                                       choices=MammographyDict.mammo_mass_location_right_breast_choice)
    fld_loc_right_breast_other = StringField("Other")
    fld_loc_left_breast = SelectField("Location of mass in Left Breast",
                                      choices=MammographyDict.mammo_mass_location_left_breast_choice)
    fld_loc_left_breast_other = StringField("Other")
    fld_dist = StringField("Distance of mass from nipple(cm)")
    fld_dist_other = StringField("Other")
    fld_dim_mass = StringField("Dimension of mass(cm)")
    fld_dim_mass_other = StringField("other")
    fld_shape = SelectField("Shape of mass", choices=MammographyDict.mammo_mass_shape_choice)
    fld_shape_other = StringField("Other")
    fld_margin = SelectField("Margins of mass", choices=MammographyDict.mammo_mass_margin_choice)
    fld_margin_other = StringField("Other")
    submit_button = SubmitField('Submit Form')


class MammoCalcificationForm(SectionForm):
    fld_number = IntegerField("Group of calcification", default=1)
    fld_loc_right_breast = SelectField("Location of calcification in Right Breast",
                                       choices=MammographyDict.mammo_calc_location_right_breast_choice)
    fld_loc_right_breast_other = StringField("Other")
    fld_loc_left_breast = SelectField("Location of calcification in Left Breast",
                                      choices=MammographyDict.mammo_calc_location_left_breast_choice)
    fld_loc_left_breast_other = StringField("Other")
    fld_type = SelectField("Calcification Type", choices=MammographyDict.mammo_calcification_type_choice)
    fld_type_other = StringField("Other")
    submit_button = SubmitField('Submit Form')


class MammographyForm(SectionForm):
    fld_mammo_location = SelectField('Mammography Diagnosis at', choices=MammographyDict.mammo_location_choice)
    fld_mammo_date = DateField("Date of mammography")
    fld_mammo_indication = TextAreaField("Indication for mammography: ")
    fld_mammo_lesion = SelectField(label="Is skin lesion present", choices=MammographyDict.mammo_lesion_choice,
                                   default='tbd')
    fld_mammo_lesion_right_breast = SelectField("Location of skin lesion on right breast",
                                                choices=MammographyDict.mammo_lesion_right_breast_choice)
    fld_mammo_lesion_left_breast = SelectField("Location of skin lesion on left breast",
                                               choices=MammographyDict.mammo_lesion_left_breast_choice)
    fld_mammography_tomosynthesis_form_present = SelectField("Has 3D Tomosynthesis been done for the patient?",
                                                             choices=CommonDict.form_yes_no_choice)
    mammography_tomosynthesis_form = FormField(TomosynthesisForm)
    fld_mammo_birad = SelectField("BI-RAD classification (if available)", choices=MammographyDict.mammo_birad_choice)
    fld_mammo_impression = TextAreaField("Input Impression(if available): ")
    fld_mammography_abvs_form_present = SelectField("Has ABVS been done for the patient?",
                                                    choices=CommonDict.form_yes_no_choice)
    mammography_abvs_form = FormField(AbvsForm)
    submit_button = SubmitField('Submit Form')