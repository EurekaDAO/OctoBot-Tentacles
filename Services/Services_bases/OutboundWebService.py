import octobot_services.constants as services_constants
import octobot_services.services as services
import requests

class OutboundWebService(services.AbstactService):
    @staticmethod
    def is_setup_correctly(config):
        return True

    @staticmethod
    def get_is_enabled(config):
        return True

    def has_required_configuration(self):
        return True

    def get_successful_startup_message(self):
        return "", True

    async def send_to_backend(self, content):
        # URL of the backend location
        url = 'https://www.example.com/api/send_json'
        # Send the data as a POST request
        response = requests.post(url, content)
        return response

