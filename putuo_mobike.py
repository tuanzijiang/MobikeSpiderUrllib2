# -*- coding: utf-8 -*-
import json
import urllib2
import random
from time import sleep

import MySQLdb
import time
import sys

DISTX =[]
DISTY =[]
COUNT = 0
def address():
    global DISTX
    global DISTY
    db = MySQLdb.connect(host='localhost',passwd='123aaaaaa',user='root',db='ofo',charset='utf8')
    cursor = db.cursor()
    sql = 'SELECT * FROM putuo_address_info;'
    cursor.execute(sql)
    for row in cursor.fetchall():
        DISTX.append(row[1])
        DISTY.append(row[2])
    db.close()
def link():
    global DISTY
    global DISTX
    global COUNT
    for num in xrange(len(DISTX)):
        lon = DISTX[COUNT]
        lat = DISTY[COUNT]
        spider(lon,lat,10)
        COUNT=COUNT+1
        if COUNT<5248:
            next_lon = DISTX[COUNT]
            next_lat = DISTY[COUNT]
            print ("next start")
            spider(next_lon, next_lat, 10)
        else:
            localtime = time.asctime(time.localtime(time.time()))
            print "本地时间为 :", localtime

def spider(lon,lat,num):
    global DISTY
    global DISTX
    global COUNT
    http_proxy = {'http': '116.28.109.64:808'}
    url = "https://mwx.mobike.com/mobike-api/rent/nearbyBikesInfo.do"
    payload = "?latitude=%s&longitude=%s&errMsg=getMapCenterLocation" % (lat, lon)
    url = url + payload
    headers = {
        'charset': "utf-8",
        'platform': "4",
        "referer": "https://servicewechat.com/wx40f112341ae33edb/1/",
        'content-type': "application/x-www-form-urlencoded",
        'user-agent': "MicroMessenger/6.5.4.1000 NetType/WIFI Language/zh_CN",
        'host': "mwx.mobike.com",
        'connection': "Keep-Alive",
        'accept-encoding': "gzip",
        'cache-control': "no-cache"
    }
    proxy = [
        '119.29.103.13:8888',
        '121.232.145.77:9000',
        '121.232.144.160:9000',
        '60.178.7.255:8081',
        '121.232.194.212:9000',
        '121.232.148.80:9000',
        '120.77.206.98:8118',
        '121.232.145.21:9000',
        '112.115.132.73:8998',
        '123.59.187.44:8118',
        '121.232.146.156:9000',
        '121.232.144.92:9000',
        '121.232.147.89:9000',
        '121.232.148.11:9000',
        '182.87.38.54:9000',
        '115.151.7.10:808',
        '118.117.139.105:9000',
        '163.125.31.108:8118',
        '121.232.144.198:9000',
        '182.129.240.150:9000',
        '117.90.0.89:9000',
        '121.232.147.175:9000',
        '121.232.146.67:9000',
        '117.90.5.55:9000',
        '101.4.136.34:81',
        '121.232.144.36:9000',
        '117.90.0.7:9000',
        '117.90.2.178:9000',
        '121.232.144.206:9000',
        '121.232.145.197:9000',
        '111.155.116.196:8123',
        '118.117.138.29:9000',
        '121.232.145.37:9000',
        '117.90.1.124:9000',
        '111.12.96.188:80',
        '121.232.148.136:9000',
        '121.232.145.21:9000',
        '121.232.145.236:9000',
        '125.67.75.82:9000',
        '121.232.144.72:9000',
        '121.232.148.238:9000',
        '124.235.145.162:80',
        '121.232.144.182:9000',
        '171.215.236.26:9000',
        '117.90.1.19:9000',
        '121.232.148.107:9000',
        '111.155.116.207:8123',
        '171.92.53.71:9000',
        '117.90.2.26:9000',
        '120.77.156.16:8888',
        '121.232.146.50:9000',
        '114.113.126.32:80',
        '117.90.0.179:9000',
        '219.153.76.77:8080',
        '171.39.40.110:8123',
        '121.232.146.106:9000',
        '121.232.146.150:9000',
        '60.178.131.71:8081',
        '111.155.116.220:8123',
        '121.232.146.9:9000',
        '117.90.6.213:9000',
        '182.141.46.93:9000',
        '60.178.169.58:8081',
        '121.232.144.230:9000',
        '121.232.144.116:9000',
        '60.178.129.250:8081',
        '110.73.6.219:8123',
        '117.90.3.184:9000',
        '121.232.147.141:9000',
        '121.232.146.246:9000',
        '122.96.59.106:81',
        '117.90.6.23:9000',
        '218.64.92.154:808',
        '118.117.138.29:9000',
        '121.232.144.37:9000',
        '117.90.3.61:9000',
        '117.90.7.113:9000',
        '121.232.144.136:9000',
        '101.6.34.137:8123',
        '117.90.7.208:9000',
        '60.178.7.131:8081',
        '60.178.15.47:8081',
        '117.90.2.210:9000',
        '117.90.5.178:9000',
        '121.232.147.173:9000',
        '118.117.137.217:9000',
        '117.90.6.16:9000',
        '122.96.59.100:83',
        '182.129.248.143:9000',
        '171.92.57.131:9000',
        '114.239.148.60:808',
        '121.232.146.57:9000',
        '121.232.145.251:9000',
        '114.239.145.132:808',
        '125.117.112.11:9000',
        '121.232.147.254:9000',
        '117.90.6.10:9000',
        '114.113.126.32:80',
        '117.64.237.248:3128',
        '121.232.147.34:9000',
        '113.140.25.4:81',
        '121.232.144.190:9000',
        '140.255.69.194:808',
        '121.232.144.63:9000',
        '121.232.146.187:9000',
        '110.73.11.79:8123',
        '59.49.129.60:8998',
        '106.120.78.129:80',
        '111.155.116.201:8123',
        '118.117.138.233:9000',
        '60.178.5.235:8081',
        '183.240.87.229:8080',
        '122.96.59.102:80',
        '121.232.144.186:9000',
        '182.88.166.82:8123',
        '183.240.87.229:8080',
        '117.90.3.232:9000',
        '183.240.87.229:8080',
        '122.96.59.102:83',
        '110.73.51.136:8123',
        '121.232.146.116:9000',
        '121.232.147.205:9000',
        '210.29.26.250:80',
        '60.178.4.139:8081',
        '117.68.193.40:3128',
        '111.155.116.215:8123',
        '210.29.26.250:80',
        '121.232.145.229:9000',
        '121.232.147.247:9000',
        '121.31.151.203:8123',
        '121.232.146.55:9000',
        '121.31.149.115:8123',
        '121.232.144.52:9000',
        '121.232.147.33:9000',
        '121.232.147.33:9000',
        '110.73.7.135:8123',
        '117.90.6.155:9000',
        '121.232.144.204:9000',
        '139.196.121.161:80',
        '121.40.81.129:8118',
        '114.226.5.217:9000',
        '121.31.102.82:8123',
        '60.178.131.7:8081',
        '119.29.103.13:8888',
        '110.73.48.68:8123',
        '121.232.144.64:9000',
        '110.73.8.53:8123',
        '60.178.5.253:8081',
        '110.73.51.213:8123',
        '110.73.8.58:8123',
        '121.31.103.238:8123',
        '121.232.147.151:9000',
        '121.232.146.202:9000',
        '122.96.59.103:80',
        '121.31.103.51:8123',
        '121.232.199.19:9000',
        '101.4.136.34:81',
        '118.117.137.46:9000',
        '125.85.186.118:8998',
        '121.31.156.117:8123',
        '121.232.147.170:9000',
        '117.90.1.98:9000',
        '60.178.15.189:8081',
        '117.90.4.85:9000',
        '223.223.187.195:80',
        '122.96.59.103:82',
        '121.31.146.131:8123',
        '121.232.145.104:9000',
        '121.232.144.148:9000',
        '121.232.144.182:9000',
        '60.178.8.68:8081',
        '111.74.56.249:9000',
        '121.232.147.103:9000',
        '117.90.0.59:9000',
        '122.96.59.103:80',
        '117.79.87.165:80',
        '117.90.1.80:9000',
        '117.90.2.103:9000',
        '121.232.144.16:9000',
        '110.73.34.20:8123',

    ]
    temp = random.randint(0,175)
    http_proxy['http'] = proxy[temp]
    proxy = urllib2.ProxyHandler(http_proxy)
    opener = urllib2.build_opener(proxy)
    request = urllib2.Request(url, headers=headers)
    try:
        response = opener.open(request, timeout=1)
        info = response.read()
        info = json.loads(info)
        bikes = info['object']
        bikes_size = len(bikes)
        print (str(COUNT)+'th:"("'+str(lon)+","+str(lat)+ ")---" + str(bikes_size))
        if(bikes_size!=0):
            db = MySQLdb.connect(host='localhost', passwd='123aaaaaa', user='root', db='ofo', charset='utf8')
            cursor = db.cursor()
            sql = "insert into ofo.putuo_valid (distX,distY,num,save_time) values (%s,%s,%s,%s) on duplicate key update num = %s"
            param = (lon,lat,str(bikes_size),'2017-08-12 10:30:00',str(bikes_size))
            cursor.execute(sql,param)
            db.commit()
            db.close()
            print ("size ok")
            pass
        for bike in bikes:
            db = MySQLdb.connect(host='localhost', passwd='123aaaaaa', user='root', db='ofo', charset='utf8')
            cursor = db.cursor()
            sql = "insert into putuo_mobike_address (distX,distY,bikeIds,save_time) values (%s,%s,%s,'2017-08-12 10:30:00') on duplicate key update distY = %s"
            param = (str(bike['distX']),str(bike['distY']),str(bike['bikeIds']),str(bike['distY']))
            cursor.execute(sql,param)
            db.commit()
            db.close()
            pass
        print ("bike info ok")


    except Exception as ex:
        print ex.message
        if(num>0):
            print ("again")
            num=num-1
            spider(lon,lat,num)
        else:
            print ("failure")
            COUNT=COUNT+1
            next_lon = DISTX[COUNT]
            next_lat = DISTY[COUNT]
            spider(next_lon, next_lat, 10)
    # try:
    #     COUNT= COUNT+1
    #     info = response.read()
    #     # print info
    #     info = json.loads(info)
    #     bikes = info['object']
    #     bikes_size = len(bikes)
    #     # print (str(COUNT)+'th: '+str(num)+"("+lon+","+lat+")---"+str(bikes_size))
    #     if(bikes_size!=0):
    #         db = MySQLdb.connect(host='localhost', passwd='123aaaaaa', user='root', db='ofo', charset='utf8')
    #         cursor = db.cursor()
    #         sql = "insert into ofo.shanghai_valid (distX,distY,num) values (%s,%s,%s) on duplicate key update num = %s"
    #         param = (lon,lat,str(bikes_size),str(bikes_size))
    #         cursor.execute(sql,param)
    #         db.commit()
    #         db.close()
    #         pass
    #     for bike in bikes:
    #         db = MySQLdb.connect(host='localhost', passwd='123aaaaaa', user='root', db='ofo', charset='utf8')
    #         cursor = db.cursor()
    #         sql = "insert into ofo_address (distX,distY,bikeIds,save_time) values (%s,%s,%s,'2017-08-04 22:02:00') on duplicate key update distY = %s"
    #         param = (str(bike['distX']),str(bike['distY']),str(bike['bikeIds']),str(bike['distY']))
    #         cursor.execute(sql,param)
    #         db.commit()
    #         db.close()
    #     next_lat=count_lat+0.002
    #     if next_lat<UPPER[count_lon]:
    #         spider(lon,str(next_lat),5,count_lon,next_lat)
    #         # print ("%f , %f : %s"%(bike['distY'],bike['distX'],bike['bikeIds']))
    # except Exception as ex:
    #     print ex.message
    #     num = num-1
    #     if num <= 2:
    #         print ("die total"+str(http_proxy['http']))
    #         next_lat = count_lat + 0.002
    #         if next_lat < UPPER[count_lon]:
    #             spider(lon, str(next_lat), 5, count_lon, next_lat)
    #     else:
    #         spider(lon,lat,num,count_lon,count_lat)
    #     pass

if __name__ == '__main__':
    sys.setrecursionlimit(400000)
    address()
    link()