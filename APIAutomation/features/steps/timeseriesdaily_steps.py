import time
from os import path
from behave import *
import requests
from utilities.config import *
from utilities.logger import *


@given('given time series url with required params')
def given_time_series_url_with_required_params(context):
    context.baseurl = get_config()['API']['baseurl']


@when(u'hit url without optional params')
def hit_url_without_optional_params(context):
    request_url = context.baseurl + "function=TIME_SERIES_DAILY&symbol=IBM&apikey=" + get_config()['API']['key']
    response_text = "Our standard API call frequency is 5 calls per minute and 500 calls per day"
    Log.logger.info('Request URL is ' + request_url)
    print('Request URL is ' + request_url)

    context.response = requests.get(request_url)
    Log.logger.info('Response is ' + context.response.text)
    print('Response is ' + context.response.text)

    if context.response.text.__contains__(response_text):
        print("waiting for a minute to overcome Throttle limit")
        time.sleep(60)
        context.response = requests.get(request_url)
        Log.logger.info('Response is ' + context.response.text)
        print('Response is ' + context.response.text)


@when('hit url with all optional params with symbol value as {symbol_value}')
def hit_url_with_all_optional_params(context, symbol_value):
    request_url = context.baseurl + "function=TIME_SERIES_DAILY&symbol=" + symbol_value + "&outputsize=compact&datatype=json&apikey=" + \
                  get_config()['API']['key']
    response_text = "Our standard API call frequency is 5 calls per minute and 500 calls per day"
    Log.logger.info('Request URL is ' + request_url)
    print('Request URL is ' + request_url)

    context.response = requests.get(request_url)
    Log.logger.info('Response is ' + context.response.text)
    print('Response is ' + context.response.text)

    if context.response.text.__contains__(response_text):
        print("waiting for a minute to overcome Throttle limit")
        time.sleep(60)
        context.response = requests.get(request_url)
        Log.logger.info('Response is ' + context.response.text)
        print('Response is ' + context.response.text)


@when('hit url with partial optional params (without datatype parameter)')
def with_partial_optional_params(context):
    request_url = context.baseurl + "function=TIME_SERIES_DAILY&symbol=" + get_config()['API'][
        'symbol'] + "&outputsize=compact&apikey=" + get_config()['API']['key']
    response_text = "Our standard API call frequency is 5 calls per minute and 500 calls per day"
    Log.logger.info('Request URL is ' + request_url)
    print('Request URL is ' + request_url)

    context.response = requests.get(request_url)
    Log.logger.info('Response is ' + context.response.text)
    print('Response is ' + context.response.text)

    if context.response.text.__contains__(response_text):
        print("waiting for a minute to overcome Throttle limit")
        time.sleep(60)
        context.response = requests.get(request_url)
        Log.logger.info('Response is ' + context.response.text)
        print('Response is ' + context.response.text)


@when('hit url without key')
def hit_url_without_key(context):
    request_url = context.baseurl + "function=TIME_SERIES_DAILY&symbol=" + get_config()['API'][
        'symbol'] + "&outputsize=compact&datatype=json&apikey="
    response_text = "Our standard API call frequency is 5 calls per minute and 500 calls per day"
    Log.logger.info('Request URL is ' + request_url)
    print('Request URL is ' + request_url)

    context.response = requests.get(request_url)
    Log.logger.info('Response is ' + context.response.text)
    print('Response is ' + context.response.text)

    if context.response.text.__contains__(response_text):
        print("waiting for a minute to overcome Throttle limit")
        time.sleep(60)
        context.response = requests.get(request_url)
        Log.logger.info('Response is ' + context.response.text)
        print('Response is ' + context.response.text)


@when('hit url with with outputsize as full')
def with_outputsize_as_full(context):
    request_url = context.baseurl + "function=TIME_SERIES_DAILY&symbol=" + get_config()['API'][
        'symbol'] + "&outputsize=full&datatype=json&apikey=" + get_config()['API']['key']
    response_text = "Our standard API call frequency is 5 calls per minute and 500 calls per day"
    Log.logger.info('Request URL is ' + request_url)
    print('Request URL is ' + request_url)

    context.response = requests.get(request_url)
    Log.logger.info('Response is ' + context.response.text)
    print('Response is ' + context.response.text)

    if context.response.text.__contains__(response_text):
        print("waiting for a minute to overcome Throttle limit")
        time.sleep(60)
        context.response = requests.get(request_url)
        Log.logger.info('Response is ' + context.response.text)
        print('Response is ' + context.response.text)


@when('hit url with with datatype as csv')
def url_with_datatype_as_csv(context):
    request_url = context.baseurl + "function=TIME_SERIES_DAILY&symbol=" + get_config()['API'][
        'symbol'] + "&outputsize=full&datatype=csv&apikey=" + get_config()['API']['key']
    response_text = "Our standard API call frequency is 5 calls per minute and 500 calls per day"
    Log.logger.info('Request URL is ' + request_url)
    print('Request URL is ' + request_url)

    context.response = requests.get(request_url)
    Log.logger.info('Response is ' + context.response.text)
    print('Response is ' + context.response.text)

    if context.response.text.__contains__(response_text):
        print("waiting for a minute to overcome Throttle limit")
        time.sleep(60)
        context.response = requests.get(request_url)
        Log.logger.info('Response is ' + context.response.text)
        print('Response is ' + context.response.text)


@then(u'response is seen with status code as 200')
def response_is_seen_with_status_code_as_200(context):
    assert context.response.status_code == 200


@then('Meta data information has 5 items')
def Meta_data_information_has_5_items(context):
    assert len(context.response.json()['Meta Data']) == 5


@then('ensure Content-Type header value is displayed as application/json')
def all_headers_are_displayed(context):
    assert context.response.headers['Content-Type'] == "application/json"


@then('Meta data has 2. Symbol value is same as {symbol_value} provided in query param')
def symbolvalue_is_as_expected(context, symbol_value):
    assert context.response.json()['Meta Data']['2. Symbol'] == symbol_value


@then('100 points are only returned')
def hundred_points_are_only_returned(context):
    assert len(context.response.json()['Time Series (Daily)']) == 100


@then('response is in JSON format')
def response_is_in_JSON_format(context):
    assert context.response.headers['Content-Type'] == 'application/json'


@then('every entry in Time Series (Daily) has 5 items')
def every_entry_in_Time_Series_Daily_has_5_items(context):
    for key in context.response.json()['Time Series (Daily)']:
        assert len(context.response.json()['Time Series (Daily)'][key]) == 5


@then('reponse should display error')
def response_should_display_error(context):
    assert context.response.text.__contains__("\"Error Message\": \"the parameter apikey is invalid or missing")


@then('Meta data has 4. Output Size value as Full Size')
def outputsize_same_as_queryparam_outputsize(context):
    assert context.response.json()['Meta Data']['4. Output Size'] == "Full size"


@then('20+ years of historical data are returned')
def twenty_years_historical_data(context):
    assert "2001-10-01" in list(context.response.json()['Time Series (Daily)'])


@then('csv file is downloaded')
def csv_file_is_downloaded(context):
    url_content = context.response.content
    csv_file = open(get_config()['API']['csvfilename'], 'wb')
    csv_file.write(url_content)
    csv_file.close()

    assert path.exists(get_config()['API']['csvfilename'])


@then('ensure all columns are displayed in file')
def some_info_available_in_file(context):
    columnnames = ["timestamp", "open", "high", "low", "close", "volume"]
    with open(get_config()['API']['csvfilename']) as file:
        content = file.read()
        for columns in columnnames:
            assert content.__contains__(columns)
