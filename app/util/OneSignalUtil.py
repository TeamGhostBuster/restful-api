import requests
import json
from app import app


class OneSignal:
    def __init__(self):
        self.header = {
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": "Basic {}".format(app.config['ONE_SIGNAL_SETTINGS']['API_KEY'])
        }

    def create_invitation_notification(self, invitations):
        target_users = list()
        for each in invitations:
            target_users.append({'field': 'tag', 'key': 'email', 'relation': '=', 'value': each.invitee.email})

        payload = {
            'app_id': app.config['ONE_SIGNAL_SETTINGS']['API_ID'],
            'filters': target_users,
            'contents': {'en': '{} sent you a invitation'.format(invitations[0].inviter.first_name)}
        }

        req = requests.post('https://onesignal.com/api/v1/notifications',
                            headers=self.header,
                            data=json.dumps(payload))

        if req.status_code == 200:
            app.logger.info('Push notification sent')

