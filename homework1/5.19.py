  # Luke Gilin 1216992
print('Davy\'s auto shop services')
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12\n')
service_1 = input('Select first service:\n')
service_2 = input('Select second service:\n\n')

carServices = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12}  # create dic

if service_1 != '-' and service_2 != '-':  # create conditionals where no service is selected
    print('Davy\'s auto shop invoice\n')
    print('Service 1: {service}, ${price}'.format(service=service_1, price=carServices[service_1]))
    print('Service 2: {service}, ${price}\n'.format(service=service_2, price=carServices[service_2]))
    total = carServices[service_1] + carServices[service_2]
elif service_1 == '-' and service_2 != '-':
    print('Davy\'s auto shop invoice\n')
    print('Service 1: No service')
    print('Service 2: {service}, ${price}\n'.format(service=service_2, price=carServices[service_2]))
    total = carServices[service_2]
elif service_2 == '-' and service_1 != '-':
    print('Davy\'s auto shop invoice\n')
    print('Service 1: {service}, ${price}'.format(service=service_1, price=carServices[service_1]))
    print('Service 2: No service\n')
    total = carServices[service_1]
elif service_2 == '-' and service_1 == '-':
    print('Davy\'s auto shop invoice\n')
    print('Service 1: No service')
    print('Service 2: No service\n')
    total = 0

print('Total: ${price}'.format(price=total))

