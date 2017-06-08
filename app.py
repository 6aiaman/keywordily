from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import numpy as np
import re

from generate_kw import * 
from intent_kw import *
import intent_kw
from twitter_news import *

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
	
	""" For non-members - goes to search and result view pages """

	if request.method == "POST":
		user_search_query = request.form['kw_query']
		generated_kw = fetch_data(user_search_query)
		generated_kw_df = pd.DataFrame(generated_kw)
		test_data = test_data_df(generated_kw_df)
		intent_kw_list = kw_intent_finder(test_data)
		df_to_html = re.sub('row-border', '" id="data_kw', intent_kw_list.to_html(classes='row-border'))

		twitter_list = twitter_feed(user_search_query)

		return render_template('view.html', df=df_to_html, twitter_list=twitter_list)
	return render_template('home.html')


if __name__ == '__main__':
	app.run(debug=True)
