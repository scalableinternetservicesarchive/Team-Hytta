======================
FunkLoad_ bench report
======================


:date: 2014-12-13 22:21:14
:abstract: Simple demo
           Bench result of ``Simple.test_createCabin``: 
           No test description

.. _FunkLoad: http://funkload.nuxeo.org/
.. sectnum::    :depth: 2
.. contents:: Table of contents
.. |APDEXT| replace:: \ :sub:`1.5`

Bench configuration
-------------------

* Launched: 2014-12-13 22:21:14
* From: Mariannes-MacBook-Pro.local
* Test: ``test_simple.py Simple.test_createCabin``
* Target server: http://ec2-54-149-146-62.us-west-2.compute.amazonaws.com
* Cycles of concurrent users: [10, 20, 30]
* Cycle duration: 10s
* Sleeptime between request: from 0.0s to 0.5s
* Sleeptime between test case: 0.01s
* Startup delay between thread: 0.01s
* Apdex: |APDEXT|
* FunkLoad_ version: 1.16.1


Test stats
----------

The number of Successful **Tests** Per Second (STPS) over Concurrent Users (CUs).

Sorry no test have finished during a cycle, the cycle duration is too short.


Page stats
----------

The number of Successful **Pages** Per Second (SPPS) over Concurrent Users (CUs).
Note that an XML RPC call count like a page.

 .. image:: pages_spps.png
 .. image:: pages.png

 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                CUs             Apdex*             Rating               SPPS            maxSPPS              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                 10              0.864               Good              3.000             10.000                 30                 30             0.00%              0.675              2.595              6.571              0.893              1.817              4.744              6.523
                 20              0.655               POOR              2.400             18.000                 24                 24             0.00%              1.779              6.292              9.074              2.625              6.966              8.908              9.042
                 30              0.769               FAIR              7.300             18.000                 73                 73             0.00%              0.823              2.516              8.262              1.267              2.502              3.614              4.335
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
                 10              0.864               Good              5.500             16.000                 55                 55             0.00%              0.176              1.415              4.882              0.345              0.920              3.702              3.808
                 20              0.661               POOR              5.900             41.000                 59                 59             0.00%              0.211              2.746              8.300              0.306              1.266              7.274              7.524
                 30              0.810               FAIR             13.400             65.000                134                134             0.00%              0.203              1.522              5.221              0.240              1.254              3.289              3.572
 ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

 \* Apdex |APDEXT|

Slowest requests
----------------

The 5 slowest average response time during the best cycle with **10** CUs:

* In page 001, Apdex rating: POOR, avg response time: 2.71s, link: ``/bootstrap/3.2.0/css/bootstrap.min.css``
  ``
* In page 002, Apdex rating: POOR, avg response time: 2.43s, image: ``/data/images/full/4061/bill-gates-wealthiest-person.jpg?w=600``
  ``
* In page 003, Apdex rating: POOR, avg response time: 1.61s, image: ``/wp-content/uploads/2014/09/Beach-Cottage-in-Florida-200x200.jpg``
  ``
* In page 002, Apdex rating: Excellent, avg response time: 1.35s, post: ``/users``
  `Create New User`
* In page 001, Apdex rating: Good, avg response time: 1.24s, get: ``/users/sign_up``
  `View the sign in page`

Page detail stats
-----------------


PAGE 001: View the sign in page
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url ``/users/sign_up``

     .. image:: request_001.001.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                     10              0.900               Good                 10                 10             0.00%              0.176              1.237              4.882              0.281              0.390              4.882              4.882
                     20              0.889               Good                 18                 18             0.00%              0.211              1.271              8.300              0.257              0.395              4.593              8.300
                     30              1.000          Excellent                 16                 16             0.00%              0.216              0.288              0.399              0.229              0.275              0.356              0.399
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|
* Req: 002, link, url ``/assets/application-500a35ad55c8b3922bcf5e47c6b912b7.css``

     .. image:: request_001.002.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                     10              1.000          Excellent                 10                 10             0.00%              0.345              0.529              0.584              0.483              0.555              0.584              0.584
                     20              0.947          Excellent                 19                 19             0.00%              0.302              0.919              3.633              0.306              0.434              3.630              3.633
                     30              0.933               Good                 30                 30             0.00%              0.203              0.839              5.221              0.225              0.298              3.301              3.388
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|
* Req: 003, link, url ``/bootstrap/3.2.0/css/bootstrap.min.css``

     .. image:: request_001.003.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                     10              0.650               POOR                 10                 10             0.00%              0.983              2.714              3.808              1.066              3.338              3.808              3.808
                     20              0.125       UNACCEPTABLE                 16                 16             0.00%              4.986              6.495              7.699              5.190              6.891              7.524              7.699
                     30              0.883               Good                 30                 30             0.00%              0.247              1.246              2.642              0.614              1.156              2.068              2.227
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|

PAGE 002: Create New User
~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, post, url ``/users``

     .. image:: request_002.001.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                     10              0.950          Excellent                 10                 10             0.00%              0.887              1.346              3.163              0.938              1.202              3.163              3.163
                     20              0.500               POOR                  6                  6             0.00%              2.448              2.956              3.490              2.448              3.077              3.490              3.490
                     30              0.672               POOR                 29                 29             0.00%              1.129              2.314              3.632              1.326              2.432              3.580              3.614
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|
* Req: 002, get, url ``/``

     .. image:: request_002.002.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                     10              0.944          Excellent                  9                  9             0.00%              0.241              0.816              1.817              0.241              0.798              1.817              1.817
                     30              0.648               POOR                 27                 27             0.00%              0.823              2.377              4.335              0.960              2.615              3.381              4.330
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|
* Req: 003, image, url ``/data/images/full/4061/bill-gates-wealthiest-person.jpg?w=600``

     .. image:: request_002.003.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                     10              0.625               POOR                  4                  4             0.00%              0.791              2.428              3.206              0.791              3.040              3.206              3.206
                     30              0.500               POOR                  1                  1             0.00%              2.658              2.658              2.658              2.658              2.658              2.658              2.658
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|

PAGE 003: View the all-cabin page
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Req: 001, get, url ``/cabins``

     .. image:: request_003.001.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                     10              1.000          Excellent                  1                  1             0.00%              0.920              0.920              0.920              0.920              0.920              0.920              0.920
                     30              0.500               POOR                  1                  1             0.00%              2.855              2.855              2.855              2.855              2.855              2.855              2.855
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================

     \* Apdex |APDEXT|
* Req: 002, image, url ``/wp-content/uploads/2014/09/Beach-Cottage-in-Florida-200x200.jpg``

     .. image:: request_003.002.png

     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                    CUs             Apdex*             Rating              TOTAL            SUCCESS              ERROR                MIN                AVG                MAX                P10                MED                P90                P95
     ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ================== ==================
                     10              0.500               POOR                  1                  1             0.00%              1.606              1.606              1.606              1.606              1.606              1.606              1.606
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