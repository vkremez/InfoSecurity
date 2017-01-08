#!/usr/bin/env python
# Coded by @VK_Intel
# Python 3.4
import requests
import re
import csv
import time
import os
from elasticsearch import Elasticsearch, RequestsHttpConnection
from datetime import datetime
from threading import Timer

# Create a Dridex Class
class Dridex:
    @staticmethod
    def get_data(path=None):
        try:
            url = requests.get(path)
            data = url.content
            global ips
            ips = re.findall(r'Host: ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})', str(data))
            rdate = re.findall(r'Firstseen: ([0-9\W:]{19})', str(data))
            malware = []
            for i in range(len(ips)):
                i = 'Dridex'
                malware.append(i)
            global zipped
            zipped = zip(ips, rdate, malware)
        except ConnectionError as e:
            print(e)
            raise
        return

    @staticmethod
    def check_dups():
        dridex_file = open('<FILE LOCATION', 'r+')
        first_line = dridex_file.readline().split(',')[0]
        if first_line == ips[0]:
            print("No changes; Need to Sleep More!")
            print("Sleeping 10 minutes")
            time.sleep(5000)
            a = Dridex()
            a.get_data()
        else:
            print("Go Scrape!!!")
        return

    # def hailey_query(self,ip_address=None):
    #     r = requests.get('<ENRICHMENT CLASS>/%s' % str(ip_address))
    #     r_dict = r.json()
    #     nets = r_dict['nets']
    #     r_dict.pop('nets', None)
    #     dict_list = []
    #     for net in nets:
    #         z = {**net, **r_dict}
    #         dict_list.append(z)
    #     return dict_list

    @staticmethod
    def writer_func(local=None):
        with open(local, "w+") as csvfile:
            try:
                writer = csv.writer(csvfile)
                for rdate, ips, malware in zipped:
                    writer.writerow([rdate, ips, malware])
            except IOError as e:
                print("Error: ", e)
        return

    @staticmethod
    def run():
        while True:
            d = Dridex()
            try:
                d.get_data("<URL>")
                d.check_dups()
                print("Done!!")
            except IndexError as e:
                print("Failed to retrieve an index: ", e)
                raise
            try:
                t = Timer(30.0, d.writer_func("dridex"))
                t.start()
                print("Done!!!")
            except IOError as e:
                print("Failed to write data locally: ", e)
                raise
            try:
                a = Elasticsearch_Connection()
                a.es_conn()
                a.push_to_es('<PATH>', '<NODE NAME>')
                print("Done!!!!!")
            except Exception as e:
                print(e)
            try:
                os.system("logstash -f geoip.conf")
            except Exception as e:
                print(e)
            print("Done!!!!!!!")
            print("Sleeping 5 minutes")
            time.sleep(30) # todo fix back to 5 mins

class Elasticsearch_Connection:

    @staticmethod
    def es_conn():
        global es_client
        es_client = Elasticsearch(
        ['localhost:9200/'],connection_class=RequestsHttpConnection)
        return es_client

    @staticmethod
    def push_to_es(dridex_file=None, es_index=None):
        res_dict = {}
        with open(dridex_file, 'r+') as dridex_file:
            for line in dridex_file:
                fields = line.split(',')
                try:
                    # Convert user_join_date to "datetime" object time so that elasticsearch can properly index
                    res_dict['dateSeen'] = datetime.strptime(fields[1], "%Y-%m-%d %H:%M:%S")
                except Exception as e:
                   pass
                try:
                    res_dict['IOC'] = fields[0].strip()
                except Exception as e:
                   pass
                try:
                    res_dict['malware'] = fields[2].strip()
                except Exception as e:
                   pass
                #res_dict['source'] = fields[3].strip()
                print(res_dict)
        es_client.index(index=es_index, doc_type="Analyzed_Dridex_C2", body=res_dict)

print("\n===============================================\n")
print("Run DridexHostConverter to obtain geographical location of Dridex C2 servers.")
if __name__ == "__main__":
    Dridex.run()
