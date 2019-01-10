from db_dict.common_dict import CommonDict

class ClinicalExamDict():
    def __init__(self, key, value):
        self.key = key
        self.value = value

    palpable_dict = {'tbd':"To be filled",'definite':"Definite", 'vague':"Vague", 'diffuse':"Diffuse", 'nil':"Nil",
                    'other':"Other"}
    lump_size_dict = {'tbd':"To be filled",'1':"less than 2cm",'2':"2-5cm",'3':"more than 5cm",'other':"Other"}
    lump_number_dict = {'tbd':"To be filled",'single':"Single",'multiple':"Multiple",'other':"Other"}
    lump_consistency_dict = {'tbd':"To be filled",'soft':"Soft",'Firm':"Firm",'hard':"Hard",'cystic':"Cystic",
                             'mobile':"Mobile",'other':"Other"}
    lump_fixity_dict = {'tbd':"To be filled",'skin':"Skin",'chest wall':"Chest_Wall",
                        'Pectoral_major_muscle':"Pectoral major muscle",'no_fixation':"No fixation",'other':"Other"}
    metastasis_type_dict = {'tbd':"To be filled",'diffuse':"Diffuse",'sectoral':"Sectoral",'other':"Other"}
    discharge_type_dict = {'tbd':"To be filled",'milky':"Milky",'serous':"Serous",'brown':"Brown",'blood':"Blood",
                           'other':"Other"}
    skin_change_type_dict = {'tbd':"To be filled",'dimpling':"Dimpling",'ulceration':"Ulceration",
                             'discoloration':"Discoloration",'eczema':"Eczema",'edema':"Edema",'redness':"Redness",
                             'peau':"Peau d'orange",'other':"Other"}
    contalateral_breast_dict = {'tbd':"To be filled",'normal':"Normal",'diffuse mastitis':"diffuse mastitis",
                                 'Localised Mastitis':"Localised Mastitis", 'other':"Other"}
    arm_edema_dict = {'tbd':"To be filled",'right':"Right",'left':"Left",'not present':"Not present",'both':"Both",
                      'other':"Other"}
    usg_abdomen_dict = {'nd':"Not Done",'normal':"Normal",'abnormal':"Abnormal"}
    cect_abdomen_thorax_dict = {'nd':"Not done",'normal':"Normal",'visceral metastasis':"Visceral Metastasis"}
    pet_scan_dict = {'nd':"Not Done",'normal':"Normal",'visceral metastasis':"Visceral Metastasis",
                     'skeletal metastasis':"Skeletal Metastasis"}
    bone_scan_dict = {'nd':"Not Done",'normal':"Normal", 'skeletal metastasis':"Skeletal Metastasis"}


    palpable_choice = CommonDict.generate_choice(palpable_dict)
    lump_size_choice = CommonDict.generate_choice(lump_size_dict)
    lump_number_choice = CommonDict.generate_choice(lump_number_dict)
    lump_consistency_choice = CommonDict.generate_choice(lump_consistency_dict)
    lump_fixity_choice = CommonDict.generate_choice(lump_fixity_dict)
    metastasis_type_choice = CommonDict.generate_choice(metastasis_type_dict)
    discharge_type_choice = CommonDict.generate_choice(discharge_type_dict)
    skin_change_type_choice = CommonDict.generate_choice(skin_change_type_dict)
    contalateral_breast_choice = CommonDict.generate_choice(contalateral_breast_dict)
    arm_edema_choice = CommonDict.generate_choice(arm_edema_dict)
    usg_abdomen_choice = CommonDict.gender_choice(usg_abdomen_dict)
    cect_abdomen_thorax_choice = CommonDict.gender_choice(cect_abdomen_thorax_dict)
    pet_scan_choice = CommonDict.gender_choice(pet_scan_dict)
    bone_scan_choice = CommonDict.gender_choice(bone_scan_dict)