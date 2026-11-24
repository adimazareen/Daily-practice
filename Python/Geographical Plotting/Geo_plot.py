# Enable Matplotlib inline
%matplotlib inline

# Import libraries
try:
    import geopandas as gpd
    import matplotlib.pyplot as plt
    import requests
except ImportError:
    print("Required packages (geopandas, matplotlib, requests) are not installed. Please install them using:")
    print("`pip install geopandas matplotlib requests` or `conda install geopandas matplotlib requests`")
    raise

# Function to check if URL is accessible
def check_url(url):
    try:
        response = requests.head(url)
        if response.status_code == 200:
            return True
        else:
            print(f"URL {url} returned status code {response.status_code}")
            return False
    except requests.RequestException as e:
        print(f"Error accessing URL {url}: {e}")
        return False

try:
    # 1. Load the world map shapefile from a reliable GeoJSON URL
    url = "https://raw.githubusercontent.com/datasets/geo-boundaries-world-110m/master/countries.geojson"
    
    # Check if the URL is accessible
    if not check_url(url):
        raise Exception("GeoJSON URL is not accessible. Please try an alternative source.")

    world = gpd.read_file(url)

    # 2. Create a basic plot of the world map
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    world.plot(ax=ax, color='lightgray', edgecolor='black')

    # 3. Example of overlaying data points (e.g., major cities)
    cities_data = {
        'City': ['New Delhi', 'New York', 'Tokyo'],
        'Latitude': [28.6, 40.7, 35.7],
        'Longitude': [77.2, -74.0, 139.7]
    }
    gdf_cities = gpd.GeoDataFrame(
        cities_data,
        geometry=gpd.points_from_xy(cities_data['Longitude'], cities_data['Latitude'])
    )

    # Plot cities on the map
    gdf_cities.plot(ax=ax, marker='o', color='red', markersize=50, label='Major Cities')

    # Customize the plot
    ax.set_title('World Map with Major Cities (GeoPandas)')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    plt.legend()
    plt.show()

except Exception as e:
    print(f"An error occurred: {e}")
    print("Alternative GeoJSON sources to try:")
    print("- https://raw.githubusercontent.com/datasets/geo-boundaries-world-110m/master/countries.geojson")
    print("- https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_110m_admin_0_countries.geojson")
