import requests

post_codes_req_response = requests.get("https://api.postcodes.io/postcodes/kt48ya")

print(post_codes_req_response)
print(type(post_codes_req_response))

print(f"Status code: {post_codes_req_response.status_code}")
print(f"Headers: {post_codes_req_response.headers}")
print(f"Content: {post_codes_req_response.content}")
print(type(post_codes_req_response.content))
print(f"JSON: {post_codes_req_response.json()}")
print(f"Data type of JSON: {type(post_codes_req_response.json())}")
print(post_codes_req_response.json("region"))



