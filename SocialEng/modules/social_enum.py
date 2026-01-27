import os
import json
import requests
from datetime import datetime

RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"

PLATFORMS = {
    # Major global social
    "GitHub": "https://github.com/{}",
    "GitLab": "https://gitlab.com/{}",
    "Bitbucket": "https://bitbucket.org/{}",
    "X": "https://x.com/{}",  # formerly Twitter
    "Facebook": "https://www.facebook.com/{}",
    "Instagram": "https://www.instagram.com/{}",
    "LinkedIn": "https://www.linkedin.com/in/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "YouTube": "https://www.youtube.com/@{}",
    "Pinterest": "https://pinterest.com/{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "Snapchat": "https://www.snapchat.com/add/{}",

    # Creator / streaming / video
    "Twitch": "https://www.twitch.tv/{}",
    "Kick": "https://kick.com/{}",
    "MixerLegacy": "https://mixer.com/{}",  # legacy
    "Vimeo": "https://vimeo.com/{}",
    "Dailymotion": "https://www.dailymotion.com/{}",
    "Odysee": "https://odysee.com/@{}",
    "Rumble": "https://rumble.com/c/{}",
    "Bitchute": "https://www.bitchute.com/channel/{}", 

    # Messaging / contact / voice
    "Telegram": "https://t.me/{}",
    "WhatsApp": "https://wa.me/{}",  # phone number format
    "Signal": "search-only",         # no single public profile URL
    "Discord": "https://discord.com/users/{}",  # numeric user id

    # Developer / code / package registries
    "StackOverflow": "https://stackoverflow.com/users/{}",
    "Gist": "https://gist.github.com/{}",
    "CodePen": "https://codepen.io/{}",
    "Replit": "https://replit.com/@{}",
    "NPM": "https://www.npmjs.com/~{}",
    "PyPI": "https://pypi.org/user/{}",
    "RubyGems": "https://rubygems.org/profiles/{}",
    "DockerHub": "https://hub.docker.com/u/{}",
    "Packagist": "https://packagist.org/users/{}",

    # Design / photography / portfolios
    "Dribbble": "https://dribbble.com/{}",
    "Behance": "https://www.behance.net/{}",
    "ArtStation": "https://www.artstation.com/{}",
    "DeviantArt": "https://www.deviantart.com/{}",
    "Flickr": "https://www.flickr.com/people/{}",
    "500px": "https://500px.com/{}",
    "Unsplash": "https://unsplash.com/@{}",

    # Audio / music / podcasts
    "SoundCloud": "https://soundcloud.com/{}",
    "Bandcamp": "https://{}/",  # artist subdomain: artist.bandcamp.com
    "Mixcloud": "https://www.mixcloud.com/{}",
    "LastFM": "https://www.last.fm/user/{}",
    "SpotifyArtist": "https://open.spotify.com/artist/{}",  # requires artist id

    # Marketplaces / commerce / freelancing
    "Etsy": "https://www.etsy.com/people/{}",
    "eBay": "https://www.ebay.com/usr/{}",
    "AmazonSeller": "https://www.amazon.com/sp?seller={}",  # seller id
    "Shopify": "https://{}.myshopify.com",
    "Gumroad": "https://gumroad.com/{}",
    "Fiverr": "https://www.fiverr.com/{}",
    "Upwork": "https://www.upwork.com/freelancers/~{}",  # ~id

    # Blogging / personal websites
    "Medium": "https://medium.com/@{}",
    "Tumblr": "https://{}.tumblr.com",
    "Substack": "https://{}.substack.com",
    "WordPress": "https://{}.wordpress.com",
    "Blogger": "https://{}.blogspot.com",
    "Ghost": "https://{}.ghost.io",  # example subdomain

    # Q&A / communities / forums
    "Quora": "https://www.quora.com/profile/{}",
    "Discourse": "https://{instance}/u/{}",          # instance required
    "VanillaForums": "https://{instance}/profile/{}",
    "MetaFilter": "https://www.metafilter.com/user/{}",
    "StackExchange": "https://stackexchange.com/users/{}",
    "HackerNews": "https://news.ycombinator.com/user?id={}",

    # Professional / business / directories
    "Crunchbase": "https://www.crunchbase.com/person/{}",
    "AngelList": "https://angel.co/{}",
    "Glassdoor": "search-only",
    "Indeed": "search-only",
    "ZoomInfo": "search-only",

    # Academic / research / citation
    "ResearchGate": "https://www.researchgate.net/profile/{}",
    "ORCID": "https://orcid.org/{}",                     # 16-digit id
    "GoogleScholar": "https://scholar.google.com/citations?user={}",

    # Crypto / NFT / web3
    "OpenSea": "https://opensea.io/{}",
    "Rarible": "https://rarible.com/{}?tab=items",
    "Etherscan": "https://etherscan.io/address/{}",
    "LooksRare": "https://looksrare.org/collections/{}",  # collection or profile paths vary

    # Region-specific / Asian platforms
    "Weibo": "https://weibo.com/{}",
    "WeChat": "search-only",
    "Bilibili": "https://space.bilibili.com/{}",
    "Douyin": "https://www.douyin.com/user/{}",
    "Xiaohongshu": "https://www.xiaohongshu.com/user/profile/{}",
    "QQ": "https://user.qzone.qq.com/{}",

    # Reviews / local / travel
    "Yelp": "https://www.yelp.com/user_details?userid={}",
    "TripAdvisor": "https://www.tripadvisor.com/members/{}",
    "Trustpilot": "https://www.trustpilot.com/review/{}",  # business pages, may vary

    # Wikis / knowledge
    "WikipediaUser": "https://en.wikipedia.org/wiki/User:{}",
    "Wikidata": "https://www.wikidata.org/wiki/Q{}",  # usually numeric id

    # Niche / other social
    "Goodreads": "https://www.goodreads.com/{}",
    "Patreon": "https://www.patreon.com/{}",
    "KoFi": "https://ko-fi.com/{}",
    "OnlyFans": "https://onlyfans.com/{}",
    "Tistory": "https://{}.tistory.com",
    "LiveJournal": "https://{}.livejournal.com",
    "AboutMe": "https://about.me/{}",
    "Gravatar": "https://en.gravatar.com/{}",

    # Gaming / esports
    "SteamCommunity": "https://steamcommunity.com/id/{}",  # vanity id or numeric
    "Xbox": "https://account.xbox.com/en-us/profile?gamertag={}",  # not always public
    "PlayStation": "https://my.playstation.com/{}",  # varied

    # Photo / creative marketplaces
    "CreativeMarket": "https://creativemarket.com/{}",
    "Envato": "https://themeforest.net/user/{}",  # example for envato network

    # Code hosting alternatives
    "SourceForge": "https://sourceforge.net/u/{}",
    "Launchpad": "https://launchpad.net/~{}",  # tilde username

    # Additional social / microblogging
    "Mastodon": "https://{instance}/@{}",        # instance required
    "Pixelfed": "https://{instance}/@{}",       # instance required
    "Friendica": "https://{instance}/profile/{}",# instance required

    # Misc / directories
    "TMDB": "https://www.themoviedb.org/u/{}",   # user profile on TMDB
    "Letterboxd": "https://letterboxd.com/{}",
    "IMDB": "https://www.imdb.com/user/{}",     # usually u/ or nm/ ids

    # Add additional niche platforms below as needed...
}

