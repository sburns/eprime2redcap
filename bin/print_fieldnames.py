#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This serves to document all the fieldnames for each task
mi1: Mental imagery from NFRO1
swr1: Single Word Reading from NFRO1
rep1: repitition task from NFRO1
pic1: Picture task from NFRO1
"""




data = {'mi1': {'per_mission': [('imag_rtavg', 'Imaginary Mean RT'),
                                ('imag_rtsd', 'Imaginary RT SD'),
                                ('imag_acc', 'Imaginary Accuracy'),
                                ('imag_accsd', 'Imaginary Accuracy SD'),
                                ('imag_omit', 'Imaginary Omit'),
                                ('imag_fn', 'Imaginary False Negative'),
                                ('imag_fp', 'Imaginary False Positive'),
                                ('cont_rtavg', 'Control Mean RT'),
                                ('cont_rtsd', 'Control RT SD'),
                                ('cont_acc', 'Control Accuracy'),
                                ('cont_accsd', 'Control Accuracy SD'),
                                ('cont_omit', 'Control Omit'),
                                ('cont_fn', 'Control False Negative'),
                                ('cont_fp', 'Control False Positive')],
               'visit': [('pre', 'Pre'),
                         ('post', 'Post')],
               'mission': [('m1', 'Mission1'),
                           ('m2', 'Mission2')],
               'per_visit': [('upload', 'Upload Complete')],
               'form': 'MentalImagery1'},
        'swr1': {'per_mission': [('hai_acc', 'High Abstract Irregular Accuracy'),
                                 ('hai_accsd', 'High Abstract Irregular Accuracy SD'),
                                 ('hai_rtavg', 'High Abstract Irregular Mean RT'),
                                 ('hai_rtsd', 'High Abstract Irregular RT SD'),
                                 ('hai_omit', 'High Abstract Irregular Omit'),
                                 ('hai_comit', 'High Abstract Irregular Comit'),
                                 ('har_acc', 'High Abstract Regular Accuracy'),
                                 ('har_accsd', 'High Abstract Regular Accuracy SD'),
                                 ('har_rtavg', 'High Abstract Regular Mean RT'),
                                 ('har_rtsd', 'High Abstract Regular RT SD'),
                                 ('har_omit', 'High Abstract Regular Omit'),
                                 ('har_comit', 'High Abstract Regular Comit'),
                                 ('hci_acc', 'High Concrete Irregular Accuracy'),
                                 ('hci_accsd', 'High Concrete Irregular Accuracy SD'),
                                 ('hci_rtavg', 'High Concrete Irregular Mean RT'),
                                 ('hci_rtsd', 'High Concrete Irregular RT SD'),
                                 ('hci_omit', 'High Concrete Irregular Omit'),
                                 ('hci_comit', 'High Concrete Irregular Comit'),
                                 ('hcr_acc', 'High Concrete Regular Accuracy'),
                                 ('hcr_accsd', 'High Concrete Regular Accuracy SD'),
                                 ('hcr_rtavg', 'High Concrete Regular Mean RT'),
                                 ('hcr_rtsd', 'High Concrete Regular RT SD'),
                                 ('hcr_omit', 'High Concrete Regular Omit'),
                                 ('hcr_comit', 'High Concrete Regular Comit'),
                                 ('word_acc', 'All Words Accuracy'),
                                 ('word_accsd', 'All Words Accuracy SD'),
                                 ('word_rtavg', 'All Words Mean RT'),
                                 ('word_rtsd', 'All Words RT SD'),
                                 ('word_omit', 'All Words Omit'),
                                 ('word_comit', 'All Words Comit'),
                                 ('nonword_acc', 'Nonword Accuracy'),
                                 ('nonword_accsd', 'Nonword Accuracy SD'),
                                 ('nonword_rtavg', 'Nonword Mean RT'),
                                 ('nonword_rtsd', 'Nonword RT SD'),
                                 ('nonword_omit', 'Nonword Omit'),
                                 ('nonword_comit', 'Nonword Comit')],
                 'visit': [('pre', 'Pre'),
                           ('post', 'Post')],
                 'mission': [('m1', 'Mission1'),
                             ('m2', 'Mission2')],
                 'per_visit': [('upload', 'Upload Complete'),
                               ('aprime', 'A Prime')],
                 'form': 'SingleWordReading1'},
        'pic1': {'per_mission': [('con_acc', 'Consonant Accuracy'),
                                 ('con_accsd', 'Consonant Accuracy SD'),
                                 ('con_rtavg', 'Consonant Mean RT'),
                                 ('con_rtsd', 'Consonant RT SD'),
                                 ('con_omit', 'Consonant Omit'),
                                 ('con_comit', 'Consonant Comit'),
                                 ('match_acc', 'Match Accuracy'),
                                 ('match_accsd', 'Match Accuracy SD'),
                                 ('match_rtavg', 'Match Mean RT'),
                                 ('match_rtsd', 'Match RT SD'),
                                 ('match_omit', 'Match Omit'),
                                 ('match_comit', 'Match Comit'),
                                 ('psw_acc', 'Pseudowords Accuracy'),
                                 ('psw_accsd', 'Pseudowords Accuracy SD'),
                                 ('psw_rtavg', 'Pseudowords Mean RT'),
                                 ('psw_rtsd', 'Pseudowords RT SD'),
                                 ('psw_omit', 'Pseudowords Omit'),
                                 ('psw_comit', 'Pseudowords Comit'),
                                 ('wrd_acc', 'Words Accuracy'),
                                 ('wrd_accsd', 'Words Accuracy SD'),
                                 ('wrd_rtavg', 'Words Mean RT'),
                                 ('wrd_rtsd', 'Words RT SD'),
                                 ('wrd_omit', 'Words Omit'),
                                 ('wrd_comit', 'Words Comit')],
                'visit': [('pre', 'Pre'),
                          ('post', 'Post')],
                'mission': [('m1', 'Mission1'),
                            ('m2', 'Mission2')],
                'per_visit': [('upload', 'Upload Complete')],
                'form': 'PictureTask1'},
        'rep1': {'per_mission': [('abs_acc', 'Abstract Accuracy'),
                                 ('abs_accsd', 'Abstract Accuracy SD'),
                                 ('abs_rtavg', 'Abstract Mean RT'),
                                 ('abs_rtsd', 'Abstract RT SD'),
                                 ('abs_omit', 'Abstract Omit'),
                                 ('abs_comit', 'Abstract Comit'),
                                 ('conc_acc', 'Concrete Accuracy'),
                                 ('conc_accsd', 'Concrete Accuracy SD'),
                                 ('conc_rtavg', 'Concrete Mean RT'),
                                 ('conc_rtsd', 'Concrete RT SD'),
                                 ('conc_omit', 'Concrete Omit'),
                                 ('conc_comit', 'Concrete Comit'),
                                 ('cons_acc', 'Consonant Accuracy'),
                                 ('cons_accsd', 'Consonant Accuracy SD'),
                                 ('cons_rtavg', 'Consonant Mean RT'),
                                 ('cons_rtsd', 'Consonant RT SD'),
                                 ('cons_omit', 'Consonant Omit'),
                                 ('cons_comit', 'Consonant Comit'),
                                 ('non_acc', 'Nonword Accuracy'),
                                 ('non_accsd', 'Nonword Accuracy SD'),
                                 ('non_rtavg', 'Nonword Mean RT'),
                                 ('non_rtsd', 'Nonword RT SD'),
                                 ('non_omit', 'Nonword Omit'),
                                 ('non_comit', 'Nonword Comit')],
                'visit': [('', '')],
                'mission': [('m1', 'Mission1'),
                            ('m2', 'Mission2'),
                            ('m3', 'Mission3')],
                'per_visit': [('upload', 'Upload Complete')],
                'form': 'RepetitionTask1'},
        'nback1': {'per_mission': [('acc', 'Single Mission Accuracy'),
                                   ('high_acc', 'High Frequency Accuracy'),
                                   ('low_acc', 'Low Frequency Accuracy'),
                                   ('trained_acc', 'Trained Accuracy'),
                                   ('untrained_acc', 'Untrained Accuracy'),
                                   ('repeat_acc', 'Repeat Accuracy')],
                    'visit':[('', '')],
                    'mission': [('m1', 'Mission1'),
                                ('m2', 'Mission2'),
                                ('m3', 'Mission3'),
                                ('m4', 'Mission4')],
                    'per_visit': [('upload', 'Upload Complete'),
                                  ('all_acc', 'All Accuracy')],
                    'form': 'NBack1'},
        'sent1': {'per_mission': [('all_acc', 'All Accuracy'),
                                  ('all_comit', 'All Comit'),
                                  ('all_corr_rtavg', 'All Mean RT'),
                                  ('all_corr_rtsd', 'All RT SD'),
                                  ('all_omit', 'All Omit'),
                                  ('all_tot', 'All Total'),
                                  ('pseudo_acc', 'Pseudowords Accuracy'),
                                  ('pseudo_comit', 'Pseudowords Comit'),
                                  ('pseudo_corr_rtavg', 'Pseudowords Mean RT'),
                                  ('pseudo_corr_rtsd', 'Pseudowords RT SD'),
                                  ('pseudo_omit', 'Pseudowords Omit'),
                                  ('pseudo_tot', 'Pseudowords Total'),
                                  ('realword_acc', 'Real Words Accuracy'),
                                  ('realword_comit', 'Real Words Comit'),
                                  ('realword_corr_rtavg', 'Real Words Mean RT'),
                                  ('realword_corr_rtsd', 'Real Words RT SD'),
                                  ('realword_omit', 'Real Words Omit'),
                                  ('realword_tot', 'Real Words Total'),
                                  ('semantic_acc', 'Semantic Accuracy'),
                                  ('semantic_comit', 'Semantic Comit'),
                                  ('semantic_corr_rtavg', 'Semantic Mean RT'),
                                  ('semantic_corr_rtsd', 'Semantic RT SD'),
                                  ('semantic_omit', 'Semantic Omit'),
                                  ('semantic_tot', 'Semantic Total'),
                                  ('syntatic_acc', 'Syntatic Accuracy'),
                                  ('syntatic_comit', 'Syntatic Comit'),
                                  ('syntatic_corr_rtavg', 'Syntatic Mean RT'),
                                  ('syntatic_corr_rtsd', 'Syntatic RT SD'),
                                  ('syntatic_omit', 'Syntatic Omit'),
                                  ('syntatic_tot', 'Syntatic Total'),
                                  ('truesent_acc', 'True Sentences Accuracy'),
                                  ('truesent_comit', 'True Sentences Comit'),
                                  ('truesent_corr_rtavg', 'True Sentences Mean RT'),
                                  ('truesent_corr_rtsd', 'True Sentences RT SD'),
                                  ('truesent_omit', 'True Sentences Omit'),
                                  ('truesent_tot', 'True Sentences Total')],
                  'visit': [('', '')],
                  'mission': [('m1', 'Mission1'),
                              ('m2', 'Mission2'),
                              ('m3', 'Mission3'),
                              ('m4', 'Mission4'),
                              ('m5', 'Mission5'),
                              ('m6', 'Mission6')],
                  'per_visit': [('upload', 'Upload Complete'),
                                ('all_all_acc', 'All Missions All Types Accuracy'),
                                ('all_all_comit', 'All Mission All Types Comit'),
                                ('all_all_corr_rtavg', 'All Mission All Types Mean RT'),
                                ('all_all_corr_rtsd', 'All Mission All Types RT SD'),
                                ('all_all_omit', 'All Mission All Types Omit'),
                                ('all_all_tot', 'All Mission All Types Total'),
                                ('all_pseudo_acc', 'All Missions Pseudowords Accuracy'),
                                ('all_pseudo_comit', 'All Mission Pseudowords Comit'),
                                ('all_pseudo_corr_rtavg', 'All Mission Pseudowords Mean RT'),
                                ('all_pseudo_corr_rtsd', 'All Mission Pseudowords RT SD'),
                                ('all_pseudo_omit', 'All Mission Pseudowords Omit'),
                                ('all_pseudo_tot', 'All Mission Pseudowords Total'),
                                ('all_realword_acc', 'All Missions Real Words Accuracy'),
                                ('all_realword_comit', 'All Mission Real Words Comit'),
                                ('all_realword_corr_rtavg', 'All Mission Real Words Mean RT'),
                                ('all_realword_corr_rtsd', 'All Mission Real Words RT SD'),
                                ('all_realword_omit', 'All Mission Real Words Omit'),
                                ('all_realword_tot', 'All Mission Real Words Total'),
                                ('all_semantic_acc', 'All Missions Semantic Accuracy'),
                                ('all_semantic_comit', 'All Mission Semantic Comit'),
                                ('all_semantic_corr_rtavg', 'All Mission Semantic Mean RT'),
                                ('all_semantic_corr_rtsd', 'All Mission Semantic RT SD'),
                                ('all_semantic_omit', 'All Mission Semantic Omit'),
                                ('all_semantic_tot', 'All Mission Semantic Total'),
                                ('all_syntatic_acc', 'All Missions Syntatic Accuracy'),
                                ('all_syntatic_comit', 'All Mission Syntatic Comit'),
                                ('all_syntatic_corr_rtavg', 'All Mission Syntatic Mean RT'),
                                ('all_syntatic_corr_rtsd', 'All Mission Syntatic RT SD'),
                                ('all_syntatic_omit', 'All Mission Syntatic Omit'),
                                ('all_syntatic_tot', 'All Mission Syntatic Total'),
                                ('all_truesent_acc', 'All Missions True Sentences Accuracy'),
                                ('all_truesent_comit', 'All Mission True Sentences Comit'),
                                ('all_truesent_corr_rtavg', 'All Mission True Sentences Mean RT'),
                                ('all_truesent_corr_rtsd', 'All Mission True Sentences RT SD'),
                                ('all_truesent_omit', 'All Mission True Sentences Omit'),
                                ('all_truesent_tot', 'All Mission True Sentences Total')],
                        'form': 'SentenceTask1'},
        'rep2':{'per_mission':[('word_acc','Words Accuracy'),
                              ('word_mrt','Words Mean Reaction Time (correct)'),
                              ('word_rtsd','Word MRT STD'),
                              ('word_omit','Word Omit'),
                              ('word_comit','Word Comit'),
                              ('pseudoword_acc','Pseudowords Accuracy'),
                              ('pseudoword_mrt','Pseudowords Mean Reaction Time (correct)'),
                              ('pseudoword_rtsd','Pseudowords MRT STD'),
                              ('pseudoword_omit','Pseudowords Omit'),
                              ('pseudoword_comit','Pseudowords Comit')],
               'visit':[('', '')],
               'mission':[('m1', 'Mission1'),
                          ('m2', 'Mission2'),
                          ('m3', 'Mission3'),
                          ('m4', 'Mission4')],
                'per_visit': [('m1_acc','Mission1 Total Accuracy'),
                              ('m2_acc','Mission2 Total Accuracy'),
                              ('m3_acc','Mission3 Total Accuracy'),
                              ('m4_acc','Mission4 Total Accuracy'),
                              ('m1_mrt','Mission1 Total Mean Reaction Time'),
                              ('m2_mrt','Mission2 Total Mean Reaction Time'),
                              ('m3_mrt','Mission3 Total Mean Reaction Time'),
                              ('m4_mrt','Mission4 Total Mean Reaction Time'),
                              ('m1_rtsd','Mission1 Total MRT STD'),
                              ('m2_rtsd','Mission2 Total MRT STD'),
                              ('m3_rtsd','Mission3 Total MRT STD'),
                              ('m4_rtsd','Mission4 Total MRT STD'),
                              ('m1_omit','Mission1 Total Omit'),
                              ('m2_omit','Mission2 Total Omit'),
                              ('m3_omit','Mission3 Total Omit'),
                              ('m4_omit','Mission4 Total Omit'),
                              ('m1_comit','Mission1 Total Comit'),
                              ('m2_comit','Mission2 Total Comit'),
                              ('m3_comit','Mission3 Total Comit'),
                              ('m4_comit','Mission4 Total Comit'),
                              ('all_acc', 'All Missions Accuracy'),
                              ('all_mrt', 'All Missions Mean Reaction Time'),
                              ('all_rtsd', 'All Missions MRT STD'),
                              ('all_omit', 'All Missions Omit'),
                              ('all_comit', 'All Missions Comit'),
                              ('upload', 'Upload Complete')],
                'form': 'RepetitionTask2'}}

for task, d in data.items():
    for visit, visit_text in d['visit']:
        for m, m_text in d['mission']:
            for res, res_text in d['per_mission']:
                task_print = [task]
                if visit:
                    task_print.append(visit)
                if m:
                    task_print.append(m)
                task_print.append(res)

                print('\t'.join(['_'.join(task_print), d['form'], '', 'text', ' '.join([d['form'], visit_text, m_text, res_text])]))
                # print '_'.join(task_print)
        for res,res_text in d['per_visit']:
            if res:
                task_print = [task]
                if visit:
                    task_print.append(visit)
                task_print.append(res)
                print('\t'.join(['_'.join(task_print), d['form'], '', 'text', ' '.join([d['form'], visit_text, res_text])]))
                # print '_'.join(task_print)
