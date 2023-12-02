from scraper.TrackScraper import TrackScraper
from database.Database import Database

scraper = TrackScraper()
database = Database()

scraper.open_url('https://www.iracing.com/tracks/')
iracing_tracks = scraper.get_iracing_tracks('item-desc')
database.load_track_list_to_database(iracing_tracks, 'iRacing')

scraper.open_url('https://assettocorsa.gg/assetto-corsa/')
asseto_corsa_tracks = scraper.get_asseto_corsa_tracks('staggered-once')
database.load_track_list_to_database(asseto_corsa_tracks, 'Asseto Corsa')

scraper.open_url('https://assettocorsa.gg/assetto-corsa-competizione/')
asseto_corsa_competizione_tracks = scraper.get_asseto_corsa_competizione_tracks('col-track')
database.load_track_list_to_database(asseto_corsa_competizione_tracks, 'Asseto Corsa Competizione')

scraper.open_url('https://www.gran-turismo.com/gb/products/gtsport/tracklist/')
gran_turismo_sport_tracks = scraper.get_gran_turismo_sport_tracks('tracklist')
database.load_track_list_to_database(gran_turismo_sport_tracks, 'Gran Turismo Sport')

scraper.open_url('https://coachdaveacademy.com/tutorials/rfactor-tracks/')
rfactor2_tracks = scraper.get_rfactor2_car_names('elementor-toc__list-wrapper')
cont = 0
for rfactor2_track in rfactor2_tracks:
    index = rfactor2_track.find(' – ')
    if index != -1:
        rfactor2_tracks[cont] = rfactor2_track[:index]
    cont = cont + 1
scraper.close_url()
database.load_track_list_to_database(rfactor2_tracks, 'rFactor 2')
