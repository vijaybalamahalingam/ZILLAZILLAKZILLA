import uuid
rupee_symbol = u"\u20B9"
constant = 1
print()
print("__________ WELCOME TO ELECTRICITY BILL CALCULATOR __________")
print()
while constant > 0 :
    try :
        print()
        print(f">> Client Id - {uuid.uuid4()}")

        #COLLECTING DATA
        consumer_name = input(".. Enter consumer name : ")
        while constant > 0 :
            area_type = input(".. Enter area type (Urban/Rural) : ").lower()
            area_type = area_type.strip()
            if area_type in ['urban','rural'] :
                break
            else:
                print(".. Error in area type.")
        unit_consumed = float(input(".. Enter number of units consumed : "))
        
        
        if unit_consumed <= 100.00 :
            unit_distribution = [unit_consumed, 0, 0]
        elif 100.00 < unit_consumed <= 300.00 :
            unit_distribution = [100.00, round((unit_consumed-100),2), 0]
        elif 300.00 < unit_consumed :
            unit_distribution = [100.00, 200.00, round((unit_consumed-300),2)]

        tariff_list = [5.05,6.35,7.18]

        #CALCULATING BILL
        base_amt_slab = list(map(lambda x,y : round(x*y,2), unit_distribution, tariff_list))
        total_base_amt = 0
        for i in range(0,3):
            total_base_amt += base_amt_slab[i]

        if area_type == "rural" :
            subsidy = round(0.25*total_base_amt, 2)
        else :
            subsidy = 0

        if unit_consumed > 300.00 :
            surcharge = round(0.025*total_base_amt, 2)
        else :
            surcharge = 0

        total_bill = total_base_amt - subsidy + surcharge

        #PRINTING THE BILL
        print()
        print(f".... Elecricity Bill for {consumer_name} ....")
        for j in range(0,3):
            if j == 0 :
                prefix = 'first'
            else :
                prefix = 'next'
            if unit_distribution[j] > 0 :
                print(f".. Base amount for {prefix} {'%.2f' % unit_distribution[j]} units is : {rupee_symbol}{'%.2f' % base_amt_slab[j]} ({rupee_symbol}{'%.2f' % tariff_list[j]}/unit)")
                
        print(f".. Total base amount is : {rupee_symbol}{'%.2f' % total_base_amt}")        
        print(f".. Surcharge : {'Not Applicable' if surcharge==0 else rupee_symbol+str('%.2f' % surcharge)}")    
        print(f".. Subsidy : {'Not Applicable' if subsidy==0 else rupee_symbol+str('%.2f' % subsidy)}")
        print(f".. Total bill amount to be paid is : {rupee_symbol}{'%.2f' % total_bill}")
        print()

    except :
        print(".. Error - Invalid input.")
        print()
        
