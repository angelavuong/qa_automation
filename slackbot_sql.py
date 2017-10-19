import selenium
import schedule
from selenium import webdriver
from datetime import datetime, time, timedelta
import time
from slackclient import SlackClient
import sys
import pymysql
import os
import prettytable

token = "XXXX"
slack_client = SlackClient(token)
BOT_NAME = 'snowflake-bot'

def yeti_databse_connection_read():
    db = pymysql.connect(host="XXX", port=XXXX, db="XXXX", user="XXXX", password="XXXX", read_timeout = 60)
    return db

def fetching_sql_data(sql):
    pid = []
    p_name = []
    newlist = []
    db = yeti_databse_connection_read()
    cursor = db.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    x = prettytable.PrettyTable(["XXXX", "XXXX"])
    x.align = "l"
    x.padding_width = 5 # One space between column edges and contents (default)
    for row in data:
        x.add_row(row)
    return x

def main():
    time = datetime.now() + timedelta(hours=5)
    sql = '''select 	a.partner_id,
		                b.p_name
                FROM 	database1 a
                		INNER JOIN database2 b
                			ON a.partner_id = b.p_id
                WHERE 	a.partner_id != 0
                		AND a.mobile=0
                		AND a.pageviews =0
                		AND a.data_date >= now() - interval 60 minute
                        AND b.p_parent !=1806
                        AND b.p_parent !=1749
                        AND b.p_parent !=1874'''
    try:
        pid = fetching_sql_data(sql)
    except pymysql.err.OperationalError as e:
        print("ERROR: Connection error to the database")
    slack_client.api_call("chat.postMessage", channel="@user1", text="The following sites are indicating 0 pageviews in the last hour: \n" + "```" + str(pid) + "```", as_user=True)
    slack_client.api_call("chat.postMessage", channel="@user2", text="The following sites are indicating 0 pageviews in the last hour: \n" + "```" + str(pid) + "```", as_user=True)


if (datetime.now().hour > 7 and datetime.now().hour < 22):
    schedule.every(1).minutes.do(main)
    print(datetime.now().hour)
while True:
    schedule.run_pending()
    time.sleep(1)
