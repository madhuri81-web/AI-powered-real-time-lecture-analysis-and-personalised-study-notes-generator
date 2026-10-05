from youtube_transcript_api import YouTubeTranscriptApi
import re


def extract_video_id(url):

    patterns = [
        r"youtube\.com/watch\?v=([^&]+)",
        r"youtu\.be/([^?]+)",
        r"youtube\.com/embed/([^?]+)"
    ]

    for pattern in patterns:

        match = re.search(pattern, url)

        if match:
            return match.group(1)

    return None


def get_youtube_transcript(url):

    video_id = extract_video_id(url)

    if not video_id:
        return None

    try:

        api = YouTubeTranscriptApi()

        transcript = api.fetch(video_id)

        text = " ".join(
            snippet.text
            for snippet in transcript
        )

        return text

    except Exception as e:

        return f"ERROR: {str(e)}"