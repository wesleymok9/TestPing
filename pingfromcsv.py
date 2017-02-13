import subprocess
import csv
import socket

with open('111 subnet.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    lines = []
    first_row=next(reader)
    for row in reader:
        if row[6] == "Not Assigned":
            host = row[3]
            #print(host)
            try:
                name = socket.gethostbyaddr(host)[0]
                output = (subprocess.Popen(["ping.exe", host], stdout=subprocess.PIPE).communicate()[0]).decode('UTF-8')
                #(output)
                out_rows = []
                if row[21] == "":
                    out_rows.append("No Contact")
                else:
                    out_rows.append(row[21])
                if('Request timed out' in output):
                    out_rows.append(host)
                    out_rows.append("Still has DNS name and is not pinging")
                else:
                    out_rows.append(host)
                    out_rows.append("Is still online with DNS name but is showing Not Assigned")
                lines.append(out_rows)
                print(out_rows)
            except socket.herror:
                print("None")
with open('ouput.csv', 'w') as o:
    writer = csv.writer(o)
    writer.writerows(lines)
