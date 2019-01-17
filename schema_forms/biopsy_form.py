from wtforms import StringField, validators, IntegerField, SelectField, SubmitField, TextAreaField
from wtforms.fields.html5 import DateField
from db_dict.biopsy import BiopsyDict
from schema_forms.form_utilities import SectionForm
from db_dict.common_dict import CommonDict
from datetime import date


class BiopsyForm (SectionForm):
    def get_summary(self):
        return self.fld_biopsy_tumour_diagnosis.data


    fld_block_serial_number_biopsy = StringField('Block Serial Number', [validators.Length(min=1, max=50)])
    fld_block_location_biopsy = StringField("Block Location ID (Cabinet No.-Drawer No.-Column No.-Front/Back",
                                            default='To be Filled')
    fld_block_current_location_biopsy = StringField("Current location of block")
    fld_reason_for_biopsy = SelectField("Reason for biopsy", choices=BiopsyDict.biopsy_reason_choice)
    fld_reason_for_biopsy_other = StringField("Give details")

    fld_biopsy_site = SelectField("Site of biopsy", choices=BiopsyDict.biopsy_site_choice)
    fld_biopsy_site_other = StringField("Other")
    fld_biopsy_custody_pccm = SelectField('Is the biopsy report in PCCM custody?',
                                          choices=BiopsyDict.biopsy_custody_pccm_choice)#is this the cjoice as mentioned or yes/no?
    fld_biopsy_custody_pccm_other = StringField("Other")
    fld_block_received_pccm_date = DateField("Date when block was placed in the cabinet", default=date.today())
    fld_biopsy_ihc_report_pccm = SelectField("Biopsy IHC report in PCCM custody", choices=CommonDict.yes_no_choice)
    fld_biopsy_block_id = StringField("Biopsy Block ID", choices=BiopsyDict.biopsy_block_id_choice)#major doubt
    fld_biopsy_block_id_other = StringField("other")
    fld_biopsy_no_of_blocks = IntegerField("Number of blocks")
    fld_biopsy_date = DateField("Date of Biopsy", default=date.today())
    fld_biopsy_block_source = SelectField("Reports have been generated from", choices=BiopsyDict.biopsy_block_source_choice)
    fld_biopsy_block_source_other = StringField("Give details")
    fld_biopsy_lab_id_sid = StringField("Biopsy Lab ID")
    fld_biopsy_type = SelectField("Biopsy Type", choices=BiopsyDict.biopsy_type_choice)
    fld_biopsy_type_other = StringField("Other")
    fld_biopsy_diagnosis = TextAreaField('Mention the diagnosis in its fullform.'
                                         ' Eg: Infiltrating Duct Carcinoma/Invasive Mammary Carcinoma/ DCIS/Fibroadenoma; '
                                         'Infiltrating Duct Carcinoma + DCIS')
    fld_biopsy_diagnosis_comment = StringField("Descriptive or indicative notes while diagnosis")
    fld_biopsy_tumour_grade = SelectField("Tumour Grade", choices=BiopsyDict.tumour_grade_choice)
    fld_biopsy_tumour_grade_other = StringField("Give details")
    fld_biopsy_lymphovascular_emboli = SelectField('Are Lymphovascular emboli seen?',
                                                   choices=BiopsyDict.lymphovascular_emboli_choice)
    fld_biopsy_lymphovascular_emboli_other = StringField("Other")
    fld_dcis_biopsy = SelectField("Does the biopsy show DCIS", choices=BiopsyDict.dcis_biopsy_choice)
    fld_dcis_biopsy_other = StringField("Other")
    fld_tumour_er_biopsy = SelectField("ER Status", choices=BiopsyDict.tumour_er_choice)
    fld_tumour_er_biopsy_other = StringField("Other")
    fld_tumour_er_percent_biopsy = StringField("ER Percent")
    fld_tumour_pr_biopsy = SelectField("PR Status", choices=BiopsyDict.tumour_pr_choice)
    fld_tumour_pr_biopsy_other = StringField("Other")
    fld_tumour_pr_percent_biopsy = StringField("PR Percent")
    fld_tumour_her2_biopsy = SelectField("HER2 Status", choices=BiopsyDict.tumour_her2_choice)
    fld_tumour_her2_biopsy_other = StringField("Other")
    fld_tumour_her2_grade_biopsy = StringField("HER2 Grade", default="0")
    fld_tumor_biopsy_fish = SelectField("Tumor biopsy FISH", choices=BiopsyDict.tumor_biopsy_fish_choice)
    fld_tumor_biopsy_fish_other = StringField("Other")
    fld_tumour_ki67_biopsy = StringField("Ki67 Percent", default="0")
    fld_fnac = SelectField("Lymph Node biopsy FNAC", choices=BiopsyDict.fnac_choice)
    fld_fnac_other = StringField("Other")
    fld_fnac_location = SelectField("FNAC Location", choices=BiopsyDict.fnac_location_choice)
    fld_fnac_location_other = StringField("Other")
    fld_fnac_diagnosis = SelectField("FNAC Diagnosis", choices=BiopsyDict.fnac_diagnosis_choice)
    fld_fnac_diagnosis_other = StringField("Other")
    submit_button = SubmitField('Submit Form')
