# Flask Asset Checkout Form
This app is used to simply reduce the user inputs taken from a user in the process of checking out and asset from the asset supply room. The previous process called for all information to be entered manually. With this application only 4 inputs will be needed:

	1. Task ID - This identification number is associated with the task that calls for the asset to be checked out. 
	2. Asset Tag - This is an identification number associated with the asset. This identification number can be scanned with a barcode scanner from the device. 
	3. Quantity - Some assets have the same asset number depending on the asset. If multiple assets are checked out it can be logged using multiple quantities. 
	4. Badge Number - This is an identification number associated to the employee. This ensures that the correct cost center is attached to the device during the time of task completion. 

# Setup
## First setup your environment, activate your environment and install required packages.
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Second, set your app’s api credentials as an environment variables. 
```
export ASSET_CHECKOUT_API_USER= username credential
export ASSET_CHECKOUT_API_PASSWORD= password credential
```

## Before running shell commands, 
```
export FLASK_APP=/path/to/autoapp.py
export FLASK_DEBUG=1
```

In your production environment, make sure the FLASK_DEBUG environment variable is unset or is set to 0.
