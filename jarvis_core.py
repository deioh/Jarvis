import argparse
import os
from datetime import datetime

# Define the paths to our memory files
CONVERSATION_LOG = "conversation_log.md"
RECALL_FILE = "recall.md"
RUBY_NOTES = "rubynotes.md"
README_FILE = "README.md"

def get_status():
    """Provides a quick status update of the Jarvis memory system."""
    print("--- Jarvis Status Report ---")
    
    files_to_check = {
        "Conversation Log": CONVERSATION_LOG,
        "Recall File": RECALL_FILE,
        "Ruby's Notes": RUBY_NOTES,
        "Project README": README_FILE
    }
    
    for name, path in files_to_check.items():
        if os.path.exists(path):
            last_modified_time = os.path.getmtime(path)
            print(f"- {name}: Last modified on {datetime.fromtimestamp(last_modified_time).strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print(f"- {name}: Not found.")

    print("\n--- Last Conversation Entry ---")
    if os.path.exists(CONVERSATION_LOG):
        try:
            with open(CONVERSATION_LOG, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                # Find the last user entry to provide context
                last_user_entry = ""
                for line in reversed(lines):
                    if line.strip().startswith("**User:**"):
                        last_user_entry = line.strip()
                        break
                if last_user_entry:
                    print(last_user_entry)
                else:
                    print("No user entries found in conversation log.")
        except Exception as e:
            print(f"Error reading conversation log: {e}")
    else:
        print("Conversation log not found.")


def search_memories(keyword):
    """Searches for a keyword across all memory files."""
    print(f"--- Searching for '{keyword}' across all memories ---")
    
    files_to_search = {
        "Conversation Log": CONVERSATION_LOG,
        "Recall File": RECALL_FILE,
        "Ruby's Notes": RUBY_NOTES,
        "Project README": README_FILE
    }
    
    found_match = False
    for name, path in files_to_search.items():
        if os.path.exists(path):
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    for i, line in enumerate(lines):
                        if keyword.lower() in line.lower():
                            if not found_match:
                                found_match = True
                            print(f"\nFound in '{name}' on line {i+1}:")
                            # Print a snippet of context
                            context_start = max(0, i-1)
                            context_end = min(len(lines), i+2)
                            for j in range(context_start, context_end):
                                print(f"  {j+1}: {lines[j].strip()}")
            except Exception as e:
                print(f"Error reading {name}: {e}")

    if not found_match:
        print("No matches found.")


def update_dashboard():
    """Updates the README.md to act as a project dashboard."""
    print("--- Updating Dashboard ---")
    
    # Get last user prompt and my last response
    last_user_prompt = "Not found"
    last_ruby_response = "Not found"
    if os.path.exists(CONVERSATION_LOG):
        try:
            with open(CONVERSATION_LOG, 'r', encoding='utf-8') as f:
                lines = [line.strip() for line in f.readlines() if line.strip()]
                for i in reversed(range(len(lines))):
                    if lines[i].startswith("**User:**"):
                        last_user_prompt = lines[i].replace("**User:**", "").strip()
                        # Look for the next CLI response
                        if i + 1 < len(lines) and lines[i+1].startswith("**CLI:**"):
                            last_ruby_response = lines[i+1].replace("**CLI:**", "").strip()
                        break
        except Exception as e:
            print(f"Could not read conversation log for activities: {e}")

    # Get last learning from rubynotes
    last_learning = "No recent learnings."
    if os.path.exists(RUBY_NOTES):
        try:
            with open(RUBY_NOTES, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                last_entry = content.split('---')[-1].strip()
                if last_entry:
                    last_learning = last_entry
        except Exception as e:
            print(f"Could not read rubynotes for learnings: {e}")


    readme_content = f"""# Jarvis Project Dashboard

*Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*

This dashboard provides a real-time overview of our project's status, managed by the `jarvis_core.py` script.

---

## Current Status

**Last thing you said:**
> {last_user_prompt}

**Last thing I did:**
> {last_ruby_response}

---

## Last Thing I Learned

{last_learning}

---

## Quick Links

- [Conversation Log](conversation_log.md)
- [Recall File](recall.md)
- [Ruby's Notes](rubynotes.md)

"""

    try:
        with open(README_FILE, 'w', encoding='utf-8') as f:
            f.write(readme_content)
        print("Successfully updated the README.md dashboard.")
    except Exception as e:
        print(f"Error writing to README.md: {e}")

import sys

import shutil

def backup_memories():
    """Creates a timestamped zip archive of the Jarvis memory directory."""
    print("--- Backing up Jarvis memories ---")
    try:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        archive_name = f"D:\jarvis\PROJECTS\jarvis_backup_{timestamp}"
        
        # The root directory to archive is the one containing this script
        source_dir = os.path.dirname(os.path.abspath(__file__))
        
        shutil.make_archive(archive_name, 'zip', source_dir)
        print(f"Successfully created backup: {archive_name}.zip")
    except Exception as e:
        print(f"Error creating backup: {e}")

def add_note():
    """Adds a new, timestamped note to rubynotes.md from stdin."""
    print("--- Please provide your note below. Press Ctrl+Z and Enter (Windows) or Ctrl+D (Linux) to save. ---")
    message = sys.stdin.read().strip()
    
    if not message:
        print("No message provided. Note not added.")
        return

    print(f"--- Adding note: '{message[:50]}...' ---")
    try:
        with open(RUBY_NOTES, 'a', encoding='utf-8') as f:
            f.write("\n---\n\n")
            f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"{message}\n")
        print("Successfully added note to Ruby's Notes.")
    except Exception as e:
        print(f"Error adding note: {e}")



def main():
    """Main function to parse arguments and call the appropriate function."""
    parser = argparse.ArgumentParser(description="Jarvis Core Script: Your workflow and memory assistant.")
    
    # Create a subparser for the commands
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Status command (default)
    status_parser = subparsers.add_parser('status', help='Get a quick status report of the Jarvis project.')
    
    # Search command
    search_parser = subparsers.add_parser('search', help='Search for a keyword across all memory files.')
    search_parser.add_argument('keyword', type=str, help='The keyword to search for.')
    
    # Update-dashboard command
    dashboard_parser = subparsers.add_parser('update-dashboard', help='Update the README.md dashboard.')
    
    # Backup command
    backup_parser = subparsers.add_parser('backup', help='Create a zip archive of the Jarvis memory folder.')

    # Add-note command
    add_note_parser = subparsers.add_parser('add-note', help="Add a new note to Ruby's notes (reads from stdin).")

    args = parser.parse_args()

    if args.command == 'search':
        search_memories(args.keyword)
    elif args.command == 'update-dashboard':
        update_dashboard()
    elif args.command == 'add-note':
        add_note()
    elif args.command == 'backup':
        backup_memories()
    else: # Default to 'status' if no command is given
        get_status()

if __name__ == "__main__":
    main()
