from db_dict.common_dict import CommonDict

class SurgeryReportDict():
    def __init__(self, key, value):
        self.key = key
        self.value = value

    location_of_lesion_dict = {'tbd':"To be done",'left':"Left",'right':"Right",'bilateral':"Bilateral",'other':"Other"}
    incision_dict = {'tbd':"To be done",'inframammary_fold_incision':"Inframammary Fold Incision",'lateral_fold':""'other':"Other"}

    location_of_lesion_choice = CommonDict.generate_choice(location_of_lesion_dict)