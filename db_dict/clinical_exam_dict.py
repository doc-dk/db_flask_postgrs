from db_dict.common_dict import CommonDict

class ClinicalExamDict():
    def __init__(self, key, value):
        self.key = key
        self.value = value

    options_dict = {'tbd':"To be filled",'definite':"Definite", 'vague':"Vague", 'diffuse':"Diffuse", 'nil':"Nil",'other':"Other"}

    options_choice = CommonDict.generate_choice(options_dict)