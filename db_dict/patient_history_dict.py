from db_dict.common_dict import CommonDict

class PatientHistoryDict():
    def __init__(self, key, value):
        self.key = key
        self.value = value

    diet_dict = {'tbd':"To be filled",'veg':"Vegetarian", 'non-veg':"Non-Vegetarian", 'egg':"Ovo-Vegetarian", 'other':"Other"}
    period_type_dict = {'tbd':"To be filed",'regular':"Regular",'irregular':"Irregular",'other':"Other"}
    menopausal_status_dict = {'tbd':"To be filled",'pre':"Pre Menopausal",'post':"Post Menopausal",
                              'peri':"Peri Menopausal",'other':"Other"}
    tobacco_dict =  {'tbd':"To be filled",'no':'No exposure', 'passive':'Passive','active':'Active',
                     'pa':'Passive and Active'}
    tobacco_type_passive_dict = {'tbd':"To be filled",'no':'No exposure','home':"Home", 'work':"Work", 'commute':"Commute",
                                 'social':"Social Interactions", 'other':'Other'}
    tobacco_type_dict = {'tbd':"To be filled",'no':'No exposure','cig':"Cigarette", 'beedi':"Beedi", 'gutka':"Gutkha",
                         'pan_masala':"Pan Masala", 'jarda':"Jarda/Maava", 'hookah':"Hookah", 'patch':"Nicotine Patch", 'mishri':"Mishri",
                         'other':"Other"}
    yes_no_dict = {'tbd': "To be filled", "N": "No", "Y": "Yes", 'other': "Other"}
    current_complain_dict = {'tbd':"To be filled",'self':"Self",'physician':"Physician",'screening_camp_id':"Screening Camp ID",
                             'other':"Other"}
    annual_income_dict = {'tbd':"To be filled",'1':"0-2.5 lakhs",'2':"2.5-5 lakhs",'3':"5-10 lakhs",
                          '4':"more than 10 lakhs"}
    metastasis_symptoms_dict = {'tbd': "To be filled", 'N': "Absent", 'jauncice':"Jaundice", 'bone pain':"Bone Pain", 'cough':"Cough",
                                'weight loss':"Weight Loss",'headache':"Headache" }
    treatment_type_dict = {'tbd': "To be filled", 'surgery': "Surgery", 'radiation': "Radiation",
                           'chemotherapy': "Chemotherapy", 'hormone': "Hormone",
                           'alternative therapy': "Alternative Therapy", 'home remedies': "Home Remedies",
                           'none': "None", 'other': "Other"}
    degree_of_relation_dict = {'tbd':"To be filled",'i':"Immediate Family",'m':"Maternal Family",'p':"Paternal Family",
                               'other':"Other"}
    diet_choice = CommonDict.generate_choice(diet_dict)
    tobacco_choice = CommonDict.generate_choice(tobacco_dict)
    tobacco_type_passive_choice = CommonDict.generate_choice(tobacco_type_passive_dict)
    tobacco_type_choice = CommonDict.generate_choice(tobacco_type_dict)
    current_complain_choice = CommonDict.generate_choice(current_complain_dict)
    annual_income_choice = CommonDict.generate_choice(annual_income_dict)
    period_type_choice = CommonDict.generate_choice(period_type_dict)
    menopausal_status_choice = CommonDict.generate_choice(menopausal_status_dict)
    metastasis_symptoms_choice = CommonDict.generate_choice(metastasis_symptoms_dict)
    treatment_type_choice = CommonDict.generate_choice(treatment_type_dict)
    degree_of_relation_choice = CommonDict.generate_choice(degree_of_relation_dict)
