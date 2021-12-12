<h3> Spam_detector using LSTM_RNN and Bidirectional_LSTM_RNN</h3>
Bidirectional LSTM

<img src="/images/1.png" width="700" height="400">

Spam - whether in the form of emails, messages, etc. - is a nuisance. Thanks to deep learning algorithms, the problem is now well under control. Here I show with a Recurrent Neural Network (RNN) model how fast and uncomplicated a model can be calculated that can distinguish spam from non-spam. The used dataset is the "SMS Spam Collection", which can be found at Kaggle under "https://www.kaggle.com/ishansoni/sms-spam-collection-dataset".


<h3>  Data preprocessing </h3>
 
     1 . Cleaning the text 
     2 . changing the text format to lower cases
     3 . stemming 
     4 . Lemmatization
     5 . stopwords
     
<h3> Vectorization <h3>
   
     1 . one_hot_encoding
     2 . Bag_of_words
     3 . TF_IDF
     4 . Word_Embeddings
         a . word_2_vec
         b . Glove 

 <h3>  Build Data loaders </h3>
 So far, data is processed and prepared as vectorized form.
 Now, it is turn to build data loaders that will feed the batches of datasets into our model.

 To do so,

 A custom data loader class was built
 3 data loaders were instantiated : for train, validation, and test
 
 <h3>  Custom Data Loader </h3>
  Sequence here means a vectorized list of words in an email.
 As we prepared 6,000 e-mails, we have 6,000 sequences.

 As sequences have different lengths, it is required to pass the length of each sequence into our model not to train our model on dummy numbers ( 0s for padding ).

 Consequently, we need custom data loaders that return lengths of each sequence along with sequences and labels.

 Plus, The data loader should sort the batch by each sequence's length and returns the longest one first in the batch to use torch's pack_padded_sequence() (you will see this     function in model code)
 
 <h3>   Structure the model </h3>
       
        1 . Embedding
        2 . Pack the sequences (get rid of paddings)
        3 . LSTM
        4 . Unpack the sequences (recover paddings)
        5 . Fully Connected Layer
        6 . Sigmoid Activation
 

 <h3>  Embedding </h3>
According to Tensorflow.org's documentation, "word embeddings are a representation of the semantics of a word"
 
<br> 
<h3> Use of pack_padded_sequence() </h3>
  Please recall that we added padding(0)s to sequences. Since sequences have different lengths, it is required to add paddings into shorter sequences to match the dimension in     tensor. The problem is that model should not be trained on padding values. pack_padded_sequence() will get rid of paddings in the batch of data and re-organized it

 
<br>
 

 
Project URL : https://email-spam-1.herokuapp.com/
