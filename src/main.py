from src.webscrape.application import App

def main():
    travian_helper = App()
    travian_helper.run()
    travian_helper.login()
    travian_helper.serverChooser()
    travian_helper.getInfraView()
    travian_helper.getFieldView()

if __name__ == '__main__':
    main()
