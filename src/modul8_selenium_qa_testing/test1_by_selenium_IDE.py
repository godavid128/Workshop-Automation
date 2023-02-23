# Generated by Selenium IDE

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTest1():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_test1(self):
    self.driver.get("https://formy-project.herokuapp.com/")
    self.driver.set_window_size(814, 852)
    self.driver.find_element(By.LINK_TEXT, "Autocomplete").click()
    self.driver.find_element(By.ID, "autocomplete").click()
    self.driver.find_element(By.ID, "autocomplete").send_keys("Str. Crinului")
    self.driver.find_element(By.CSS_SELECTOR, ".dismissButton").click()
    self.driver.find_element(By.ID, "locality").click()
    self.driver.find_element(By.ID, "locality").send_keys("Iasi")
    self.driver.find_element(By.ID, "administrative_area_level_1").click()
    self.driver.find_element(By.ID, "administrative_area_level_1").send_keys("Jud. Iasi")
    self.driver.find_element(By.ID, "postal_code").click()
    self.driver.find_element(By.ID, "postal_code").send_keys("74700")
    self.driver.find_element(By.ID, "country").click()
    self.driver.find_element(By.ID, "country").send_keys("Anglia")
    self.driver.find_element(By.LINK_TEXT, "Form").click()
    self.driver.find_element(By.ID, "first-name").click()
    self.driver.find_element(By.ID, "first-name").send_keys("go")
    self.driver.find_element(By.ID, "last-name").send_keys("david")
    self.driver.find_element(By.ID, "job-title").send_keys("QA Automation")
    self.driver.find_element(By.ID, "radio-button-3").click()
    self.driver.find_element(By.ID, "checkbox-1").click()
    self.driver.find_element(By.ID, "select-menu").click()
    dropdown = self.driver.find_element(By.ID, "select-menu")
    dropdown.find_element(By.XPATH, "//option[. = '0-1']").click()
    self.driver.find_element(By.ID, "datepicker").click()
    self.driver.find_element(By.CSS_SELECTOR, ".today:nth-child(5)").click()
    self.driver.find_element(By.LINK_TEXT, "Submit").click()
  