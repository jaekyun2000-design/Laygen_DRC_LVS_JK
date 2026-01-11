import numpy as np
import matplotlib.pyplot as plt

def get_bit_positions(number):
    positions = []

    position = 0
    number_new = number
    while 0 <= position < number_new:
        if number % 2 == 1:
            positions.append(position)
        number = int (number >> 1)
        position += 1

    return positions

# print(get_bit_positions(15))

def calculate_dac_output(capacitors, dummy_capacitor, digital_input, V_ref=1):

    total_cap = sum(capacitors) + sum(dummy_capacitor)
    V_out = 0
    selected_capacitors_sum = 0

    position_number_array = get_bit_positions(digital_input)
    for j in range(len(position_number_array)):
        # print(position_number_array[j])
        selected_capacitors_sum += capacitors[position_number_array[j]]


    V_out = (selected_capacitors_sum / total_cap) * V_ref
    return V_out



# capacitor value
capacitors = [1.78247,3.57436,7.14115,14.2752,28.2749,57.4286]
dummy_capacitor = [1.76043]
V_ref = 1

n_bits = len(capacitors)
# Ideal_LSB = V_ref/(2**n_bits)
output_voltage_array=[]

DNL_array = []
INL_array = []

INL_output = 0

for digital_input in range(64):
    output_voltage = 0
    output_voltage = calculate_dac_output(capacitors, dummy_capacitor, digital_input, V_ref)
    binary_input = f"{digital_input:06b}"
    print(f"Digital input : {digital_input}")
    print(f"Digital input : {binary_input} -> output voltage : {output_voltage:.5f}V")

    output_voltage_array.append(output_voltage)

One_LSB = output_voltage_array[-1] / (2**n_bits - 1)
print(One_LSB)
digital_input = 0

for digital_input in range(64):
    # DNL
    DNL_output = 0
    # print(output_voltage_array[digital_input])
    # print(digital_input * One_LSB)

    # DNL_output = (output_voltage_array[digital_input] - digital_input * One_LSB) / One_LSB

    if (digital_input != 0):
        DNL_output = (output_voltage_array[digital_input] - output_voltage_array[digital_input - 1] - One_LSB)/One_LSB
    DNL_array.append(DNL_output)
    binary_input = f"{digital_input:06b}"
    print(f"Digital input : {binary_input} -> DNL : {DNL_output:.5f}LSB")

    # INL
    # if(len(output_voltage_array) > 1):
    INL_output += DNL_output
    INL_array.append(INL_output)
    binary_input = f"{digital_input:06b}"
    print(f"Digital input : {binary_input} -> INL : {INL_output:.5f}LSB")

# plotting the results
digital_inputs = np.arange(64)

# plot for DNL
plt.figure(figsize=(12,6))

plt.subplot(1,2,1)
plt.plot(digital_inputs, DNL_array, marker = 'o', linestyle = '-', color = 'b')
plt.title('DNL (Differential Non-Linearity)')
plt.xlabel('Digital input')
plt.ylabel('DNL (LSB)')
plt.grid(True)

# for i, txt in enumerate(DNL_array):
#     plt.annotate(f'{txt:.5f}', (digital_inputs[i], DNL_array[i]), textcoords = 'offset points', xytext = (0,10), ha = 'center')

# plot for INL
# plt.figure(figsize=(12,6))

plt.subplot(1,2,2)
plt.plot(digital_inputs, INL_array, marker = 'o', linestyle = '-', color = 'b')
plt.title('INL (Integral Non-Linearity)')
plt.xlabel('Digital input')
plt.ylabel('INL (LSB)')
plt.grid(True)

# for i, txt in enumerate(INL_array):
#     plt.annotate(f'{txt:.5f}', (digital_inputs[i], INL_array[i]), textcoords = 'offset points', xytext = (0,10), ha = 'center')

#
# # plot digital input, output voltage
#
# plt.subplot(2,2,3)
# plt.plot(digital_inputs, output_voltage_array, marker = 'o', linestyle = '-', color = 'b')
# plt.title('Analog output voltage vs Digital input')
# plt.xlabel('Digital input')
# plt.ylabel('Analog output voltage')
# plt.grid(True)
#

plt.tight_layout()
plt.show()
