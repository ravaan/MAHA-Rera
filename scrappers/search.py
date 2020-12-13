from lxml import html

from scrappers.utils import send_http_request

XPATH = '//*[@id="gridview"]/div[1]/div/table/tbody/tr/td[5]/b/a'
URL = "https://maharerait.mahaonline.gov.in/SearchList/Search"


def _send_request(application_no):
    headers = {
        'Origin': 'https://maharerait.mahaonline.gov.in',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/87.0.4280.88 Safari/537.36',
        'Referer': 'https://maharerait.mahaonline.gov.in/SearchList/Search',
    }
    payload = {
        'Type': 'Promoter',
        'pageTraverse': 1,
        'CertiNo': application_no,
        'hdnCertiNo': application_no,
        'btnSearch': 'Search',
        'TotalRecords': 1,
        'CurrentPage': 1,
        'TotalPages': 1,
    }

    response = send_http_request("POST", URL, headers=headers, data=payload)
    return response


def get_details_link(application_no):
    response = _send_request(application_no)
    tree = html.fromstring(response.text)
    elements = tree.xpath(XPATH)
    if not elements:
        return
    link = 'https://maharerait.mahaonline.gov.in' + elements[0].attrib['href']
    return link