def check_username(platform, username):
    url = PLATFORMS[platform].format(username)

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=5, allow_redirects=True)

        if response.status_code == 200:
            return True, url
        elif response.status_code == 404:
            return False, url
        else:
            return None, url

    except requests.exceptions.Timeout:
        return None, url
    except requests.exceptions.RequestException:
        return None, url

def enumerate_username(username):
    results = {
        'username': username,
        'timestamp': datetime.now().isoformat(),
        'found': [],
        'not_found': [],
        'unknown': []
    }

    print(f"\n{CYAN}[*] Checking username '{username}' across platforms...{RESET}\n")

    for platform in PLATFORMS:
        status, url = check_username(platform, username)

        if status is True:
            print(f"  {GREEN}[+]{RESET} {platform:<12} {GREEN}FOUND{RESET}       {url}")
            results['found'].append({'platform': platform, 'url': url})
        elif status is False:
            print(f"  {RED}[-]{RESET} {platform:<12} {RED}NOT FOUND{RESET}   {url}")
            results['not_found'].append({'platform': platform, 'url': url})
        else:
            print(f"  {YELLOW}[?]{RESET} {platform:<12} {YELLOW}UNKNOWN{RESET}     {url}")
            results['unknown'].append({'platform': platform, 'url': url})

    return results

def save_enumeration_results(results):
    targets_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'targets')
    os.makedirs(targets_dir, exist_ok=True)

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    username = results['username']
    filename_json = os.path.join(targets_dir, f'social_enum_{username}_{timestamp}.json')
    filename_txt = os.path.join(targets_dir, f'social_enum_{username}_{timestamp}.txt')

    with open(filename_json, 'w') as f:
        json.dump(results, f, indent=4)

    with open(filename_txt, 'w') as f:
        f.write("="*67 + "\n")
        f.write("SOCIAL MEDIA ENUMERATION RESULTS\n")
        f.write("="*67 + "\n\n")
        f.write(f"Username: {username}\n")
        f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        if results['found']:
            f.write("FOUND PROFILES\n")
            f.write("-"*67 + "\n")
            for item in results['found']:
                f.write(f"{item['platform']:<15} {item['url']}\n")
            f.write("\n")

        if results['not_found']:
            f.write("NOT FOUND\n")
            f.write("-"*67 + "\n")
            for item in results['not_found']:
                f.write(f"{item['platform']:<15} {item['url']}\n")
            f.write("\n")

        if results['unknown']:
            f.write("UNKNOWN STATUS\n")
            f.write("-"*67 + "\n")
            for item in results['unknown']:
                f.write(f"{item['platform']:<15} {item['url']}\n")

        f.write("\n" + "="*67 + "\n")

    print(f"\n{GREEN}[+] Results saved:{RESET}")
    print(f"    {CYAN}├─ JSON:{RESET} {filename_json}")
    print(f"    {CYAN}└─ TXT:{RESET}  {filename_txt}")

def enumerate_social():
    os.system('clear')

    print(f"""
{BOLD}{GREEN}SOCIAL MEDIA ENUMERATION{RESET}
{CYAN}═══════════════════════════════════════════════════════════════════{RESET}

{YELLOW}Check username availability across social media platforms{RESET}
{RED}For authorized reconnaissance only{RESET}

""")

    username = input(f"{BOLD}Enter username to enumerate:{RESET} ").strip()

    if not username:
        print(f"{RED}[-] No username provided{RESET}")
        input(f"\n{BOLD}Press Enter to continue...{RESET}")
        return

    print(f"\n{CYAN}{'='*67}{RESET}")
    results = enumerate_username(username)
    print(f"{CYAN}{'='*67}{RESET}")

    print(f"\n{BOLD}SUMMARY:{RESET}")
    print(f"  {GREEN}Found:{RESET}     {len(results['found'])} profile(s)")
    print(f"  {RED}Not Found:{RESET} {len(results['not_found'])} platform(s)")
    print(f"  {YELLOW}Unknown:{RESET}   {len(results['unknown'])} platform(s)")

    save_enumeration_results(results)

    input(f"\n{BOLD}Press Enter to continue...{RESET}")
