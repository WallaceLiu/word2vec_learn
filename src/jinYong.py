import jieba
import gensim.models.word2vec as w2v

file_path = '../txt/jinYong.txt'
file_segment_path = '../txt/jinYong_segment.txt'

fin = open(file_path, 'r', encoding='UTF-8')
fou = open(file_segment_path, 'w', encoding='UTF-8')
line = fin.readline()
while line:
    newline = jieba.cut(line, cut_all=False)
    str_out = ' '.join(newline).replace('，', '').replace('。', '').replace('?', '').replace('!', '') \
        .replace('“', '').replace('”', '').replace('：', '').replace('‘', '').replace('’', '').replace('-', '') \
        .replace('（', '').replace('）', '').replace('《', '').replace('》', '').replace('；', '').replace('.', '') \
        .replace('、', '').replace('...', '').replace(',', '').replace('？', '').replace('！', '')
    print(str_out, file=fou)
    line = fin.readline()
fin.close()
fou.close()

model_file_name = '../txt/jinYong_vector.txt'
# 模型训练，生成词向量
sentences = w2v.LineSentence(file_segment_path)
model = w2v.Word2Vec(sentences, size=20, window=5, min_count=5, workers=4)
model.save(model_file_name)
