from wtforms import StringField, validators, IntegerField, FloatField, SubmitField, SelectField, SelectMultipleField, DateField, FormField
from schema_forms.form_utilities import SectionForm, BaseForm
from db_dict.patient_history_dict import PatientHistoryDict
from db_dict.common_dict import CommonDict
from datetime import date

tbd = 'To be filled'
class AlcoholConsumptionForm(BaseForm):
    fld_alcohol_age = StringField("Consumption of alcohol from which age (yrs)", default=tbd)
    fld_alcohol_quant = StringField("Quantity of alcohol consumed per week", default=tbd)
    fld_alcohol_duration = StringField("Duration of alcohol consumption", default=tbd)
    fld_alcohol_comments = StringField("Additional comments for alcohol consumption", default=tbd)


class TaboccoExposureForm(BaseForm):
    fld_tobacco_active_passive = SelectField("Tobacco exposure (Passive and/or Active)", choices=PatientHistoryDict.tobacco_choice)
    fld_tobacco_active_passive_other = StringField('Other')
    fld_tobacco_type_passive = SelectField("Mode of passive consumption",
                                           choices=PatientHistoryDict.tobacco_type_passive_choice)
    fld_tobacco_type_passive_other = StringField("Other")
    fld_tobacco_type_passive_home = StringField("What is the specific source of passive exposure at home",
                                                default='None')
    fld_tobacco_type = SelectMultipleField("Type of tobacco use", choices=PatientHistoryDict.tobacco_type_choice)
    fld_tobacco_type_other = StringField("Other")
    fld_tobacco_age = StringField("Consumption of tobacco from which age (yrs)", default=tbd)
    fld_tobacco_freq = StringField("Frequency of tobacco consumption", default=tbd)
    fld_tobacco_quant = StringField("Quantity of tobacco consumed per week", default=tbd)
    fld_tobacco_duration = StringField("Duration of tobacco consumption", default=tbd)
    fld_tobacco_comments = StringField("Additional comments for tobacco consumption", default=tbd)


class SymptomsRightBreastDurationForm(BaseForm):
    fld_pain_tender = StringField("Pain or tenderness", default = 'absent')
    fld_lump = StringField("Lumps", default = 'absent')
    fld_nip_dis = StringField("Nipple Discharge", default = 'absent')
    fld_nip_ret = StringField("Nipple retraction", default = 'absent')
    fld_dim = StringField("Dimpling", default = 'absent')
    fld_discol = StringField("Discoloration", default = 'absent')
    fld_ulcer = StringField("ulceration", default = 'absent')
    fld_ecz = StringField("Eczema", default = 'absent')
    submit_button = SubmitField('Submit Form')

class SymptomsLeftBreastDurationForm(BaseForm):
    fld_pain_tender = StringField("Pain or tenderness", default = 'absent')#same fld name?
    fld_lump = StringField("Lumps", default = 'absent')
    fld_nip_dis = StringField("Nipple Discharge", default = 'absent')
    fld_nip_ret = StringField("Nipple retraction", default = 'absent')
    fld_dim = StringField("Dimpling", default = 'absent')
    fld_discol = StringField("Discoloration", default = 'absent')
    fld_ulcer = StringField("ulceration", default = 'absent')
    fld_ecz = StringField("Eczema", default = 'absent')
    submit_button = SubmitField('Submit Form')

