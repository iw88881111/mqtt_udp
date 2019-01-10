import configparser
import logging
import re


# ------------------------------------------------------------------------
#
# Log
#
# ------------------------------------------------------------------------


log = logging.getLogger("mqtt-udp")
#logger.setLevel(logging.ERROR)

# First to stdout

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stdout_handler.setFormatter(formatter)
log.addHandler(stdout_handler)

# ------------------------------------------------------------------------
#
# Config
#
# ------------------------------------------------------------------------


config = configparser.ConfigParser()


config['DEFAULT'] = {
    'logfile' : '',     # no log file by default
    'verbose' : True    # debug mode, application will chat a lot
    }


config['openhab-gate'] = {
    'port': "8080",
    'blacklist' : '^\\$',   # regexp: prevent matching topics to come through, match on MQTT/UDP side
    'sitemap'	: 'default'
    }

config['mqtt-gate'] = {
#    'host': 'smart.',
    'port': 1883,
    'subscribe': '#',
#    'convertfrom': '',  # regexp to convert topic from mqtt to UDP
#    'convertfrom': '',  # regexp to convert topic from mqtt to UDP
#    'convertto': '',    # regexp to convert topic from UDP to mqtt
#    'convertto': '',    # regexp to convert topic from UDP to mqtt
    'blacklist' : '^\\$'   # regexp: prevent matching topics to come through, match on MQTT/UDP side
    }

config.read('mqtt-udp.ini')


#for key in config['mqtt-gate']:  
#    print(key)
def dump():
    for sec in config:  
        print( '['+ sec + ']' )
        for key in config[sec]:
            print( '\t' + key + "=" + config[sec][key] )


caller_group = ''

# Set config file group, also turn logging to file on, if set in conf

def set_group(group):
    global caller_group
    caller_group = group

    log_file = get("logfile");
    if len(log_file) > 0:

        fh = logging.FileHandler(log_file)
     
        formatter = logging.Formatter('%(asctime)s  %(levelname)s:%(name)s  %(message)s')
        fh.setFormatter(formatter)
        
        # add handler to logger object
        log.addHandler(fh)
        
        verbose = getboolean('verbose' )
        if verbose:
            fh.setLevel(logging.INFO)
    
        log.info("Started: "+group)

        log.removeHandler(stdout_handler)

def setGroup(group):
    set_group(group):






def get(item):
    global caller_group
    return config.get( caller_group, item )

def getboolean(item):
    #global caller_group
    return config.getboolean( caller_group, item )

def getint(item):
    return config.getint( caller_group, item )

def getfloat(item):
    return config.getfloat( caller_group, item )



def check_black_list(topic,blacklist):
    ''' Check for topic to be in black list regular expression '''
    #print(topic,blacklist)
    return (len(blacklist) > 0) and (re.match( blacklist, topic ))



