from wtforms import StringField, validators, IntegerField, FloatField, SubmitField, SelectField, SelectMultipleField, DateField, FormField
from schema_forms.form_utilities import SectionForm, BaseForm
from db_dict.patient_history_dict import PatientHistoryDict
from db_dict.common_dict import CommonDict
from datetime import date

class PhysicalActivityForm(SectionForm):
    fld_phys_act = SelectField("Physical Activity", choices= CommonDict.yes_no_choice)
    fld_phys_act_other = StringField('Other')
    fld_type_phys_act = StringField("Type of physical activity")
    fld_freq_phys_act = StringField("Frequency of physical activity")
    submit_button = SubmitField('Submit Form')

class NutritionalSupplementsForm(SectionForm):
    fld_nut_supplements = SelectField("Nutrition Supplement taken ", choices = CommonDict.yes_no_choice)
    fld_nut_supplements = StringField("Other")
    fld_nut_supplements_type = StringField("Type of nutritional supplements taken")
    fld_nut_supplements_quant = StringField("Quantity of nutritional supplements taken per day")
    fld_nut_supplements_duration = StringField("Duration of nutritional supplements use")
    submit_button = SubmitField('Submit Form')

class AlcoholConsumptionForm(BaseForm):


    fld_alcohol_age = StringField("Consumption of alcohol from which age (yrs)")
    fld_alcohol_quant = StringField("Quantity of alcohol consumed per week")
    fld_alcohol_duration = StringField("Duration of alcohol consumption")
    fld_alcohol_comments = StringField("Additional comments for alcohol consumption")
    submit_button = SubmitField('Submit Form')

class MetastasisSymptomsForm(SectionForm):
    #add to main form
    fld_bon_pain = SelectField("Bone pain", choices=CommonDict.yes_no_choice)
    fld_cough = SelectField("Cough", choices=CommonDict.yes_no_choice)
    fld_jaun = SelectField("Jaundice", choices=CommonDict.yes_no_choice)
    fld_headache = SelectField("Headache", choices=CommonDict.yes_no_choice)
    fld_wei_los = SelectField("Weight loss", choices=CommonDict.yes_no_choice)
    submit_button = SubmitField('Submit Form')

class SymptomsRightBreastDurationForm(SectionForm):
    fld_pain_tender = StringField("Pain or tenderness", default = 'absent')
    fld_lump = StringField("Lumps", default = 'absent')
    fld_nip_dis = StringField("Nipple Discharge", default = 'absent')
    fld_nip_ret = StringField("Nipple retraction", default = 'absent')
    fld_dim = StringField("Dimpling", default = 'absent')
    fld_discol = StringField("Discoloration", default = 'absent')
    fld_ulcer = StringField("ulceration", default = 'absent')
    fld_ecz = StringField("Eczema", default = 'absent')
    submit_button = SubmitField('Submit Form')

class SymptomsLeftBreastDurationForm(SectionForm):
    fld_pain_tender = StringField("Pain or tenderness", default = 'absent')#same fld name?
    fld_lump = StringField("Lumps", default = 'absent')
    fld_nip_dis = StringField("Nipple Discharge", default = 'absent')
    fld_nip_ret = StringField("Nipple retraction", default = 'absent')
    fld_dim = StringField("Dimpling", default = 'absent')
    fld_discol = StringField("Discoloration", default = 'absent')
    fld_ulcer = StringField("ulceration", default = 'absent')
    fld_ecz = StringField("Eczema", default = 'absent')
    submit_button = SubmitField('Submit Form')

class TaboccoExposureForm(BaseForm):
    fld_tobacco = SelectField("Tobacco exposure (Passive and/or Active)", choices=PatientHistoryDict.tobacco_choice)
    fld_tobacco_type_passive = SelectField("Mode of passive consumption",
                                           choices=PatientHistoryDict.tobacco_type_passive_choice)
    fld_tobacco_type_passive_other = StringField("Other")
    fld_tobacco_type_passive_home = StringField("What is the specific source of passive exposure at home",
                                                default='None')
    fld_tobacco_type = SelectMultipleField("Type of tobacco use", choices=PatientHistoryDict.tobacco_type_choice)
    fld_tobacco_type_other = StringField("Other")
    fld_tobacco_age = StringField("Consumption of tobacco from which age (yrs)")
    fld_tobacco_freq = StringField("Frequency of tobacco consumption")
    fld_tobacco_quant = StringField("Quantity of tobacco consumed per week")
    fld_tobacco_duration = StringField("Duration of tobacco consumption")
    fld_tobacco_comments = StringField("Additional comments for tobacco consumption")
    submit_button = SubmitField('Submit Form')

