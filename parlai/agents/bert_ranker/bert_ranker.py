#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
from .biencoder_ranker import BiEncoderRankerAgent  # NOQA
from .crossencoder_ranker import CrossEncoderRankerAgent  # NOQA
from .bothencoder_ranker import BothEncoderRankerAgent  # NOQA
from parlai.core.torch_agent import TorchAgent


class BertRankerAgent(TorchAgent):

    def __init__(self, opt, shared=None):
        raise RuntimeError("You must specify which ranker to use. Choices: \n"
                           "-m bert_ranker:BiEncoderRanker \n"
                           "-m bert_ranker:CrossEncoderRanker \n"
                           "-m bert_ranker:BothEncoderRanker")
