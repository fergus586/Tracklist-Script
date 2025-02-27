# Tracklist Display 

A beautiful command-line tool to display and manage your music tracklists with style! Perfect for DJs, music enthusiasts, or anyone who wants to present their playlists in a cool way.

Created by [@fergus586](https://github.com/fergus586) 

## First Time Setup 

Never coded before? No problem! Here's how to get started using just your terminal:

### 1. Install Python
First, you'll need to install Python on your computer:

#### On Windows:
1. Open PowerShell or Command Prompt (press Windows key + X, then select "Windows PowerShell" or "Command Prompt")
2. Install Python using winget (Windows Package Manager):
```bash
winget install Python.Python.3
```
3. Restart your terminal after installation

#### On Mac:
1. Open Terminal (press Cmd + Space, type "Terminal", press Enter)
2. Install Homebrew (a tool that helps install programmes) by pasting this command:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
3. After Homebrew is installed, install Python:
```bash
brew install python
```

#### On Linux:
Python usually comes pre-installed! But if it's not:
```bash
sudo apt-get update
sudo apt-get install python3
```

### 2. Download This Programme
You can download the programme directly from the terminal:

#### Using Git (recommended):
```bash
# Install Git if you don't have it
# For Mac:
brew install git
# For Ubuntu/Debian:
sudo apt-get install git
# For Windows (in PowerShell):
winget install Git.Git

# Clone the repository
git clone https://github.com/fergus586/Tracklist-script.git
```

#### Using curl (alternative):
```bash
# For Mac/Linux:
curl -L https://github.com/fergus586/Tracklist-script/archive/refs/heads/main.zip -o tracklist.zip
unzip tracklist.zip
rm tracklist.zip

# For Windows (PowerShell):
curl.exe -L https://github.com/fergus586/Tracklist-script/archive/refs/heads/main.zip -o tracklist.zip
Expand-Archive -Path tracklist.zip -DestinationPath .
Remove-Item tracklist.zip
```

### 3. Navigate to the Programme
In your terminal, change to the programme directory:
```bash
cd Tracklist-script
```

### 4. Install Required Packages
Install the required Python packages:
```bash
pip install -r requirements.txt
```

Now you're ready to use the programme! 

## Features 

- Beautiful coloured display of your tracklist
- Progress bar to show how far you are in the playlist
- Secret mode that reveals tracks one by one (perfect for live sets!)
- Multiple display options to suit your needs

## How to Use 

### Basic Display
Simply run the script to see your full tracklist:
```bash
python tracklist_display.py
```

### Play Mode
To simulate playing through the tracklist (press Enter to move to next track):
```bash
python tracklist_display.py --play
```

### Secret Mode
Want to keep upcoming tracks a surprise? Use secret mode:
```bash
python tracklist_display.py --secret
```

### Highlight a Specific Track
To highlight a specific track in the list (replace N with track number, starting from 0):
```bash
python tracklist_display.py --current N
```

## Requirements 
- Python 3.x
- A terminal that supports colours (most modern terminals do)

## Tips 
- Use secret mode during live sets to keep your audience guessing!
- The progress bar helps you keep track of how far along you are in your set
- Press Ctrl+C at any time to exit the programme
- If you see "python: command not found", try using `python3` instead of `python`
- On Windows, if you see "python is not recognised", try closing and reopening your Command Prompt

## Troubleshooting 🔧

### Common Issues:
1. **"python not found"**: Try using `python3` instead of `python`
2. **"not recognised as a command"**: Make sure Python is installed correctly. Try running:
   ```bash
   # On Windows:
   refreshenv
   # On Mac/Linux:
   source ~/.bashrc  # or source ~/.zshrc if using zsh
   ```
3. **Colours not showing**: Try a different terminal app (like Windows Terminal from Microsoft Store)
4. **Permission errors**: Try adding `sudo` before commands on Mac/Linux
5. **Package installation issues**: Try updating pip first:
   ```bash
   python -m pip install --upgrade pip
   ```

Need more help? Feel free to open an issue on GitHub!

## Customisation 
To add your own tracks, edit the `tracklist` list in the `tracklist_display.py` file. Each track should be in the format:
```
"Artist Name - Track Title"
```

---
Made by [@fergus586](https://github.com/fergus586) 