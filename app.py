from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

app = Flask(__name__)

my_bot = ChatBot(name='PyBot', read_only=True,
                 logic_adapters=['chatterbot.logic.BestMatch'])
small_talk = ['hi there!',
              'hi!',
              'how do you do?',
              'how are you?',
              'fine.',
              'fine',
              'always cool.',
              'i\'m ok',
              'glad to hear that.',
              'i\'m fine',
              'glad to hear that.',
              'i feel awesome',
              'excellent, glad to hear that.',
              'not so good',
              'sorry to hear that.',
              'what\'s your name?',
              'i\'m pybot. ask me a question, please.'
              'Can we know about your college Fee Structure'
              'Yeah Sure:)\n $xx - CSE \n $xx - EEE \n $ECE - $xx'
              'For Management quota'
              'For management quota based on your grades starting with normal college fee'
              'Hostel Fee and Hostel environment'
              'At first hostel fee is same for all is $XXX . We will provide home environment'
              'Any recent events done in your college'
              'XXXX events with brochure'
              'Tell me more about your college and events'
              'Why dont you contact with our students do get know our college'
              'Yeah,Sure'
              'contact some student through outer system'
              ]

math_talk_1 = ['college fee structure',
              'Yeah Sure:)\n $xx - CSE \n $xx - EEE \n $ECE - $xx'
               ,'can we know about your college fee structure',
              'Yeah Sure:)\n $xx - CSE \n $xx - EEE \n $ECE - $xx']

math_talk_2 = ['for management quota',
              'For management quota based on your grades starting with normal college fee','management quota',
              'For management quota based on your grades starting with normal college fee']
math_talk_3 = ['hostel fee and hostel environment',
              'At first hostel fee is same for all is $XXX . We will provide home environment']
math_talk_4 = ['any recent college events',
              'XXXX events with brochure',
               'college events',
               'XXXX events with brochure'
               ]
math_talk_5 = ['tell me more about your college events',
              'Why dont you contact with our students do get know our college']
math_talk_6 = ['Yeah,Sure',
              'contact some student through outer system']
math_talk_7 = []
math_talk_8 = []



list_trainer = ListTrainer(my_bot)
for item in (small_talk, math_talk_1, math_talk_2,math_talk_3,math_talk_4,math_talk_5,math_talk_6):

    list_trainer.train(item)
#english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
#trainer = ChatterBotCorpusTrainer(my_bot)
#trainer.train("chatterbot.corpus.english")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(my_bot.get_response(userText))


if __name__ == "__main__":
    app.run()