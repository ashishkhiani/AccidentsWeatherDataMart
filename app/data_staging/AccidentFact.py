from db.dal.data_mart.AccidentFactDAL import AccidentFactDAL


class AccidentFact(object):

    @staticmethod
    def populate():
        AccidentFactDAL.populate()
