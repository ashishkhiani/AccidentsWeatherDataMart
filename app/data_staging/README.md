These are the steps taken to stage the data.

1. Import raw climate data into PostGreSQL database server for pre-processing.
    * Import raw climate data for Alberta into `data_source.climate_data_alberta`
    * Import raw climate data for Ontario into `data_source.climate_data_ontario`

2. Filter climate Data based on cities/weather stations of interest.
    * Filter climate data for Calgary into `data_source.climate_data_calgary`
    * Filter climate data for Toronto into `data_source.climate_data_toronto`
    * Filter climate data for Ottawa into `data_source.climate_data_ottawa`
    
3. Import raw collision data into PostGreSQL database server for pre-processing.
    * Import raw collision data for Calgary into `data_source.collision_data_calgary`
    * Import raw collision data for Toronto into `data_source.collision_data_toronto`
    * Import raw collision data for Ottawa into `data_source.collision_data_ottawa`
        * Notes about 2017 data: The columns `Longitude`, `Latitude`, and `Year` were removed.
        * Notes about 2014, 2015, 2016, 2017 data: Files were converted to csv format. 

4. Populate Hour Dimension from 2007 to 2017.

5. Clean weather data and populate Weather Dimension. 