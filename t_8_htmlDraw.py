from bs4 import BeautifulSoup
import requests
import time



def fetch_html(url):
    """获取指定url的html内容"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
    }    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"获取网页内容失败，状态码：{response.status_code}")
        return None

def extract_text_from_html(html_content):
    """从HTML内容中提取正文文本"""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 去掉不必要的脚本和样式内容
    for script in soup(["script", "style"]):
        script.extract()
    
    # 获取正文文本
    text = soup.get_text(separator='\n', strip=True)
    return text

def extract_link_from_html(html_content):
    """从HTML内容中提取链接信息"""
    soup = BeautifulSoup(html_content, 'html.parser')
    links = set()
    for tag, attr in [('a', 'href'), ('img', 'src'), ('link', 'href'), ('script', 'src'), ('iframe', 'href')]:
        for element in soup.find_all(tag, **{attr: True}):
            if element[attr].startswith('http'):
                links.add(element[attr])

    return sorted(links)


if __name__ == "__main__":
    url = "https://www.google.com/"  # 替换为你要抓取的网页URL
    html_content = fetch_html(url)
    if html_content:
        links = extract_link_from_html(html_content)
        print("提取到的链接:")
        for link in links:
            print(link)