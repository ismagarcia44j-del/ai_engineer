#TWO FORMATS ACCEPTED input:
## (MM/DD/YYYY) and (MONTH DAY,YEAR)

#output:
## (YYYY-MM-DD)

#REJECTS:
##when input is not aligned with 2 formats accepted

def main():
    while True:
            try:
                date=input("Date: ").strip()
                if "/" in date:
                    date_slash=date.split("/")
                    for i in range(2):
                        date_slash[i]=int(date_slash[i])
                    if 12>=date_slash[0]>=1:
                        if 31>=date_slash[1]>=1:
                            new_date=f"{date_slash[2]}-{date_slash[0]:02}-{date_slash[1]:02}"
                            print(new_date)
                            break
                elif "," in date:
                    date_coma=date.replace(","," ").split()
                    date_coma[1]=int(date_coma[1])
                    date_coma[2]=int(date_coma[2])
                    months={
                            "January":"01",
                            "February":"02",
                            "March":"03",
                            "April":"04",
                            "May":"05",
                            "June":"06",
                            "July":"07",
                            "August":"08",
                            "September":"09",
                            "October":"10",
                            "November":"11",
                            "December":"12"
                    }
                    if date_coma[0] in months:
                        month=months[date_coma[0]]
                        if 31>=date_coma[1]>=1:
                            new_date=f"{date_coma[2]}-{month}-{date_coma[1]:02}"
                            print(new_date)
                            break
            except ValueError:
                 continue
main()
