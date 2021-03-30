# ByteDance 

_Round 1_
1. Tell me about the chatbot project

Was built to serve Freshmen. Answer FAQ. Focus on less code and more scalability and low maintenance. 

2. How do you prepare your training data
   
Collect from departments, store in excel due to expertise level at NTU Depts.

3. What kind of queries do the chatbot accept

General enquiry. No technical (law, medical, etc...)

4. How do you code the chatbot? 

Hello I was using Dialogflow API

1. Do you know what the mechanism behind is? 

Probably an early bert. Although api.ai might have used a very simple intent detection system. 

_Round 2:_ 

1. Introduce yourself 

2. Chatbot Project 

3. SVM versus Logistic Regression
   
Both are supervised. Used for classification problems. SVM tries to maximize margin between support vectors. LR tries to maximize posteriors. LR is used if you think data is non-linear separable. (although there is SVM with non-linear kernel like RBF)

[source 1](https://medium.com/axum-labs/logistic-regression-vs-support-vector-machines-svm-c335610a3d16)

4. Code to test if two strings are 1 edit distance away from each other. 

There are two approaches: 
a. Brute force insertion, deletion and replacement (which is what i did)
b. Use DP for calculating Levenshtein (all cost = 1), then find if they are 1. 

5. Are you familiar with Tf and Pytorch? 
   Well yes

6. Explain Transformers architecture? 
   Use the diagram to explain

7. Why do we need a masked multi headed attention in the decoder?
   Because we want it to predict the nextword, but Transformer input the whole sequence all at once. Masking it one at a time makes it more _rnn_ like. 







_P.S. Notes:_ qns I ask them:

_Round 1:_

What is the culture like? -- \[open, aggressive, collaborative.\] 

Has mentor that you can ask anything -- \[life, career, progress etc. \]

_Round 2:_

The most exciting project you have embarked on? -- _OSA_ 

What is the workflow there? -- Have separate Data Engineering Team and NLP Team. NLP Team can issue request for data, and then focus more on model buildings.

