import os
import shutil
from icrawler.builtin import BingImageCrawler

# 1. THE ARCHIVE MAP
# We search for specific terms to ensure high-quality FNaF lore images.
CHARACTER_MAP = {
    "william_afton.png": "William Afton Purple Guy FNAF",
    "gabriel.png": "Gabriel FNAF Freddy soul 1985",
    "springtrap.png": "Springtrap FNAF high quality render",
    "puppet.png": "The Puppet FNAF Charlotte Emily",
    "michael_afton.png": "Michael Afton FNAF",
    "elizabeth_afton.png": "Elizabeth Afton Circus Baby",
    "crying_child.png": "FNAF Crying Child 1983"
}

def setup_folders():
    if not os.path.exists('assets'):
        os.makedirs('assets')
    if not os.path.exists('temp_search'):
        os.makedirs('temp_search')

def fetch_and_organize():
    setup_folders()
    
    for filename, search_query in CHARACTER_MAP.items():
        print(f"🕵️ ARCHIVE SCAN: Searching for {search_query}...")
        
        # Download to a temporary folder
        crawler = BingImageCrawler(storage={'root_dir': 'temp_search'})
        crawler.crawl(keyword=search_query, max_num=1)
        
        # Find the file icrawler created
        downloaded_files = os.listdir('temp_search')
        if downloaded_files:
            old_path = os.path.join('temp_search', downloaded_files[0])
            new_path = os.path.join('assets', filename)
            
            # Move and rename it to your final assets folder
            shutil.move(old_path, new_path)
            print(f"✅ DATA SECURED: Saved as assets/{filename}")
            
            # Clear the temp folder for the next search
            for f in os.listdir('temp_search'):
                os.remove(os.path.join('temp_search', f))
        else:
            print(f"❌ ERROR: Could not find image for {filename}")

    if os.path.exists('temp_search'):
        os.rmdir('temp_search')
    print("\n🚀 ALL ASSETS DOWNLOADED TO /assets/")

if __name__ == "__main__":
    fetch_and_organize()