from db_dict.common_dict import CommonDict

class PatientHistoryDict():
    def __init__(self, key, value):
        self.key = key
        self.value = value

    diet_dict = {'veg':"Vegetarian", 'non-veg':"Non-Vegetarian", 'egg':"Ovo-Vegetarian", 'other':"Other"}
    period_type_dict = {'regular':"Regular",'irregular':"Irregular",'other':"Other"}
    menopausal_status_dict = {'pre':"Pre Menopausal",'post':"Post Menopausal",'peri':"Peri Menopausal",'other':"Other"}
    tobacco_dict =  {'no':'No exposure', 'passive':'Passive','active':'Active', 'pa':'Passive and Active'}
    tobacco_type_passive_dict = {'no':'No exposure','home':"Home", 'work':"Work", 'commute':"Commute",
                                 'social':"Social Interactions", 'other':'Other'}
    tobacco_type_dict = {'no':'No exposure','cig':"Cigarette", 'beedi':"Beedi", 'gutka':"Gutkha", 'pan_masala':"Pan Masala",
                         'jarda':"Jarda/Maava", 'hookah':"Hookah", 'patch':"Nicotine Patch", 'mishri':"Mishri",
                         'other':"Other"}
    yes_no_dict = {'tbd': "To be filled", "N": "No", "Y": "Yes", 'other': "Other"}
    current_complain_dict = {'self':"Self",'physician':"Physician",'screening_camp_id':"Screening Camp ID",'other':"Other"}
    annual_income_dict = {'1':"0-2.5lacks",'2':"2.5-5lacks",'3':"5-10lacks",'4':"more than 10 lacks"}
    metastasis_symptoms_dict = {'tbd': "To be filled", 'N': 'Absent', 'Rest of symptoms': 'TBD'}
    #todo
    diet_choice = CommonDict.generate_choice(diet_dict)
    tobacco_choice = CommonDict.generate_choice(tobacco_dict)
    tobacco_type_passive_choice = CommonDict.generate_choice(tobacco_type_passive_dict)
    tobacco_type_choice = CommonDict.generate_choice(tobacco_type_dict)
    current_complain_choice = CommonDict.generate_choice(current_complain_dict)
    annual_income_choice = CommonDict.generate_choice(annual_income_dict)
    period_type_choice = CommonDict.generate_choice(period_type_dict)
    menopausal_status_choice = CommonDict.generate_choice(menopausal_status_dict)
    metastasis_symptoms_choice = CommonDict.generate_choice(metastasis_symptoms_dict)