import pandas as pd 

class PDDB(object):
    def __init__(self):
        unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
        self.users = pd.read_table('./initdata/users.dat', sep='::', header=None, names=unames)

        rnames = ['user_id', 'movie_id', 'rating', 'timestamp']                 
        self.ratings = pd.read_table('./initdata/ratings.dat', sep='::', header=None, names=rnames) 

        mnames = ['movie_id', 'title', 'genres']            
        self.movies = pd.read_table('./initdata/movies.dat', sep='::', header=None, names=mnames)
    
    def merge_tables(self):
        """关联三张表"""

        data = pd.merge(pd.merge(self.ratings, self.users), self.movies)

        return data

    def active_titles(self):
        """过滤少于250个评分的电影"""

        data = self.merge_tables()
        ratings_by_title = data.groupby('title').size()
        active_titles = ratings_by_title.index[ratings_by_title >= 250]

        return active_titles

    def rating_std_by_title(self):
        """通过评分的方差来计算出最大异议的电影"""

        data = self.merge_tables()
        active_titles = self.active_titles()
        rating_std_by_title = data.groupby('title')['rating'].std()
        rating_std_by_title = rating_std_by_title.loc[active_titles]
        
        return rating_std_by_title

    