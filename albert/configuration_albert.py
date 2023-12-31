""" BERT model configuration """
from __future__ import absolute_import, division, print_function, unicode_literals

import json
import logging
import sys
from io import open

from .configuration_utils import PretrainedConfig
logger = logging.getLogger(__name__)

class AlbertConfig(PretrainedConfig):
    r"""
        Arguments:
            vocab_size_or_config_json_file: Vocabulary size of `inputs_ids` in `BertModel`.
            hidden_size: Size of the encoder layers and the pooler layer.
            num_hidden_layers: Number of hidden layers in the Transformer encoder.
            num_attention_heads: Number of attention heads for each attention layer in
                the Transformer encoder.
            intermediate_size: The size of the "intermediate" (i.e., feed-forward)
                layer in the Transformer encoder.
            hidden_act: The non-linear activation function (function or string) in the
                encoder and pooler. If string, "gelu", "relu" and "swish" are supported.
            hidden_dropout_prob: The dropout probabilitiy for all fully connected
                layers in the embeddings, encoder, and pooler.
            attention_probs_dropout_prob: The dropout ratio for the attention
                probabilities.
            max_position_embeddings: The maximum sequence length that this model might
                ever be used with. Typically set this to something large just in case
                (e.g., 512 or 1024 or 2048).
            type_vocab_size: The vocabulary size of the `token_type_ids` passed into
                `BertModel`.
            initializer_range: The sttdev of the truncated_normal_initializer for
                initializing all weight matrices.
            layer_norm_eps: The epsilon used by LayerNorm.
    """
    def __init__(self,
                 # 单词数量，VS
                 vocab_size_or_config_json_file=30000,
                 # 嵌入向量长度，ES
                 embedding_size=128,
                 # 隐藏层嵌入向量长度，HIS
                 # 注意和上面那个不一样
                 hidden_size=4096,
                 # TFBlock 数量 NL
                 num_hidden_layers=12,
                 # TFBlock 分组数量，NG
                 num_hidden_groups=1,
                 # 注意力头部数量,HC
                 num_attention_heads=64,
                 # FFN 层嵌入向量长度，一般是 4HIS
                 intermediate_size=16384,
                 # 组内 TF 块的数量
                 inner_group_num=1,
                 # 激活函数
                 hidden_act="gelu_new",
                 # FFN 的 Dropout 概率
                 hidden_dropout_prob=0,
                 # 注意层的 Fropout 概率
                 attention_probs_dropout_prob=0,
                 # 最大序列长度，SL
                 max_position_embeddings=512,
                 # TVS，句子个数
                 type_vocab_size=2,
                 # 随机初始化范围
                 initializer_range=0.02,
                 # LN 的容差项
                 layer_norm_eps=1e-12,
                 **kwargs):
        super(AlbertConfig, self).__init__(**kwargs)
        if isinstance(vocab_size_or_config_json_file, str) or (sys.version_info[0] == 2
                        and isinstance(vocab_size_or_config_json_file, unicode)):
            # 如果`vocab_size_or_config_json_file`是个字符串，它保存 JSON 配置文件名称
            # 将其读入并解析，然后把所有属性导入对象中
            with open(vocab_size_or_config_json_file, "r", encoding='utf-8') as reader:
                json_config = json.loads(reader.read())
            for key, value in json_config.items():
                self.__dict__[key] = value
        elif isinstance(vocab_size_or_config_json_file, int):
            # 如果`vocab_size_or_config_json_file`是整数，将所有参数赋给同名属性
            self.vocab_size = vocab_size_or_config_json_file
            self.hidden_size = hidden_size
            self.num_hidden_layers = num_hidden_layers
            self.num_attention_heads = num_attention_heads
            self.hidden_act = hidden_act
            self.intermediate_size = intermediate_size
            self.hidden_dropout_prob = hidden_dropout_prob
            self.attention_probs_dropout_prob = attention_probs_dropout_prob
            self.max_position_embeddings = max_position_embeddings
            self.type_vocab_size = type_vocab_size
            self.initializer_range = initializer_range
            self.layer_norm_eps = layer_norm_eps
            self.embedding_size = embedding_size
            self.inner_group_num = inner_group_num
            self.num_hidden_groups = num_hidden_groups
        else:
            raise ValueError("First argument must be either a vocabulary size (int)"
                             " or the path to a pretrained model config file (str)")
