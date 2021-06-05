from schema_forms.form_utilities import SectionForm
from wtforms import StringField, validators, IntegerField, FloatField, SubmitField, SelectField, SelectMultipleField
from datetime import date
from db_dict.common_dict import CommonDict
from db_dict.patient_history_dict import PatientHistoryDict
from schema_forms.form_utilities import SectionForm, BaseForm
from wtforms.fields.html5 import DateField
from wtforms import StringField, IntegerField, FloatField, SubmitField, TextAreaField, SelectField, SelectMultipleField,\
    FormField
<< << << < HEAD

tbd = 'To be filled'


class NutritionalSupplementsForm(BaseForm):
    fld_nut_supplements_type = TextAreaField("Type of nutritional supplements taken(Separate with ; between different "
                                             "supplements)", default=tbd)
    fld_nut_supplements_quant = StringField(
        "Quantity of nutritional supplements taken per day", default=tbd)
    fld_nut_supplements_duration = StringField(
        "Duration of nutritional supplements use", default=tbd)


class PhysicalActivityForm(BaseForm):
    fld_type_phys_act = TextAreaField("Type of physical activity(separate different physical activity using ;)",
                                      default=tbd)
    fld_freq_phys_act = StringField(
        "Frequency of physical activity", default=tbd)


class AlcoholConsumptionForm(BaseForm):
    fld_alcohol_age = StringField(
        "Consumption of alcohol from which age (yrs)", default=tbd)
    fld_alcohol_quant = StringField(
        "Quantity of alcohol consumed per week", default=tbd)
    fld_alcohol_duration = StringField(
        "Duration of alcohol consumption", default=tbd)
    fld_alcohol_comments = StringField(
        "Additional comments for alcohol consumption", default=tbd)


class TobaccoExposureForm(BaseForm):
    fld_tobacco_active_passive = SelectField("Tobacco exposure (Passive and/or Active)",
                                             choices=PatientHistoryDict.tobacco_choice)
    fld_tobacco_active_passive_other = StringField('Other')
    fld_tobacco_type_passive = SelectField("Mode of passive consumption",
                                           choices=PatientHistoryDict.tobacco_type_passive_choice)
    fld_tobacco_type_passive_other = StringField("Other")
    fld_tobacco_type_passive_home = StringField("What is the specific source of passive exposure at home",
                                                default=tbd)
    fld_tobacco_type = SelectMultipleField(
        "Type of tobacco use", choices=PatientHistoryDict.tobacco_type_choice)
    fld_tobacco_type_other = StringField("Other")
    fld_tobacco_age = StringField(
        "Consumption of tobacco from which age (yrs)", default=tbd)
    fld_tobacco_freq = StringField(
        "Frequency of tobacco consumption", default=tbd)
    fld_tobacco_quant = StringField(
        "Quantity of tobacco consumed per week", default=tbd)
    fld_tobacco_duration = StringField(
        "Duration of tobacco consumption", default=tbd)
    fld_tobacco_comments = StringField(
        "Additional comments for tobacco consumption", default=tbd)


class BreastFeedingForm(BaseForm):
    fld_breast_feeding_children = SelectField(
        "Were all children breast fed?", choices=CommonDict.yes_no_choice)
    fld_breast_feeding_duration = TextAreaField('Please enter breast feeding duration in months for each child '
                                                '(in the format Child Number: Breast feed months: Preferred Breast Side; )')


class SymptomsRightBreastDurationForm(BaseForm):
    fld_pain_tender_right = SelectField(
        "Pain or tenderness", choices=PatientHistoryDict.symptom_absent_present_choice)
    fld_pain_tender_right_other = StringField("Duration")
    fld_lump_right = SelectField(
        "Lumps", choices=PatientHistoryDict.symptom_absent_present_choice)
    fld_lump_right_other = StringField("Duration")
    fld_nipple_discharge_right = SelectField("Nipple Discharge",
                                             choices=PatientHistoryDict.symptom_absent_present_choice)
    fld_nipple_discharge_right_other = StringField("Duration")
    fld_nipple_retraction_right = SelectField("Nipple retraction",
                                              choices=PatientHistoryDict.symptom_absent_present_choice)
    fld_nipple_retraction_right_other = StringField("Duration")
    fld_dimpling_right = SelectField(
        "Dimpling", choices=PatientHistoryDict.symptom_absent_present_choice)
    fld_dimpling_right_other = StringField("Duration")
    fld_discoloration_right = SelectField(
        "Discoloration", choices=PatientHistoryDict.symptom_absent_present_choice)
    fld_discoloration_right_other = StringField("Duration")
    fld_ulcer_right = SelectField(
        "Ulceration", choices=PatientHistoryDict.symptom_absent_present_choice)
    fld_ulcer_right_other = StringField("Duration")
    fld_eczema_right = SelectField(
        "Eczema", choices=PatientHistoryDict.symptom_absent_present_choice)
    fld_eczema_right_other = StringField("Duration")


