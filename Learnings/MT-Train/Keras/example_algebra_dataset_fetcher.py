"""
This module is sample code that shows how to invoke the web service to get datasets
We will show how to use this for problem on identifying algebric identities
Author: Palacode Narayana Iyer Anantharaman
Date: 5 Oct 2018
"""
from api_client import ApiClient

if __name__ == "__main__":
    # in order to use the web service, first create the instance of ApiClient class
    client = ApiClient()

    # test it with echo service
    val = client.echo("hi there!!!!")
    print("The Service Returned: ", val)

    # you can use the method algebric identity simulated dataset
    # this will be rate limited
    num_samples = 5
    val = client.algebra(5)
    inputs = val["inputs"]
    outputs = val["outputs"]
    for inp, outp in zip(inputs, outputs):
        print(inp, outp)
