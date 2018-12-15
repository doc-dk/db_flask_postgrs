from db_dict.common_dict import CommonDict

class ClinicalExamDict():
    def __init__(self, key, value):
        self.key = key
        self.value = value

    options_dict = {'tbd':"To be filled",'definite':"Definite", 'vague':"Vague", 'diffuse':"Diffuse", 'nil':"Nil",'other':"Other"}
    lump_size_dict = {'tbd':"To be filled",'1':"less than 2cm",'2':"2-5cm",'3':"more than 5cm",'other':"Other"}
    lump_number_dict = {'tbd':"To be filled",'single':"Single",'multiple':"Multiple",'other':"Other"}
    lump_consistency_dict = {'tbd':"To be filled",'soft':"Soft",'Firm':"Firm",'hard':"Hard",'cystic':"Cystic",'mobile':"Mobile",'other':"Other"}# should i put 1 2 3?
    lump_fixity_dict = {'tbd':"To be filled",'skin':"Skin",'chest wall':"Chest_Wall",'Pectoral_major_muscle':"Pectoral major muscle",'no_fixation':"No fixation",'other':"Other"}

    options_choice = CommonDict.generate_choice(options_dict)
    lump_size_choice = CommonDict.generate_choice(lump_size_dict)
    lump_number_choice = CommonDict.generate_choice(lump_number_dict)
    lump_consistency_choice = CommonDict.generate_choice(lump_consistency_dict)
    lump_fixity_choice = CommonDict.generate_choice(lump_fixity_dict)