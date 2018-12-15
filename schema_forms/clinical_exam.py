from wtforms import StringField, IntegerField, SubmitField, SelectField, SelectMultipleField, validators, TextAreaField, FormField
from schema_forms.form_utilities import SectionForm, BaseForm
from db_dict.common_dict import CommonDict
from db_dict.clinical_exam_dict import ClinicalExamDict

tbd = 'To be filled'

class PalpableLumpForm(BaseForm):
    fld_palpable_lump = SelectMultipleField("The palpable lump is ", choices=ClinicalExamDict.options_choice)
    fld_breast_lump = SelectMultipleField("The lump is present in", choices=CommonDict.breast_choice)
    fld_lump_localisation = SelectMultipleField("location of lump", choices=CommonDict.breast_location_choice)
    fld_lump_localisation_other = StringField("Other")
    submit_button = SubmitField('Submit Form')


class ClinicalExamForm(SectionForm):
    fld_provisional_diagnosis = StringField("Provisional diagnosis", default=tbd)

    fld_palpable_lump_form_present = SelectField("Palpable lump in the breast?", choices=CommonDict.form_yes_no_choice)
    palpable_lump_form = FormField(PalpableLumpForm)
    fld_lump_size = SelectField("Lump Size", choices=ClinicalExamDict.lump_size_choice)
    fld_lump_size_other = StringField("Other")
    fld_limp_number = SelectField("Number of lump", choices=ClinicalExamDict.lump_number_choice)
    fld_lump_number_other = StringField("Other")
    fld_lump_consistency = SelectField("Consistency of lumps", choices=ClinicalExamDict.lump_consistency_dict)# should it be multiple select?
    fld_fixity = SelectField("Lump fixity to",choices=ClinicalExamDict.lump_fixity_choice)
    fld_fixity_other = StringField("Other")
    


    submit_button = SubmitField('Submit Form')

