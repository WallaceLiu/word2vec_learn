import jieba
# import gensim.models.word2vec as w2v
from gensim.test.utils import common_texts
from gensim.models import KeyedVectors, Word2Vec

# file_path = '../txt/yitiantulongji.txt'

#
# fin = open(file_path, 'r', encoding='UTF-8')
# fou = open(file_segment_path, 'w', encoding='UTF-8')
# line = fin.readline()
# while line:
#     newline = jieba.cut(line, cut_all=False)
#     str_out = ' '.join(newline).replace('，', '').replace('。', '').replace('?', '').replace('!', '') \
#         .replace('“', '').replace('”', '').replace('：', '').replace('‘', '').replace('’', '').replace('-', '') \
#         .replace('（', '').replace('）', '').replace('《', '').replace('》', '').replace('；', '').replace('.', '') \
#         .replace('、', '').replace('...', '').replace(',', '').replace('？', '').replace('！', '')
#     print(str_out, file=fou)
#     line = fin.readline()
# fin.close()
# fou.close()
for t in common_texts:
    print(t)

# model = Word2Vec(common_texts, size=100, window=5, min_count=1, workers=4)
# word_vectors = model.wv






#
# file_segment_path = '../txt/jinYong_segment.txt'
# model_file_name = '../txt/jinYong_vector.txt'
# # sentences = w2v.LineSentence(file_segment_path)
#
# word_vectors = KeyedVectors.load(model_file_name, mmap='r')
#
# # word_vectors = KeyedVectors.load_word2vec_format(datapath('word2vec_pre_kv_c'), binary=False)
#
# # model = w2v.Word2Vec(sentences, size=20, window=5, min_count=5, workers=4)
# s = word_vectors.most_similar('张君宝')
#
# # gensim.models.keyedvectors.WordEmbeddingsKeyedVectors.most_similar
# print(s)
