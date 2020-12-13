from bs4 import BeautifulSoup as Parser


def get_links(html_text):
    parsed_html = Parser(html_text)
    links = parsed_html.find('div', {'id': "DivProfessional"}).find("table").find_all("a")
    agent_links = [link['href'] for link in links]
    return agent_links