class PatientHistoryForm(SectionForm):
    fld_med_rec_no = StringField('Medical Record Number', default=tbd)
    fld_nam = StringField('Name of the patient', default=tbd)
    fld_id_type = StringField('Enter type of ID used', default=tbd)
    fld_id_no = StringField('Identity Number', default=tbd)
    fld_first_visit_date = DateField('Date of first visit', default=date.today())
    fld_permanent_address = StringField('Permanent Address', default=tbd)
    fld_current_address = StringField('Current Address', default='Same as Permanent Address')
    fld_contact_number = IntegerField('Contact Number')
    fld_alternative_contact = IntegerField('Alternative Contact Number')
    fld_email = StringField('e-mail id', default=tbd)
    fld_occupation = StringField('Occupation', default=tbd)
    fld_gender = SelectField("Gender", choices = CommonDict.gender_choice)
    fld_gender_other = StringField('Other')
    fld_age = IntegerField('Current Age (yrs)', default = 0)
    #fld_age_diagnosis = IntegerField('Age at diagnosis (yrs)', [validators.required()]) # current age or age of diagnosis?
    fld_date_of_birth = DateField('Date Of Birth (YYYY/MM/DD)',default = date.today())
    fld_place_of_birth = StringField('Place Of Birth', default=tbd)
    fld_height_cm = FloatField('Height (in cm)', [validators.required()])
    fld_weight_kg = FloatField('Weight (in kg)', [validators.required()])
    fld_diet = SelectField("Diet", choices=PatientHistoryDict.diet_choice)
    fld_diet_other = StringField("Other", default=tbd)
    fld_nutrition_supplement = SelectField("Nutritional Supplement taken?", choices=CommonDict.yes_no_choice)
    fld_physical_activity = SelectField("Any physical activity done?", choices=CommonDict.yes_no_choice)
    fld_alcohol_consumption_form_present = SelectField("Alcohol Consumtion",
                                                         choices=CommonDict.form_yes_no_choice)
    alcohol_consumption_form = FormField(AlcoholConsumptionForm)
    fld_tobacco_exposure_form_present = SelectField("Has the patient been exposed to tobacco?",
                                               choices=CommonDict.form_yes_no_choice)
    tobacco_exposure_form = FormField(TaboccoExposureForm)
    fld_other_del_habits = StringField("Other Deleterious Habits (if present give details)")
    fld_marital_status = StringField("Marital Status", default = 'married')
    fld_siblings = SelectField("Siblings", choices=CommonDict.yes_no_choice)
    fld_siblings_other = StringField("Other")
    fld_sister = IntegerField('Number of Sisters', default = 0)
    fld_brother = IntegerField('Number Of Brothers', default = 0)
    fld_child = SelectField("Children", choices=CommonDict.yes_no_choice)
    fld_child_other = StringField("Other")
    fld_daughter = IntegerField('Number of Daugthers', default = 0)
    fld_son = IntegerField('Number of sons', default = 0)
    fld_menarche = IntegerField('Age at Menarche', default = 0)
    fld_period_type = SelectField("Period Type", choices=PatientHistoryDict.period_type_choice)
    fld_period_type_other = StringField('Other')
    fld_last_date_period = DateField('Date of last menstrual Period', default=date.today())
    fld_menopausal_status = SelectField("Menopausal Status", choices=PatientHistoryDict.menopausal_status_choice)
    fld_menopausal_status_other = StringField('Other')
    fld_menopause_age = IntegerField('Age at Menopause', default = 0)
    fld_menopause_complications = StringField("Complications associated with menopause", default=tbd)
    fld_pregnancy = IntegerField('Pregnancy carried to term', default = 0)
    fld_pregnancy_complication = StringField("Any complications during pregnancy", default=tbd)
    fld_abortion = IntegerField('Number of abortions', default= 0)
    fld_pregnancy_number = IntegerField('Number of pregnancies', default=0)
    fld_age_first_child = IntegerField('Age of first child',default= 0)
    fld_age_first_pregnancy = IntegerField('Age at first pregnancy', default=0)
    fld_age_last_pregnancy = IntegerField('Age at last pregnancy', default=0)
    fld_twice_birth_in_year =  SelectField("Twice birth in a year(not including twins)", choices = CommonDict.yes_no_choice)
    fld_breast_feed = SelectField("Breast feeding", choices=CommonDict.yes_no_choice)
    fld_fertility_treat = SelectField("Fertility Treatment", choices=CommonDict.yes_no_choice)
    fld_type_fertility_treat = StringField("Type of fertility treatment", default=tbd)
    fld_detail_fertility_treat = StringField("Details of fertility treatments", default=tbd)
    fld_cycles_fertility_treat = StringField("Cycles of fertility treatment", default=tbd)
    fld_success_fertility_treat = SelectField("Success of fertility treatment", choices=CommonDict.yes_no_choice)
    fld_success_fertility_treat_other = StringField('Other')
    fld_birth_control = StringField("Type of birth control used", default=tbd)
    fld_detail_birth_control = StringField("Detail of birth control used", default=tbd)
    fld_duration_birth_control = StringField("Duration of birth control used", default=tbd)
    fld_cancer_history = SelectField("Diagnosed with cancer earlier?", choices=CommonDict.yes_no_choice)
    fld_family_cancer = SelectField("Any family member been detected with cancer?", choices=CommonDict.yes_no_choice)
    fld_medical_history = SelectField("Diagnosed with any other disease?", choices=CommonDict.yes_no_choice)
    fld_right_breast_symptoms_form_present = SelectField("Are there symmptoms in the right breast?",
                                                             choices=CommonDict.form_yes_no_choice)
    fld_right_breast_symptoms_form_present_other = StringField('Other')
    right_breast_symptoms_form = FormField(SymptomsRightBreastDurationForm)
    fld_left_breast_symptoms_form_present = SelectField("Are there symmptoms in the left breast?",
                                                         choices=CommonDict.form_yes_no_choice)
    fld_left_breast_symptoms_form_present_other = StringField('Other')
    left_breast_symptoms_form = FormField(SymptomsLeftBreastDurationForm)
    fld_complain_detected_by = SelectField("Current complains detected by", choices=PatientHistoryDict.current_complain_choice)
    fld_complain_detected_by_other = StringField('Other')
    fld_duration_current_complain = StringField("Duration of current complains", default=tbd)
    fld_metastasis_symptoms = SelectMultipleField("Metastasis Symptoms", choices=PatientHistoryDict.metastasis_symptoms_choice)
    fld_metastasis_symptoms_other = StringField('Other')
    fld_annual_income = SelectField("Annual house income is", choices=PatientHistoryDict.annual_income_choice)
    fld_annual_income_other = StringField('Other')
    submit_button = SubmitField('Submit Form')

class PhysicalActivityForm(SectionForm):
    fld_phys_act = SelectField("Physical Activity", choices= CommonDict.yes_no_choice)
    fld_phys_act_other = StringField('Other')
    fld_type_phys_act = StringField("Type of physical activity", default=tbd)
    fld_freq_phys_act = StringField("Frequency of physical activity", default=tbd)
    submit_button = SubmitField('Submit Form')

class NutritionalSupplementsForm(SectionForm):
    fld_nut_supplements = SelectField("Nutrition Supplement taken ", choices = CommonDict.yes_no_choice)
    fld_nut_supplements_other = StringField("Other")
    fld_nut_supplements_type = StringField("Type of nutritional supplements taken", default=tbd)
    fld_nut_supplements_quant = StringField("Quantity of nutritional supplements taken per day", default=tbd)
    fld_nut_supplements_duration = StringField("Duration of nutritional supplements use", default=tbd)
    submit_button = SubmitField('Submit Form')