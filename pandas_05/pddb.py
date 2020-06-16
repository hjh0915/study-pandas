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

    def sex_ratings(self):
        """按性别分级每部电影的平均电影评分"""

        data = self.merge_tables()
        mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')

        return mean_ratings

    def active_titles(self):
        """过滤少于250个评分的电影"""

        data = self.merge_tables()
        ratings_by_title = data.groupby('title').size()
        active_titles = ratings_by_title.index[ratings_by_title >= 250]

        return active_titles

    def get_active_rows(self):
        """从mean_ratings中选出评分多于250个的电影信息"""

        active_titles = self.active_titles()
        mean_ratings = self.sex_ratings().loc[active_titles]

        return mean_ratings
