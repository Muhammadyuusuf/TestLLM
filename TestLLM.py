# Install the requests library if not already installed
!pip install requests

import requests
import json

# Define the URL and headers for the API request
url = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer YOUR_ACCESS_TOKEN'  # Replace with your actual token
}

# Define the payload with the appropriate JSON structure
payload = {
    "input": (
        "Please provide top 5 bullet points in the review provided below.\n\n\nReview:\n"
        "I had 2 problems with my experience with my refinance. 1) The appraisal company used only tried to lower my "
        "house value to fit the comps that he was able to find in the area. My house is unique and he did not use the "
        "unique pictures to compare value. He purposely left them out of the appraisal. 2) I started my loan process "
        "on a Thursday. On Saturday I tried to contact my loan officer to tell him of the American Express offer that "
        "I wanted to apply for. I was informed that it was too late and I could not use it because it would delay the "
        "process. I had just received the email about the offer and I had just started the process so how was it too "
        "late to get in on the $2,000 credit on my current bill. I let it go but I should have dropped the process and "
        "restarted it because that would have helped me out with my bill.\n\n"
        "Top bullet points:\n"
        "1. The appraisal company undervalued the reviewer's house by purposely excluding unique pictures that would "
        "have accurately assessed its value.\n"
        "2. The uniqueness of the house was not taken into consideration, and the appraiser relied solely on comps that "
        "did not reflect its true worth.\n"
        "3. The loan officer was informed too late about the American Express offer, which could have provided a $2,000 "
        "credit.\n"
        "4. The process of obtaining the loan was initiated quickly, but important opportunities were missed.\n"
        "5. The reviewer felt that the appraisal process was unfair and detrimental to the loan process.\n"
    ),
    "parameters": {
        "decoding_method": "greedy",
        "max_new_tokens": 300,
        "min_new_tokens": 50,
        "stop_sequences": [],
        "repetition_penalty": 1
    },
    "model_id": "google/flan-ul2",
    "project_id": "3e1390f9-358c-4ae5-98d9-5dff78241f36",
    "moderations": {
        "hap": {
            "input": {
                "enabled": True,
                "threshold": 0.5,
                "mask": {
                    "remove_entity_value": True
                }
            },
            "output": {
                "enabled": True,
                "threshold": 0.5,
                "mask": {
                    "remove_entity_value": True
                }
            }
        }
    }
}

# Send the POST request to the API
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Print the response from the API
print(response.json())
