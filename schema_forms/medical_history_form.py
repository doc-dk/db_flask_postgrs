from wtforms import StringField, IntegerField, SubmitField, SelectField, SelectMultipleField
from schema_forms.form_utilities import SectionForm
from db_dict.patient_history_dict import PatientHistoryDict

tbd = 'To be filled'

class PatientCancerHistoryForm(SectionForm):
    fld_previous_cancer_history = StringField("Previous Cancer History(use ; to differentiate between multiple cancer history)", default=tbd)
    fld_type_of_previous_cancer = StringField("Type of previous cancer", default=tbd)
    fld_year_of_diagnosis = IntegerField("Year of diagnosis", default='0000')
    fld_treatment_taken = SelectMultipleField("Type of treatment taken", choices = PatientHistoryDict.treatment_type_choice)
    fld_treatment_taken_other = StringField('Other')
    fld_details_of_treatment_take = StringField('Details of treatment taken(add all treatment details)', default=tbd)
    fld_treatment_duration = StringField('Duration of treatment', default=tbd)
    submit_button = SubmitField('Submit Form')

class MedicalHistoryForm(SectionForm):
    fld_type_pf_medical_history = StringField('Type of medical history', default=tbd)
    fld_year_of_diagnosis = StringField("Year of diagnosis", default=tbd)
    fld_treatment = StringField("treatment", default=tbd)
    submit_button = SubmitField('Submit Form')

class FamilyHistoryForm(SectionForm):
    fld_type_of_cancer = StringField('Type of Cancer', default=tbd)
    fld_degree_of_relation = SelectField("Degree of relation", choices= PatientHistoryDict.degree_of_relation_choice)
    fld_degree_of_relation_other = ("Other")
    fld_type_of_relation = StringField("Type of Relation", default=tbd)
    fld_age_at_diagnosis = IntegerField("Age at Diagnosis", default=0)
    submit_button = SubmitField('Submit Form')

