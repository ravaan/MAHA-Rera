import pandas

columns = ['id', 'division', 'userid', 'Name_of_Project', 'PlotBearing', 'BoundriesE', 'BoundriesW', 'BoundriesN',
           'BoundriesS', 'locality', 'street', 'Project_Village', 'Project_Taluka', 'Project_District',
           'Project_Division', 'Project_State', 'PinCode', 'Registration No.', 'Application_No', 'lat', 'lng']
data = pandas.read_csv('data/project_data.csv', names=columns)

ids = data.Application_No.tolist()
