from wtforms import StringField, validators, IntegerField, SelectField, SubmitField, TextAreaField, FormField
from wtforms.fields.html5 import DateField
from db_dict.surgery_report_dict import SurgeryReportDict
from schema_forms.form_utilities import SectionForm, BaseForm
from db_dict.common_dict import CommonDict
from datetime import date

tbd = "To be done"

class SurgeryReportForm (SectionForm):
    fld_date = DateField("Today's Date",choice = date.today())
    fld_name_of_hospital = StringField("Name of the Hospital",default=tbd)
    fld_anaesthetist = StringField("Name of the Anaesthetist",default=tbd)
    fld_location_of_lesion = SelectField("Location of lesion", choices=SurgeryReportDict.location_of_lesion_choice)
    fld_weight_of_tumour_left_breast = IntegerField("Weight of the tumour or tissues removed from left breast (in gms)",
                                                    default=0)
    fld_weight_of_tumour_right_breast = IntegerField("Weight of the tumour or tissues removed from right breast (in gms)",
                                                    default=0)
    fld_incision = SelectField("Type of incision performed", choices=)
    fld_surgery_form_present = SelectField("is surgery performed",
                                           choices=CommonDict.form_yes_no_choice)
    surgery_form = FormField(SurgeryForm)