class SymptomsLeftBreastDurationForm(BaseForm):
    fld_pain_tender_left = SelectField(
        "Pain or tenderness", choices=PatientHistoryDict.symptom_absent_present_choice)
    fld_pain_tender_left_other = StringField("Duration")
    fld_lump_left = SelectField(
        "Lumps", choices=PatientHistoryDict.symptom_absent_present_choice)
    fld_lump_left_other = StringField("Duration")
    fld_nipple_discharge_left = SelectField(
        "Nipple Discharge", choices=PatientHistoryDict.symptom_absent_present_choice)
    fld_nipple_discharge_left_other = StringField("Duration")
    fld_nipple_retraction_left = SelectField("Nipple retraction",
                                             choices=PatientHistoryDict.symptom_absent_present_choice)
    fld_nipple_retraction_left_other = StringField("Duration")
    fld_dimpling_left = SelectField(
        "Dimpling", choices=PatientHistoryDict.symptom_absent_present_choice)
    fld_dimpling_left_other = StringField("Duration")
    fld_discoloration_left = SelectField(
        "Discoloration", choices=PatientHistoryDict.symptom_absent_present_choice)
    fld_discoloration_left_other = StringField("Duration")
    fld_ulcer_left = SelectField(
        "ulceration", choices=PatientHistoryDict.symptom_absent_present_choice)
    fld_ulcer_left_other = StringField("Duration")
    fld_eczema_left = SelectField(
        "Eczema", choices=PatientHistoryDict.symptom_absent_present_choice)
    fld_eczema_left_other = StringField("Duration")


