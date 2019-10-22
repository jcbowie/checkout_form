import requests
import urllib3
import gspread
from oauth2client.service_account import ServiceAccountCredentials
urllib3.disable_warnings()


def task_pull(x):
    url = 'https://shawdev.service-now.com/api/now/table/sc_task?sysparm_query=number%3D{}&sysparm_fields=number%2Cu_cost_center&sysparm_limit=1'.format(x)
    user = 'AssetsCage'
    pwd = 'A$$etsCag3'
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    response = requests.get(url, auth=(user, pwd), headers=headers, verify=False)
    result = response.json()['result']
    taskid = result[0]['number']
    cost_center = result[0]['u_cost_center']
    return taskid, cost_center


def serial_num(y):
    url = 'https://shawdev.service-now.com/api/now/table/cmdb_ci?sysparm_query=serial_number%3D{}&sysparm_fields=serial_number%2Cmodel_id%2Casset_tag&sysparm_limit=1'.format(y)
    user = 'AssetsCage'
    pwd = 'A$$etsCag3'
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    response = requests.get(url, auth=(user, pwd), headers=headers, verify=False)
    result = response.json()['result']
    asset = result[0]['asset_tag']
    serial = result[0]['serial_number']
    model = result[0]['model_id']['value']
    return asset, serial, model


def display_name(z):
    url = 'https://shawdev.service-now.com/api/now/table/cmdb_hardware_product_model?sysparm_query=sys_id%3D{}&sysparm_fields=display_name&sysparm_limit=1'.format(z)
    user = 'AssetsCage'
    pwd = 'A$$etsCag3'
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    response = requests.get(url, auth=(user, pwd), headers=headers, verify=False)
    result = response.json()['result']
    description = result[0]['display_name']
    return description


def sheet(**args):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('Cage Test-d66fa3df57c7.json', scope)
    gc = gspread.authorize(credentials)
    wks = gc.open('Cage Test').sheet1
    return wks.append_row([args])



