Demo application to test Websockets+Flask+Gunicorn+Nginx on Docker
==================================================================

Minimal Flask/Websockets application to test deployment under different
configurations.

    # Run standalone on port 5000
    $ ./runserver.py

    # Run on Gunicorn on port 8001
    $ POLICY_SERVER=false gunicorn runserver:app -b :8001 -w 1 --worker-class socketio.sgunicorn.GeventSocketIOWorker --error-logfile /dev/stdout --access-logfile /dev/stdout

    # Run on Docker or port 80 (needs to be available: stop other webservers!)
    $ cd docker
    $ docker-compose build
    $ docker-compose up -d
    # Containers logs go to host's syslog. On Debian/Ubuntu do:
    $ tail -f /var/log/syslog
