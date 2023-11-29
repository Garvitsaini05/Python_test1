def convertSalary():


    print("Enter the COUNTRY you want to migrate to: (canada, usa, cambodia, uk)")
country_to_migrate_to=input(":- ").lower()

print("Enter your annual salary in GERMANY EUROS: ")
annual_salary_in_euro=float(input(":- "))

if country_to_migrate_to=="canada" or "usa" or "cambodia" or "uk":
    print("")
else:
    print("ERROR: Wrong Country")

exchange_to_CAD= 1.49*annual_salary_in_euro
exchange_to_USD= 1.10*annual_salary_in_euro
exchange_to_Cambodian= 0.00022*annual_salary_in_euro
exchange_to_UK= 1.16*annual_salary_in_euro

if country_to_migrate_to=="canada":
    if exchange_to_CAD >= 56000:
        print("You will be RICH in ",country_to_migrate_to,"with a salary of", exchange_to_CAD , "CAD.")
    else:
        print("You will be POOR in ",country_to_migrate_to,"with a salary of", exchange_to_CAD , "CAD.")

if country_to_migrate_to=="usa":
    if exchange_to_USD >= 45000:
        print("You will be RICH in ",country_to_migrate_to,"with a salary of", exchange_to_USD , "USD.")
    else:
        print("You will be POOR in ",country_to_migrate_to,"with a salary of", exchange_to_USD , "USD.")

if country_to_migrate_to=="cambodia":
    if exchange_to_Cambodian >= 7649856:
        print("You will be RICH in ",country_to_migrate_to,"with a salary of", exchange_to_Cambodian , "Cambodian RIEL.")
    else:
        print("You will be POOR in ",country_to_migrate_to,"with a salary of", exchange_to_Cambodian , "Cambodian RIEL.")


if country_to_migrate_to=="uk":
    if exchange_to_UK >= 45423:
        print("You will be RICH in ",country_to_migrate_to,"with a salary of", exchange_to_UK , "EURO.")
    else:
        print("You will be POOR in ",country_to_migrate_to,"with a salary of", exchange_to_UK , "EURO.")

convertSalary()