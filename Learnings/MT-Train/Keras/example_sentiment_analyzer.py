"""
This module is sample code that shows how to invoke the web service to get datasets
Author: Palacode Narayana Iyer Anantharaman
Date: 5 Oct 2018
"""
from nltk import sent_tokenize, word_tokenize
from api_client import ApiClient

if __name__ == "__main__":
    # in order to use the web service, first create the instance of ApiClient class
    client = ApiClient()

    # test it with echo service
    val = client.echo("hi there!!!!")
    print("The Service Returned: ", val)

    # you can use the method get_amazon_product_reviews to get data for sentiment analysis
    # this will be rate limited to 500 samples per call
    num_samples = 5
    val = client.get_amazon_product_reviews(num_samples)

    # you can print the variable returned by the service and examine the output fields
    print(val)

    # you can access individual fields such as "summary" and "rating" that can be used
    # to find the sentiment
    for item in val[:100]:
        print("Summary ==> ", item["summary"], "\t\tRating ==> ", item["rating"])
    
    # summary may be one or more sentences of text. We need to break these in to words
    # further, we need to convert each word to a vector form
    # our web service provides a function that accepts a list of words and returns the
    # corresponding vectors. In the example below, we take the first item returned by the
    # previous call and convert that in to a sequence of vectors
    text = val[0]["summary"]
    print("The input text is: ", text)

    # get sentence tokens from text that may have more than 1 sentence
    # we use NLTK's sent_tokenize for this
    sentences = sent_tokenize(text) # we get the list of sentences
    all_words = []
    for sentence in sentences:
        all_words.extend(word_tokenize(sentence))
    
    # all_words contains all the words in the text as a single list
    # let us get the vectors for these
    vals = client.w2v(all_words)
    for val in vals:
        print(val["word"], val["vec"])

    # now you can continue further by vectoring the class label and creating the required dataset
    # your code ......
