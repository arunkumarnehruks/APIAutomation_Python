# Instructions to execute API tests for TIME_SERIES_DAILY
***
**Prerequitisites needed**
* Install Python
* After installing python, add couple of environment path variables (1. until python installation folder and 2. is until scripts in installation folder)
* Confirm python is installed as expected with this command,

  `python --version`

* Install IDE pycharm
* Install requirements.txt using below command,

  `pip install -r requirements.txt`
  This will install all different libraries that are used in the project
* Once requirements are installed, open pycharm and ensure to use right Python interpreter by checking the python.exe folder location it is pointing to. when it points to right one, we can see all libraries we have installed through requirements.txt



  
**To run Tests**
* To run the test, you can use any of the below commands in pycharm terminal,
  
  `behave features/timeseriesdaily.feature`

  `behave features`

* To run tests without any explicit report generated, then use below command,
    
    `behave features`
* To run tests with Allure report, then use below command, 
    
    `behave features/timeseriesdaily.feature --no-capture -f allure_behave.formatter:AllureFormatter -o timeseriesdaily_allure_report`
  * This report will not have request and response logged in the report whereas it will display different metrics

* To run tests with junit report, then use below command,

  `behave features/timeseriesdaily.feature --no-capture --junit`
  * This report will not have all metrics captured but the request and response will be available in the report

**To view different generated Reports**
* If you would like to view the report generated by Allure then run below command (you need to update location to point to the right one in below command),

  `allure serve APIAutomation\timeseriesdaily_allure_report`
  * This will open report in browser
  
* If you would like to view the report generated by junit then run the below command,

  `junit2html reports/TESTS-timeseriesdaily.xml reports/timeseriesdaily_html_report.html`
  * Report will be generated in html format and available in reports folder. We can now use any browser to view the report




