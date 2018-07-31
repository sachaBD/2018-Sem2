from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
import time
from bs4 import BeautifulSoup
import datetime as datetime

# Needs a multithreading timeout
# A maximum number of courses to get at a time

timetables = []

full_path = os.path.realpath(__file__)
outLocation = "\\".join(full_path.split('\\')[:-1]) + "\\enrollement" + datetime.datetime.now().strftime("%Y-%m-%d_%H") + ".csv"
timetableLocation = "\\".join(full_path.split('\\')[:-1]) + "\\timetables" + datetime.datetime.now().strftime("%Y-%m-%d_%H") + ".csv"
print(outLocation + "\n")

f = open(outLocation, "a")
timetableFile = open(timetableLocation, "a") 

# url = "https://www.sinet.uq.edu.au/psc/ps_2/EMPLOYEE/HRMS/c/UQMY_GUEST.UQMY_GUEST_TTBLE.GBL"
url = "https://www.sinet.uq.edu.au"

prefixes = [
"ABTS", "ACCT", "ADVT", "AERO", "AGRC", "ANAT", "ANCH", "ANIC", "ANIM", "ANTH", "AQUA", "ARCA", "ARCH", "ARCS", "ARTT", "AUDL", "AUST", "BESC", "BINF", "BIOC", "BIOL", "BIOM", "BIOT", "BIPH", "BISM", "BLDG", "BOTN", "CELL", "CHEE", "CHEM", "CHIN", "CIVL", "CMED", "COGS", "COMP", "COMS", "COMU", "CONS", "COSC", "COUN", "CRIM", "CRMD", "CSSE", "DATA", "DECO", "DENT", "DEVB", "DIET", "DIPAG", "DIPAH", "DIPMG", "DIPPP", "DIPSC", "DRAM", "ECHO", "ECOL", "ECON", "EDUC", "EIBS", "ELEC", "ENGG", "ENGL", "ENGY", "ENTM", "ENVM", "ERTH", "EVNT", "EXCH", "EXMD", "FINM", "FIRE", "FOOD", "FREN", "FRST", "GEND", "GENP", "GEOG", "GEOM", "GEOS", "GNET", "GREK", "GRMN", "GRRS", "HIST", "HLTH", "HMST", "HORT", "HOSP", "HPRM", "HRSS", "HSER", "HUFA", "HUMN", "IBUS", "IENV", "IMED", "INDH", "INDN", "INFS", "IREL", "JAPN", "JOUR", "KORN", "LAND", "LATN", "LAWS", "LEIS", "LING", "LPWM", "LTCS", "MARS", "MATE", "MATH", "MEBS", "MECH", "MEDI", "METR", "MGTS", "MICR", "MIDW", "MINE", "MKTG", "MMDS", "MOLB", "MOLI", "MRES", "MSTU", "MUSC", "MUSM", "NEUR", "NUMW", "NURS", "NUTR", "OCTY", "OGYN", "OHSS", "ORAL", "ORGC", "PARA", "PATH", "PCAH", "PCOL", "PHAS", "PHIL", "PHRM", "PHTY", "PHYL", "PHYS", "PLAN", "PLNT", "PMDC", "POLS", "POLY", "PORT", "PPES", "PSYC", "PUBH", "PUBT", "PXMH", "PXPY", "RADL", "RBUS", "REDE", "REIT", "RELA", "RELN", "RESC", "RSCH", "RSSN", "SBIO", "SCIE", "SLAT", "SOCY", "SOSC", "SPAN", "SPCG", "SPCH", "SPMD", "STAT", "SURG", "SWSP", "TECH", "TIMS", "TOUR", "TOXY", "TRFCR", "UNITS", "VETS", "VPAT", "VREX", "WATR", "WENG", "WRIT", "ZOOL"]
prefixes = prefixes[prefixes.index('ECON'):]
 
driver = webdriver.Chrome("C:\\Users\\Sacha\\Documents\\University\\hackathon\\uqcshackaton2017\\node_modules\\chromedriver\\lib\\chromedriver\\chrome-2.36\\chromedriver.exe")

driver.get(url)

# Give the user time to log in
input("Press Enter when logged in...")

# while True:
#     elem = driver.find_element_by_xpath("//*")
#     source_code = elem.get_attribute("outerHTML")
#     print(source_code)
#
#     input("Press Enter when logged in...")


