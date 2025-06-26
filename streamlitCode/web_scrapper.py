import streamlit as st
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def identify_technologies(soup: BeautifulSoup):
    """
    Scans the BeautifulSoup object for clues about the web technologies used.
    It's a basic "fingerprinting" function.
    """

    found_techs = set()
    #wordpress
    if soup.find(lambda tag: (tag.name in ['link', 'script']) and tag.get('href') and 'wp-content' in tag.get('href', '')) or \
        soup.find(lambda tag: (tag.name == 'script') and tag.get('src') and 'wp-content' in tag.get('src', '')):
        found_techs.add("WordPress")

    # jQuery check: Looks for script tags loading jQuery
    if soup.find('script', src=lambda s: s and 'jquery' in s.lower()):
        found_techs.add("jQuery")
        
    # React check: Looks for the common <div id="root"></div> or react scripts
    if soup.find('div', id='root') or soup.find('script', src=lambda s: s and 'react' in s.lower()):
        found_techs.add("React")
        
    # Vue.js check: Looks for the common <div id="app"></div> or data-v attributes
    if soup.find('div', id='app') or soup.find(lambda tag: any(attr.startswith('data-v-') for attr in tag.attrs)):
        found_techs.add("Vue.js")

    # Bootstrap check: Looks for links or scripts containing "bootstrap"
    if soup.find('link', href=lambda h: h and 'bootstrap' in h.lower()) or \
       soup.find('script', src=lambda s: s and 'bootstrap' in s.lower()):
        found_techs.add("Bootstrap")
        
    # Tailwind CSS check: Looks for links to the Tailwind CDN
    if soup.find('link', href=lambda h: h and 'cdn.tailwindcss.com' in h):
        found_techs.add("Tailwind CSS")

    if not found_techs:
        return ["No specific frameworks identified from common patterns."]
        
    return list(found_techs)

def scrape_website(url: str):
    """
    Scrapes the given url and extracts title, meta description, headings(h1, h2, h3), images and links
    """
    try:
        #add header to mimic a browser visit
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.123 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    
    except requests.exceptions.RequestException as error:
        st.error(f"Error fetching the url: {error}")
        return None
    
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extracting the data
    # Title
    title = soup.title.string if soup.title else "No title found"

    # Meta Description
    description_tag = soup.find('meta', attrs={'name': 'description'})
    meta_description = description_tag['content'] if description_tag else "No meta description found"

    # Headings
    headings = {'h1': [], 'h2': [], 'h3':[]}

    for h in soup.find_all(['h1', 'h2', 'h3']):
        headings[h.name].append(h.get_text(strip=True))

    # Images
    images = []
    for img in soup.find_all('img'):
        src = img.get('src')
        if src:
            absolute_src = urljoin(url, src) #/assets/beach.png instead we need https://website.com/assets/beach.png
            alt_text = img.get('alt', 'No alt text')
            images.append({'src': absolute_src, 'alt': alt_text})

    # Links
    links = []
    for a in soup.find_all('a', href=True):
        href = a['href']
        if href and not href.startswith('#'): # #blog we need to convert to https://website.com/blog
            absolute_href = urljoin(url, href)
            link_text = a.get_text(strip=True)
            if not link_text:
                link_text = "No link text"
            links.append({'href': absolute_href, 'text':link_text})
    
    #Technology Identification
    technologies = identify_technologies(soup)

    return {
        'title': title,
        'meta_description': meta_description,
        'headings': headings,
        'images': images,
        'links': links,
        'technologies': technologies
    }

#Creating the UI using StreamLit

st.set_page_config(page_title="Web Scrapper App", layout="wide")
st.title("🔎 Website Scraper & Analyzer")
st.markdown("Enter a website URL below to extract its title, meta description, headings, images, and links.")

url_input = st.text_input("Enter URL (eg., https://www.google.com)", "")

if st.button("Scrape Website"):
    if url_input:
        if not urlparse(url_input).scheme:
            url_input = "https://" + url_input

        with st.spinner("Scraping {url_input}... Please Wait"):
            scraped_data = scrape_website(url_input)
        
        if scraped_data:
            st.success("Scraping completed successfully!")

            #Display the results
            st.header("Page Details")
            st.subheader("Title")
            st.write(scraped_data['title'])

            st.subheader("Meta Description")
            st.write(scraped_data['meta_description'])

            col1, col2 = st.columns(2)

            with col1:
                with st.expander("📄 Headings (H1, H2, H3)"):
                    if scraped_data['headings']['h1']:
                        st.markdown('### H1 tags')
                        st.dataframe(scraped_data['headings']['h1'], use_container_width=True)
                    if scraped_data['headings']['h2']:
                        st.markdown('### H2 tags')
                        st.dataframe(scraped_data['headings']['h2'], use_container_width=True)
                    if scraped_data['headings']['h3']:
                        st.markdown('### H3 tags')
                        st.dataframe(scraped_data['headings']['h3'], use_container_width=True)
            
            with col2:
                with st.expander("🖼️ Images Found"):
                    if scraped_data['images']:
                        for img in scraped_data['images']:
                            img_col1, img_col2 = st.columns([1, 4])
                            with img_col1:
                                try:
                                    st.image(img['src'], width=100)
                                except Exception:
                                    st.warning("Could not load image")
                            with img_col2:
                                st.write(f"Alt Text: {img['alt']}")
                                st.caption(f"URL: {img['src']}")
                            st.divider()
                    else:
                        st.info("No images found on the page")

            with st.expander("💻 Technologies Identified", expanded=True):
                if scraped_data['technologies']:
                    for tech in scraped_data['technologies']:
                        st.info(f"**{tech}** was detected")
                else:
                    st.write("Could not indentify specific technologies")

            with st.expander("🔗 Links Found"):
                if scraped_data['links']:
                    link_data = [{"Text": link['text'], "URL": link['href']} for link in scraped_data['links']]
                    st.dataframe(link_data, use_container_width=True, height=400)
                else:
                    st.info("No links found on the page")
                
    else:
        st.warning("Please enter a URL to scrape")




    