#!/usr/bin/python

#username
username=<username>
password=<password>
number=<number here>
msg=<message here>


import time
import pygvoicelib

#try:
#    input = raw_input
#except NameError:
#    input = input

def run_test(user, passwd, call_number):
    voice = pygvoicelib.GoogleVoice(user, passwd)

    try:
        phone_list = voice.get_numbers()
    except pygvoicelib.LoginError, e:
        print 'Failed to login. Reason: %s' % (e.reason)
        print 'Reasons Legend:'
        print '  failed -> Invalid credentails'
        print '  captcha -> Account is captcha locked'
        print '  error -> Unknown/Other errors'
        return

    from_num = ''
    for num in phone_list:
        if num.isdigit() and phone_list[num]['verified']:
            from_num = num
    print 'Login successful.'
    if not from_num:
        print 'Unable to find a validated phone to test a call with. Aborting the test ...'
        return
    #print 'Testing sms. Result -> ' + repr(voice.call('+' + call_number,'+'+from_num))
    print 'Testing sms. Result -> ' + repr(voice.sms('+' + call_number,'meh'))
    print 'sent'
    #print 'Sleeping 30 seconds ...'
    #time.sleep(30)
    #print 'Testing a cancel. Result -> ' + repr(voice.cancel())
    #print 'Note: Results returned by google might not be that reliable'
    #print
    #print 'Here is the state that can be saved in DB or somewhere else: ' + repr(voice.get_state())
    #print
    #print 'Now we will save the state and load it from scratch to test'
    #state = voice.get_state()
    #voice = pygvoicelib.GoogleVoice(*state)
    #try:
    #    phone_list = voice.get_numbers()
    #except pygvoicelib.LoginError, e:
    #    print 'Failed to login. Reason: %s' % (e.reason)
    #    return
    #except pygvoicelib.ServerError, e:
    #    print 'Google server error. Reason: %s' % (e.reason)
    #    return
    #print 'Test all successful. We are AWESOME!'

if __name__ == '__main__':
    run_test(username, password, number)
