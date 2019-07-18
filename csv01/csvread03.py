import csv

output_csv_file = input("\nEnter the CSV Filename:")

with open(output_csv_file, mode='w') as csv_file:
    fieldnames = ['hostname', 'ip', 'service']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'hostname': 'dumbledore', 'ip': '192.168.9.22', 'service': 'objectstorage'})
    writer.writerow({'hostname': 'hermione', 'ip': '10.0.2.66', 'service': 'httpd'})
