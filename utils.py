import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY_HERE")

def call_model(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": 0.3,
        }
    )

    return response.text