import jieba
import gensim.models.word2vec as w2v

# file_path = '../txt/jinYong.txt'

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

file_segment_path = '../txt/jinYong_segment.txt'
# model_file_name = '../txt/jinYong_vector.txt'
sentences = w2v.LineSentence(file_segment_path)
model = w2v.Word2Vec(sentences, size=20, window=5, min_count=5, workers=4)
s = model.most_similar('张三丰')
print(s)
