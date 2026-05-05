from datetime import datetime

greetings = []
current_time = datetime.now()

moring = [g for g in greetings if g ['hour'] < 12]
evening = [g for g in greetings if g ['hour'] >= 12]

def show_moring():
    moring_list = [g for g in greetings if g ['hour'] < 12]
    update_greetings(moring_list) 

    def show_evening():
        evening_list = [g for g in greetings if g ['hour'] >= 12]
        update_greetings(evening_list)
        