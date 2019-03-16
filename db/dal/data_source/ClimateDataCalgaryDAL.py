# from db.dal.data_source.DataSourceDAL import DataSourceDAL
#
#
# class ClimateDataCalgaryDAL(object):
#     """
#     This functionality of this class is to interact with the database.
#     ALl methods defined in the class must be solely responsible
#     for READING from 'data_source.climate_data_calgary'.
#     No business logic is allowed here.
#     """
#
#     @staticmethod
#     def fetch_all():
#         return DataSourceDAL.fetch_all("""SELECT * FROM data_source.climate_data_calgary""")
#
#     @staticmethod
#     def get_count():
#         return DataSourceDAL.get_count("""SELECT count(*) FROM data_source.climate_data_calgary""")
