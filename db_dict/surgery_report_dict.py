from db_dict.common_dict import CommonDict

class SurgeryReportDict():
    def __init__(self, key, value):
        self.key = key
        self.value = value

    location_of_lesion_dict = {'tbd':"To be done",'left':"Left",'right':"Right",'bilateral':"Bilateral",'other':"Other"}
    incision_dict = {'tbd':"To be done",'inframammary_fold_incision':"Inframammary Fold Incision",
                     'lateral_fold':"Lateral Fold",'lateral_crease':"Lateral Crease",'wise_pattern':"Wise Pattern",
                     'radial':"Radial",'oblique':"Oblique",'transveres_oblique':"Transverse Oblique",
                     'oblique_with_supra_aerolar':"Oblique with supra areolar",
                     'circum_areolar_at_margin':"Circum areolar at margin",
                     'circum_areolar_away_from_margin':"Circum areolar away from margin",
                     'axillary':"Axillary",'vertical_scar':"Vertical scar",'other':"Other"}
    masectomy_type_dict = {'tbd':"To be done",'aereolar_sparing':"Aereolar Sparing",'nipple_sparing':"Nipple Sparing",
                      'skin_sparing':"Skin Sparing",'mrm':"Modified Radical Masectomy",'other':"Other"}
    type_of_surgery_ibr_dict = {'tbd':"To be done",'non_sling_conventional_ibrs':"Non Sling Conventional IBRS",
                            'sling_alds':"Sling ALDS",'advanced_sling_aalds':"Advanced sling AALDS",
                            'ld_flap_and_implant':"LD Flap+Implant",'tdap_and_implant':"TDAP+Implant",
                            'licap_and_implant':"LICAP+Implant",'other':"Other"}
    type_of_surgery_cbs_dict = {'tbd':"To be done",'conventional_surgery':"Conventional Surgery",
                                'oncoplastic_surgery':"Oncoplastic Surgery",'other':"Other"}
    type_of_conventional_surgery_dict = {'tbd':"To be done",'NA':"Not Done",'lumpectomy':"Lumpectomy",'quadrantectomy':"Quadrantectomy",
                                        'wedge_resection':"Wedge Resection",'other':"Other"}
    implant_used_dict = {'tbd':"To be done",'fixed_volume_smooth':"Fixed volume: smooth",
                         'fixed_volume_textured':"Fixed volume: textured",
                         'fixed_volume_microtextured':"Fixed Volume: Microtextured",'dual_lumen':"Dual Lumen",'other':"Other"}
    level_oncoplastic_dict = {'tbd':"To be done",'1':"1",'2':"2",'3':"3",'other':"Other"}
    type_levelone_oncoplastic_dict = {'tbd':"To be done",'NA':"Not done",'simple_oncoplastic':"Simple Oncoplastic or mammoplasty",
                                      'volume_displacement':"Volume Displacement",'other':"Other"}
    type_flap_used_oncoplastic_levelone_dict = {'tbd':"To be done",'NA':"Not available",'grisotti':"Grisotti Flap",
                                                'round_block':"Round Block",'batwing_procedure':"Batwing Procedure",
                                                'other':"other"}
    type_therapeytic_type_leveltwo_oncoplastic_dict = {'tbd':"To be done",'NA':"Not available",'simple':"Simple Therapeutic",
                                                       'extreme':"Extreme Therapeutic",'other':"other"}
    plan_simple_therapeutic_dict = {'tbd':"To be done",'NA':"Not available",'wise_pattern':"Wise Pattern",
                                    'vertical_scar':"Vertical scar",'other':"other"}
    pedicle_type_simple_therapeutic_dict = {'tbd':"To be done",'NA':"Not available",'lower_pedicle':"Lower pedicle",
                                            'superior_pedicle':"Superior pedicle",
                                            'superio_medial_pedicle':"Superio-medial pedicle",'lateral_pedicle':"Lateral pedicle",
                                            'dual_pedicle':"Dual Pedicle",'other':"other"}
    tumour_filled_by_extreme_therapeutic_dict = {'tbd':"To be done",'NA':"Not available",
                                                'extended_primary_pedicle':"Extended Primary pedicle",
                                                'secondary_pedicle':"Secondary pedicle",'other':"Other"}
    flap_used_levelthree_dict = {'tbd':"To be done",'NA':"Not available",'local_thoraco_epigastric':"Local thoraco epigastric flap",
                                 'local_licap':"Local LICAP",'Local_tdap':"Local TDAP",'local_aicap':"Local AiCAP",
                                 'local_micap':"Local MiCAP",'ld_flaps':"LD Flaps",'mini_ld':"Mini LD",'other':"Other"}
    type_of_surgery_contralateral_dict = {'tbd':"To be done",'NA':"Not available",
                                          'symmetrisation_same':"Symmetrisation;same as other",
                                          'symmetrisation_different':"Symmetrisation;different than other",
                                          'prophylactic_masectomy_wiht_reconstruction':"Prophylactic masectomy with reconstruction",
                                          'other':"Other"}
    primary_pedicle_extreme_therapeutic_dict = {'tbd':"To be done",'NA':"Not available",'lower':"Lower pedicle",
                                                'superior':"Superior pedicle",'superio_medial':"Superio-medial pedicle",
                                                'lateral':"Lateral pedicle",'inferior':"Inferior pedicle",
                                               'inferior medial':"Inferior medial pedicle",
                                                'inferior_medial_lateral':"Inferior medial lateral pedicle",'other':"other"}
    secondary_pedicle_extreme_therapeutic_dict = {'tbd':"To be done",'NA':"Not available",'inferior':"Inferior pedicle",
                                                  'inferior_lateral':"Inferior lateral pedicle",
                                                 'inferior_lateral_medial':"Inferior lateral medial pedicle",
                                                  'superior':"Superior pedicle",'superior_medial':"Superior medial pedicle",
                                                  'inferior_medial':"Inferior medial pedicle",'other':"other"}
    nodes_guided_by_dict = {'tbd':"To be done",'NA':"Not available",'palpation':"Palpation",'usg_guided':"USG guided",
                            'wire_placement':"Wire placement guided",'gamma_camera':"Gamma camera guided",
                            'blue_dye':"Blue dye",'other':"Other"}
    sample_sent_from_dict = {'tbd':"To be done",'NA':"Not available",'senital_node':"Senital Node",
                             'under_nipple_surface':"Under nipple surface",'margin_additional':"Margin additional",
                             'tumour_free_margin':"Tumour free margin",'any_other_specimen':"Any other specimen",
                             'other':"Other"}
    nodes_excised_dict = {'tbd':"To be done",'NA':"Not available",'senital':"Senital Node",'axillary':"Axillary Node",
                          'senital_axillary':"Senital and axillary",'other':"Other"}
    level_lymph_node_excised_dict = {'tbd':"To be done",'NA':"Not available",'1':"Level 1",'2':"Level 2",'3':"Level 3",
                                     'other':"other"}
    post_surgery_plan_dict = {'tbd':"To be done",'NA':"Not available",'chemotherapy':"Chemotherapy",'radiology':"Radiology",
                             'other':"Other"}
    intervention_type_dict = {'tbd':"To be done",'NA':"Not available",'surgical':"Surgical",'non_surgical':"Non Surgical"}
    location_recurrence_dict = {'tbd':"To be done",'NA':"Not available",'loco_regional':"Loco regional",'breast':"Breast",
                                'axilla':"Axilla",'distant':"Distant",'other':"Other"}
    labelling_senitinel_node_dict = {'tbd':"To be done",'NA':"Not done",'isotope':"Isotope",'blue_dye':"Blue dye",
                                     'isotope_blue_dye':"Isotope and Blue dye",'other':"Other"}
    location_of_lesion_choice = CommonDict.generate_choice(location_of_lesion_dict)
    incision_choice = CommonDict.generate_choice(incision_dict)
    masectomy_type_choice = CommonDict.generate_choice(masectomy_type_dict)
    type_of_surgery_ibr_choice = CommonDict.generate_choice(type_of_surgery_ibr_dict)
    implant_used_choice = CommonDict.generate_choice(implant_used_dict)
    type_of_surgery_cbs_choice = CommonDict.generate_choice(type_of_surgery_cbs_dict)
    type_of_conventional_surgery_choice = CommonDict.generate_choice(type_of_conventional_surgery_dict)
    level_oncoplastic_choice = CommonDict.generate_choice(level_oncoplastic_dict)
    type_levelone_oncoplastic_choice = CommonDict.generate_choice(type_levelone_oncoplastic_dict)
    type_flap_used_oncoplastic_levelone_choice = CommonDict.generate_choice(type_flap_used_oncoplastic_levelone_dict)
    type_therapeytic_type_leveltwo_oncoplastic_choice = CommonDict.generate_choice(type_therapeytic_type_leveltwo_oncoplastic_dict)
    plan_simple_therapeutic_choice = CommonDict.generate_choice(plan_simple_therapeutic_dict)
    pedicle_type_simple_therapeutic_choice = CommonDict.generate_choice(pedicle_type_simple_therapeutic_dict)
    tumour_filled_by_extreme_therapeutic_choice = CommonDict.generate_choice(tumour_filled_by_extreme_therapeutic_dict)
    flap_used_levelthree_choice = CommonDict.generate_choice(flap_used_levelthree_dict)
    type_of_surgery_contralateral_choice = CommonDict.generate_choice(type_of_surgery_contralateral_dict)
    primary_pedicle_extreme_therapeutic_choice = CommonDict.generate_choice(primary_pedicle_extreme_therapeutic_dict)
    secondary_pedicle_extreme_therapeutic_choice = CommonDict.generate_choice(secondary_pedicle_extreme_therapeutic_dict)
    nodes_guided_by_choice = CommonDict.generate_choice(nodes_guided_by_dict)
    sample_sent_from_choice = CommonDict.generate_choice(sample_sent_from_dict)
    nodes_excised_choice = CommonDict.generate_choice(nodes_excised_dict)
    level_lymph_node_excised_choice = CommonDict.generate_choice(level_lymph_node_excised_dict)
    post_surgery_plan_choice = CommonDict.generate_choice(post_surgery_plan_dict)
    intervention_type_choice = CommonDict.generate_choice(intervention_type_dict)
    location_recurrence_choice = CommonDict.generate_choice(location_of_lesion_dict)
    labelling_senitinel_node_choice = CommonDict.generate_choice(labelling_senitinel_node_dict)