from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.fields.html5 import DateField
from db_dict.chemo import ChemoDict
from db_dict.common_dict import CommonDict
from schema_forms.form_utilities import SectionForm

tbd = 'To be filled'


class NeoAdjuvantChemoTherapyForm (SectionForm):
    def get_summary(self):
        return self.fld_nact_status.data

    fld_place_nact = SelectField(
        'Has neo adjuvant therapy been done at PCCM?', choices=ChemoDict.place_nact_choice)
    fld_details_nact = SelectField('Are neo adjuvant therapy details available?',
                                   choices=ChemoDict.details_nact_choice)
    fld_nact_status = SelectField('Has neo adjuvant therapy been done for the patient?',
                                  choices=CommonDict.yes_no_choice)
    fld_plan_nact = StringField("What is the plan of NACT (for eg., 4 cycles AC + 12 cycles Paclitaxel)",
                                default=tbd)
    fld_date_start_nact = DateField("Date of starting neo-adjuvant therapy")
    fld_patient_wt = StringField(
        'Weight of patient at start of therapy (in kgs)', default=tbd)
    fld_patient_wt_additional = StringField('Weight of patient at any other point in therapy (cycle; wieght)',
                                            default='No')
    fld_nact_response_by = StringField(
        "Response to NACT measured by", default=tbd)
    fld_nact_response = SelectField(
        "Response of tumour", choices=ChemoDict.tumour_response_choice)
    fld_nact_response_other = StringField("Other")
    fld_tumour_nact_size = StringField("Size of tumour")
    fld_tumour_nact_size_unit_ = StringField("Size unit", default="cm")
    fld_tumour_check_date = DateField("Date tumour response checked")
    fld_trast_nact = SelectField(
        "Trastuzumab used?", choices=CommonDict.yes_no_choice)
    fld_trast_nact_other = StringField("Other")
    fld_trast_regime_nact = SelectField(
        "Trastuzumab use was", choices=ChemoDict.trast_regime_nact_choice)
    fld_trast_regime_nact_other = StringField("Other")
    fld_trast_courses_nact = StringField(
        "Number of courses of trastuzumab/herceptin taken", default=tbd)
    fld_date_complete_nact = DateField("Date of completion of NACT")
    fld_complete_nact_other = SelectField("Reason for discontinuation",
                                          choices=ChemoDict.reason_incomplete_nact_choice)
    fld_hormone_therapy_nact = SelectField(
        "Was hormone therapy given?", choices=CommonDict.yes_no_other_choice)
    fld_hormone_therapy_nact_other = SelectField(
        'Hormone therapy type', choices=ChemoDict.trast_regime_nact_choice)
    fld_therapy_duration_nact = StringField(
        "What was the duration of therapy?")
    fld_therapy_side_nact = SelectField(
        "Were any side effects observed", choices=CommonDict.yes_no_other_choice)
    fld_therapy_side_nact_other = StringField(
        "Please give details of side effects observed")
    fld_complete_nact = SelectField(
        "Was NACT completed as per schedule?", choices=CommonDict.yes_no_other_choice)
    fld_change_nact_plan = SelectField(
        "Changes to NACT treatment", choices=ChemoDict.nact_change_choice)
    fld_change_nact_plan_type = StringField(
        "Type of change to NACT plan", default="No change to NACT plan")
    submit_button = SubmitField('Submit Form')


class NeoAdjuvantChemoDrugForm (SectionForm):
    fld_drug_nact = SelectField(
        "Drug used for therapy", choices=ChemoDict.drugs_choice)
    fld_drug_other_nact = StringField("Other")
    fld_dose_nact = IntegerField("Dose of drug")
    fld_drug_unit_nact = StringField("Unit of druge dose", default="mg")
    fld_cyc_freq_week_nact = IntegerField('Cycle Frequency (frequency per week, so three weekly is 3 and weekly is 1)',
                                          default=3)
    fld_number_cycle_nact = IntegerField(
        'Number of cycles actually given', default=0)
    submit_button = SubmitField('Submit Form')


class NeoAdjuvantChemoToxicityForm (SectionForm):
    fld_tox_nact = SelectField(
        "Were there any toxic effects?", choices=CommonDict.yes_no_choice)
    fld_tox_type_nact = SelectField(
        "Toxic effects", choices=ChemoDict.toxic_side_effects_choice)
    fld_tox_type_other_nact = StringField("Other")
    fld_tox_grade_nact = SelectField(
        "Grade of toxic effects", choices=ChemoDict.toxic_side_effects_grade_choice)
    fld_tox_grade_other_nact = StringField("Other")
    fld_treatment_nact = StringField(
        "Treatment given for toxicity", default=tbd)
    fld_response_treatment_nact = SelectField("Response to treatment for toxicity",
                                              choices=ChemoDict.tumour_response_choice)
    fld_response_treatment_other_nact = StringField("Other")
    fld_cyc_tox_nact = IntegerField(
        "Cycle at which toxicity occured", default=0)
    submit_button = SubmitField('Submit Form')
