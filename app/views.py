from app.methods import *
from flask import *
from datetime import datetime
from app import app, user, pwd


@app.route("/")
@app.route("/home")
def home():
    return render_template('log.html')


@app.route("/handle_data", methods=["POST"])
def handle_data():
    task_id = request.form['taskid']
    serial_asset = request.form['soa']
    qty = request.form['qty']
    badge_scan = request.form['badge']
    date = datetime.now().strftime('%m/%d/%Y (%H:%M)')
    task_pull_taskid, task_pull_cost_center = task_pull(user, pwd, task_id)
    serialnum_asset, serialnum_serial, serialnum_model = serial_num(user, pwd, serial_asset)
    displayname_description = display_name(user, pwd, serialnum_model)
    employee_name, employee_cc, employee_manager = employee_info(user, pwd, badge_scan)
    sheet([date, task_pull_taskid, task_pull_cost_center,
          serialnum_asset, serialnum_serial, qty, displayname_description,
           badge_scan, employee_name, employee_cc, employee_manager])
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)