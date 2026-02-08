import os
import sys
import subprocess

# This script automatically finds main.py and runs it with Streamlit
if __name__ == "__main__":
    # Get the folder where this script is saved
    current_folder = os.path.dirname(os.path.abspath(__file__))
    
    # FORCE the system to look in this folder, not 'music_stream_app'
    os.chdir(current_folder)
    
    target_file = "main.py"
    
    if not os.path.exists(target_file):
        print(f"❌ Error: I cannot find 'main.py' inside {current_folder}")
        print("Please make sure launcher.py and main.py are in the same folder.")
    else:
        print(f"🚀 Found main.py! Launching from: {current_folder}")
        # Run Streamlit
        subprocess.run([sys.executable, "-m", "streamlit", "run", target_file])