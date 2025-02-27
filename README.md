# Tracklist Display 

A minimal CLI tool for DJs and music enthusiasts to display and manage tracklists with style.

## Quick Start

### Prerequisites
- Python 3.x
- Terminal with color support

### Installation

```bash
# Clone the repo
git clone https://github.com/fergus586/Tracklist-script.git
cd Tracklist-script

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
# Display full tracklist
python tracklist_display.py

# Play mode - press Enter to advance tracks
python tracklist_display.py --play

# Secret mode - hide upcoming tracks
python tracklist_display.py --secret

# Highlight specific track (N = track number, 0-based)
python tracklist_display.py --current N
```

## Features
- Colored track display with progress bar
- Live playback simulation
- Secret mode for surprise reveals
- Track highlighting

## Customization
Edit the `tracklist` list in `tracklist_display.py`:
```python
"Artist Name - Track Title"
```

## Troubleshooting

If you run into issues:
- Try `python3` instead of `python`
- Update pip: `python -m pip install --upgrade pip`
- For permission errors, use `sudo` (Mac/Linux)
- If colors aren't showing, try a modern terminal emulator

Need help? Open an issue on GitHub.

---
Created by [@fergus586](https://github.com/fergus586)