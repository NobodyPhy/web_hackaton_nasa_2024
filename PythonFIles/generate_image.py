import datetime as dt
import meteomatics.api as api
import numpy as np
from shapely.geometry import Point
import geopandas as gpd
import matplotlib.pyplot as plt
import xarray as xr



# No OUTPUT: Downloads filedata.nc
def get_netcdf(coordinates, resolution, parameter, interval=12, before=0, after=7, model='mix', filepath=".", filename=''):

    '''
    Get netcdf file from meteomatics API.
    Coordinates format: [North latitude, West longitude, South Latitude, West longitude]
    Resolutions format: [Latitude Resolution, Longitude Resolution]
    Parameter: Climatologic parameter
    Interval: hours
    Before: Days before now (past)
    After: Days after now (forecast)
    '''

    # Credentials
    username = 'burgos_alexander'
    password = 'NF0xCcC38p'

    # Coordinates of the area and its resolution
    lat_N, lon_W, lat_S, lon_E = coordinates
    res_lat, res_lon = resolution
    
    # Date and time limits
    today = dt.datetime.utcnow().replace(hour=12, minute=0, second=0, microsecond=0)
    startdate = today - dt.timedelta(days=before)
    enddate = today + dt.timedelta(days=after)
    interval = dt.timedelta(hours=interval)
    
    # Parameter name for filename
    parameter_name = parameter.replace(":","")
    # .nc filename

    if not filename: 
        filename = f"{parameter_name}__{startdate.year}_{startdate.month}_{startdate.day}__{enddate.year}_{enddate.month}_{enddate.day}-{startdate.hour}_{startdate.minute}.nc"
    # filepath
    filepath = filepath + "/"

    # Query to the meteomatics API
    try:
        api.query_netcdf(filepath+filename, startdate, enddate, interval, parameter, 
                        lat_N, lon_W, lat_S, lon_E, res_lat, res_lon, username, password, model)
        print("Filename: {}".format(filename))

    except Exception as e:
        print("Failed, exception is {}.".format(e))


# Make a mask acoording to a polygon object
def make_mask(longitudes, latitudes, polygon, parameter):

    # Uniformize shape
    lons2d, lats2d = np.meshgrid(longitudes, latitudes)

    # Create the mask
    mask = np.array( [ [polygon.contains(Point(lon, lat)) for lon, lat in zip(lon_row, lat_row)] for lon_row, lat_row in zip(lons2d, lats2d) ] )

    # Get the parameter matrix masked
    P_masked = np.where(mask, parameter, np.nan)

    return P_masked


# Plot department
def plot_dep(lons, lats, parameter, data, departament="AYACUCHO", save=False, filepath="."):

    # Filter geopandas according to departament
    dept = data[data['NOMBDEP'] == departament]

    # Get polygon for department
    dept_polygon = dept.geometry.values[0]

    # Mask parameter matrix according to department polygon
    P_masked = make_mask(lons, lats, dept_polygon, parameter)

    ################################

    # Crear la figura y los ejes
    fig, ax = plt.subplots(figsize=(5, 6))

    # Graficar el contorno de temperatura sobre los ejes
    contorno = ax.contourf(lons, lats, P_masked, cmap='magma', levels=50)
    cbar = plt.colorbar(contorno, ax=ax, label='T (°C)',fraction=0.046, pad=0.04, shrink=0.8)

    # Graficar los límites del departamento de Ayacucho sobre el mismo eje
    # dept.plot(ax=ax, edgecolor='black', facecolor='none', linewidth=1)
    dept.plot(ax=ax, edgecolor='black', facecolor='none', linewidth=1)

    # Personalizar el gráfico
    ax.set_title(departament)
    ax.axis('off')

    # # Save figure
    # if save:
    #     plt.savefig(filepath + "/ayacucho_final.png")

    # Save figurels
    if save:
        plt.savefig(r"C:\Users\janus\OneDrive\Documentos\droplaipc\rx1\RXpython\assets" + "/ayacucho_final.jpg")



###### Download netcdf file #######
lat_N = -12.167468
lon_W = -75.1398261
lat_S = -15.630065
lon_E = -72.8468246
res_lat = 0.01
res_lon = 0.01

coordinates = [lat_N,lon_W,lat_S,lon_E]
resolution = [res_lat,res_lon]
parameters = 't_2m:C'

get_netcdf(coordinates, resolution, parameters, filepath="data", filename="datos_brutos.nc")


###### Donwload masked department
# Cargar los geodataframes
prov_path = r'C:\Users\janus\OneDrive\Documentos\droplaipc\rx1\RXpython\PythonFIles\data\peru_provincial_simple.geojson'
dept_path = (r'C:\Users\janus\OneDrive\Documentos\droplaipc\rx1\RXpython\PythonFIles\data\peru_departamental_simple'
             r'.geojson')

# Cargar el archivo provincial
data_prov = gpd.read_file(prov_path)

# Cargar el archivo departamental para Ayacucho
data_dept = gpd.read_file(dept_path)


# Abrir el archivo NetCDF
ds = xr.open_dataset('data/datos_brutos.nc') # array
P = ds.data_vars['t_2m'].values[7, :, :] # matrix data for T parameter

lons = ds.coords['longitude'].values # longitude values
lats = ds.coords['latitude'].values # latitude values


plot_dep(lons, lats, P, data_dept, save=True,   filepath="data")
