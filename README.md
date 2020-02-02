# 目录
- 20世纪60年代——词袋（bag-of-words，BoW）
- 20世纪70年代——TF-IDF
- 前馈神经网络——基于上下文 word2vec
- 参考

# 20世纪60年代——词袋（bag-of-words，BoW）

对于文本数据，我们可以从一个单词数量的统计列表开始，这称为词袋（bag-of-words，BoW）。

- 行是单词，列是文章
- 每个单词，都是一个高维空间中的某一个特定维表示，
- 这样一个词就可以用一个只有一维为1而其他维为0的向量（one-hot-vector）来表示。
- 在词袋向量中，每个单词都是向量的一个维。如果词汇表中有n个单词，
那么一篇文章就是n维空间中的一个点。
- 进而，一篇文章，可以用它所包含的词向量`相加`表示，得到文章的向量。
- 进而，两篇文章的额相似性，用它们的`余弦`值来度量。
- 通过定义文本文档的词袋特征化，一个特征就是一个单词，
一个特征向量由这个单词在每篇文档中出现的次数组成。

缺点：
- 词袋远非完美。如果我们无差别地对所有单词计数，
那么有些单词会被过分强调。
- 单词列表并不试图找出有意义的实体。
- 将句子分解为单词会破坏语义。无论是在中文，还是英文，都会存在歧义。
- 词袋中没有任何序列，它只是记录每个单词在文本中出现的次数。
- 没有考虑上下文。
词袋也不表示任何单词层次。例如，"动物"这个词，包括狗、猫等，但是在词袋中，
这些单词在向量中都是平行的。
- 词袋是一种简单而有效的启发式方法，离正确的文本语义理解还想去甚远。

优点：
- 词袋表示法简单易懂，容易计算，并对分类和搜索任务非常有效。
但有时当呃呃呃单词还是太简单了，无法表述文本中的某些信息。
- 在词袋表示中，重要的是特征空间中的数据分布。
所以，把BoW当做是一种文档分类、信息提取的工具，很合适。
- 两种任务：文档分类、信息提取，都可以凭借单词级别的特征圆满地完成，
因为特定词是否存在于文档中这个指标可以很好地标识问的那个的主题内容。

# 20世纪70年代——TF-IDF

在此之前，是各种相似度计算方法的改进。

TF-IDF算法，改进了词权重的计算方法。大幅度提高了文档相似度计算的准确率。
在计算文档向量时，不再用简单的0、1，而是用一个权重来表示词的重要性。
对于未出现的词，仍然用0.

以这个词在当前文档中出现的次数为分子
已该词在所有文档中出现的次数的log值为分母
两者相除作为权重。
理解为：把所有文档放在一起考虑，那些文档中较少出现的词往往表达了更加具体，更有针对性。
给予更高的权重，否则，表达的含义更宽泛，权重也越小。

缺点：
- 换汤不换药。
- 仍然基于one-hot-vector，只是计算权重方式不同而已。
- 无法表达词的语义相关度。
- 实际中，会发现，`称赞`和`夸奖`是近义词；`称赞`和`诋毁`是反义词；`称赞`和`营业`无关词。
但他们的相似度都是0.

# 前馈神经网络——基于上下文 word2vec

神经网络节点之间的连接不存在环（存在环，CNN），即前一层节点的输出作为后一层节点的输入。
这样，一层层计算，直到最后输出层输出结果。

为了解决这个问题，我们要求助长更长的序列。
n元词袋是词袋的一种自然推广，他的概念非常好理解，计算起来也和词袋一样容易。
n元词袋（bag-of-n-grams），是词袋的一种自然扩展。1-gram，2-gram，n-gram

通常只使用二元词和三元词，很少使用更长的n元词。

优点：
- 与one-hot-vector不同，这个向量每个维都有值，并非只有一个维为非0.
- 语义相关度，两个向量之间的余弦。对于两个近义词，他们的向量往往比较接近。
- 例如，国王是男人，王后是女人。那么，e queen -e women = e king -e man
- 如果说，武则天呢，其实一样的。

缺点：
- 无法很好地表达一些特定的短语。
这些短语由多个词构成，但其语义却不是所含各个词的语义的简单叠加。
这个问题，不仅仅是英文存在很大问题，中文的问题更大，比如，典故。
- 基于词的上下文（当前词临近的一个小窗口内的词）信息学习词汇语义的特点，
似的他可能不足以表达一个词的完整语义。
例如，`good`和`bad`反义词，完全不同的情感取向，但它们对应的分布式表达却比较接近，
这对于诸如情感分析应用是一个大问题。

# 召回

鉴于以上（文档分类、信息提取），用`word2vec`做粗排召回很合适的。


# 参考
- [gensim API Reference](https://radimrehurek.com/gensim/apiref.html)
- [gensim Documentation](https://radimrehurek.com/gensim/auto_examples/index.html)
- [Word2Vec Model](https://radimrehurek.com/gensim/auto_examples/tutorials/run_word2vec.html#sphx-glr-auto-examples-tutorials-run-word2vec-py)
- [models.word2vec – Word2vec embeddings](https://radimrehurek.com/gensim/models/word2vec.html)
- [Doc2Vec Model](https://radimrehurek.com/gensim/auto_examples/tutorials/run_doc2vec_lee.html#sphx-glr-auto-examples-tutorials-run-doc2vec-lee-py)
- [FastText Model](https://radimrehurek.com/gensim/auto_examples/tutorials/run_fasttext.html#sphx-glr-auto-examples-tutorials-run-fasttext-py)
- [LDA Model](https://radimrehurek.com/gensim/auto_examples/tutorials/run_lda.html#sphx-glr-auto-examples-tutorials-run-lda-py)
- [Core Concepts](https://radimrehurek.com/gensim/auto_examples/core/run_core_concepts.html)
- [text8 Data](http://mattmahoney.net/dc/text8.zip)