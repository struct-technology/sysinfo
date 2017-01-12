from copy import deepcopy

from flask_api import FlaskAPI, status

from core import SysInfoApp
from helpers.mask import mask_full_field, mask_half_field

sys_info_app = SysInfoApp()

app = FlaskAPI(__name__)


@app.route("/")
def welcome():
    return {'message': 'Welcome to SysInfo App!'}, status.HTTP_200_OK


@app.route("/clients/", methods=['GET'])
def clients():
    masked_clients = deepcopy(sys_info_app.clients)

    for client in masked_clients:
        client['username'] = mask_half_field(client.get('username'))
        client['password'] = mask_full_field(client.get('password'))

    return masked_clients, status.HTTP_200_OK


@app.route("/collect-data/<string:hash>/", methods=['POST'])
def collect_data(hash):
    return {'success': True}, status.HTTP_201_CREATED


@app.route("/send-alert/<string:hash>/", methods=['POST'])
def send_alert(hash):
    return {'success': True}, status.HTTP_202_ACCEPTED


if __name__ == "__main__":
    app.run()