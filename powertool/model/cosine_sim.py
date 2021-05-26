from numpy import dot
from numpy.linalg import norm
import numpy as np
import glob
from Data import gds2string
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import linear_kernel

from itertools import combinations, islice

from sklearn.metrics.pairwise import cosine_similarity

import difflib
import math
# similar_score = cosine_similarity()

class GDSMixer:
    def __init__(self):
        self.gds_string_list = []
        self.gds_file_name_list = []
        self.group_labels = []
        self.pattern_labels = []
        self.group_and_pattern_labels = dict(group=[], pattern=[])

        self.pattern_hash_flag = True
        self.pattern_hash = dict()

        self.debug_gds_string_list=[]

    def load_folder(self, path):
        for file in glob.iglob(path + '/*.gds'):
            self.load_file(file)
            # loader = gds2string.GDSloader(file=file, structure_include_flag=False)
            # self.gds_string_list.append(loader.transform_gds_to_string())
            #
            # if self.pattern_hash_flag:
            #     self.pattern_hash[loader.transform_gds_to_string()] = self.extract_pattern_from_filename(file)
            #     self.debug_gds_string_list.append(loader.transform_gds_to_string())

    def load_file(self,file):
        loader = gds2string.GDSloader(file=file, structure_include_flag=False)
        self.gds_string_list.append(loader.transform_gds_to_string())

        if self.pattern_hash_flag:
            self.pattern_hash[loader.transform_gds_to_string()] = self.extract_pattern_from_filename(file)
            self.debug_gds_string_list.append(loader.transform_gds_to_string())


    def mixing(self, combination=2, max_num = 10000):
        #### flushing ####
        self.group_labels = []
        self.pattern_labels = []
        self.group_and_pattern_labels = dict(group=[], pattern=[])
        concat_list = []
        ##################

        # do combination
        combination_list = list(islice(combinations(self.gds_string_list, combination),max_num))

        # for each combination, divide group,
        for combi in combination_list:
            tmp_group_labels = [x.count("\n") for x in combi]
            concat_list.append("".join(combi))
            idx_list = list(range(concat_list[-1].count("\n")))
            group_labels = []
            pattern_labels = []
            for i, count in enumerate(tmp_group_labels):
                # group labels
                group_labels.append(idx_list[0:count])
                del idx_list[0:count]

                # pattern labels
                if combi[i] in self.pattern_hash:
                    pattern_labels.append(self.pattern_hash[combi[i]])
                else:
                    raise Exception("Pattern labeling failed, pattern_hash_flag should be True.")


            self.group_labels.append(group_labels)
            self.group_and_pattern_labels['group'].append(group_labels)
            self.group_and_pattern_labels['pattern'].append(pattern_labels)

            # if i >= max_num:
            #     break
        return concat_list

    def get_group_answer(self):
        return self.group_labels

    def get_labels(self):
        return self.group_and_pattern_labels

    def extract_pattern_from_filename(self,file_name):
        if 'boundary_array' in file_name:
            return 'boundary_array'
        elif 'path_array' in file_name:
            return 'path_array'
        elif 'connect' in file_name:
            return 'connect'
        elif 'distance' in file_name:
            return 'distance'

