from pprint import pprint

van_tor_price = 250
van_ott_price = 280
van_mon_price = 240
van_edm_price = 150
van_cal_price = 180

van_tor_travel_time = 3.5
van_ott_travel_time = 4
van_mon_travel_time = 4
van_edm_travel_time = 1.5
van_cal_travel_time = 1

ott_ber_price = 1350
mon_lon_price = 1300
edm_lon_price = 1290
cal_lon_price = 1400
tor_mun_price = 990

ott_layover = 3.5
mon_layover = 2
edm_layover = 5
cal_layover = 2.5
tor_layover = 1.5

ott_ber_travel_time = 9
mon_lon_travel_time = 8
edm_lon_travel_time = 10
cal_lon_travel_time = 10
tor_mun_travel_time = 9.5

options = {}

options['vanOttBer'] = (van_ott_price + ott_ber_price) / (van_ott_travel_time + ott_layover + ott_ber_travel_time)
options['vanTorMun'] = (van_tor_price + tor_mun_price) / (van_tor_travel_time + tor_layover + tor_mun_travel_time)
options['vanCalLon'] = (van_cal_price + cal_lon_price) / (van_cal_travel_time + cal_layover + cal_lon_travel_time)
options['vanMonLon'] = (van_mon_price + mon_lon_price) / (van_mon_travel_time + mon_layover + mon_lon_travel_time)
options['vanEdmLon'] = (van_edm_price + edm_lon_price) / (van_edm_travel_time + edm_layover + edm_lon_travel_time)

pprint(options)
print("Best Value:", min(options, key=options.get))
