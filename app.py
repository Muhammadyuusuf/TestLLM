curl "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer cpd-apikey-IBMid-694000ANSQ-2024-05-24T10:15:27Z' \
  -d '{
	"input": "<s>[INST] <<SYS>>\nYou are a marketing consultant. \n<</SYS>>\n\nPlease generate a promotional email to visit the following attractions in Washington, DC:\n1. The National Mall\n2. The Smithsonian Museums\n3. The White House\n4. The U.S. Capitol \n5. The National Gallery of Art\n[/INST]Subject: Discover the Best of Washington, DC - Must-Visit Attractions!\n\nDear [Recipient],\n\nAre you planning a trip to Washington, DC? Look no further! We'\''ve got you covered with the top must-visit attractions in the nation'\''s capital. From iconic landmarks to world-class museums, we'\''ve compiled a list of the best experiences that DC has to offer.\n\n1. The National Mall:\nBegin your journey at the National Mall, a sprawling green space that stretches from the Lincoln Memorial to the United States Capitol. Take a stroll along the Mall'\''s scenic paths, visit the World War II Memorial, the Vietnam Veterans Memorial, and the Korean War Veterans Memorial. Don'\''t miss the chance to snap a photo in front of the iconic Washington Monument!\n2. The Smithsonian Museums:\nNext, explore the world-famous Smithsonian Museums, a collection of 19 museums and galleries, as well as the National Zoo. From art to history, science to culture, there'\''s something for everyone. Must-visit museums include the National Museum of Natural History, the National Air and Space Museum, and the National Museum of American History.\n3. The White House:\nExperience the grandeur of the White House, the official residence and workplace of the President of the United States. While tours of the inside of the building are difficult to come by, you can take a tour of the grounds and see the exterior of this historic building. Be sure to plan ahead and request your tour tickets well in advance through your member of Congress.\n4. The U.S. Capitol:\nVisit the seat of American democracy, the U.S. Capitol Building. Take a guided tour to learn about the history and architecture of this iconic landmark, and be sure to stop by the Capitol Visitor Center to learn more about the legislative process. Don'\''t miss the stunning views of the National Mall from the Capitol steps.\n5. The National Gallery of Art:\nFinally, spend an afternoon exploring the National Gallery of Art, one of the world'\''s premier art museums. With a collection that spans from the Middle Ages to modern",
	"parameters": {
		"decoding_method": "sample",
		"max_new_tokens": 500,
		"min_new_tokens": 0,
		"random_seed": null,
		"stop_sequences": [],
		"temperature": 0.7,
		"top_k": 50,
		"top_p": 1,
		"repetition_penalty": 1
	},
	"model_id": "meta-llama/llama-2-70b-chat",
	"project_id": "3e1390f9-358c-4ae5-98d9-5dff78241f36",
	"moderations": {
		"hap": {
			"input": {
				"enabled": true,
				"threshold": 0.5,
				"mask": {
					"remove_entity_value": true
				}
			},
			"output": {
				"enabled": true,
				"threshold": 0.5,
				"mask": {
					"remove_entity_value": true
				}
			}
		}
	}
}'
