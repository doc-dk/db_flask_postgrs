from wtforms import StringField, IntegerField, SelectField, SubmitField
from schema_forms.form_utilities import SectionForm
from db_dict.surgery_report_dict import SurgeryReportDict
from db_dict.common_dict import CommonDict


class NodesFrozenSectionForm(SectionForm):
    fld_guided_by = SelectField("The frozen sections are guided by",choices=SurgeryReportDict.nodes_guided_by_choice)
    fld_guided_by_other = StringField("other")
    fld_sample_sent_from = SelectField("Samples sent for frozen", choices=SurgeryReportDict.sample_sent_from_choice)
    fld_sample_sent_from_other = StringField("other")
    fld_size_of_tumour = IntegerField("Size of tumour on cross section(cm)",default=0)
    fld_skin_involved = SelectField("Skin involved", choices=CommonDict.yes_no_choice)
    fld_skin_involved_other = StringField("other")
    fld_nodes_excised = SelectField("Nodes excised", choices=SurgeryReportDict.nodes_excised_choice)
    fld_nodes_excised_other = StringField("other")
    fld_number_nodes_excised = IntegerField("Number of nodes excised", default=0)
    fld_level_lymph_node_excised = SelectField("Number of lymph node excised" ,
                                                choices=SurgeryReportDict.level_lymph_node_excised_choice )
    fld_labelling_senitinel_node = SelectField("Method of labelling senitinel node",
                                               choices=SurgeryReportDict.labelling_senitinel_node_choice)
    fld_labelling_senitinel_node_other = StringField("other")
    fld_blue_node = SelectField("Blue node", choices=CommonDict.yes_no_choice)
    fld_blue_node_other = StringField("other")
    fld_hot_node = SelectField("Hot node", choices=CommonDict.yes_no_choice)
    fld_hot_node_other = StringField("other")
    fld_blue_hot_node = SelectField("Blue Hot node", choices=CommonDict.yes_no_choice)
    fld_blue_hot_node_other = StringField("other")
    fld_non_blue_non_hot_node = SelectField("Non blue non hot node", choices=CommonDict.yes_no_choice)
    fld_non_blue_non_hot_node_other = StringField("other")
    fld_palpable_node = SelectField("Is the node palpable", choices=CommonDict.yes_no_choice)
    fld_palpable_node_other = StringField("other")
    fld_tumour_size = IntegerField("Size on the tumour on cross section(cm)", default=0)
    fld_drain_insertion = SelectField("Drain insertion", choices=CommonDict.yes_no_choice)
    fld_drain_insertion_other = StringField("other")
    fld_post_surgery_plan = SelectField("Post surgery plan is", choices=SurgeryReportDict.post_surgery_plan_choice)
    fld_post_surgery_plan_other = StringField("Please specify")
    submit_button = SubmitField('Submit Form')
