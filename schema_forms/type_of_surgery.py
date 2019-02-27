from wtforms import StringField, validators, IntegerField, SelectField, SubmitField, TextAreaField, FormField
from wtforms.fields.html5 import DateField
from db_dict.surgery_report_dict import SurgeryReportDict
from schema_forms.form_utilities import SectionForm, BaseForm
from db_dict.common_dict import CommonDict
from datetime import date

tbd = "To be done"

class ImplantBasedReconstructionForm(BaseForm):
    fld_type_of_surgery_ibs = SelectField("Type of surgery",choices=SurgeryReportDict.type_of_surgery_ibr_choice)
    fld_type_of_surgery_ibs_other = StringField("other")
    fld_implant_used = SelectField("the type of implant used",choices=SurgeryReportDict.implant_used_choice)
    fld_implant_used_other = StringField("other")
    fld_implant_size = StringField("Size of the implant",default=tbd)


class ConservativeBreastSurgeryForm(BaseForm):
   fld_type_of_surgery_cbs = SelectField("Type of surgery performed", choices= SurgeryReportDict.type_of_surgery_cbs_choice)
   fld_type_of_surgery_cbs_other = StringField("Give details")
   fld_type_of_conventional_surgery = SelectField("Type of conventional surgery performed",
                                                  choices=SurgeryReportDict.type_of_conventional_surgery_choice)
   fld_type_of_conventional_surgery_other = StringField("Give details")
   fld_oncoplastic_level = SelectField("Level used for oncoplastic surgery",
                                       choices=SurgeryReportDict.level_oncoplastic_choice)
   fld_oncoplastic_level_other = StringField("other")
   fld_type_levelone_omcoplastic = SelectField("Type of approach used in level 1 oncoplastic surgery",
                                               choices=SurgeryReportDict.type_levelone_oncoplastic_choice)
   fld_type_levelone_omcoplastic_other = StringField("other")
   fld_type_flap_used_oncoplastic_levelone = SelectField("Type of flap used in oncoplastic surgery",
                                                         choices=SurgeryReportDict.type_flap_used_oncoplastic_levelone_choice)
   fld_type_flap_used_oncoplastic_levelone_other = StringField("other")
   fld_therapeutic_type_leveltwo_oncoplastic = SelectField("Type of therapeutic approach for level 2 oncoplastic surgery",
                                                           choices=SurgeryReportDict.type_therapeytic_type_leveltwo_oncoplastic_choice)
   fld_therapeutic_type_leveltwo_oncoplastic_other = StringField("other")
   fld_plan_simple_thrapeutic = SelectField("Plan for simple therapeutic oncoplastic surgery",
                                            choices=SurgeryReportDict.plan_simple_therapeutic_choice)
   fld_plan_simple_thrapeutic_other = StringField("other")
   fld_pedicle_type_simple_therapeutic = SelectField("Type of pedicle used for simple therapeutc oncoplastic surgery",
                                                     choices=SurgeryReportDict.pedicle_type_simple_therapeutic_choice)
   fld_pedicle_type_simple_therapeutic_other = StringField("other")
   fld_plan_extreme_thrapeutic = SelectField("Plan for extreme therapeutic oncoplastic surgery",
                                            choices=SurgeryReportDict.plan_simple_therapeutic_choice)
   fld_plan_extreme_thrapeutic_other = StringField("other")
   fld_tumour_filled_in_extreme_therapeutic_surgery = SelectField("In extreme therapeutic surgery the tumor is filled by",
                                                                  choices=SurgeryReportDict.tumour_filled_by_extreme_therapeutic_choice)
   fld_tumour_filled_in_extreme_therapeutic_surgery_other = StringField("other")
   fld_nac_graft = SelectField("Was NAC graft done", choices=CommonDict.yes_no_choice)
   fld_primary_pedicle_extreme_therapeutic = SelectField("Type of primary pedicle used",
                                                         choices=SurgeryReportDict.primary_pedicle_extreme_therapeutic_choice)
   fld_primary_pedicle_extreme_therapeutic_other = StringField("other")
   fld_secondary_pedicle_extreme_therapeutic = SelectField("Type of secondary pedicle used",
                                                           choices=SurgeryReportDict.secondary_pedicle_extreme_therapeutic_choice)
   fld_secondary_pedicle_extreme_therapeutic_other = StringField("other")
   fld_flap_used_levelthree = SelectField("Flap used in level three oncoplastic surgery",
                                          choices=SurgeryReportDict.flap_used_levelthree_choice)
   fld_flap_used_levelthree_other = StringField("other")

class ContralateralSideSurgeryForm (BaseForm):
    fld_type_of_surgery_performed = SelectField("Type of suregery performed",
                                                choices=SurgeryReportDict.type_of_surgery_contralateral_choice)
    fld_type_of_surgery_performed_other = StringField("other")
    fld_surgery_description = TextAreaField("Describe the type of approach for the suregery")#do we need to remove this
    fld_surgery_notes = TextAreaField("Surgery notes if any")

class SurgeryReportForm (SectionForm):
    fld_date = DateField("Today's Date", default=date.today())
    fld_name_of_hospital = StringField("Name of the Hospital", default=tbd)
    fld_anaesthetist = StringField("Name of the Anaesthetist", default=tbd)
    fld_location_of_lesion = SelectField("Location of lesion", choices=SurgeryReportDict.location_of_lesion_choice)
    fld_location_of_lesion_other = StringField("other")
    fld_weight_of_tumour_left_breast = IntegerField("Weight of the tumour or tissues removed from left breast (in gms)",
                                                    default=0)
    fld_weight_of_tumour_right_breast = IntegerField("Weight of the tumour or tissues removed from right breast (in gms)",
                                                    default=0)
    fld_incision = SelectField("Type of incision performed", choices=SurgeryReportDict.incision_choice)
    fld_incision_other = StringField("other")
    fld_masectomy = SelectField("is masectomy done?", choices=CommonDict.yes_no_choice)
    fld_masectomy_other = StringField("other")
    fld_masectomy_type = SelectField("Type of masectomy", choices=SurgeryReportDict.masectomy_type_choice)
    fld_masectomy_type_other = StringField("other")
    fld_implant_based_reconstruction_form_present = SelectField("Implant based reconstruction done",
                                                        choices=CommonDict.form_yes_no_choice)
    implant_based_reconstruction_form = FormField(ImplantBasedReconstructionForm)
    fld_conservative_breast_surgery_form_present = SelectField("conservative breast surgery done",
                                                                choices=CommonDict.form_yes_no_choice)
    conservative_breast_surgery_form = FormField(ConservativeBreastSurgeryForm)
    fld_contralateral_side_surgery_form_present = SelectField("surgery on contralaterla side done",
                                                               choices=CommonDict.form_yes_no_choice)
    contralateral_side_surgery_form = FormField(ContralateralSideSurgeryForm)
    fld_drain_removal_date = DateField("Drain removal date", default=date.today())
    submit_button = SubmitField('Submit Form')