# app.py
import streamlit as st
import requests
import json

# Judul aplikasi
st.title("API Text Generation with IBM Cloud")

# Input token dari pengguna
access_token = st.text_input("cpd-apikey-IBMid-694000ANSQ-2024-05-24T10:15:27Z:", type="password")

# Input ulasan dari pengguna
review_text = st.text_area("Mantapppp:", height=200)

if st.button("Kirim Permintaan"):
    if not access_token:
        st.error("Access Token diperlukan!")
    elif not review_text:
        st.error("Teks ulasan diperlukan!")
    else:
        # URL dan header untuk permintaan API
        url = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {access_token}'
        }

        # Payload dengan struktur JSON yang sesuai
        payload = {
            "input": (
                "Please provide top 5 bullet points in the review provided below.\n\n\nReview:\n"
                + review_text +
                "\n\nTop bullet points:\n"
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

        # Mengirimkan permintaan POST ke API
        response = requests.post(url, headers=headers, data=json.dumps(payload))

        # Menampilkan respons dari API
        if response.status_code == 200:
            response_data = response.json()
            st.success("Permintaan berhasil!")
            st.json(response_data)
        else:
            st.error(f"Permintaan gagal dengan status code: {response.status_code}")
            st.text(response.text)
