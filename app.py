from scraper.Scraper import Scraper
from database.Database import Database

database = Database()
scraper = Scraper()

scraper.open_url('https://www.iracing.com/cars/')
iracing_cars = scraper.get_iracing_car_names('item-desc')
database.load_car_list_to_database(iracing_cars, 'iRacing')

scraper.open_url('https://assettocorsa.gg/assetto-corsa/')
asseto_corsa_cars = scraper.get_asseto_corsa_car_names('img-hover')
database.load_car_list_to_database(asseto_corsa_cars, 'Asseto Corsa')

scraper.open_url('https://assettocorsa.gg/assetto-corsa-competizione/')
asseto_corsa_competizione_cars = scraper.get_asseto_corsa_car_names('img-hover')
cont = 0
for asseto_corsa_competizione_car in asseto_corsa_competizione_cars:
    if asseto_corsa_competizione_car == 'Porsche 992 GT3 Cup (2021)':
        cont = cont + 1
        asseto_corsa_competizione_cars = asseto_corsa_competizione_cars[:cont]
        break
    cont = cont + 1
database.load_car_list_to_database(asseto_corsa_competizione_cars, 'Asseto Corsa Competizione')

scraper.open_url('https://www.gran-turismo.com/us/products/gtsport/carlist/')
gran_turismo_sport_cars = scraper.get_gran_turismo_sport_car_names('carlist_table')
scraper.close_url()
database.load_car_list_to_database(gran_turismo_sport_cars, 'Gran Turismo Sport')
