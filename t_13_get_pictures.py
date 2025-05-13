import requests 
from bs4 import BeautifulSoup

def get_pictures(url, path):
    """下载图片"""
    headers = { 
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        with open(path, 'wb') as f:
            f.write(response.content)
        print(f'图片{path}下载成功')

def fetch_html(url):
    """获取指定url的html内容"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"获取网页内容失败，状态码：{response.status_code}")
        return None

def extract_link_from_html(html_content):
    """从HTML内容中提取链接信息"""
    soup = BeautifulSoup(html_content, 'html.parser')
    links = set()
    for element in soup.find_all('img'):
        if element.has_attr('src') and element['src'].endswith('jpg'):
            links.add(element['src'])

    return sorted(links)


if __name__ == "__main__":
    url = "https://wallpapershome.com/" 
    html_content = fetch_html(url)
    if html_content:
        links = extract_link_from_html(html_content)
        print("提取到的链接:")
        for link in links:
            if link.startswith('/'):
                link =  url + link
            print('downloading:', link)
            get_pictures(link, link.split('/')[-1])
