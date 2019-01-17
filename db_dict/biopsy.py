from db_dict.common_dict import CommonDict

class BiopsyDict():
    def __init__(self, key, value):
        self.key = key
        self.value = value

    biopsy_reason_dict = {'tbd':"To be filled",'diagnostic':"Diagnostic",'follow_up':"Follow-up",
                          'nact_follow-up':"NACT follow up",'recurrence':"Recurrence",'other':"Other"}
    biopsy_site_dict = {'tbd':"To be filled",'left_breast':"Left Breast",'right_breast':"Right Breast",
                        'left_axillary':"Left Axillary",'right_axillary':"Right Axillary",'other':"Other"}
    biopsy_block_id_dict ={'tbd':"To be filled",'physically_present_at_pccm':"If the blocks are physically present at PCCM enter the block id from the blocks",
                           'not_physically_present_at_pccm':"If the blocks are not physically present at PCCM enetr the block ID from the biopsy report",
                           'no_source_of_block':"If there is no source for the block ID mention as requires follow up",'other':"Other"}  #major doubt
    biopsy_block_source_dict = {'tbd':"To be filled",'ag_diagnostics':"A.G. Diagnostics",'ruby_hall_clinic':"Ruby Hall Clinic",
                           'srl_pathlab':"SRL Pathlab",'golwilkar_lab':"Golwilkar Lab",'other':"Other"}
    biopsy_type_dict ={'tbd':"To be filled","direct":"Direct", "usg_guided":"USG Guided","vab":"VAB",
                       "trucut":"Tru-cut", "stereo":"Steriotactic", 'other':"Other"}

    biopsy_custody_pccm_dict = {'tbd':"To be filled","Y":"In PCCM Custody", "N":"Not in PCCM custody"}
    tumour_grade_dict = {'tbd':"To be filled","1":'Grade 1', "2": "Grade 2","3": "Grade 3"}
    lymphovascular_emboli_dict = {'tbd':"To be filled","Y": "Lymphovascular Emboli Seen",
                                  "N":"No Lymphovascular Emboli Seen", 'report': 'Not mentioned in Report',
                                  'other': 'Other'}
    dcis_biopsy_dict = {'tbd':"To be filled","Y":"DCIS seen", "N": "DCIS not seen", 'report': 'Not mentioned in Report',
                                  'other': 'Other'}
    tumour_er_dict = {'tbd':"To be filled","pos":"Positive", "neg": "Negative", 'report': 'Not mentioned in Report',
                                  'other': 'Other'}
    tumour_pr_dict = {'tbd':"To be filled","pos":"Positive", "neg": "Negative", 'report': 'Not mentioned in Report',
                                  'other': 'Other'}
    tumour_her2_dict = {'tbd':"To be filled","pos": "Positive", "eqv": "Equivocal", "neg": "Negative",
                        'report': 'Not mentioned in Report', 'other': 'Other'}
    tumor_biopsy_fish_dict = {'tbd':"To be filled",'positive':"Positive",'negetive':"Negetive",'not_done':"Not Done",
                              'other': 'Other'}
    fnac_dict = {'tbd':"To be filled","Y":"Done", "N":"Not Done", 'report': 'Not mentioned in Report',
                                  'other': 'Other'}
    fnac_location_dict = {'tbd':"To be filled", "rb":"Right", "lb":"Left", "both":"Both",
                          'report': 'Not mentioned in Report', 'other': 'Other'}
    fnac_diagnosis_dict = {'tbd':"To be filled", "normal":"Normal", "benign":"Benign", "malignant":"Malignant",
                           'report': 'Not mentioned in Report', 'other': 'Other'}

    biopsy_reason_choice = CommonDict.gender_choice(biopsy_reason_dict)
    biopsy_site_choice = CommonDict.gender_choice(biopsy_site_dict)
    biopsy_block_id_choice = CommonDict.generate_choice(biopsy_block_id_dict)
    biopsy_block_source_choice = CommonDict.generate_choice(biopsy_block_source_dict)
    biopsy_type_choice = CommonDict.generate_choice(biopsy_type_dict)
    biopsy_custody_pccm_choice = CommonDict.generate_choice(biopsy_custody_pccm_dict)
    tumour_grade_choice = CommonDict.generate_choice(tumour_grade_dict)
    lymphovascular_emboli_choice = CommonDict.generate_choice(lymphovascular_emboli_dict)
    dcis_biopsy_choice = CommonDict.generate_choice(dcis_biopsy_dict)
    tumour_er_choice = CommonDict.generate_choice(tumour_er_dict)
    tumour_pr_choice = CommonDict.generate_choice(tumour_pr_dict)
    tumour_her2_choice = CommonDict.generate_choice(tumour_her2_dict)
    tumor_biopsy_fish_choice = CommonDict.generate_choice(tumor_biopsy_fish_dict)
    fnac_choice = CommonDict.generate_choice(fnac_dict)
    fnac_location_choice = CommonDict.generate_choice(fnac_location_dict)
    fnac_diagnosis_choice = CommonDict.generate_choice(fnac_diagnosis_dict)