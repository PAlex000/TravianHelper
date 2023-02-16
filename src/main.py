from webscrape.application import App

def main():
    travian_helper = App()
    travian_helper.login()
    travian_helper.server_chooser()
    travian_helper.get_infra_view()

if __name__ == '__main__':
    main()
