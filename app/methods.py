import requests
import urllib3
import gspread
from oauth2client.service_account import ServiceAccountCredentials
urllib3.disable_warnings()


def task_pull(user, pwd, x):
    url = 'https://shaw.service-now.com/api/now/table/sc_task?sysparm_query=' \
          'number%3D{}&sysparm_fields=number%2Cu_cost_center&sysparm_limit=1'.format(x)
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    response = requests.get(url, auth=(user, pwd), headers=headers, verify=False)
    result = response.json()['result']
    taskid = result[0]['number']
    cost_center = result[0]['u_cost_center']
    return taskid, cost_center


def serial_num(user, pwd, y):
    url = 'https://shaw.service-now.com/api/now/table/cmdb_ci?sysparm_query=' \
          'serial_number%3D{}&sysparm_fields=serial_number%2Cmodel_id%2Casset_tag&sysparm_limit=1'.format(y)
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    response = requests.get(url, auth=(user, pwd), headers=headers, verify=False)
    result = response.json()['result']
    asset = result[0]['asset_tag']
    serial = result[0]['serial_number']
    model = result[0]['model_id']['value']
    return asset, serial, model


def display_name(user, pwd, z):
    url = 'https://shaw.service-now.com/api/now/table/cmdb_hardware_product_model?sysparm_query' \
          '=sys_id%3D{}&sysparm_fields=display_name&sysparm_limit=1'.format(z)
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    response = requests.get(url, auth=(user, pwd), headers=headers, verify=False)
    result = response.json()['result']
    description = result[0]['display_name']
    return description


def employee_info(user, pwd, badge):
    url = 'https://shaw.service-now.com/api/now/table/cmdb_hardware_product_model?sysparm_query' \
          '=sys_id%3D{}&sysparm_fields=display_name&sysparm_limit=1'.format(badge)
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    response = requests.get(url, auth=(user, pwd), headers=headers, verify=False)
    result = response.json()['result']
    employee_name = result[0]['name']
    employee_cc = result[0]['cost_center']
    employee_manager = result[0]['manager']
    return employee_name, employee_cc, employee_manager


def sheet(**args):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('Cage Test-d66fa3df57c7.json', scope)
    gc = gspread.authorize(credentials)
    wks = gc.open('Cage Test').sheet1
    return wks.append_row([args])