class Grouping:
    def __init__(self, vectorizer='Counter'):
        self.vector_type = vectorizer
        if self.vector_type is 'Counter':
            self.vectorizer = CountVectorizer()
        elif self.vector_type is 'Tfidf':
            self.vectorizer = TfidfVectorizer()
        else:
            raise Exception("vectorizer should be 'Counter' or 'Tfidf'.")

        self.sentence_matrix = None
        self.idx = None

    def grouping_main(self, sentences, vectorizer=None, threshold=0.5, labels=None, score=False, pseudo_labeling=False):
        output = dict()
        if vectorizer != None:
            self.vector_type=vectorizer
        self.load_series_of_sentence(sentences)
        group_dict = self.grouping(threshold=threshold)
        output['group_of_gds_string'] = self.group_dict_to_gds_string_group(group_dict,self.sentence_chunk_to_list(sentences))
        if score:
            if not labels:
                raise Exception('To activate score, label is required.')
            output['score'] = self.score(group_dict,labels['group'])

        if pseudo_labeling:
            if not labels:
                raise Exception('To activate pseudo_labeling, label is required.')
            output['pseudo_label'] = self.pseudo_labeling(predict=group_dict,group_and_pattern_labels=labels)
        return output

    def group_dict_to_gds_string_group(self,group_dict,sentences):
        gds_string_group = []
        for key in group_dict:
            sentences_of_group = []
            for idx in group_dict[key]:
                sentences_of_group.append(sentences[idx])
            gds_string_group.append("\n".join(sentences_of_group))

        return gds_string_group


    def sentence_chunk_to_list(self, chunk):
        # chunk_ex ="BOUNDARY X_100 Y_200 LAYER_50 \nPATH LAYER_30 X_100 Y_200"
        if type(chunk) is str:
            sentence_list = chunk.split('\n')
        else:
            raise Exception("Chunk type should be str")
        return sentence_list

    def load_series_of_sentence(self, sentences):
        if self.vector_type is 'Counter':
            self.vectorizer = CountVectorizer()
        elif self.vector_type is 'Tfidf':
            self.vectorizer = TfidfVectorizer()
        else:
            raise Exception("vectorizer should be 'Counter' or 'Tfidf'.")

        if type(sentences) is str:
            sentences = self.sentence_chunk_to_list(sentences)
        elif type(sentences) is list:
            pass
        else:
            raise Exception("sentences type should be str or list.")

        self.sentence_matrix = self.vectorizer.fit_transform(sentences)
        self.idx = np.arange(len(sentences))

    def grouping(self, threshold=0.5):
        if self.sentence_matrix == None:
            raise Exception("You should call load_series_of_sentence before calling grouping")
        similarity_matrix = cosine_similarity(self.sentence_matrix, self.sentence_matrix)
        # print(similarity_matrix)
        idx = np.where(similarity_matrix >= threshold)
        group_dict = dict()
        for i in range(len(idx[0])):
            x, y = idx[0][i], idx[1][i]
            if y <= x:
                pass
            else:
                if x not in group_dict:
                    group_dict[x] = [x, y]
                else:
                    group_dict[x].append(y)

        #delete subset group.
        delete_index = []
        for target in group_dict:
            for ref in list(filter(lambda x: x<target, group_dict.keys())):
                if self.subset_checker(group_dict[target],group_dict[ref]):
                    delete_index.append(target)
                    # del group_dict[target]
                    break
        # del group_dict[key in delete_index]
        # print(delete_index)
        for delete_target in delete_index:
            del group_dict[delete_target]
        return group_dict

    def subset_checker(self, subset, mainset):
        for sub_element in subset:
            if sub_element not in mainset:
                return False
        return True

    def similarity_analyze(self, sentences, vectorizer='Counter'):
        if type(sentences) is str:
            sentences = self.sentence_chunk_to_list(sentences)
        elif type(sentences) is list:
            pass
        else:
            raise Exception("sentences type should be str or list.")

        if vectorizer is 'Counter':
            _vectorizer = CountVectorizer()
        elif vectorizer is 'Tfidf':
            _vectorizer = TfidfVectorizer()
        else:
            raise Exception("vectorizer should be 'Counter' or 'Tfidf'.")
        sentence_matrix = _vectorizer.fit_transform(sentences)
        similarity_matrix = cosine_similarity(sentence_matrix, sentence_matrix)
        print(similarity_matrix)

    def score(self,predict,label):
        """
        :param predict: grouping model's output -> dict type
        :param label:  answer of the grouping -> doubled list type
        :return: score
        """
        labels_count = len(label)
        predict_count = len(predict)
        if predict_count is 0:
            return [0,0,0,0]

        similarity_list = []
        for predict_key in predict:
            similarity_list.append(
                max([difflib.SequenceMatcher(None,predict[predict_key],x).ratio() for x in label])
            )

        score_1 = (labels_count-abs(labels_count-predict_count)/10)/labels_count * np.mean(similarity_list)
        score_2 = (1-math.exp(-1/labels_count)*abs(labels_count-predict_count)/labels_count)*np.mean(similarity_list)
        score_3 = (1-math.exp(-1/labels_count)*abs(labels_count-predict_count)/labels_count/2)*np.mean(similarity_list)
        score_4 = np.mean(similarity_list)
        if score_3 < 0:
            print('debug')
        # if math.isnan(score_1 or score_2 or score_3):
        #     print(similarity_list)
        return [score_1,score_2,score_3,score_4]

    def pseudo_labeling(self,predict,group_and_pattern_labels, thrsehold = 0.0):
        """
        :param predict:  grouping model's output -> dict type
        :param label: answer of the grouping -> doubled list type
        :return: grouping model's output and pseudo label -> dict type
        """
        group_labels = group_and_pattern_labels['group']
        pattern_labels = group_and_pattern_labels['pattern']
        pseudo_pattern_list = []
        for predict_key in predict:
            similar_vector = [difflib.SequenceMatcher(None,predict[predict_key],x).ratio() for x in group_labels]
            if max(similar_vector) > thrsehold:
                labels_idx = similar_vector.index(max(similar_vector))
                pseudo_pattern = pattern_labels[labels_idx]
            #TODO when similarity is less than threshold, I need to handle exceptional case.
            else:
                pseudo_pattern = 'Unknown'
            pseudo_pattern_list.append(pseudo_pattern)

        return pseudo_pattern_list




