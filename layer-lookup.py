import os
import pandas as pd
import shapefile

# Function to check if a file is a shapefile
def is_shapefile(filename):
    return filename.lower().endswith(".shp")

# Function to get information from a shapefile
def get_shapefile_info(filepath):
    try:
        sf = shapefile.Reader(filepath)
        fields = sf.fields[1:]  # Exclude the first field (DeletionFlag)
        field_names = [field[0] for field in fields]
        return {
            "filename": os.path.basename(filepath),
            "description": sf.shapeTypeName,
            "source": sf.bbox,
            "field_names": ", ".join(field_names),
            "note": ""  # You can modify this to add any specific notes
        }
    except shapefile.ShapefileException as e:
        print(f"Error reading shapefile {filepath}: {e}")
        return None

# Directory where shapefiles are located - REPLACE THIS PATH
folder_path = r"M:\MapCom\Data\CityOfSM_2017"

# List to store shapefile information
shapefile_info_list = []

# Iterate through files in the folder
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)
    if is_shapefile(file_path):
        shapefile_info = get_shapefile_info(file_path)
        if shapefile_info:
            shapefile_info_list.append(shapefile_info)

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(shapefile_info_list)

# Specify the path for the output folder
output_folder = "C:/Users/tb1302/Documents/workspace/layer-lookup/output"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Specify the path for the output Excel file
output_excel = os.path.join(output_folder, "shapefile_info_CoSM2.xlsx")

# Write DataFrame to Excel using openpyxl engine
df.to_excel(output_excel, index=False, engine='openpyxl')

print("Shapefile information has been written to:", output_excel)