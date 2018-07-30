# plabs-gearman-workers
### Worker LIST
- Reverse String
  - reverse_string_py3.py
    - Reverse String
    - Python 3

Configuration
~~~~~~~~~~~~~

    $ mkdir workdir
    $ cd workdir
    $ git clone https://github.com/prabhatmaurya/plabs-gearman-workers.git
    $ cd plabs-gearman-workers
    $ cp config.ini.example config.ini
    $ vi config.ini
    $ docker build -t reverse_string_py3:1 .
    $ docker run reverse_string_py3:1  
~~~~~~~~~~~~~
