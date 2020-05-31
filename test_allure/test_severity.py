import allure

@allure.feature('test_module_01')
@allure.story('test_story_01')
@allure.severity('blocker')
def test_case_01():
    '''用例描述：Test case 01'''
    pass

@allure.feature('test_module_01')
@allure.story('test_story_02')
@allure.severity('normal')
def test_case_02():
    '''用例描述：Test case 02'''
    pass
