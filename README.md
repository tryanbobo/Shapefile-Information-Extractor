# Shapefile Information Extractor

The script will process the shapefiles, extract information, and create an Excel file (`shapefile_info.xlsx`) in the `output` folder with the following columns:

- `filename`: Name of the shapefile
- `description`: Type of geometry (e.g., Point, Line, Polygon)
- `source`: Bounding box coordinates
- `field_names`: Field names in the shapefile
- `note`: Additional notes (modifiable in the script)

## Usage

1. Place your shapefiles in a folder.
2. Update the `folder_path` variable in the script (`layer-lookup.py`) to point to your folder containing shapefiles.
3. Run the script using the command:

## Notes

- If a shapefile is found to be corrupt or unreadable, the script will skip it and continue processing other shapefiles.
- The `output` folder will be created in the same directory as the script if it doesn't exist.

Feel free to modify the script to suit your specific requirements or add more functionality.
"""


