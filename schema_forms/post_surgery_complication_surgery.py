from wtforms import StringField, IntegerField, SelectField, SubmitField, FormField, DateField, TextAreaField
from schema_forms.form_utilities import SectionForm, BaseForm
from db_dict.surgery_report_dict import SurgeryReportDict
from db_dict.common_dict import CommonDict
from datetime import date
tbd = 'To be filled'

class SeromaComplicationForm(BaseForm):
    fld_date = DateField("Date", default=date.today())
    fld_intervention_type = SelectField("Intervention Type", choices=SurgeryReportDict.intervention_type_choice)
    fld_intervention_type_other = StringField("other")
    fld_treatment = TextAreaField("Treatment", default=tbd)

class FlapNecrosisComplicationForm(BaseForm):
    fld_date = DateField("Date", default=date.today())
    fld_intervention_type = SelectField("Intervention Type", choices=SurgeryReportDict.intervention_type_choice)
    fld_intervention_type_other = StringField("other")
    fld_treatment = TextAreaField("Treatment", default=tbd)

class HematomaComplicationForm(BaseForm):
    fld_date = DateField("Date", default=date.today())
    fld_intervention_type = SelectField("Intervention Type", choices=SurgeryReportDict.intervention_type_choice)
    fld_intervention_type_other = StringField("other")
    fld_treatment = TextAreaField("Treatment", default=tbd)

class SurgicalSiteInfectionComplicationForm(BaseForm):
    fld_date = DateField("Date", default=date.today())
    fld_intervention_type = SelectField("Intervention Type", choices=SurgeryReportDict.intervention_type_choice)
    fld_intervention_type_other = StringField("other")
    fld_treatment = TextAreaField("Treatment", default=tbd)

class DelayedWoundHealingComplicationForm(BaseForm):
    fld_date = DateField("Date", default=date.today())
    fld_intervention_type = SelectField("Intervention Type", choices=SurgeryReportDict.intervention_type_choice)
    fld_intervention_type_other = StringField("other")
    fld_treatment = TextAreaField("Treatment", default=tbd)

class LymphoedemaComplicationForm(BaseForm):
    fld_date = DateField("Date", default=date.today())
    fld_intervention_type = SelectField("Intervention Type", choices=SurgeryReportDict.intervention_type_choice)
    fld_intervention_type_other = StringField("other")
    fld_treatment = TextAreaField("Treatment", default=tbd)

class PostSurgeryComplicationForm(SectionForm):
    fld_seroma_complication_form_present = SelectField("Is seroma a post surgery complication",
                                                              choices=CommonDict.form_yes_no_choice)
    seroma_complication_form = FormField(SeromaComplicationForm)
    fld_flap_necrosis_complication_form_present = SelectField("Is flap necrosis a post surgery complication",
                                                       choices=CommonDict.form_yes_no_choice)
    flap_necrosis_complication_form = FormField(FlapNecrosisComplicationForm)
    fld_hematoma_complication_form_present = SelectField("Is hematoma a post surgery complication",
                                                              choices=CommonDict.form_yes_no_choice)
    hematoma_complication_form = FormField(HematomaComplicationForm)
    fld_surgical_site_infection_complication_form_present = SelectField("Is surgical site infection a post surgery complication",
                                                         choices=CommonDict.form_yes_no_choice)
    surgical_site_infection_complication_form = FormField(SurgicalSiteInfectionComplicationForm)
    fld_delayed_wound_healing_complication_form_present = SelectField("Is dealyed wound healing a post surgery complication",
                                                         choices=CommonDict.form_yes_no_choice)
    delayed_wound_healing_complication_form = FormField(DelayedWoundHealingComplicationForm)
    fld_lymphoedema_complication_form_present = SelectField("Is lymphoedema a post surgery complication",
                                                  choices = CommonDict.form_yes_no_choice)
    lymphoedema_complication_form = FormField(LymphoedemaComplicationForm)
    fld_recurrence = SelectField("Recurrence seen", choices=CommonDict.yes_no_choice)
    fld_recurrence_other = StringField("other")
    fld_date_recurrence = DateField("Date of recurrence", default=date.today())
    fld_location_recurrence = SelectField("Location of the recurrence", choices=SurgeryReportDict.location_recurrence_choice)
    fld_location_recurrence_other = StringField("other")
    submit_button = SubmitField('Submit Form')


