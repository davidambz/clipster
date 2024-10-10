# Clipster

**Clipster** is a Python-based tool for merging video clips into a single video. It organizes clips into a designated folder structure and uses FFmpeg to concatenate them efficiently.

## Features

- Merges multiple video clips into a single video file.
- Organizes clips and output videos into a structured folder system.
- Uses FFmpeg for fast and reliable video processing.
- Flexible configuration with a `.env` file to specify the project directory.

## Folder Structure

Before using the tool, create a folder named `clipster` in your desired location. Inside this folder, create two subfolders: `clips` for your input video clips and `videos` for the output merged video. The structure should look like this:

```
clipster/        # Main project folder
├── clips/       # Folder where all the input video clips are stored
│   ├── clip1.mp4
│   ├── clip2.mp4
│   └── ...
│
└── videos/      # Folder where the final merged video will be saved
    └── final_video.mp4
```

## Requirements

- Python 3.x
- FFmpeg (installed and added to PATH)
- Poetry (for dependency management)

## Installation

1. Clone the repository:

   ```
   git clone git@github.com:davidambz/clipster.git
   cd clipster
   ```

2. Install dependencies using Poetry:

   ```
   poetry install
   ```

3. Copy the `.env-template` to `.env` and edit it to set the `CLIPESTER_PATH`:

   ```
   cp .env-template .env
   ```

   Update the `CLIPESTER_PATH` in the `.env` file to point to the folder where you created the `clips` and `videos` folders.

## Usage

1. Add your video clips to the `clips/` folder.
2. Run the script to merge the clips into a single video:

   ```
   poetry run python merge_videos.py
   ```

   The final video will be saved in the `videos/` folder as `final_video.mp4`.

## Contributing

Feel free to open issues or submit pull requests to improve this tool.