def main1():
    doc = ['BOUNDARY X_100 Y_200',
           'PATH X_200 Y_400',
           'PATH X_100 Y_400',
           'BOUNDARY LAYER_10 X_300 Y_400']

    # doc = Grouping().sentence_chunk_to_list('BOUNDARY X_100 Y_200 LAYER_50 \nPATH LAYER_30 X_100 Y_200')

    vectorizer = TfidfVectorizer()
    vectorizer_count = CountVectorizer()
    vector_sent = vectorizer.fit_transform(doc)
    vector_sent_count = vectorizer_count.fit_transform(doc)


    mixer = GDSMixer()
    mixer.load_folder('./Data/mix_test_data')


    for combi in [2,3,4,5,10]:
        # for combi in [10]:
        k = mixer.mixing(combination=combi)
        labels = mixer.get_group_answer()

        mixer_group = Grouping()
        print('Counter')
        score_list = []
        sc2_list, sc3_list, sc4_list = [], [], []
        for i, mixed_sentences in enumerate(k):
            mixer_group.load_series_of_sentence(mixed_sentences)
            predict = mixer_group.grouping(0.4)
            # score_l = mixer_group.score(predict = predict,label = labels[i])
            score,sc2,sc3, sc4 = mixer_group.score(predict = predict,label = labels[i])
            # score,sc2,sc3 = score_l[0],score_l[1],score_l[2]
            if score<0.1:
                print(predict)
                print(mixed_sentences)
                print(f'score:{score}')
            score_list.append(score)
            sc2_list.append(sc2)
            sc3_list.append(sc3)
            sc4_list.append(sc4)

        avg1 = np.mean(score_list)
        avg1_2 = np.mean(sc2_list)
        avg1_3 = np.mean(sc3_list)
        avg1_4 = np.mean(sc4_list)
        # print('Average Score = {}'.format(avg1))

        print('Tfidf')
        mixer_group = Grouping('Tfidf')
        score_list = []
        sc2_list, sc3_list, sc4_list = [], [], []
        for i, mixed_sentences in enumerate(k):
            mixer_group.load_series_of_sentence(mixed_sentences)
            predict = mixer_group.grouping(0.2)
            # score_l = mixer_group.score(predict = predict,label = labels[i])
            score_l= mixer_group.score(predict = predict,label = labels[i])
            score,sc2,sc3, sc4 = score_l[0],score_l[1],score_l[2], score_l[3]
            if sc2 < 0.1:
                print(labels[i])
                print(predict)
                print(mixed_sentences)
                print(f'score:{sc2}')
            score_list.append(score)
            sc2_list.append(sc2)
            sc3_list.append(sc3)
            sc4_list.append(sc4)

        avg2 = np.mean(score_list)
        avg2_2 = np.mean(sc2_list)
        avg2_3 = np.mean(sc3_list)
        avg2_4 = np.mean(sc4_list)
        print(f'Combination = {combi}, num of data = {len(k)}')
        print(f'Group coefficient: 1/10')
        print('Average Score1 (counter) = \t{}'.format(avg1))
        print('Average Score1 (Tfidf )  = \t{}'.format(avg2))
        print(f'Group coefficient: exp(-1/AG)')
        print('Average Score2 (counter) = \t{}'.format(avg1_2))
        print('Average Score2 (Tfidf )  = \t{}'.format(avg2_2))
        print(f'Group coefficient: exp(-1/2AG)')
        print('Average Score3 (counter) = \t{}'.format(avg1_3))
        print('Average Score3 (Tfidf )  = \t{}'.format(avg2_3))
        print(f'Group coefficient: 0')
        print('Average Score4 (counter) = \t{}'.format(avg1_4))
        print('Average Score4 (Tfidf )  = \t{}'.format(avg2_4))

