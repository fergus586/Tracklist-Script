#!/usr/bin/env python3

"""
CLI tool for displaying music tracklists with visual styling.
Designed for DJs and music enthusiasts to manage and present their playlists.
"""

import time
import random
import os
import sys

# Colours to make the display look beautiful
class Colours:
    """ANSI color codes for terminal output"""
    RESET = '\033[0m'      # Returns text colour to normal
    BOLD = '\033[1m'       # Makes text bold
    RED = '\033[91m'       # Makes text red
    GREEN = '\033[92m'     # Makes text green
    YELLOW = '\033[93m'    # Makes text yellow
    BLUE = '\033[94m'      # Makes text blue
    MAGENTA = '\033[95m'   # Makes text magenta
    CYAN = '\033[96m'      # Makes text cyan
    WHITE = '\033[97m'     # Makes text white

def clear_screen():
    """Clear terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

# Your tracklist - each line should be "Artist Name - Track Title"
tracklist = [
    "Artist - Track Title",
    "Two Shell - Mum Is Calling"
]

def print_header():
    """Shows a cool ASCII art header at the top of the display"""
    header = r"""
 _____ ___  _   ___ _  ___    ___ ___ _____ 
|_   _| _ \/ \ / __| |/ / |  |_ _/ __|_   _|
  | | |   / _ \ (__| ' <| |__ | |\__ \ | |  
  |_| |_|_\_/ \_\___|_|\_\____|___|___/|_|  
                                            
    """
    
    # Make the header cyan coloured
    print(f"{Colours.CYAN}{header}{Colours.RESET}")
    print(f"\n✧ ✧ ✧  TRACKLIST  ✧ ✧ ✧\n")

def display_track(index, track, is_current=False, secret_mode=False, revealed_tracks=None):
    """
    Display a single track with formatting.
    
    Args:
        index: Track number (0-based)
        track: Track info in "Artist - Title" format
        is_current: Whether this is the active track
        secret_mode: Whether to hide upcoming tracks
        revealed_tracks: List of revealed track indices
    """
    if revealed_tracks is None:
        revealed_tracks = []
    
    # Split the track into artist and title parts
    if " - " in track:
        artist, title = track.split(" - ", 1)
    else:
        artist, title = track, ""
    
    # Make the track number look nice (01, 02, etc.)
    track_num = f"{index+1:02d}"
    
    # Show the current track differently from other tracks
    if is_current:
        prefix = "▶ "  # Play symbol
        artist_style = f"{Colours.GREEN}"
        title_style = f"{Colours.CYAN}"
        num_style = f"{Colours.YELLOW}"
        
        print(f"{prefix}{num_style}{track_num}{Colours.RESET} | {artist_style}{artist}{Colours.RESET} - {title_style}{title}{Colours.RESET}")
    elif secret_mode and index > is_current and index not in revealed_tracks:
        # Hide upcoming tracks in secret mode
        prefix = "  "
        print(f"{prefix}{Colours.YELLOW}{track_num}{Colours.RESET} | {Colours.WHITE}??? - ???{Colours.RESET}")
    else:
        prefix = "  "
        artist_style = f"{Colours.WHITE}"
        title_style = Colours.CYAN
        num_style = Colours.YELLOW
        
        print(f"{prefix}{num_style}{track_num}{Colours.RESET} | {artist_style}{artist}{Colours.RESET} - {title_style}{title}{Colours.RESET}")

def display_progress_bar(current, total, width=40):
    """
    Display a progress bar showing playlist position.
    
    Args:
        current: Current track number
        total: Total tracks
        width: Progress bar width in characters
    """
    progress = int(width * current / total)
    bar = "█" * progress + "░" * (width - progress)
    percentage = current / total * 100
    
    print(f"\n{Colours.BLUE}Progress: {Colours.RESET}[{Colours.CYAN}{bar}{Colours.RESET}] {Colours.YELLOW}{percentage:.1f}%{Colours.RESET}")

def display_tracklist(current_track=-1, animate=True, secret_mode=False, revealed_tracks=None):
    """
    Display the full tracklist with optional effects.
    
    Args:
        current_track: Index of currently playing track
        animate: Enable animation when displaying tracks
        secret_mode: Hide upcoming tracks
        revealed_tracks: List of revealed track indices
    """
    clear_screen()
    print_header()
    
    for i, track in enumerate(tracklist):
        if animate and i != current_track:
            display_track(i, track, False, secret_mode, revealed_tracks)
            time.sleep(0.05)  # Small delay for animation effect
        else:
            display_track(i, track, i == current_track, secret_mode, revealed_tracks)
    
    if current_track >= 0:
        display_progress_bar(current_track + 1, len(tracklist))

def simulate_playback():
    """Interactive playback simulation with track-by-track progression"""
    for i in range(len(tracklist)):
        display_tracklist(i, animate=False)
        
        print(f"\n{Colours.GREEN}Now Playing: {tracklist[i]}{Colours.RESET}")
        input(f"\n{Colours.YELLOW}Press Enter for next track...{Colours.RESET}")

def secret_playback():
    """Secret mode that reveals tracks one by one - ideal for live sets"""
    print(f"{Colours.MAGENTA}🎵 SECRET MODE: Tracks will be revealed as they play! 🎵{Colours.RESET}")
    time.sleep(2)
    
    revealed_tracks = []
    
    for i in range(len(tracklist)):
        revealed_tracks.append(i)
        display_tracklist(i, animate=False, secret_mode=True, revealed_tracks=revealed_tracks)
        
        print(f"\n{Colours.GREEN}Now Playing: {tracklist[i]}{Colours.RESET}")
        
        next_text = "next secret track" if i < len(tracklist) - 1 else "finish"
        input(f"\n{Colours.YELLOW}Press Enter to reveal the {next_text}...{Colours.RESET}")

def static_display():
    """Display tracklist without effects or animation"""
    display_tracklist(animate=False)
    print(f"\n{Colours.YELLOW}Total tracks: {len(tracklist)}{Colours.RESET}")

if __name__ == "__main__":
    import argparse
    
    # Set up the command-line options
    parser = argparse.ArgumentParser(description="Display your tracklist in a beautiful way")
    parser.add_argument("--play", action="store_true", help="Play through the tracklist track by track")
    parser.add_argument("--current", type=int, default=-1, help="Show which track is currently playing (start counting from 0)")
    parser.add_argument("--secret", action="store_true", help="Hide upcoming tracks until they're played")
    
    args = parser.parse_args()
    
    try:
        if args.secret:
            secret_playback()
        elif args.play:
            simulate_playback()
        elif args.current >= 0 and args.current < len(tracklist):
            display_tracklist(args.current, animate=False)
        else:
            static_display()
    except KeyboardInterrupt:
        print(f"{Colours.RESET}\nExiting...\n")
        sys.exit(0) 