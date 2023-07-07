import vertexai
from vertexai.language_models import TextGenerationModel

vertexai.init(project="gen-higenai-team", location="us-central1")
parameters = {
    "temperature": 0.2,
    "max_output_tokens": 542,
    "top_p": 0.8,
    "top_k": 40
}
model = TextGenerationModel.from_pretrained("text-bison@001")
response = model.predict(
    """short description: \"\"\" A girl wearing a maroon saree \"\"\"
Generate product name, description of 2 lines, categorization using the short description and export the result in json format

input: short description: \"\"\" A girl wearing a maroon saree \"\"\"
output: {
\"name\": \"saree\",
\"description\":\"A girl wearing a beaturiful maroon saree\",
\"category\": \"clothing\",
\"sub-category\":\"saree\",
\"type\":\"ethnic wear\",
\"gender\":\"female\",
\"colour\":\"maroon\",
\"product tags\": [\'india\", \"ethnic\",\"traditional dress\", \"wedding\" , \"casual wear\"],
\"occasion\": [\"wedding\", \"party\"],
\"brand\":\"Insufficient data\"
}

input: short description: \"\"\" nike men\'s sahara team india fanwear jersey \"\"\"
output: {
\"name\": \"nike men\'s sahara team india fanwear jersey\",
\"description\":\"Nike men\'s sahara team india fanwear jersey.\",
\"category\": \"clothing\",
\"sub-category\":\"jersey\",
\"type\":\"sports wear\",
\"gender\":\"male\",
\"colour\":\"blue\",
\"product tags\": [\'nike\', \'india\', \'sports\', \'jersey\'],
\"occasion\": [\"cricket match\", \"sports\"],
\"brand\":\"Nike\"
}

input: short description: \"\"\" a boy wearing scuba diving suit \"\"\"
output: {
\"name\": \"scuba diving suit\",
\"description\":\"A boy wearing a scuba diving suit.\",
\"category\": \"sports\",
\"sub-category\":\"diving\",
\"type\":\"sports wear\",
\"gender\":\"male\",
\"colour\":\"blue\",
\"product tags\": [\'diving\', \'scuba diving\', \'sports\', \'suit\'],
\"occasion\": [\"diving\", \"sports\"],
\"brand\":\"Insufficient data\"
}

input: short description: \"\"\"track pants \"\"\"
output: {
\"name\": \"track pants\",
\"description\":\"Track pants.\",
\"category\": \"clothing\",
\"sub-category\":\"pants\",
\"type\":\"sports wear\",
\"gender\":\"unisex\",
\"colour\":\"Insufficient data\",
\"product tags\": [\'sports\', \'pants\'],
\"occasion\": [\"sports\", \"gym\"],
\"brand\":\"Insufficient data\"
}

input: short description: \"\"\"a boy wearing Argentina\'s football jersey\"\"\"
output:
""",
    **parameters
)
print(f"Response from Model: {response.text}")