#!/usr/local/bin/python2.7

"""

00

"""

from subprocess import Popen, PIPE
import requests
import json
import datetime


def ast_com(command):
    com = "/usr/sbin/asterisk -x \"{}\"".format(command)
    return Popen(com, shell=True, stdin=PIPE, stdout=PIPE).stdout.read().split()


def core_show(chan):
    #res = ast_com('core show channel ' + chan)
    res = ['--', 'General', '--', 'Name:', 'SIP/258-000c589a', 'Type:', 'SIP', 'UniqueID:', '1525691887.904025', 'LinkedID:', '1525691887.904025', 'Caller', 'ID:', '258', 'Caller', 'ID', 'Name:', '258', 'Connected', 'Line', 'ID:', '295', 'Connected', 'Line', 'ID', 'Name:', '295', 'Eff.', 'Connected', 'Line', 'ID:', '295', 'Eff.', 'Connected', 'Line', 'ID', 'Name:', '295', 'DNID', 'Digits:', '295', 'Language:', 'ru', 'State:', 'Up', '(6)', 'Rings:', '0', 'NativeFormats:', '(alaw)', 'WriteFormat:', 'alaw', 'ReadFormat:', 'alaw', 'WriteTranscode:', 'No', 'ReadTranscode:', 'No', '1st', 'File', 'Descriptor:', '51', 'Frames', 'in:', '3232', 'Frames', 'out:', '3244', 'Time', 'to', 'Hangup:', '0', 'Elapsed', 'Time:', '0h1m8s', 'Direct', 'Bridge:', 'SIP/295-000c589b', 'Indirect', 'Bridge:', 'SIP/295-000c589b', '--', 'PBX', '--', 'Context:', 'macro-dial-one', 'Extension:', 's', 'Priority:', '42', 'Call', 'Group:', '0', 'Pickup', 'Group:', '0', 'Application:', 'Dial', 'Data:', 'SIP/295,,trWwI', 'Blocking', 'in:', 'ast_waitfor_nandfds', 'Call', 'Identifer:', '[C-0005cc49]', 'Variables:', 'BRIDGEPVTCALLID=7a7c24e91f63ff2e2f6fa96e7fd29f02@10.126.16.20:5060', 'BRIDGEPEER=SIP/295-000c589b', 'DIALEDPEERNUMBER=295', 'DIALEDPEERNAME=SIP/295-000c589b', 'DIALSTATUS=ANSWER', 'DIALEDTIME=', 'ANSWEREDTIME=', 'MACRO_DEPTH=2', 'D_OPTIONS=trWwI', 'DB_RESULT=295', 'KEEPCID=TRUE', 'CWIGNORE=', 'GOSUB_RETVAL=', 'DSTRING=SIP/295', 'ITER=2', 'THISDIAL=SIP/295', 'ITER2=2', 'NEWDIAL=SIP/295&', 'THISPART2=SIP/295', 'LOOPCNT2=1', 'LOOPCNT=1', 'DEVICES=295', 'EXTHASCW=', 'DIALSTATUS_CW=', 'DEXTEN=295', 'ARG3=295', 'ARG2=trWw', 'ARG1=', 'MACRO_PRIORITY=7', 'MACRO_CONTEXT=macro-exten-vm', 'MACRO_EXTEN=s', 'REC_STATUS=RECORDING', 'MIXMONITOR_FILENAME=/var/spool/asterisk/monitor/2018/05/07/exten-295-258-20180507-151807-1525691887.904025.wav', 'REC_POLICY_MODE=always', 'CALLFILENAME=exten-295-258-20180507-151807-1525691887.904025', 'FROMEXTEN=258', 'TIMESTR=20180507-151807', 'YEAR=2018', 'MONTH=05', 'DAY=07', 'NOW=1525691887', 'MON_FMT=wav', 'REC_POLICY_MODE_SAVE=', 'RT=', 'PICKUPMARK=295', 'EXTTOCALL=295', 'RingGroupMethod=none', 'TTL=64', 'DIAL_OPTIONS=trWw', 'AMPUSERCID=258', 'AMPUSERCIDNAME=258', 'AMPUSER=258', 'REALCALLERIDNUM=258', 'TOUCH_MONITOR=1525691887.904025', 'ARG5=0', 'ARG4=0', 'RINGTIMER=15', 'SIPCALLID=437a016b-ef5a7c22eefb5e1105940080f0808080@KX-HDV100RU', 'SIPDOMAIN=10.126.16.20', 'SIPURI=sip:258@10.126.21.133:5060', 'CDR', 'Variables:', 'level', '1:', 'dnid=295', 'level', '1:', 'recordingfile=exten-295-258-20180507-151807-1525691887.904025.wav', 'level', '1:', 'cnam=258', 'level', '1:', 'cnum=258', 'level', '1:', 'clid="258"', '<258>', 'level', '1:', 'src=258', 'level', '1:', 'dst=295', 'level', '1:', 'dcontext=from-internal', 'level', '1:', 'channel=SIP/258-000c589a', 'level', '1:', 'dstchannel=SIP/295-000c589b', 'level', '1:', 'lastapp=Dial', 'level', '1:', 'lastdata=SIP/295,,trWwI', 'level', '1:', 'start=2018-05-07', '15:18:07', 'level', '1:', 'answer=2018-05-07', '15:18:10', 'level', '1:', 'duration=1568', 'level', '1:', 'billsec=64', 'level', '1:', 'disposition=ANSWERED', 'level', '1:', 'amaflags=DOCUMENTATION', 'level', '1:', 'uniqueid=1525691887.904025', 'level', '1:', 'linkedid=1525691887.904025', 'level', '1:', 'sequence=1177841']
    for i in res:
        if i[0:9] == 'duration=':
            if int(i[9:])>1500:
                return True


class Alert:
    def __init__(self):
        log = ""
        text = ""

    def logging(self, log):
        log_file = open("hangupallchan.log", "a")
        text = str(datetime.datetime.now()) + " " + log + "\n"
        log_file.write(text)
        log_file.close()

    def webhook(self, text):
        url = 'http://10.126.21.42:3000/hooks/hRjhvdsCxtQu6XLuK/agDtz4zWvFNvEp7bAxugksTq2MNicNjGmmKSNyhoGNQiPoXB'
        payload = {'text': text}
        r = requests.post(url, data=json.dumps(payload))


com = "group show channels"
#channels = ast_com(com)
channels = ["Channel", "Group", "Category", "SIP/911-00048e96", "xxx", "xxx", "SIP/914-00048ca6", "yyy", "yyy", "SIP/912-00048e4a", "zzz", "zzz", 3, "active", "channels"]
al = Alert()

if len(channels) < 7:
    al.logging("No channels is active!")
else:
    active_chan = int((len(channels) - 6) / 3)
    if active_chan > 1:
        i = active_chan
        sip_9xx = []
        al.logging("Active channels is: " + str(active_chan))
        while active_chan > 0:
            n = 3 * active_chan
            sip_chan = str(channels[n])
            if sip_chan[0:5] == "SIP/9":
                sip_9xx.append(channels[n])
                active_chan -= 1
        counter = len(sip_9xx)
        if counter == 0:
            al.logging("Channels is not locked!")
        else:
            for x in sip_9xx:
                if core_show(x):
                    ast_com("channel request hangup " + x)

    else:
        al.logging("One channel is active!")

