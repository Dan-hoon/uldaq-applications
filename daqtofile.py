
from __future__ import print_function
from time import sleep
from os import system
from sys import stdout
import pandas as pd

from uldaq import (get_daq_device_inventory, DaqDevice, AInScanFlag, ScanStatus,
                   ScanOption, create_float_buffer, InterfaceType, AiInputMode)

import numpy as np

daq_device = None
ai_device = None
status = ScanStatus.IDLE

range_index = 0
interface_type = InterfaceType.ANY
low_channel = 0
high_channel = 0
samples_per_channel = 22000
rate = 20000
scan_options = ScanOption.CONTINUOUS
flags = AInScanFlag.DEFAULT

dataAsList=[]
timeAsList=[]


def display_scan_options(bit_mask):
    """Create a displays string for all scan options."""
    options = []
    if bit_mask == ScanOption.DEFAULTIO:
        options.append(ScanOption.DEFAULTIO.name)
    for option in ScanOption:
        if option & bit_mask:
            options.append(option.name)
    return ', '.join(options)

def reset_cursor():
    """Reset the cursor in the terminal window."""
    stdout.write('\033[1;1H')


def clear_eol():
    """Clear all characters to the end of the line."""
    stdout.write('\x1b[2K')

def findDevice():
    global daq_device
    global ai_info
    global ai_device

    # Get descriptors for all of the available DAQ devices.
    devices = get_daq_device_inventory(interface_type)
    number_of_devices = len(devices)
    if number_of_devices == 0:
        raise RuntimeError('Error: No DAQ devices found')

    print('Found', number_of_devices, 'DAQ device(s):')
    for i in range(number_of_devices):
        print('  [', i, '] ', devices[i].product_name, ' (',
              devices[i].unique_id, ')', sep='')

    descriptor_index = input('\nPlease select a DAQ device, enter a number'
                             + ' between 0 and '
                             + str(number_of_devices - 1) + ': ')
    descriptor_index = int(descriptor_index)
    if descriptor_index not in range(number_of_devices):
        raise RuntimeError('Error: Invalid descriptor index')

    # Create the DAQ device from the descriptor at the specified index.
    daq_device = DaqDevice(devices[descriptor_index])

    # Get the AiDevice object and verify that it is valid.
    ai_device = daq_device.get_ai_device()
    if ai_device is None:
        raise RuntimeError('Error: The DAQ device does not support analog '
                           'input')

    # Verify the specified device supports hardware pacing for analog input.
    ai_info = ai_device.get_info()
    if not ai_info.has_pacer():
        raise RuntimeError('\nError: The specified DAQ device does not '
                           'support hardware paced analog input')

def connectDevice():

            global deq_device
            global ai_info
            global high_channel
            global range_index
            global channel_count
            global descriptor
            global input_mode
            global ranges
            # Establish a connection to the DAQ device.
            descriptor = daq_device.get_descriptor()
            print('\nConnecting to', descriptor.dev_string, '- please wait...')
            # For Ethernet devices using a connection_code other than the default
            # value of zero, change the line below to enter the desired code.
            daq_device.connect(connection_code=0)

            # The default input mode is SINGLE_ENDED.
            input_mode = AiInputMode.SINGLE_ENDED
            # If SINGLE_ENDED input mode is not supported, set to DIFFERENTIAL.
            if ai_info.get_num_chans_by_mode(AiInputMode.SINGLE_ENDED) <= 0:
                input_mode = AiInputMode.DIFFERENTIAL

            # Get the number of channels and validate the high channel number.
            number_of_channels = ai_info.get_num_chans_by_mode(input_mode)
            if high_channel >= number_of_channels:
                high_channel = number_of_channels - 1
            channel_count = high_channel - low_channel + 1

            # Get a list of supported ranges and validate the range index.
            ranges = ai_info.get_ranges(input_mode)
            if range_index >= len(ranges):
                range_index = len(ranges) - 1

def disconnectDevice():
    global daq_device
    global status
    global ScanStatus
    global ai_device


    if daq_device:
        # Stop the acquisition if it is still running.
        if status == ScanStatus.RUNNING:
            ai_device.scan_stop()
        if daq_device.is_connected():
            daq_device.disconnect()
        daq_device.release()



def main():

    global status
    global descriptor
    global ranges
    global rate
    global ai_device


    try:
        findDevice()
        connectDevice()
        # Allocate a buffer to receive the data.
        data = create_float_buffer(channel_count, int(1.5*samples_per_channel))

        print('\n', descriptor.dev_string, ' ready', sep='')
        print('    Function demonstrated: ai_device.a_in_scan()')
        print('    Channels: ', low_channel, '-', high_channel)
        print('    Input mode: ', input_mode.name)
        print('    Range: ', ranges[range_index].name)
        print('    Samples per channel: ', samples_per_channel)
        print('    Rate: ', rate, 'Hz')
        print('    Scan options:', display_scan_options(scan_options))
        try:
            input('\nHit ENTER to continue\n')
        except (NameError, SyntaxError):
            pass

        system('clear')

        # Start the acquisition.
        rate = ai_device.a_in_scan(low_channel, high_channel, input_mode,
                                   ranges[range_index], int(1.5*samples_per_channel),
                                   rate, scan_options, flags, data)

        try:
            while True:
                try:
                    # Get the status of the background operation
                    status, transfer_status = ai_device.get_scan_status()

                    reset_cursor()
                    print('Please enter CTRL + C to terminate the process\n')
                    print('Active DAQ device: ', descriptor.dev_string, ' (',
                          descriptor.unique_id, ')\n', sep='')

                    print('actual scan rate = ', '{:.6f}'.format(rate), 'Hz\n')

                    index = transfer_status.current_index
                    print('currentTotalCount = ',
                          transfer_status.current_total_count)
                    print('currentScanCount = ',
                          transfer_status.current_scan_count)
                    print('currentIndex= ', index, '\n')

                    # Display the data.
                    for i in range(channel_count):
                        clear_eol()
                        print('chan =',
                              i + low_channel, ': ',
                              '{:.6f}'.format(data[index + i]))
                    #sleep(0.1)

                    if (int(transfer_status.current_total_count)>(samples_per_channel)):
                        break
                except (ValueError, NameError, SyntaxError):
                    break
        except KeyboardInterrupt:
            pass
        print("data",len(data))
        print("dd",int(transfer_status.current_total_count))

        for i in range(samples_per_channel):
            dataAsList.append(data[i])
            timeAsList.append((1/rate)*(i+1))




        a = {'data': dataAsList,'time': timeAsList, }
        df=pd.DataFrame(a)
        df.to_csv('foo1.csv')

    except RuntimeError as error:
        print('\n', error)

    finally:
        disconnectDevice()


if __name__ == '__main__':
    main()