# New URL
timetableURL = "https://www.sinet.uq.edu.au/psc/ps/EMPLOYEE/SA/c/UQMY_GUEST.UQMY_GUEST_TTBLE.GBL?PAGE=UQMY_GUEST_TTBLE&PortalActualURL=https%3a%2f%2fwww.sinet.uq.edu.au%2fpsc%2fps%2fEMPLOYEE%2fSA%2fc%2fUQMY_GUEST.UQMY_GUEST_TTBLE.GBL%3fPAGE%3dUQMY_GUEST_TTBLE&PortalContentURL=https%3a%2f%2fwww.sinet.uq.edu.au%2fpsc%2fps%2fEMPLOYEE%2fSA%2fc%2fUQMY_GUEST.UQMY_GUEST_TTBLE.GBL&PortalContentProvider=SA&PortalCRefLabel=Course%20%26%20Timetable%20Info&PortalRegistryName=EMPLOYEE&PortalServletURI=https%3a%2f%2fwww.sinet.uq.edu.au%2fpsp%2fps%2f&PortalURI=https%3a%2f%2fwww.sinet.uq.edu.au%2fpsc%2fps%2f&PortalHostNode=SA&NoCrumbs=yes&PortalKeyStruct=yes"

errorList = []

for prefix in prefixes:
    # try:
        # driver.get(timetableURL)
        time.sleep(2)


        inputField = driver.find_element_by_id("UQ_DRV_CRSE_SRC_UQ_SUBJECT_SRCH")

        print(inputField.get_attribute("innerHTML"))

        # inputField.clear()

        inputField.send_keys(prefix)

        time.sleep(3)

        driver.find_element_by_id("UQ_DRV_TT_GUEST_UQ_SEARCH_PB").click()

        time.sleep(3)

        # Find enrollment
        page = BeautifulSoup(driver.page_source, 'html.parser')

        numCoursesFound = 0
        for course in page.find_all('tr'):
            if course is None or not course.has_attr('id'):
                continue

            if "trUQ_DRV_TT_GUEST$0_row" in course.attrs['id']:
                courseCode, enrollment = "", ""

                # Save the enrollment data
                for div in course.find_all('div'):
                    if div is None or not div.has_attr('id'):
                        continue

                    if "win2divUQ_DRV_TT_GUEST_UQ_CRSE_CODE$" in div.attrs['id']:
                        courseCode = div.text.strip()

                    if "win2divUQ_DRV_TT_GUEST_ENRL_TOT$" in div.attrs['id']:
                        enrollment = div.text.strip()

                f.write(courseCode + ", " + enrollment + "\n")
                numCoursesFound += 1

            # Mark each check box

        for i in range(0, numCoursesFound):
            try:
                element = driver.find_element_by_id("UQ_DRV_TT_GUEST$selm$" + str(i) + "$$0")
                driver.execute_script("return arguments[0].scrollIntoView();", element)

                if element is not None:
                    element.click()
            except:
                print("Failed to check", i)

        # Click the next button
        driver.find_element_by_id("UQ_DRV_TT_GUEST_UQ_NEXT_BUTTON$0").click()

        # Wait for the page to open
        time.sleep(2)

        # Change to displaying dates
        if False:
            for i in range(0, numCoursesFound):
                dates = driver.find_element_by_id("UQ_DRV_TTBLE_CR_UQ_TBL_DISP_DT_BTN$" + str(i))
                driver.execute_script("return arguments[0].scrollIntoView();", dates)
                dates.click()
                time.sleep(1)
                print("Clicked date:", i)
            print("Done clicking dates")


        # Get the timetabling infomation
        elemDownloadAsCSV = driver.find_element_by_id("UQ_DRV_TTBLE_CR_UQ_PRINT_CSV_PB")
        driver.execute_script("return arguments[0].scrollIntoView();", elemDownloadAsCSV)
        time.sleep(1)

        elemDownloadAsCSV.click()
        # Wait until 2 windows are open
        while len(driver.window_handles) == 1:
            time.sleep(1)

        driver.switch_to.window(driver.window_handles[1])
        timetableFile.write(driver.page_source)
        timetableFile.write("\n\n")

        driver.close()

        # Wait until only 1 window is open
        while len(driver.window_handles) == 2:
            time.sleep(1)

        driver.switch_to.window(driver.window_handles[0])
    # except:
    #     errorList.append(prefix)
    #     print("Error loading", prefix)
    


driver.close()
f.close()
timetableFile.close()
