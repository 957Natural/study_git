import pytest
import os
if __name__ == '__main__':
     pytest.main(['testcase/test_site_configuration.py',
         '--agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
         '-vs',
         '-n=4',
         '--alluredir',
         './report/tmp',
         '--clean-alluredir'])
     os.system(r"allure generate ./report/tmp -o ./report/webreport --clean")
