# -*- coding: utf-8 -*-
import logging
import inspect
import traceback




class Log (object):

    myParameters = {
        # List with a +
        '(+)': '<G>-B- + <->'
    }

    '''
    <...> = text color
    <<...>> = highlight color
    <D...> = dark color version
    '''
    parameters = {
        # End
        '<->': '\033[0m',


        # Bold
        '-B-': '\033[1m',
        # Underline
        '-U-': '\033[4m',


        # White
        '<W>': '\033[37m',
        # Violet
        '<V>': '\033[95m',
        # Cyan
        '<C>': '\033[96m',
        '<DC>': '\033[36m',
        # Pink
        '<P>': '\x1b[35m',
        # Blue
        '<B>': '\033[94m',
        # Green
        '<G>': '\033[92m',
        '<<G>>': '\x1b[6;30;42m',
        # Yellow
        '<Y>': '\033[93m',
        '<<Y>>': '\x1b[5;33;43m',
        '<<DY>>': '\x1b[1;33;43m',
        # Red
        '<R>': '\033[91m'
    }


    # Log information
    '''
    - stack_trace[:-1][-1].split(', ', 2)[:-1] for give informayions about log
    (return a message with File and Line about the log)
    '''
    @staticmethod
    def dataLog(infos):
        return Log.style('\n<Y> ' +
                         "- " + infos[0].replace(" ", "") + "\n " +
                         "- " + infos[1] + "\n")


    # Stylized the message
    @staticmethod
    def style(message):
        message += "<->"
        for key, value in Log.myParameters.items():
            message = message.replace(key, value)

        for key, value in Log.parameters.items():
            message = message.replace(key, value)

        return message


    # Dev message (print improved)
    @staticmethod
    def dev(message, boolDataLog=False):
        frame = inspect.currentframe()
        stack_trace = traceback.format_stack(frame)
        infos = stack_trace[:-1][-1].split(', ', 2)[:-1]

        print Log.style(message) if not boolDataLog else Log.style(message) + Log.dataLog(infos)


    # Warning message
    '''
    (YELLOW & log informations)
    '''
    @staticmethod
    def warning(message):
        frame = inspect.currentframe()
        stack_trace = traceback.format_stack(frame)
        infos = stack_trace[:-1][-1].split(', ', 2)[:-1]

        logging.warning(Log.style('<Y>' + str(message)) + Log.dataLog(infos))



    # Error message
    '''
    (RED & )log informations
    '''
    @staticmethod
    def error(message):
        frame = inspect.currentframe()
        stack_trace = traceback.format_stack(frame)
        infos = stack_trace[:-1][-1].split(', ', 2)[:-1]

        logging.error(Log.style('<R>' + str(message)) + Log.dataLog(infos))



    # BDD log
    '''
    - message level (dev, warning or error)
    '''
    @staticmethod
    def bdd(level, message):
        getattr(Log, level)("   <<DY>><B>-B-BDD:<-> " + message + "\n")


    # End log
    '''
   (log informations)
   '''
    @staticmethod
    def end():
        frame = inspect.currentframe()
        stack_trace = traceback.format_stack(frame)
        infos = stack_trace[:-1][-1].split(', ', 2)[:-1]

        print Log.style("\n\n -B-<R> <<<<<<<<<<<<<<<< END >>>>>>>>>>>>>>>> <-> \n\n") + Log.dataLog(infos)
