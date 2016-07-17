from DBConnection import DBConnection

db = DBConnection()

route = db.routes()
route['start'] = 'Kachehri'
route['end'] = 'Secretariat'
route['id'] = 2
route['name'] = "21"
route['stops'] = ['Kachehri','Airport','Khana Pull','Kuri Road','Faizabad','Zero Point','Aabpara Market','Sarina Hotel','SBP','Secretariat']
route.save()

stop = db.stops()
stop['latitude'] = 33.585542
stop['longitude'] = 73.069509
stop['id'] = 11
stop['name'] = "Kachehri"
stop.save()

stop2 = db.stops()
stop2['latitude'] = 33.6079
stop2['longitude'] = 73.1004
stop2['id'] = 12
stop2['name'] = "Airport"
stop2.save()

stop3 = db.stops()
stop3['latitude'] = 33.629429
stop3['longitude'] = 73.115330
stop3['id'] = 13
stop3['name'] = "Khana Pull"
stop3.save()

stop4 = db.stops()
stop4['latitude'] = 33.678154
stop4['longitude'] = 73.162088
stop4['id'] = 14
stop4['name'] = "Kuri Road"
stop4.save()

stop5 = db.stops()
stop5['latitude'] = 33.714949
stop5['longitude'] = 73.103467
stop5['id'] = 15
stop5['name'] = "Sarina Hotel"
stop5.save()

stop6 = db.stops()
stop6['latitude'] = 33.722147
stop6['longitude'] = 73.0926391
stop6['id'] = 16
stop6['name'] = "SBP"
stop6.save()
