import re

from bs4 import BeautifulSoup as Parser


def get_links(html_text):
    parsed_html = Parser(html_text)
    links = parsed_html.find('div', {'id': "DivProfessional"}).find("table").find_all("a")
    agent_links = [link['href'] for link in links]
    return agent_links


def get_parsed_dict_from_html(html_text) -> dict:
    filtered_text = re.findall("for=\"PersonalInfoModel_.*?<div class=\"col-md-3 col-sm-3\">.*?</div>", html_text,
                               re.DOTALL)
    return dict([[text.split('>')[x].split('<')[0].strip() for x in [1, 4]] for text in filtered_text])


"""
{'Name': 'Vilas Javdekar &amp; Sanjeevani Developers LLP',
 'Organization Type': 'Partnership',
 'Block Number': '306',
 'Building Name': 'Siddhartha Towers',
 'Street Name': 'Sangam Press Road',
 'Locality': 'Kothrud',
 'Land mark': 'Near Sangam Press',
 'State/UT': 'MAHARASHTRA',
 'Division': '411038',
 'Office Number': '02066208000'}
"""
