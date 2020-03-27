from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


class DIU_Vote_Cracker():
    
    def __init__(self):
        self.bot = webdriver.Firefox()
        print("\n\nBot Activated....")
    
    def page_access1(self):
        bot = self.bot
        url ="https://docs.google.com/forms/d/e/1FAIpQLSdtOIgLmg3ZW__P1xdFNDwW4BBH57Ez04JUroIu5ctH9YR2EA/viewform"

        try:
            bot.get(url)
            print("Access Granted....")
        except:
            print("Access Denied....")
        
        time.sleep(2)
        gender_Path_female ="/html/body/div/div[2]/form/div/div/div[2]/div[1]/div/div[2]/div/span/div/div[1]/label/div/div[2]/div/span"
        gender_path_male ="/html/body/div/div[2]/form/div/div/div[2]/div[1]/div/div[2]/div/span/div/div[2]/label"
        gender_Unknown ="/html/body/div/div[2]/form/div/div/div[2]/div[1]/div/div[2]/div/span/div/div[1]/label"

        gender = bot.find_element_by_xpath(random.choice([gender_Path_female,gender_Unknown, gender_path_male]))
        gender.click()    

        age_16_20 = "/html/body/div/div[2]/form/div/div/div[2]/div[2]/div/div[2]/div/span/div/div[1]/label"
        age_21_25 ="/html/body/div/div[2]/form/div/div/div[2]/div[2]/div/div[2]/div/span/div/div[2]/label"
        age_above_26 ="/html/body/div/div[2]/form/div/div/div[2]/div[2]/div/div[2]/div/span/div/div[3]/label"
        age_not_tosay="/html/body/div/div[2]/form/div/div/div[2]/div[2]/div/div[2]/div/span/div/div[4]/label"
        age = bot.find_element_by_xpath(random.choice([age_16_20, age_21_25, age_above_26, age_not_tosay]))
        age.click()

        student_occ= "/html/body/div/div[2]/form/div/div/div[2]/div[3]/div/div[2]/div/span/div/div[1]/label"
        occ = bot.find_element_by_xpath(student_occ).click()


        city_urban="/html/body/div/div[2]/form/div/div/div[2]/div[4]/div/div[2]/div/span/div/div[1]/label"
        semi_urban ="/html/body/div/div[2]/form/div/div/div[2]/div[4]/div/div[2]/div/span/div/div[2]/label"
        village ="/html/body/div/div[2]/form/div/div/div[2]/div[4]/div/div[2]/div/span/div/div[3]/label"
        rural ="/html/body/div/div[2]/form/div/div/div[2]/div[4]/div/div[2]/div/span/div/div[4]/label"

        location = bot.find_element_by_xpath(random.choice([city_urban, semi_urban, village,rural]))
        location.click()
        print("on Page 1 completed")
        
        time.sleep(2)
        nextPage_path ="/html/body/div/div[2]/form/div/div/div[3]/div[1]/div/div/span"
        nextPage = bot.find_element_by_xpath(nextPage_path)
        nextPage.click()

    def page2(self):
        print("on Page 2")
        bot = self.bot
        time.sleep(2)

        mobile_data = "/html/body/div/div[2]/form/div/div/div[2]/div[2]/div/div[2]/div/span/div/div[1]/label"
        wifi ="/html/body/div/div[2]/form/div/div/div[2]/div[2]/div/div[2]/div/span/div/div[2]/label"
        both = "/html/body/div/div[2]/form/div/div/div[2]/div[2]/div/div[2]/div/span/div/div[3]/label"

        resourse = bot.find_element_by_xpath(random.choice([mobile_data,wifi,both]))
        resourse.click()

        usingMobile = "/html/body/div/div[2]/form/div/div/div[2]/div[3]/div/div[2]/div/span/div/div[1]/label"
        usign_wifi = "/html/body/div/div[2]/form/div/div/div[2]/div[3]/div/div[2]/div/span/div/div[2]/label"
        usingBoth ="/html/body/div/div[2]/form/div/div/div[2]/div[3]/div/div[2]/div/span/div/div[3]/label"

        todayRes = bot.find_element_by_xpath(random.choice([usign_wifi, usingBoth, usingMobile]))
        todayRes.click()

        conditionOfNEt_1 = "/html/body/div/div[2]/form/div/div/div[2]/div[4]/div/div[2]/div/span/div/label[1]/div[2]"
        conditionOfNEt_2 = "/html/body/div/div[2]/form/div/div/div[2]/div[4]/div/div[2]/div/span/div/label[2]/div[2]"
        conditionOfNEt_3 = "/html/body/div/div[2]/form/div/div/div[2]/div[4]/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div"
        conditionOfNEt_4 = "/html/body/div/div[2]/form/div/div/div[2]/div[4]/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div"
        conditionOfNEt_5 = "/html/body/div/div[2]/form/div/div/div[2]/div[4]/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div"
        
        conditionOfNEt = bot.find_element_by_xpath(random.choice([conditionOfNEt_1,conditionOfNEt_2, conditionOfNEt_3,conditionOfNEt_4,conditionOfNEt_4,conditionOfNEt_5]))
        conditionOfNEt.click()

        conditionOfDevice1_1 ="/html/body/div/div[2]/form/div/div/div[2]/div[5]/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div"
        conditionOfDevice1_2 ="/html/body/div/div[2]/form/div/div/div[2]/div[5]/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div"
        conditionOfDevice1_3 ="/html/body/div/div[2]/form/div/div/div[2]/div[5]/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div"
        conditionOfDevice1_4 ="/html/body/div/div[2]/form/div/div/div[2]/div[5]/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]"
        conditionOfDevice1_5 ="/html/body/div/div[2]/form/div/div/div[2]/div[5]/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div"

        conditionOfDevice1 = bot.find_element_by_xpath(random.choice([conditionOfDevice1_1,conditionOfDevice1_2,conditionOfDevice1_3,conditionOfDevice1_4,conditionOfDevice1_5]))
        conditionOfDevice1.click()

        conditionOfDevice2_1 ="/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div"
        conditionOfDevice2_2 ="/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div"
        conditionOfDevice2_3 ="/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div"
        conditionOfDevice2_4 ="/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div"
        conditionOfDevice2_5 ="/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div"
        conditionOfDevice2 = bot.find_element_by_xpath(random.choice([conditionOfDevice2_1,conditionOfDevice2_2, conditionOfDevice2_3,conditionOfDevice2_4,conditionOfDevice2_5]))
        conditionOfDevice2.click()

        less1 = "/html/body/div/div[2]/form/div/div/div[2]/div[7]/div/div[2]/div/span/div/div[1]/label"
        one_two = "/html/body/div/div[2]/form/div/div/div[2]/div[7]/div/div[2]/div/span/div/div[2]/label"
        three_five ="/html/body/div/div[2]/form/div/div/div[2]/div[7]/div/div[2]/div/span/div/div[3]/label"
        moreSix ="/html/body/div/div[2]/form/div/div/div[2]/div[7]/div/div[2]/div/span/div/div[4]/label"
        
        dailyNetuses = bot.find_element_by_xpath(random.choice([less1,one_two,three_five,moreSix]))
        dailyNetuses.click()
        

        regular_CostLess10 ="/html/body/div/div[2]/form/div/div/div[2]/div[8]/div/div[2]/div/span/div/div[1]/label"
        regular_CostLess10_20 ="/html/body/div/div[2]/form/div/div/div[2]/div[8]/div/div[2]/div/span/div/div[2]/label"
        regular_CostLess21_40 ="/html/body/div/div[2]/form/div/div/div[2]/div[8]/div/div[2]/div/span/div/div[3]/label"
        regular_CostLess41_ ="/html/body/div/div[2]/form/div/div/div[2]/div[8]/div/div[2]/div/span/div/div[4]/label"
        
        regular_Cost = bot.find_element_by_xpath(random.choice([regular_CostLess10,regular_CostLess10_20, regular_CostLess21_40, regular_CostLess41_]))
        regular_Cost.click()

        now_costL10 ="/html/body/div/div[2]/form/div/div/div[2]/div[9]/div/div[2]/div/span/div/div[1]/label"
        now_cost10_20 ="/html/body/div/div[2]/form/div/div/div[2]/div[9]/div/div[2]/div/span/div/div[2]/label"
        now_cost21_40 ="/html/body/div/div[2]/form/div/div/div[2]/div[9]/div/div[2]/div/span/div/div[3]/label"
        now_cost41_ ="/html/body/div/div[2]/form/div/div/div[2]/div[9]/div/div[2]/div/span/div/div[4]/label"

        now_cost = bot.find_element_by_xpath(random.choice([now_costL10,now_cost10_20, now_cost21_40,now_cost41_]))
        now_cost.click()

        spendTimeL1 ="/html/body/div/div[2]/form/div/div/div[2]/div[10]/div/div[2]/div/span/div/div[1]/label"
        spendTime1_2 ="/html/body/div/div[2]/form/div/div/div[2]/div[10]/div/div[2]/div/span/div/div[2]/label"
        spendTime3_5="/html/body/div/div[2]/form/div/div/div[2]/div[10]/div/div[2]/div/span/div/div[3]/label"
        spendTimeM6 ="/html/body/div/div[2]/form/div/div/div[2]/div[10]/div/div[2]/div/span/div/div[4]/label"

        spendTimeNow = bot.find_element_by_xpath(random.choice([spendTimeL1, spendTime1_2, spendTime3_5,spendTimeM6]))
        spendTimeNow.click()

        print("on Page 2 completed")
        
        gotoPage3 = "/html/body/div/div[2]/form/div/div/div[3]/div[1]/div/div[2]/span"
        goNext = bot.find_element_by_xpath(gotoPage3)
        goNext.click()
        
        time.sleep(1)



    def page3(self):
        print("on Page 3")
        bot = self.bot

        classRate_1 ="/html/body/div/div[2]/form/div/div/div[2]/div[2]/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div"
        classRate_2 ="/html/body/div/div[2]/form/div/div/div[2]/div[2]/div/div[2]/div/span/div/label[2]/div[2]/div/div/div[3]/div"
        classRate_3 ="/html/body/div/div[2]/form/div/div/div[2]/div[2]/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div"
        classRate_4 ="/html/body/div/div[2]/form/div/div/div[2]/div[2]/div/div[2]/div/span/div/label[4]/div[2]/div/div/div[3]/div"
        classRate_5 ="/html/body/div/div[2]/form/div/div/div[2]/div[2]/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div"
        classRate_6 ="/html/body/div/div[2]/form/div/div/div[2]/div[2]/div/div[2]/div/span/div/label[6]/div[2]/div/div/div[3]/div"
        classRate_7 ="/html/body/div/div[2]/form/div/div/div[2]/div[2]/div/div[2]/div/span/div/label[7]/div[2]/div/div/div[3]/div"
        classRate_8 ="/html/body/div/div[2]/form/div/div/div[2]/div[2]/div/div[2]/div/span/div/label[8]/div[2]/div/div/div[3]/div"
        classRate_9 ="/html/body/div/div[2]/form/div/div/div[2]/div[2]/div/div[2]/div/span/div/label[9]/div[2]/div/div/div[3]/div"
        classRate_10 ="/html/body/div/div[2]/form/div/div/div[2]/div[2]/div/div[2]/div/span/div/label[10]/div[2]/div/div/div[3]/div"
        
        classRate = bot.find_element_by_xpath(random.choice([classRate_1,classRate_2,classRate_3,classRate_4,classRate_5,classRate_6, classRate_7,classRate_8,classRate_9,classRate_10]))
        classRate.click()

        learnForm_Yes ="/html/body/div/div[2]/form/div/div/div[2]/div[3]/div/div[2]/div/span/div/div[1]/label"
        learnForm_SomeTime ="/html/body/div/div[2]/form/div/div/div[2]/div[3]/div/div[2]/div/span/div/div[2]/label"
        learnForm_HardLY ="/html/body/div/div[2]/form/div/div/div[2]/div[3]/div/div[2]/div/span/div/div[3]/label"
        learnFormNEVER ="/html/body/div/div[2]/form/div/div/div[2]/div[3]/div/div[2]/div/span/div/div[4]/label"

        learnForm =bot.find_element_by_xpath(random.choice([learnForm_Yes,learnForm_SomeTime,learnForm_HardLY,learnFormNEVER]))
        learnForm.click()

        decsOnline_YES ="/html/body/div/div[2]/form/div/div/div[2]/div[4]/div/div[2]/div/span/div/div[1]/label"
        decsOnline_NEver ="/html/body/div/div[2]/form/div/div/div[2]/div[4]/div/div[2]/div/span/div/div[2]/label"

        ugc_desc_OK =bot.find_element_by_xpath(random.choice([decsOnline_YES, decsOnline_NEver]))
        ugc_desc_OK.click()

        exp_Path = "/html/body/div/div[2]/form/div/div/div[2]/div[5]/div/div[2]/div[1]/div[2]/textarea"
        expr = bot.find_element_by_xpath(exp_Path)

        pernalfav_YEs = "/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div/span/div/div[1]/label"
        pernalfav_No ="/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div/span/div/div[2]/label"
        pernalfav_Maybe ="/html/body/div/div[2]/form/div/div/div[2]/div[6]/div/div[2]/div/span/div/div[2]/label"

        personalFav = bot.find_element_by_xpath(random.choice([pernalfav_Maybe,pernalfav_No,pernalfav_YEs]))
        personalFav.click()
        
        submitP ="/html/body/div/div[2]/form/div/div/div[3]/div[1]/div/div[2]/span"
        submit = bot.find_element_by_xpath(submitP)
        submit.click()
        print("Submitted ")



i =0
Amigos = DIU_Vote_Cracker()

while(True):
    print("\nsubmitted= ",i)

    Amigos.page_access1()
    time.sleep(1)
    Amigos.page2()
    time.sleep(1)
    Amigos.page3()
    i+=1
        
    
