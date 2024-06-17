from transformers import pipeline
PRETRAINED = "raynardj/ner-disease-ncbi-bionlp-bc5cdr-pubmed"
ners = pipeline(task="ner",model=PRETRAINED, tokenizer=PRETRAINED)

import pickle as pk
with open('newsave_model', 'wb') as f:
    pk.dump(ners, f)
