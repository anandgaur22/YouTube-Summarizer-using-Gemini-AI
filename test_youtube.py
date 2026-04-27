from google import genai
from google.genai import types

try:
    client = genai.Client(vertexai=True, project="youtube-summarizer-494607", location="us-central1")
    youtube_video = types.Part.from_uri(
        file_uri="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        mime_type="video/mp4",
    )
    contents = [youtube_video, types.Part.from_text(text="Summarize")]
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=contents,
    )
    print(response.text)
except Exception as e:
    import traceback
    traceback.print_exc()
