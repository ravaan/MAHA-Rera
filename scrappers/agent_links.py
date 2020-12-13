from bs4 import BeautifulSoup as s


def get_links(html_text):
    sp = s(html_text)
    links = sp.find('div', {'id':"DivProfessional"}).find("table").find_all("a")
    agent_links = [i['href'] for i in links]
    return agent_links
