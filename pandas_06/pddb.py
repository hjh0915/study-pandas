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
        sex_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')

        return sex_ratings

    def active_titles(self):
        """过滤少于250个评分的电影"""

        data = self.merge_tables()
        ratings_by_title = data.groupby('title').size()
        active_titles = ratings_by_title.index[ratings_by_title >= 250]

        return active_titles

    def top_female_ratings(self):
        """根据女性观众的top电影，按照F列降序排序"""

        active_titles = self.active_titles()
        mean_ratings = self.sex_ratings().loc[active_titles]
        top_female_ratings = mean_ratings.sort_values(ascending=False, by=['F'])

        return top_female_ratings

    def sorted_by_diff(self):
        """按照diff排序产生评分差异最大的电影(女性首选)"""

        active_titles = self.active_titles()
        mean_ratings = self.sex_ratings().loc[active_titles]
        mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
        sorted_by_diff = mean_ratings.sort_values(by='diff')

        return sorted_by_diff