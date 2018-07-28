import python3_gearman
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

CONNECTION_STRING = '%s:%s' % (config['CORE']['GEARMAN_SERVER_HOST'], config['CORE']['GEARMAN_SERVER_PORT'])
print(CONNECTION_STRING)
gm_worker = python3_gearman.GearmanWorker([CONNECTION_STRING])

# See python3_gearman.job.py to see attributes on the GearmanJob
# Send back a reversed version of the 'data' string
def task_listener_reverse(gearman_worker, gearman_job):
    return gearman_job.data[::-1]

# gm_worker.set_client_id is optional
gm_worker.set_client_id('plabs_reverse_string_py3')
gm_worker.register_task('reverse', task_listener_reverse)

# Enter our work loop and call gm_worker.after_poll() after each time we timeout/see socket activity
gm_worker.work()
