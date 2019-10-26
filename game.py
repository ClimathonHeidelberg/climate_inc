from time import sleep
from fraction import Fraction
from ecosystem import Ecosystem

class Game():

    def __init__(self, init_year, decision_dict):
        self.init_year = init_year
        self.end_year = 2100
        self.decision_dict = decision_dict

        self.fraction = Fraction(init_year)
        self.ecosystem = Ecosystem(init_year, 0)
    


    def play(self):
        for year in range(self.init_year, self.end_year):
            # sleep(10)
            print(year)
            # model = self.fraction.get_current_state()
            # self.ecosystem.perform_timestep(0)


decision_dict_1 = {'powerplant':'yes'}
decision_dict_2 = {'powerplant':'no'}
init_year = 2019


game = Game(init_year, decision_dict_1)
game.play()


# from scipy.io import netcdf

# file = netcdf.netcdf_file('', 'r')

# bla = file.variable['']