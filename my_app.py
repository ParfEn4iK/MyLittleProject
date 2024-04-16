from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel,QVBoxLayout, QRadioButton ,QHBoxLayout, QGroupBox

app = QApplication([])
main_win=QWidget()

main_win.setWindowTitle('The Best Game Ever')
main_win.move(900,70)
main_win.resize(400,200)
btn_OK=QPushButton('ответить')
lb_Question=QLabel('Кто создал undertale?')

RadioGroupBox=QGroupBox('Варианты ответов:')
rbtn1=QRadioButton('Notch')
rbtn2=QRadioButton('Toby fox')
rbtn3=QRadioButton('Robtop')
rbtn4=QRadioButton('Gabe Newell')

layout_ans1=QHBoxLayout()
layout_ans2=QVBoxLayout()
layout_ans3=QVBoxLayout()

layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

layout_line1=QHBoxLayout()
layout_line2=QHBoxLayout()
layout_line3=QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignHCenter ))
layout_line2.addWidget(RadioGroupBox)

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch = 2)
layout_line3.addStretch(1)

layout_card=QVBoxLayout()


layout_card.addLayout(layout_line1,stretch=2)
layout_card.addLayout(layout_line2,stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3,stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)


main_win.setLayout(layout_card)
main_win.show()
app.exec_()

