import os
import time
import random
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
try:
    import undetected_chromedriver as uc
    CHROME_STEALTH_AVAILABLE = True
except ImportError:
    CHROME_STEALTH_AVAILABLE = False
def get_driver():
    print("\n[System] Identifying available browsers...")
    if CHROME_STEALTH_AVAILABLE:
        try:
            print("[Checking] Attempting Chrome...")
            options = uc.ChromeOptions()
            driver = uc.Chrome(options=options)
            print("-> Success: Chrome (Stealth) launched.")
            return driver
        except Exception:
            print("-> Chrome not found or binary missing.")
    try:
        print("[Checking] Attempting Microsoft Edge...")
        from selenium.webdriver.edge.options import Options as EdgeOptions
        options = EdgeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        try:
            service = EdgeService(EdgeChromiumDriverManager().install())
            driver = webdriver.Edge(service=service, options=options)
        except:
            manual_path = r"C:\msedgedriver.exe"
            if os.path.exists(manual_path):
                service = EdgeService(executable_path=manual_path)
                driver = webdriver.Edge(service=service, options=options)
            else:
                print("-> Edge Driver not found at C:\\msedgedriver.exe")
                raise Exception("Driver Missing")
        print("-> Success: Microsoft Edge launched.")
        return driver
    except Exception as e:
        print(f"-> Edge Failed: {e}")
    try:
        print("[Checking] Attempting Brave...")
        brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
        if os.path.exists(brave_path):
            from selenium.webdriver.chrome.options import Options as ChromeOptions
            options = ChromeOptions()
            options.binary_location = brave_path
            options.add_argument("--disable-blink-features=AutomationControlled")
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
            print("-> Success: Brave launched.")
            return driver
    except:
        print("-> Brave not found.")
    return None
def perform_search(driver, keyword):
    try:
        print(f"\n[Action] Searching Google for: '{keyword}'")
        driver.get("https://www.google.com")
        time.sleep(3)
        try:
            driver.find_element(By.XPATH, "//button[contains(., 'Reject all')]").click()
        except: pass
        search_box = driver.find_element(By.NAME, "q")
        for char in keyword:
            search_box.send_keys(char)
            time.sleep(random.uniform(0.1, 0.3))
        search_box.send_keys(Keys.RETURN)
        time.sleep(5)
        safe_keyword = "".join([c for c in keyword if c.isalnum() or c==' ']).strip().replace(" ", "_")
        filename = f"{safe_keyword}.png"
        driver.save_screenshot(filename)
        print(f"\n[JOB COMPLETE]")
        print(f"Result saved as: {filename}")
        print(f"Page Title: {driver.title}")
    finally:
        driver.quit()
if __name__ == "__main__":
    print("\n" + "="*40)
    print("   PROFESSIONAL SEO AUTOMATION TOOL")
    print("="*40)
    user_input = input("\nEnter search keyword: ").strip()
    if not user_input:
        print("Error: Keyword is empty.")
    else:
        active_driver = get_driver()
        if active_driver:
            perform_search(active_driver, user_input)
        else:
            print("\n[CRITICAL ERROR] No browsers (Chrome/Edge/Brave) could be launched.")
            print("Please ensure your EdgeDriver is at C:\\msedgedriver.exe")