class PatientHistoryForm(SectionForm):
    fld_med_rec_no = StringField('Medical Record Number') #medical record number is only numbers?shld i put integerfld?
    fld_nam = StringField('Name of the patient')
    fld_id_type = StringField('Enter type of ID used')
    fld_id_no = StringField('Identity Number')  #medical record number is only numbers? # difference between idcard and id number?
    fld_first_visit_date = DateField('Date of first visit', default=date.today())
    fld_permanent_address = StringField('Permanent Address')
    fld_current_address = StringField('Current Address', default='Same as Permanent Address')
    fld_contact_number = IntegerField('Contact Number')
    fld_alternative_contact = IntegerField('Alternative Contact Number')
    fld_email = StringField('e-mail id')
    fld_occupation = StringField('Occupation')
    fld_gender = SelectField("Gender", choices = CommonDict.gender_choice)
    fld_age = IntegerField('Current Age (yrs)', default = 50)
    #fld_age_diagnosis = IntegerField('Age at diagnosis (yrs)', [validators.required()]) # current age or age of diagnosis?
    fld_date_of_birth = DateField('Date Of Birth (DD/MM/YYYY)',default = date.today())
    fld_place_of_birth = StringField('Place Of Birth')
    fld_height_cm = FloatField('Height (in cm)', [validators.required()])
    fld_weight_kg = FloatField('Weight (in kg)', [validators.required()])
    fld_diet = SelectField("Diet", choices=PatientHistoryDict.diet_choice)
    fld_diet_other = StringField("Other")
    fld_alcohol_consumption_form = SelectField("Alcohol Consumtion",
                                                         choices=CommonDict.form_yes_no_choice)
    alcohol_consumption_form = FormField(AlcoholConsumptionForm)

    fld_tobacco_exposure_form = SelectField("Tobacco Exposure",
                                               choices=CommonDict.form_yes_no_choice)
    tobacco_exposure_form = FormField(TaboccoExposureForm)


    fld_other_del_habits = StringField("Other Deleterious Habits (if present give details)")
    #added
    fld_marital_status = StringField("Marital Status")    #add default as Married
    fld_siblings = SelectField("Siblings", choices=CommonDict.yes_no_choice)
    fld_siblings_other = StringField("Other")
    fld_sister = IntegerField('Number of Sisters') #number , default is 0
    fld_brother = IntegerField('Number Of Brothers') #number
    fld_child = SelectField("Children", choices=CommonDict.yes_no_choice)
    fld_child_other = StringField("Other")
    fld_daughter = IntegerField('Number of Daugthers') #fld is full form
    fld_son = IntegerField('Number of sons')
    fld_menarche = IntegerField('Age at Menarche')
    fld_period_type = SelectField("Period Type", choices=CommonDict.period_type_choice)
    fld_last_date_period = IntegerField('Date of last menstural Period')
    fld_menopausal_status = SelectField("Menopausal Status", choices=CommonDict.menopausal_status_choice)
    fld_menopause_age = IntegerField('Age at Menopause')
    fld_meno_complications = StringField("Complications associated with menopause")
    fld_pregnancy = IntegerField('Pregnancy carried to term')
    fld_pregnancy_complication = StringField("Any complications during pregnancy")
    fld_abortion = IntegerField('Number of abortions')
    fld_pregnancy_number = IntegerField('Number of pregnancies')
    fld_age_first_child = IntegerField('Age of first child')
    fld_age_first_pregnancy = IntegerField('Age at first pregnancy')
    fld_age_last_pregnancy = IntegerField('Age at last pregnancy')
    fld_twice_birth_in_year =  StringField("Twice birth in a year(not including twins)")   # is it a yes no question?
    fld_breast_feed = SelectField("Breast feeding", choices=CommonDict.yes_no_choice)
    #table to be added
#breast feeding detail table
    fld_fertility_treat = SelectField("Fertility Treatment", choices=CommonDict.yes_no_choice) # do we need to print the comment line attached to this question
    fld_type_fertility_treat = StringField("Type of fertility treatment")
    fld_detail_fertility_treat = StringField("Details of fertility treatments")
    fld_cycles_fertility_treat = StringField("Cycles of fertility treatment")
    fld_success_fertility_treat = SelectField("Success of fertility treatment", choices=CommonDict.yes_no_choice)
    fld_birth_control = StringField("Type of birth control used")
    fld_detail_birth_control = StringField("Detail of birth control used")
    fld_duration_birth_control = StringField("Duration of birth control used")
    #other medical history table

    #current symptoms table
    #SymptomsRightBreastDurationForm yes no question
    #cxhange variabel name
    fld_right_breast_symptoms_form_present = SelectField("Are there symmptoms in the right breast?",
                                                             choices=CommonDict.form_yes_no_choice)
    right_breast_symptoms_form = FormField(SymptomsRightBreastDurationForm)
    fld_left_breast_symptoms_form_present = SelectField("Are there symmptoms in the left breast?",
                                                         choices=CommonDict.form_yes_no_choice)
    left_breast_symptoms_form = FormField(SymptomsLeftBreastDurationForm)
    fld_curr_comp = SelectField("Current complains detected by", choices=PatientHistoryDict.current_complain_choice)
    fld_duration_curr_comp = StringField("Duration of current complains")
    fld_metastasis_symptoms = SelectMultipleField("Metastasis Symptoms", choices=PatientHistoryDict.metastasis_symptoms_choice)

    #table to be added
    fld_ann_hou_inc = SelectField("Annual house income is", choice=PatientHistoryDict.annual_income_choice)
    submit_button = SubmitField('Submit Form')





