def print_func_name(func_name, *args):
    func_name = func_name.__name__.replace("_", " ").title()
    print(f"\nName of function : '{func_name}'. ")
    for arg in args:
        print(f"Function arguments : {arg}")


def open_browser(browser_name):
    print_func_name(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    print_func_name(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    print_func_name(find_registration_button_on_login_page, page_url, button_text)


open_browser('Chrome')
go_to_companyname_homepage('https://google.com/')
find_registration_button_on_login_page('https://google.com/', 'Войти')