# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import sys


class StandardOut(object):
    """ custom output for progress reporting """
    def __init__(self, out=None):
        self.out = out or sys.stdout
        self.total_val = None

    def start(self, message, total_value):
        """ start reporting progress """
        self.out.write(message)
        self.total_val = total_value

    def write(self, message, value, total_value):
        """ writes the progress """
        if value and total_value:
            self.out.write(self._format_value(value, total_value) + "\n")
        self.out.write(message + '\n')

    def _format_value(self, val, total_val):
        percent = val / total_val
        bar_len = 100
        completed = int(bar_len*percent)

        message = '\r['
        for i in range(bar_len):
            if i < completed:
                message += '#'
            else:
                message += ' '
        message += ']  {:.4%}'.format(percent)
        return message

    def flush(self):
        """ flushes the message"""
        self.out.flush()

    def end(self, message=''):
        """ stop reporting progress """
        self.out.write('Finished{}'.format(message))


class ProgressReporter(object):
    """ generic progress reporter """
    def __init__(self, transform_progress=None, out=sys.stdout):
        self.message = ''
        self.curr_val = None
        self.total_val = None
        self.tranform_progress = transform_progress
        self.out = out

    def add(self, message='', value=None):
        """ adds a progress report """
        if value:
            self.curr_val = value
        self.message = message

    def report(self):
        """ report the progress """
        progress = None
        if self.curr_val and self.total_val:
            percent = self.curr_val / self.total_val

            bar_len = 100
            completed = int(bar_len*percent)
            if self.tranform_progress and callable(self.tranform_progress):
                progress = self.tranform_progress(completed, bar_len)

        return progress, self.message


class LongRunningOperation(object):  # pylint: disable=too-few-public-methods

    def __init__(self, start_msg='', finish_msg='',
                 poller_done_interval_ms=1000.0, out=None, total_val=None):
        self.start_msg = start_msg
        self.finish_msg = finish_msg
        self.poller_done_interval_ms = poller_done_interval_ms
        from azclishell.app import ProgressView
        self.out = out or ProgressView()
        self.curr_message = 'Running'
        self.curr_val = None
        self.total_val = total_val

    def add(self, curr_val, total_val, label):
        """ add a progress report """
        self.curr_message = label
        self.curr_val = curr_val
        self.total_val = total_val

    def _delay(self):
        time.sleep(self.poller_done_interval_ms / 1000.0)

    def __call__(self, poller):
        from msrest.exceptions import ClientException
        logger.info("Starting long running operation '%s'", self.start_msg)
        correlation_message = ''
        while not poller.done():
            self.out.write(self.curr_message + '\n', self.curr_val, self.total_val)
            self.out.flush()
            try:
                # pylint: disable=protected-access
                correlation_id = json.loads(
                    poller._response.__dict__['_content'])['properties']['correlationId']

                correlation_message = 'Correlation ID: {}'.format(correlation_id)
            except:  # pylint: disable=bare-except
                pass

            try:
                self._delay()
            except KeyboardInterrupt:
                logger.error('Long running operation wait cancelled.  %s', correlation_message)
                raise

        try:
            result = poller.result()

        except ClientException as client_exception:
            telemetry.set_exception(
                client_exception,
                fault_type='failed-long-running-operation',
                summary='Unexpected client exception in {}.'.format(LongRunningOperation.__name__))
            message = getattr(client_exception, 'message', client_exception)

            try:
                message = '{} {}'.format(
                    str(message),
                    json.loads(client_exception.response.text)['error']['details'][0]['message'])
            except:  # pylint: disable=bare-except
                pass

            cli_error = CLIError('{}  {}'.format(message, correlation_message))
            # capture response for downstream commands (webapp) to dig out more details
            setattr(cli_error, 'response', getattr(client_exception, 'response', None))
            raise cli_error

        logger.info("Long running operation '%s' completed with result %s",
                    self.start_msg, result)
        self.out.end("\n")
        self.out.flush()
        return result
