import requests

def generate_blog(topic):
    url = "http://localhost:11434/api/generate"

    prompt = f"""
    Write a concise blog about: {topic}

    Include:
    - An engaging title
    - Short introduction
    - 2-3 headings with useful information
    - Short conclusion

    Keep it under 400 words. Avoid repetition.
    Return the title on the first line.
    """

    payload = {
        "model": "qwen2.5:3b",
        "prompt": prompt,
        "stream": False,
        "options": {
            "num_predict": 350
        }
    }

    response = requests.post(url, json=payload, timeout=120)
    response.raise_for_status()

    return response.json()["response"]