class PatientHistoryForm(SectionForm):
    fld_med_rec_no = StringField('Medical Record Number', default=tbd)
    fld_nam = StringField('Name of the patient', default=tbd)
    fld_id_type = StringField('Enter type of ID used', default=tbd)
    fld_id_no = StringField('Identity Number', default=tbd)
    fld_first_visit_date = DateField(
        'Date of first visit', default=date.today())
    fld_permanent_address = StringField('Permanent Address', default=tbd)
    fld_current_address = StringField(
        'Current Address', default='Same as Permanent Address')
    fld_contact_number = IntegerField('Contact Number', default=999)
    fld_alternative_contact = IntegerField(
        'Alternative Contact Number', default=999)
    fld_email = StringField('e-mail id', default=tbd)
    fld_occupation = StringField('Occupation', default=tbd)
    fld_gender = SelectField("Gender", choices=CommonDict.gender_choice)
    fld_gender_other = StringField('Other')
    fld_age = IntegerField('Current Age (yrs)', default=999)
    # todo format date.today() to dd/mm/yyyy
    fld_date_of_birth = DateField('Date Of Birth', default=date.today())
    fld_place_of_birth = StringField('Place Of Birth', default=tbd)
    fld_height_feet = StringField(
        'Height (in feet eg., 5ft 2in) ', default='0ft 0in')
    fld_weight_kg = FloatField('Weight (in kg)', default=999)
    fld_diet = SelectField("Diet", choices=PatientHistoryDict.diet_choice)
    fld_diet_other = StringField("Other")
    fld_nutrition_supplement_form_present = SelectField("Nutrition supplements taken?",
                                                        choices=CommonDict.form_yes_no_choice)
    nutrition_supplement_form = FormField(NutritionalSupplementsForm)
    fld_physical_activity_form_present = SelectField("Physical Activity done?",
                                                     choices=CommonDict.form_yes_no_choice)
    physical_activity_form = FormField(PhysicalActivityForm)
    fld_alcohol_consumption_form_present = SelectField("Alcohol Consumption",
                                                       choices=CommonDict.form_yes_no_choice)
    alcohol_consumption_form = FormField(AlcoholConsumptionForm)
    fld_tobacco_exposure_form_present = SelectField("Has the patient been exposed to tobacco?",
                                                    choices=CommonDict.form_yes_no_choice)
    tobacco_exposure_form = FormField(TobaccoExposureForm)
    fld_other_del_habits = StringField(
        "Other Deleterious Habits (if present give details)")
    fld_marital_status = SelectField(
        "Marital Status", choices=PatientHistoryDict.marital_status_choice)
    fld_marital_status_other = StringField('Other')
    fld_siblings = SelectField("Siblings", choices=CommonDict.yes_no_choice)
    fld_siblings_other = StringField("Other")
    fld_sister = IntegerField('Number of sisters', default=999)
    fld_brother = IntegerField('Number Of brothers', default=999)
    fld_child = SelectField("Children", choices=CommonDict.yes_no_choice)
    fld_child_other = StringField("Other")
    fld_daughter = IntegerField('Number of daughters', default=999)
    fld_son = IntegerField('Number of sons', default=999)
    fld_menarche = IntegerField('Age at menarche', default=999)
    fld_period_type = SelectField(
        "Period Type", choices=PatientHistoryDict.period_type_choice)
    fld_period_type_other = StringField('Other')
    fld_last_date_period = DateField(
        'Date of last menstrual Period', default=date.today())
    fld_menopausal_status = SelectField(
        "Menopausal Status", choices=PatientHistoryDict.menopausal_status_choice)
    fld_menopausal_status_other = StringField('Other')
    fld_menopause_age = IntegerField('Age at Menopause', default=999)
    fld_menopause_complications = StringField(
        "Complications associated with menopause", default=tbd)
    fld_pregnancy = IntegerField('Pregnancy carried to term', default=999)
    fld_pregnancy_complication = StringField(
        "Any complications during pregnancy", default=tbd)
    fld_abortion = IntegerField('Number of abortions', default=999)
    fld_pregnancy_number = IntegerField('Number of pregnancies', default=999)
    fld_age_first_child = IntegerField('Age of first child', default=999)
    fld_age_first_pregnancy = IntegerField(
        'Age at first pregnancy', default=999)
    fld_age_last_pregnancy = IntegerField('Age at last pregnancy', default=999)
    fld_twice_birth_in_year = SelectField("Twice birth in a year(not including twins)",
                                          choices=CommonDict.yes_no_choice)
    fld_twice_birth_in_year_other = StringField('Other')
    fld_breast_feed_form_present = SelectField(
        "Breast feeding", choices=CommonDict.form_yes_no_choice)
    breast_feed_form = FormField(BreastFeedingForm)
    fld_fertility_treat = SelectField(
        "Fertility Treatment", choices=CommonDict.yes_no_choice)
    fld_type_fertility_treat = StringField(
        "Type of fertility treatment", default=tbd)
    fld_detail_fertility_treat = StringField(
        "Details of fertility treatments", default=tbd)
    fld_cycles_fertility_treat = StringField(
        "Cycles of fertility treatment", default=tbd)
    fld_success_fertility_treat = SelectField(
        "Success of fertility treatment", choices=CommonDict.yes_no_choice)
    fld_success_fertility_treat_other = StringField('Other')
    fld_birth_control = StringField("Type of birth control used", default=tbd)
    fld_detail_birth_control = StringField(
        "Detail of birth control used", default=tbd)
    fld_duration_birth_control = StringField(
        "Duration of birth control used", default=tbd)
    fld_cancer_history = SelectField(
        "Diagnosed with cancer earlier?", choices=CommonDict.yes_no_choice)
    fld_family_cancer = SelectField(
        "Any family member been detected with cancer?", choices=CommonDict.yes_no_choice)
    fld_medical_history = SelectField(
        "Diagnosed with any other disease?", choices=CommonDict.yes_no_choice)
    fld_right_breast_symptoms_form_present = SelectField("Are there symptoms in the right breast?",
                                                         choices=CommonDict.form_yes_no_choice)
    fld_right_breast_symptoms_form_present_other = StringField('Other')
    right_breast_symptoms_form = FormField(SymptomsRightBreastDurationForm)
    fld_left_breast_symptoms_form_present = SelectField("Are there symptoms in the left breast?",
                                                        choices=CommonDict.form_yes_no_choice)
    left_breast_symptoms_form = FormField(SymptomsLeftBreastDurationForm)
    fld_complaint_detected_by = SelectField("Current complains detected by",
                                            choices=PatientHistoryDict.current_complain_choice)
    fld_complaint_detected_by_other = StringField('Other')
    fld_metastasis_symptoms = SelectMultipleField("Metastasis Symptoms",
                                                  choices=PatientHistoryDict.metastasis_symptoms_choice)
    fld_metastasis_symptoms_other = StringField('Other')
    fld_annual_income = SelectField(
        "Annual house income is", choices=PatientHistoryDict.annual_income_choice)
    fld_annual_income_other = StringField('Other')
    submit_button = SubmitField('Submit Form')


