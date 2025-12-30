from google import genai
from google.genai.errors import APIError


def req(prompt: str) -> str:

    try:
        client = genai.Client(api_key="AIzaSyC1oted8kY76A63xR8Mezg3-040-9sJXTI")
        model_name = 'gemini-2.5-flash'
        response = client.models.generate_content(
            model=model_name,
            contents=prompt
        )
        return response.text

    except APIError as e:
        return f"ОШИБКА API: Произошла ошибка при вызове Gemini API: {e}"
    except Exception as e:
        return f"Неизвестная ошибка: {e}"   
    
print(req("hello"))