def main2():

    mixer = GDSMixer()
    mixer.load_folder('./Data/TrainData_v4')
    mixer_group = Grouping('Tfidf')

    combi = 3
    mixed_gds = mixer.mixing(combination=combi)
    labels = mixer.get_labels()

    g_label = labels['group']
    p_label = labels['pattern']
    pseudo_labels = []
    for i, mixed_sentences in enumerate(mixed_gds):
        mixer_group.load_series_of_sentence(mixed_sentences)
        predict = mixer_group.grouping(0.2)
        pseudo_labels.append(mixer_group.pseudo_labeling(predict= predict,group_and_pattern_labels=dict(group=g_label[i], pattern=p_label[i])))

def main3():
    # main1()
    # main2()
    mixer = GDSMixer()
    mixer.load_folder('./Data/TrainData_v4')
    combi = 3
    mixed_gds = mixer.mixing(combination=combi)
    labels = mixer.get_labels()

    mixer_group = Grouping()
    group_data_and_label = dict(data = [], label = [])
    for i, mixed_sentences in enumerate(mixed_gds):
        tmp_label = dict(group=labels['group'][i], pattern=labels['pattern'][i])
        tmp = mixer_group.grouping_main( sentences=mixed_sentences, vectorizer='Tfidf', threshold=0.2, labels=tmp_label, score=True, pseudo_labeling=True)
        group_data_and_label['data'].extend(tmp['group_of_gds_string'])
        group_data_and_label['label'].extend(tmp['pseudo_label'])



def main_not_mixing_just_grouping():
    grouper = Grouping()
    group_data_and_label = dict(data=[],labels=[])
    for i, mixed_sentences in enumerate(mixed_gds):
        tmp_label = dict(group=labels['group'][i], pattern=labels['pattern'][i])
        tmp = mixer_group.grouping_main( sentences=mixed_sentences, vectorizer='Tfidf', threshold=0.2, labels=tmp_label, score=True, pseudo_labeling=True)
        group_data_and_label['data'].extend(tmp['group_of_gds_string'])
        group_data_and_label['labels'].extend(tmp['pseudo_label'])


if __name__ == '__main__':
    file = './Data/test_gds/nmos_2.gds'
    loader = gds2string.GDSloader(file=file, structure_include_flag= False)
    sentences = loader.transform_gds_to_string()
    print(sentences)
    grouper = Grouping()
    group_data_and_label = dict(data=[],labels=[])
    # for i, mixed_sentences in enumerate(sentences):
    # tmp_label = dict(group=labels['group'][i], pattern=labels['pattern'][i])
    tmp = grouper.grouping_main( sentences=sentences, vectorizer='Tfidf', threshold=0.2, labels=None, score=False, pseudo_labeling=False)
    group_data_and_label['data'].extend(tmp['group_of_gds_string'])
    # group_data_and_label['labels'].extend(tmp['pseudo_label'])


