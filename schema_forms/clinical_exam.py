from wtforms import StringField, IntegerField, SubmitField, SelectField, SelectMultipleField, validators, TextAreaField, FormField, FloatField
from schema_forms.form_utilities import SectionForm, BaseForm
from db_dict.common_dict import CommonDict
from db_dict.clinical_exam_dict import ClinicalExamDict

tbd = 'To be filled'

class PalpableLumpForm(BaseForm):
    fld_palpable_lump = SelectMultipleField("The palpable lump is ", choices=ClinicalExamDict.options_choice)
    fld_palpable_lump_other = StringField("Other")
    fld_breast_lump = SelectMultipleField("The lump is present in", choices=CommonDict.breast_choice)
    fld_breast_lump_other = StringField("Other")
    fld_lump_localisation = SelectMultipleField("location of lump", choices=CommonDict.breast_location_choice)
    fld_lump_localisation_other = StringField("Other")
    submit_button = SubmitField('Submit Form')

class MetastasisForm(BaseForm):
    fld_metastasis_breast = SelectField("Metastasis in", choices=CommonDict.breast_choice)
    fld_metastasis_breast_other = StringField("Other")
    fld_metastasis_location = SelectField("Location of metastasis", choices=CommonDict.breast_location_choice)
    fld_metastasis_location_other = StringField("Other")
    fld_metastasis_type = SelectField("Type of metastasis", choices=ClinicalExamDict.metastasis_type_choice)
    fld_metastasis_type_other = StringField("Other")
    submit_button = SubmitField('Submit Form')

class NippleDischargeForm(BaseForm):
    fld_discharge = SelectField("Nipple discharge seen in?",choices=CommonDict.breast_choice)
    fld_discharge_other = StringField("Other")
    fld_discharge_type = SelectField("Type of discharge", choices=ClinicalExamDict.metastasis_type_choice)
    fld_discharge_type_other = StringField("Other")
    submit_button = SubmitField('Submit Form')

class SkinChangeForm(BaseForm):
    fld_skin_change_location = SelectField("Location of skin change", choices=CommonDict.breast_choice)
    fld_skin_change_location_other = StringField("Other")
    fld_skin_change_type = SelectField("Type of skin change", choices=ClinicalExamDict.skin_change_type_choice)
    fld_skin_change_type_other = StringField("Other")
    submit_button = SubmitField('Submit Form')

class PalpableAxillaryNodeForm(BaseForm):
    fld_palpable_axillary_node_location = SelectField("Palpable axillary Node present in", choices=CommonDict.breast_choice)
    fld_palpable_axillary_node_location_other = StringField("Other")
    fld_axillary_node_number = IntegerField("Number of node", default=0)
    fld_axillary_node_size = FloatField("Size of node", default=0.0 )
    fld_axillary_node_fixity = SelectField("Fixity of axillary nodes", choices=CommonDict.yes_no_choice)
    fld_axillary_node_fixity_other = StringField("Other")
    submit_button = SubmitField('Submit Form')

class SupraClavicularNodeForm(BaseForm):
    fld_supraclavicular_node_location = SelectField("Location of supraclavicular node", choices=CommonDict.breast_choice)
    fld_supraclavicular_node_location_other = StringField("Other")
    fld_supraclavicular_node_number = IntegerField("Number of supraclavicular node", default=0)
    fld_supraclavicular_node_size = FloatField("Size of supraclavicular node", default=0.0)
    fld_supraclavicular_node_fixity = SelectField("Supraclavicular node fixity?", choices=CommonDict.yes_no_choice)
    fld_supraclavicular_node_fixity_other = StringField("Other")
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
    fld_metastasis_form_present = SelectField("Metastasis", choices=CommonDict.form_yes_no_choice)
    metastasis_form = FormField(MetastasisForm)
    fld_tender = SelectField("Tenderness in breast?", choices=CommonDict.breast_choice)
    fld_tender_other = StringField("Other")
    fld_retract = SelectField("Nipple retraction?", choices=CommonDict.breast_choice)
    fld_retract_other = StringField("Other")
    fld_discharge_form_present = SelectField("Nipple discharge", choices=CommonDict.yes_no_choice)
    discharge_form = FormField(NippleDischargeForm)
    fld_skin_change_form_present = SelectField("Any skin changes?", choices=CommonDict.yes_no_choice)
    skin_change_form = FormField(SkinChangeForm)
    fld_palpable_axillary_node_form_present = SelectField("Palpable Axillary Node?",choices=CommonDict.yes_no_choice)
    palpable_axillary_node_form = FormField(PalpableAxillaryNodeForm)
    fld_supraclavicular_node_form_present = SelectField("Palpable supraclavicular nodes", choices=CommonDict.yes_no_choice)
    supraclavicular_node_form = FormField(SupraClavicularNodeForm)
    fld_contralateral_breast = SelectField("Contralateral Breast", choices=ClinicalExamDict.contalateral_breast_choice)
    fld_contralateral_breast_other = StringField("Other")
    fld_arm_edema = SelectField("Edema of arm",choices=ClinicalExamDict.arm_edema_choice)
    fld_arm_edema_other = StringField("Other")
    fld_arm_circ_right = FloatField("Circumference of right arm(cm)", default=0)
    fld_arm_vol_right = FloatField("Upper limb volume - right arm (cc): ",default=0)
    fld_arm_elbow_right = FloatField("Distance from the elbow - right arm (cm): ",default=0)
    fld_arm_circ_left = FloatField("Circumference of left arm (cm): ",default=0)
    fld_arm_vol_left = FloatField("Upper limb volume - left arm (cc): ",default=0)
    fld_arm_elbow_left = FloatField("Distance from the elbow - left arm (cml): ",default=0)
    fld_follow_up_advised = StringField("Follow up tests advised for patient:")






    submit_button = SubmitField('Submit Form')

