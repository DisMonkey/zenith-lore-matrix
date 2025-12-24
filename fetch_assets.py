import os
import requests
from icrawler.builtin import BingImageCrawler

def fetch_specific_image(character_name, filename):
    """Searches and saves a specific image to the assets folder."""
    if not os.path.exists('assets'):
        os.makedirs('assets')
    
    print(f"🕵️ AI RESEARCH: Finding official visual for {character_name}...")
    
    # We use a temporary directory to avoid naming conflicts
    temp_dir = 'temp_search'
    crawler = BingImageCrawler(storage={'root_dir': temp_dir})
    # We add "FNAF official render" to ensure high quality
    crawler.crawl(keyword=f"{character_name} FNAF official render", max_num=1)
    
    files = os.listdir(temp_dir)
    if files:
        # Move the first result to assets with the correct name
        import shutil
        shutil.move(os.path.join(temp_dir, files[0]), os.path.join('assets', filename))
        shutil.rmtree(temp_dir)
        return True
    return False

if __name__ == "__main__":
    # Test run for core characters
    chars = {"william_afton.png": "William Afton"}
    for f, n in chars.items():
        fetch_specific_image(n, f)