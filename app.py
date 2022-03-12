from flask import Flask, jsonify, request
import stock_info

app = Flask(__name__)

@app.route('/top_gainers')
def top_gainers():
  return jsonify(stock_info.get_gainers())

@app.route('/top_losers')
def top_losers():
  return jsonify(stock_info.get_losers())