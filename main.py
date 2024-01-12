import tkinter as tk  # interface
from textblob import TextBlob  # sentimental analysis
from newspaper import Article

def Summerize():
    # summarise the news
    url = url_text.get('1.0','end').strip()
    article = Article(url)

    article.download()
    article.parse()

    article.nlp()

    analysis = TextBlob(article.text)

    title_text.config(state='normal')
    auther_text.config(state='normal')
    publish_text.config(state='normal')
    summery_text.config(state='normal')
    sen_text.config(state='normal')

    title_text.delete('1.0','end')
    title_text.insert('1.0',article.title)

    auther_text.delete('1.0', 'end')
    auther_text.insert('1.0', article.authors)

    publish_text.delete('1.0', 'end')
    publish_text.insert('1.0', str(article.publish_date))

    summery_text.delete('1.0', 'end')
    summery_text.insert('1.0', article.summary)

    sen_text.delete('1.0', 'end')
    sen_text.insert('1.0', f"{'positive' if analysis.polarity > 0 else 'negative' if analysis.polarity < 0 else 'neutral'}")

    title_text.config(state='disable')
    auther_text.config(state='disable')
    publish_text.config(state='disable')
    summery_text.config(state='disable')
    sen_text.config(state='disable')


root = tk.Tk()
root.title("News analyser")
root.geometry('1200x600')

tlabel = tk.Label(root, text="Title")
tlabel.pack()

title_text = tk.Text(root, height=1, width=120)
title_text.config(state='disable', bg='#dddddd')
title_text.pack()

alabel = tk.Label(root, text="Authors")
alabel.pack()

auther_text = tk.Text(root, height=1, width=120)
auther_text.config(state='disable', bg='#dddddd')
auther_text.pack()

plabel = tk.Label(root, text="Publish Date")
plabel.pack()

publish_text = tk.Text(root, height=1, width=120)
publish_text.config(state='disable', bg='#dddddd')
publish_text.pack()

slabel = tk.Label(root, text="Summery")
slabel.pack()

summery_text = tk.Text(root, height=15, width=120)
summery_text.config(state='disable', bg='#dddddd')
summery_text.pack()

senlabel = tk.Label(root, text="Sentiment")
senlabel.pack()

sen_text = tk.Text(root, height=1, width=120)
sen_text.config(state='disable', bg='#dddddd')
sen_text.pack()

ulabel = tk.Label(root, text="Url")
ulabel.pack()

url_text = tk.Text(root, height=1, width=120)
url_text.pack()

btn = tk.Button(root, text='Summerize', command=Summerize)
btn.pack()

root.mainloop()
