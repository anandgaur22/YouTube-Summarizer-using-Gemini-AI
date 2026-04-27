from google import genai
from google.genai import types

def test_model(model_name):
    print(f"Testing {model_name}...")
    try:
        client = genai.Client(vertexai=True, project="youtube-summarizer-494607", location="us-central1")
        youtube_video = types.Part.from_uri(
            file_uri="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            mime_type="video/mp4",
        )
        contents = [youtube_video, types.Part.from_text(text="Summarize")]
        response = client.models.generate_content(
            model=model_name,
            contents=contents,
        )
        print(f"Success with {model_name}")
    except Exception as e:
        print(f"Failed with {model_name}: {e}")

test_model("gemini-1.5-flash-001")
test_model("gemini-1.5-flash-002")
test_model("gemini-1.5-pro-001")
test_model("gemini-1.5-pro-002")
test_model("gemini-2.5-flash")
