import subprocess
import csv

with open('SEC.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    lines = []
    first_row=next(reader)
    for row in reader:
        hostname = row[1]
        #print(hostname)
        output = (subprocess.Popen(["ping.exe", hostname], stdout=subprocess.PIPE).communicate()[0]).decode('UTF-8')
        #(output)
        out_rows = []
        out_rows.append(row[2])
        out_rows.append(row[3])
        out_rows.append(row[4])
        out_rows.append(row[5])
        if('Ping request could not find' in output):
            out_rows.append(hostname + ": Ping request could not find host")
            #print(hostname + ": Ping request could not find host")
        elif('Request timed out' in output):
            out_rows.append(hostname + ": Has IP but Time out")
            #print(hostname + ": Has IP but Time out")
        else:
            out_rows.append(hostname + ": Online")
            #print(hostname + ": Online")
        print(out_rows)
        lines.append(out_rows)
        #print(lines)
    with open('ouput.csv', 'w') as o:
        writer = csv.writer(o)
        writer.writerows(lines)