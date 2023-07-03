import configparser

# Read the properties from application.properties
config = configparser.ConfigParser()
config.read("application.properties")

# Access the list property
my_list = config.get("DEFAULT", "my_list").split(",")

# Display the list
print("List:", my_list)