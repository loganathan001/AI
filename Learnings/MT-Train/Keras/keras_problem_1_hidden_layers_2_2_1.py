from api_client import ApiClient


client = ApiClient()

val = client.echo("hi there!!!!")
print("The Service Returned: ", val)
