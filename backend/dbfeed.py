from DBConnection import DBConnection

db = DBConnection()

route = db.routes()
route['start'] = 'Saddar'
route['end'] = 'Secretariat'
route['id'] = 1
route['name'] = "1C"
route['stops'] = ['Saddar','Railway Station','Marheer Hassan','Chandni Chowk','Rehman Abad','Faizabad','Zero point','Aabpara Market','Melody Market','Secretariat']
route.save()

stop = db.stops()
stop['latitude'] = 33.601799
stop['longitude'] = 73.047932
stop['id'] = 1
stop['name'] = "Saddar"
stop.save()

stop2 = db.stops()
stop2['latitude'] = 33.601799
stop2['longitude'] = 73.047932
stop2['id'] = 2
stop2['name'] = "Railway Station"
stop2.save()

stop3 = db.stops()
stop3['latitude'] = 33.599879
stop3['longitude'] = 73.063280
stop3['id'] = 3
stop3['name'] = "Marheer Hassan"
stop3.save()

stop4 = db.stops()
stop4['latitude'] = 33.630385
stop4['longitude'] = 73.072024
stop4['id'] = 4
stop4['name'] = "Chandni Chowk"
stop4.save()

stop5 = db.stops()
stop5['latitude'] = 33.636132
stop5['longitude'] = 73.074996
stop5['id'] = 5
stop5['name'] = "Rehman Abad"
stop5.save()

stop6 = db.stops()
stop6['latitude'] = 33.664482
stop6['longitude'] = 73.087142
stop6['id'] = 6
stop6['name'] = "Faizabad"
stop6.save()

stop7 = db.stops()
stop7['latitude'] = 33.693694
stop7['longitude'] = 73.065189
stop7['id'] = 7
stop7['name'] = "Zero Point"
stop7.save()

stop8 = db.stops()
stop8['latitude'] = 33.707225
stop8['longitude'] = 73.088875
stop8['id'] = 8
stop8['name'] = "Aabpara Market"
stop8.save()

stop9 = db.stops()
stop9['latitude'] = 33.717413
stop9['longitude'] = 73.086390
stop9['id'] = 9
stop9['name'] = "Melody Market"
stop9.save()


stop10 = db.stops()
stop10['latitude'] = 33.729460
stop10['longitude'] = 73.093568
stop10['id'] = 10
stop10['name'] = "Secretariat"
stop10.save()
