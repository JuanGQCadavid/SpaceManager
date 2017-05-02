# -*- coding: utf-8 -*-

import csv
import matplotlib.pyplot as plt
import numpy as np

def values_list():
	values = csv.reader(open('DatosCel.csv'))
	return list(values)

def worker_obtained_money(values_list = []):
	money_for_worker = {}

	for worker in range(1, len(values_list)):
		name_worker = values_list[worker][1]
		money = int(values_list[worker][3])

		if name_worker in money_for_worker:
			money_for_worker[name_worker] += money
		else:
			money_for_worker[name_worker] = money


	workers_name = []
	workers_money = []

	for name_worker, money in money_for_worker.items():
		workers_name.append(name_worker)
		workers_money.append(money)


	plt.bar(np.arange(len(workers_money)), workers_money, 0.8)
	plt.xticks(np.arange(len(workers_name)), workers_name)
	plt.title("Money for worker")
	plt.ylabel("Money")
	plt.xlabel("id worker")
	plt.show()


def day_obtained_money(values_list = []):
	dates = []
	days_money = {}

	for date in range(1, len(values_list)):
		day = values_list[date][4]
		money = int(values_list[date][3])

		if len(day) == 15:
			day = day[2:4]

			if day in days_money:
				days_money[day] += money
			else:
				days_money[day] = money

		else:
			day = day[2:3]

			if day in days_money:
				days_money[day] += money
			else:
				days_money[day] = money

	days = []
	money_day = []

	for day, money in days_money.items():
		days.append(day)
		money_day.append(money)


	plt.bar(np.arange(len(money_day)), money_day, 0.8)
	plt.xticks(np.arange(len(money_day)), days)
	plt.title("Money for day")
	plt.ylabel("Money")
	plt.xlabel("day")
	plt.show()


def worker_month(values_list = [], name_worker = '') :
	worker_stats = []
	worker_money = {}

	for worker in values_list:
		if worker[2] == name_worker:
			worker_stats.append(worker)


	for date in worker_stats:
		day = date[4]
		money = int(date[3])

		if len(day) == 15:
			day = day[2:4]

			if day in worker_money:
				worker_money[day] += money
			else:
				worker_money[day] = money

		else:
			day = day[2:3]

			if day in worker_money:
				worker_money[day] += money
			else:
				worker_money[day] = money

	days = []
	money_day = []

	for day, money in worker_money.items():
		days.append(day)
		money_day.append(money)


	plt.bar(np.arange(len(money_day)), money_day, 0.8)
	plt.xticks(np.arange(len(money_day)), days)
	plt.title(name_worker)
	plt.ylabel("Money")
	plt.xlabel("day")
	plt.show()


values = values_list()
#worker_obtained_money(values)
#day_obtained_money(values)
worker_month(values, 'duver')
