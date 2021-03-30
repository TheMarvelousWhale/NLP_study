# NLP Interview Questions

Well first thing first a gif.

![chaeng](./Assets/chaeng.gif)

Now the questions:

1. Explain posterior vs likelihood?

If we can clearly distinguish parameters θ and the evidence X. θ can sometimes be latent vairables, and X is usually called the observable. 

Then posterior is P(θ|X). The likelihood is P(X|θ). 

2. What are stopwords?

words that do not contribute to the meaning (semantics) of a sentence. Rather they are there for the syntactic soundness (gramatical correctness). 

3. Explain tf-idf? 

It shows how relevant a word is in a document/a collection of documents (impt for InfoRetrieval system). It combines two metrics: tf: term frequency and idf: inverse document frequency).
Term frequency (#term/#words) is a metrics showing how many times the term appears in a document. IDF is (#documents/#docs_with_t). Both take log for numerical stability (+1 for idf since #docs_with_t can be 0).

```
tf*idf = log(n_t/n_d)*log(N/(df_t+1))
```

4. Syntactic, Semantic, Pragmatic Analysis

Syntactic analysis studies the structure and order of words as well as their roles in a sentence. This can derive some meaning of the sentences, but not quite. 

The important steps are often: 
sentences tokenize > remove punctutations and symbols > lemmatize / stem > POS tagging 
_lemma is an actual word, vs stem might not be_

Semantics are study of the meaning behind a sentence, even when they are hugely different in syntax. 

Pragmatic is see if something is outdomain. 

5. NLTK

WELL FOR EACH LANGUAGE YOU GONNA USE A DIFFERENT ONE SO WOOPS. I use sentence tokenizer for each language, regex to remove punctuations and then see from there. 

important nltk imports
```
WordnetLemmatizer
PorterStemmer
nltk.[N]grams
  from nltk.corpus import stopwords
   stop_words = set(stopwords.words('english'))
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.pos_tag
```

you can also use spacy. Gensim is also a great tool, but often for similarity stuff. Stanford CoreNLP is great but u need RAM. 

6. Possible metrics
That is a task better be explained in [here](./Metrics.md)

7. Decoder Encoder? Auto encoder? 

8. What is attention? 
  
The ability of a matrix to show how each word correlates to each othter throughout the entire sequence. Was first introduced in the MLT model to make more accurate prediction. 

9.  NLPaaS and common pitfalls?

* Production wise:
  * Clear output for other business models/systems
  * Feedback/Callback for validating predictions
  * Db for training and testing, as well as production history for further trainign
  * Orchestrator: to retrain and implement
  * VC tools
  * Visualizer tools
* Pitfalls: 
  * Exposing preprocessing steps to clients
  * Error handling
  * OOV issues
  * Unexepected user input

#
[Volume 2](./NLP_interview_qns_vol2.md)

[Corporate Qns](./NLP_questions_that_Company_Asked_me.md)

