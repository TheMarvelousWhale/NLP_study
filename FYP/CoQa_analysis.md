# Preliminary Analysis on CoQa dataset

Src: https://stanfordnlp.github.io/coqa/

![wiggle](./Assets/wiggle.gif)

CoQa is a set of questions, answers and rationale tagging. The format looks like this: 

```
Q1: Who had a birthday?
A1: Jessica
R1:  Jessica went to sit in her rocking chair.  Today was herbirthday and she was turning 80.

Q2: How old would she be?
A2: 80
R2: she was turning 80

Q3: Did she plan to have any visitors?
A3: Yes
R3: Her granddaughter Annie was coming over
```

The task is given Q and R so far, give the answer to the latest question. 
This task demands that the model understand the conversational history and know what is being asked. 

What makes CoQa very, very hard is co-reference. About half the questions in CoQA contain an explicit co-reference (some indicator like him, it, her, that). Close to a fifth of the questions contain an implicit co-reference. This is when you ask a question like “where?” We are asking for something to be resolved, but it’s implied. This is very hard for machines.

The current non-ensemble method is https://arxiv.org/abs/1909.10772 
It uses:
* rationale tagging multi-task utilizing the valuable information in the answer’s rationale; 
* adversarial training (Miyato et al., 2016) in-creasing model’s robustness to perturbations (data augmentation form)
*  knowledge distillation (Furlanello et al.,2018) making use of additional training sig-nals from well-trained models.

Code wise: data is available in tensorflow, just import
https://www.tensorflow.org/datasets 

A less challenging implementation would be fine tune BERT: https://paperswithcode.com/paper/bert-pre-training-of-deep-bidirectional 

My questions would be:

*  How is understanding of conversation history useful for us? (I can think of SCDF)
*  Assuming we can train a model on CoQa, how can we finetune it to our usecase
*  If we cannot, what can we do (in terms of feature extraction or architecture) to apply the research into our model?