from src.repository.Text_repo import get_text_repo
from src.services.Game_services import Game_services, Settings

from src.domain.Board import Board
from src.UI.UI import UI


'''
    create repo
'''
repo = get_text_repo("data.txt")
'''
    create a service with 4 board and the repo
'''
serv= Game_services(Board(),Board(),Board(),Board(),repo)
'''


    create a settings obj
'''
settings = Settings()

'''
    create the UI
'''
ui = UI(serv,settings)
'''
    start the app
'''
ui.run()