== == == =


class PatientHistoryForm(SectionForm):
    fld_age_diagnosis = IntegerField(
        'Age at diagnosis (yrs)', [validators.required()])
    fld_place_birth = StringField('Place of Birth')
    fld_height_cm = FloatField('Height (in cm)', [validators.required()])
    fld_weight_kg = FloatField('Weight (in kg)', [validators.required()])
    fld_diet = SelectField("Diet", choices=PatientHistoryDict.diet_choice)
    fld_diet_other = StringField("Other")
    fld_alcohol = SelectField("Alcohol consumption",
                              choices=CommonDict.yes_no_choice)
    fld_alcohol_other = StringField("Other")
    fld_alcohol_age = StringField(
        "Consumption of alcohol from which age (yrs)")
    fld_alcohol_quant = StringField("Quantity of alcohol consumed per week")
    fld_alcohol_duration = StringField("Duration of alcohol consumption")
    fld_alcohol_comments = StringField(
        "Additional comments for alcohol consumption")
    fld_tobacco = SelectField(
        "Tobacco exposure (Passive and/or Active)", choices=PatientHistoryDict.tobacco_choice)
    fld_tobacco_type_passive = SelectField("Mode of passive consumption",
                                           choices=PatientHistoryDict.tobacco_type_passive_choice)
    fld_tobacco_type_passive_other = StringField('Other')
    fld_tobacco_type_passive_home = StringField("What is the specific source of passive exposure at home",
                                                default='None')
    fld_tobacco_type = SelectMultipleField(
        "Type of tobacco use", choices=PatientHistoryDict.tobacco_type_choice)
    fld_tobacco_type_other = StringField("Other")
    fld_tobacco_age = StringField(
        "Consumption of tobacco from which age (yrs)")
    fld_tobacco_freq = StringField("Frequency of tobacco consumption")
    fld_tobacco_quant = StringField("Quantity of tobacco consumed per week")
    fld_tobacco_duration = StringField("Duration of tobacco consumption")
    fld_tobacco_comments = StringField(
        "Additional comments for tobacco consumption")
    fld_other_del_habits = StringField(
        "Other Deleterious Habits (if present give details)")
    submit_button = SubmitField('Submit Form')


class PhysicalActivityForm(SectionForm):
    def get_summary(self):
        return "Physical activity" + str(self.fld_type_phys_act.data)
    fld_type_phys_act = StringField("Type of physical activity")
    fld_freq_phys_act = StringField("Frequency of physical activity")
    submit_button = SubmitField('Submit Form')


class NutritionalSupplementsForm(SectionForm):
    def get_summary(self):
        return "Nutritional Supplements" + str(self.fld_nut_supplements_type.data)
    fld_nut_supplements_type = StringField(
        "Type of nutritional supplements taken")
    fld_nut_supplements_quant = StringField(
        "Quantity of nutritional supplements taken per day")
    fld_nut_supplements_duration = StringField(
        "Duration of nutritional supplements use")
    submit_button = SubmitField('Submit Form')


>>>>>> > db_flask/master
