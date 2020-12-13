import logging

from rera.models import Organization, Application, RealEstateAgent, RealEstateAgentContract
from scrappers import search
from scrappers.agent_links import get_links
from scrappers.application_ids import ids
from scrappers.utils import send_http_request

logger = logging.getLogger(__name__)


def get_or_create_org_and_application(promoter_application_data, application_id):
    org, _ = Organization.objects.get_or_create(
        number=promoter_application_data['number'],
        defaults=promoter_application_data
    )

    application, _ = Application.objects.get_or_create(application_id=application_id)

    return org, application


def get_or_create_agent(data):
    agent, _ = RealEstateAgent.objects.get_or_create(pan=data['pan'], defaults=data)
    return agent


def parse_agent_data(text):
    pass


for application_id in ids:
    link = search.get_details_link(application_id)
    response = send_http_request('GET', link)
    if response.status_code != 200:
        logger.error('unexpected response: {} {}'.format(response.status_code, response.text))
    promoter_application_data = get_links(response.text)
    org, application = get_or_create_org_and_application(promoter_application_data)
    for agent_link in promoter_application_data['agent_links']:
        response = send_http_request('GET', link)
        if response.status_code != 200:
            logger.error('unexpected response: {} {}'.format(response.status_code, response.text))
        agent_data = parse_agent_data(response.text)
        agent = get_or_create_agent(agent_data)
        RealEstateAgentContract.objects.get_or_create(agent=agent, application=application)
