from src.webscrape.application import App

def main():
    travian_helper = App()
    travian_helper.login()
    travian_helper.server_chooser()
    travian_helper.get_infra_view()
    travian_helper.get_field_view()

if __name__ == '__main__':
    main()
