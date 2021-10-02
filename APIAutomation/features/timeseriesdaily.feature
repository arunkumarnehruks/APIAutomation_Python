Feature: Verify get request is working as expected

  Scenario: Verify response of Time Series (Daily) get request with only all mandatory query parameters
    Given given time series url with required params
    When hit url without optional params
    Then response is seen with status code as 200
    And Meta data information has 5 items
    And 100 points are only returned
    And response is in JSON format
    And every entry in Time Series (Daily) has 5 items
    And ensure Content-Type header value is displayed as application/json

  Scenario Outline: Verify response of Time Series (Daily) get request with all optional query parameters with default values
    Given given time series url with required params
    When hit url with all optional params with symbol value as <symbol_value>
    Then response is seen with status code as 200
    And Meta data information has 5 items
    And Meta data has 2. Symbol value is same as <symbol_value> provided in query param
    And 100 points are only returned
    And response is in JSON format
    And every entry in Time Series (Daily) has 5 items
    Examples:
      | symbol_value |
      | IBM          |
      | TSCO.LON     |

  Scenario: Verify response of Time Series (Daily) get request with partial optional query parameters i.e. datatype is missing
    Given given time series url with required params
    When hit url with partial optional params (without datatype parameter)
    Then response is seen with status code as 200
    And 100 points are only returned
    And response is in JSON format

  Scenario: Verify response of Time Series (Daily) get request when outputsize is full
    Given given time series url with required params
    When hit url with with outputsize as full
    Then response is seen with status code as 200
    And Meta data has 4. Output Size value as Full Size
    And 20+ years of historical data are returned
    And response is in JSON format
    And every entry in Time Series (Daily) has 5 items

  Scenario: Verify response of Time Series (Daily) get request when datatype is csv
    Given given time series url with required params
    When hit url with with datatype as csv
    Then response is seen with status code as 200
    And csv file is downloaded
    And ensure all columns are displayed in file

  Scenario: Negative test case - Verify response of Time Series (Daily) get request when no key is provided
    Given given time series url with required params
    When hit url without key
    Then reponse should display error