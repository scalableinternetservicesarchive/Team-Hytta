======================
FunkLoad_ bench report
======================


:date: 2014-11-25 12:24:41
:abstract: XXX the TestCase class description
           Bench result of ``BasicSignup.test_basic_signUp``: 
           XXX the test case description

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents
.. |APDEXT| replace:: \ :sub:`1.5`

Bench configuration
-------------------

* Launched: 2014-11-25 12:24:41
* From: marianne-VirtualBox
* Test: ``test_BasicSignup.py BasicSignup.test_basic_signUp``
* Target server: http://images.techtimes.com
* Cycles of concurrent users: [1, 2, 3]
* Cycle duration: 30s
* Sleeptime between request: from 0.0s to 2.0s
* Sleeptime between test case: 1.0s
* Startup delay between thread: 0.2s
* Apdex: |APDEXT|
* FunkLoad_ version: 1.16.1


Bench content
-------------

The test ``BasicSignup.test_basic_signUp`` contains: 

* 1 page(s)
* 0 redirect(s)
* 0 link(s)
* 0 image(s)
* 0 XML RPC call(s)

The bench contains:

* 77 tests
* 74 pages
* 74 requests


Test stats
----------

The number of Successful **Tests** Per Second (STPS) over Concurrent Users (CUs).

 .. image:: tests.png

 ================== ================== ================== ================== ==================
                CUs               STPS              TOTAL            SUCCESS              ERROR
 ================== ================== ================== ================== ==================
                  1              0.400                 12                 12             0.00%
                  2              0.867                 26                 26             0.00%
                  3              1.300                 39                 39             0.00%
 ================== ================== ================== ================== ==================



Page stats
----------

The number of Successful **Pages** Per Second (SPPS) over Concurrent Users (CUs).
Note that an XML RPC call count like a page.

 .. image:: pages_spps.png
 .. image:: pages.png

 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                CUs             Apdex*             Rating               SPPS            maxSPPS              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                  1              0.958          Excellent              0.400              1.000                 12                 12             0.00%              0.107              0.556              5.136              0.118              0.137              0.233              5.136
                  2              1.000          Excellent              0.867              2.000                 26                 26             0.00%              0.119              0.254              0.539              0.132              0.228              0.480              0.489
                  3              1.000          Excellent              1.200              3.000                 36                 36             0.00%              0.105              0.305              0.642              0.114              0.326              0.586              0.632
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

 \* Apdex |APDEXT|

Request stats
-------------

The number of **Requests** Per Second (RPS) successful or not over Concurrent Users (CUs).

 .. image:: requests_rps.png
 .. image:: requests.png

 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                CUs             Apdex*            Rating*                RPS             maxRPS              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                  1              0.958          Excellent              0.400              1.000                 12                 12             0.00%              0.107              0.556              5.136              0.118              0.137              0.233              5.136
                  2              1.000          Excellent              0.867              2.000                 26                 26             0.00%              0.119              0.254              0.539              0.132              0.228              0.480              0.489
                  3              1.000          Excellent              1.200              3.000                 36                 36             0.00%              0.105              0.305              0.642              0.114              0.326              0.586              0.632
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

 \* Apdex |APDEXT|

Slowest requests
----------------

The 5 slowest average response time during the best cycle with **3** CUs:

* In page 001, Apdex rating: Excellent, avg response time: 0.31s, get: ``/data/images/full/4061/bill-gates-wealthiest-person.jpg?w=600``
  `Get /data/images/full/4...althiest-person.jpg`

Page detail stats
-----------------


PAGE 001: Get /data/images/full/4...althiest-person.jpg
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url ``/data/images/full/4061/bill-gates-wealthiest-person.jpg?w=600``

     .. image:: request_001.001.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                      1              0.958          Excellent                 12                 12             0.00%              0.107              0.556              5.136              0.118              0.137              0.233              5.136
                      2              1.000          Excellent                 26                 26             0.00%              0.119              0.254              0.539              0.132              0.228              0.480              0.489
                      3              1.000          Excellent                 36                 36             0.00%              0.105              0.305              0.642              0.114              0.326              0.586              0.632
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|

Definitions
-----------

* CUs: Concurrent users or number of concurrent threads executing tests.
* Request: a single GET/POST/redirect/xmlrpc request.
* Page: a request with redirects and resource links (image, css, js) for an html page.
* STPS: Successful tests per second.
* SPPS: Successful pages per second.
* RPS: Requests per second, successful or not.
* maxSPPS: Maximum SPPS during the cycle.
* maxRPS: Maximum RPS during the cycle.
* MIN: Minimum response time for a page or request.
* AVG: Average response time for a page or request.
* MAX: Maximmum response time for a page or request.
* P10: 10th percentile, response time where 10 percent of pages or requests are delivered.
* MED: Median or 50th percentile, response time where half of pages or requests are delivered.
* P90: 90th percentile, response time where 90 percent of pages or requests are delivered.
* P95: 95th percentile, response time where 95 percent of pages or requests are delivered.
* Apdex T: Application Performance Index, 
  this is a numerical measure of user satisfaction, it is based
  on three zones of application responsiveness:

  - Satisfied: The user is fully productive. This represents the
    time value (T seconds) below which users are not impeded by
    application response time.

  - Tolerating: The user notices performance lagging within
    responses greater than T, but continues the process.

  - Frustrated: Performance with a response time greater than 4*T
    seconds is unacceptable, and users may abandon the process.

    By default T is set to 1.5s this means that response time between 0
    and 1.5s the user is fully productive, between 1.5 and 6s the
    responsivness is tolerating and above 6s the user is frustrated.

    The Apdex score converts many measurements into one number on a
    uniform scale of 0-to-1 (0 = no users satisfied, 1 = all users
    satisfied).

    Visit http://www.apdex.org/ for more information.
* Rating: To ease interpretation the Apdex
  score is also represented as a rating:

  - U for UNACCEPTABLE represented in gray for a score between 0 and 0.5 

  - P for POOR represented in red for a score between 0.5 and 0.7

  - F for FAIR represented in yellow for a score between 0.7 and 0.85

  - G for Good represented in green for a score between 0.85 and 0.94

  - E for Excellent represented in blue for a score between 0.94 and 1.

Report generated with FunkLoad_ 1.16.1, more information available on the `FunkLoad site <http://funkload.nuxeo.org/#benching>`_.