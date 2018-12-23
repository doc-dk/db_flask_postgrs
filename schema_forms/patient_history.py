from wtforms import StringField, validators, IntegerField, FloatField, SubmitField, SelectField, SelectMultipleField, \
    FormField, TextAreaField
from schema_forms.form_utilities import SectionForm, BaseForm
from db_dict.patient_history_dict import PatientHistoryDict
from db_dict.common_dict import CommonDict

class TobaccoExposureForm(BaseForm):
    fld_tobacco = SelectField("Tobacco exposure (Passive and/or Active)", choices=PatientHistoryDict.tobacco_choice)
    fld_tobacco_type_passive = SelectField("Mode of passive consumption",
                                           choices=PatientHistoryDict.tobacco_type_passive_choice)
    fld_tobacco_type_passive_other = StringField('Other')
    fld_tobacco_type_passive_home = StringField("What is the specific source of passive exposure at home",
                                                default='None')
    fld_tobacco_type = SelectMultipleField("Type of tobacco use", choices=PatientHistoryDict.tobacco_type_choice)
    fld_tobacco_type_other = StringField("Other")
    fld_tobacco_age = StringField("Consumption of tobacco from which age (yrs)")
    fld_tobacco_freq = StringField("Frequency of tobacco consumption")
    fld_tobacco_quant = StringField("Quantity of tobacco consumed per week")
    fld_tobacco_duration = StringField("Duration of tobacco consumption")
    fld_tobacco_comments = StringField("Additional comments for tobacco consumption")
    fld_other_del_habits = StringField("Other Deleterious Habits (if present give details)")

class AlcoholConsumptionForm(BaseForm):
    fld_alcohol = SelectField("Alcohol consumption", choices=CommonDict.yes_no_choice)
    fld_alcohol_other = StringField("Other")
    fld_alcohol_age = StringField("Consumption of alcohol from which age (yrs)")
    fld_alcohol_quant = StringField("Quantity of alcohol consumed per week")
    fld_alcohol_duration = StringField("Duration of alcohol consumption")
    fld_alcohol_comments = StringField("Additional comments for alcohol consumption")

class PhysicalActivityForm(BaseForm):
    fld_type_phys_act = TextAreaField("Types of physical activity (; separated)")
    fld_freq_phys_act = StringField("Frequency of each physical activity (; separated)")

class NutritionalSupplementsForm(BaseForm):
    fld_nut_supplements_type = StringField("Types of nutritional supplements taken (; separated)")
    fld_nut_supplements_quant = StringField("Quantities of nutritional supplements taken per day (; separated)")
    fld_nut_supplements_duration = StringField("Duration of each nutritional supplements use (; separated)")


class PatientHistoryForm(SectionForm):
    fld_age_diagnosis = IntegerField('Age at diagnosis (yrs)', [validators.required()])
    fld_place_birth = StringField('Place of Birth')
    fld_height_cm = FloatField('Height (in cm)', [validators.required()])
    fld_weight_kg = FloatField('Weight (in kg)', [validators.required()])
    fld_diet = SelectField("Diet", choices=PatientHistoryDict.diet_choice)
    fld_diet_other = StringField("Other")
    fld_alcohol_consumption_form_present = SelectField('Have you consumed alcohol?',
                                                       choices=CommonDict.form_yes_no_choice)
    alcohol_consumption_form = FormField(AlcoholConsumptionForm)
    fld_tobacco_exposure_form_present = SelectField('Have you been exposed to Tobacco (active/passive)?',
                                                    choices=CommonDict.form_yes_no_choice)
    tobacco_exposure_form = FormField(TobaccoExposureForm)
    fld_physical_activity_form_present = SelectField('Do you participate in regular Physical Activity (yoga/walking/gym)?',
                                             choices=CommonDict.form_yes_no_choice)
    physical_activity_form = FormField(PhysicalActivityForm)
    fld_nutritional_supplements_form_present = SelectField('Do you take nutritional supplements?',
                                                           choices=CommonDict.form_yes_no_choice)
    nutritional_supplements_form = FormField(NutritionalSupplementsForm)
    submit_button = SubmitField('Submit Form')



