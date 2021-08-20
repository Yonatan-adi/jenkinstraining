from selenium import webdriver

driver =  webdriver.Chrome(executable_path='C:/driver/chromedriver.exe')
driver.maximize_window()

driver.get('http://localhost/form.php')
driver.find_element_by_name('nip').send_keys('12345')
driver.find_element_by_name('nama').send_keys('Yona')
driver.find_element_by_name('nik').send_keys('17122321')
driver.find_element_by_name('alamat').send_keys('Alamat')
driver.find_element_by_name('perusahaan').send_keys('SAT')
driver.find_element_by_name('tanggal').send_keys('09/03/1995')
driver.find_element_by_name('divisi').send_keys('IT')
driver.find_element_by_name('posisi').send_keys('Programmer')
driver.find_element_by_name('gaji').send_keys('123456789123456789')
driver.find_element_by_name('atasan').send_keys('Yona')
driver.find_element_by_name('submit').click()

driver.close()
driver.quit()
print('Test Selesai....')