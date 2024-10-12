import os
from dotenv import load_dotenv
import ffmpeg

load_dotenv()

CLIPSTER_PATH = os.getenv('CLIPESTER_PATH')

CLIPS_DIR = os.path.join(CLIPSTER_PATH, 'clips')
VIDEOS_DIR = os.path.join(CLIPSTER_PATH, 'videos')

def combine_clips(output_filename='final_video.mp4'):
    output_path = os.path.join(VIDEOS_DIR, output_filename)

    clips = [os.path.join(CLIPS_DIR, f) for f in os.listdir(CLIPS_DIR) if f.endswith('.mp4')]

    if not clips:
        print("No clips found in 'clips' folder.")
        return

    input_streams = [ffmpeg.input(clip) for clip in clips]
    ffmpeg.concat(*input_streams).output(output_path).run()

    print(f"Combined video saved in: {output_path}")

if __name__ == "__main__":
    combine_clips()
