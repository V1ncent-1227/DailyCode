#coding=utf-8
import unittest
import time

from appium import webdriver
import traceback

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUp(self) -> None:
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = 'huawei'
        desired_caps['appPackage'] = 'com.shark.jizhang'
        desired_caps['appActivity'] = 'com.shark.jizhang.module.splash.SplashActivity'
        desired_caps['noReset'] = True
        desired_caps['unicodeKeyboard'] = True # 使用unicode编码方式发送字符串
        desired_caps['resetKeyboard'] = True # 将键盘隐藏起来 ? #重置自动化时设置的键盘 ?
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    @classmethod
    def tearDown(self) -> None:
        self.driver.quit()

    def input_amount(self, number_button, amount):
        amount_list = list(str(amount))
        for number in amount_list:
            if number == '.':
                number_button[10].click()
            else:
                number_button[int(number)].click()

    def swipe_date(self, element, target):
        single_bounds = self.single_bounds
        current = element.text
        bounds0 = element.location
        #print("滑动的长度为：" + str(single_bounds))
        #print("起始坐标：" + str(bounds0))

        x1 = bounds0['x']  # 年份起始横坐标
        y1 = bounds0['y']  # 年份起始纵坐标

        diff = int(current) - int(target)
        #
        if str(diff).count('-') == 1 and str(diff)[0] == '-':
            y2 = bounds0['y'] - single_bounds  # 如果之差为负则向上滑动,y2: 向上滑动的距离
            swipecount = -diff
        else:
            y2 = single_bounds + bounds0['y']  # 如果之差为正则向下滑动,y2: 向下滑动的距离
            swipecount = diff

        if swipecount == 0:
            return True

        element.click()
        for i in range(0, swipecount):
            self.driver.swipe(x1, y1, x1, y2)  # 年份滑动一格
            time.sleep(0.5)
            if str(int(element.text)) == str(int(target)):
                #print(element.text)
                return True

        print('[*]Date swipe wrong: ')
        print('target:', target)
        print('current-target=', diff)
        print('swipecount=', swipecount)
        print('last element.text=', str(int(element.text)))
        return False

    def test_something(self):

        with open('results.txt', 'r', encoding='utf-8') as f:
            contents = f.read().split('\n')

        time.sleep(10)

        for i, content in enumerate(contents):

            date, category, amount, remark = content.split('\t')

            print(date, category, amount, remark)

            time.sleep(2)
            add_button = self.driver.find_element_by_xpath('//android.widget.TextView[@text="记账"]')
            add_button.click()

            # 收入
            time.sleep(1)
            add_button = self.driver.find_element_by_xpath('//android.widget.TextView[@text="收入"]')
            add_button.click()

            time.sleep(1)
            category_button = self.driver.find_element_by_name(category)
            category_button.click()

            # 账单备注
            time.sleep(0.5)
            remark_text = self.driver.find_element_by_xpath('//android.widget.EditText[@resource-id="com.shark.jizhang:id/remarkName"]')
            #remark_text.click()
            remark_text.send_keys(remark)
            category_button.click()
            category_button.click()

            # 输入金额
            time.sleep(0.5)
            number_button = {}
            en_number = ['zero', 'one', 'two', 'third', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'point']
            for j, num in enumerate(en_number):
                number_button[j] = self.driver.find_element_by_xpath('//android.widget.TextView[@resource-id="com.shark.jizhang:id/%s"]' % num)
            number_button[0] = self.driver.find_element_by_xpath('//android.widget.TextView[@text="0"]')
            self.input_amount(number_button, amount)

            # 输入时间
            # 点击“今天”图片
            time.sleep(0.5)
            self.driver.find_element_by_xpath(
                '//android.widget.ImageView[@resource-id="com.shark.jizhang:id/calendarIcon"]').click()
            datelist = date.split('/')
            number_pickers = self.driver.find_elements_by_id('android:id/numberpicker_input')
            # 通过滑动更改时间
            beforeB = self.driver.find_elements_by_class_name('android.widget.Button')[0].size
            self.single_bounds = beforeB['height']
            if not self.swipe_date(number_pickers[2], datelist[2]) or not self.swipe_date(number_pickers[1], datelist[1]) or not self.swipe_date(number_pickers[0], datelist[0]):
                print('[*] %d date swipe wrong: %s %s %s %s\n' % (i, date, category, amount, remark))
                with open('run.log', 'a', encoding='utf-8') as f:
                    f.write('[*] %d date swipe wrong: %s %s %s %s\n' % (i, date, category, amount, remark))
                # 后退两次
                self.driver.keyevent(4)
                self.driver.keyevent(4)
                continue

            # 确认时间
            self.driver.find_element_by_xpath('//android.widget.TextView[@resource-id="com.shark.jizhang:id/dialog_dashboard_date_accept"]').click()

            # 点击完成
            done = self.driver.find_element_by_xpath('//android.widget.TextView[@resource-id="com.shark.jizhang:id/done"]')
            done.click()
            print('Write %d items: %s %s %s %s\n' % (i, date, category, amount, remark))
            with open('run.log', 'a', encoding='utf-8') as f:
                f.write('Write %d items: %s %s %s %s\n' % (i, date, category, amount, remark))

if __name__ == '__main__':
    unittest.main()
