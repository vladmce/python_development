"""
Acesta este un joculet care va testa nivelul de cunoastere al verbelor neregulate din limba engleza.
"""
import random
import simple_colors


print("Hello! This is a test meant to analyze your level of knowledge regarding irregular verbs in English.")
print("You will get 30 random verbs (Romanian translation) and you will have to add the 3 English forms for each of those verbs. ")
print("You will get 3 points for each good verb (1/each correct form), summing up to a total of 90.")
print("If all the forms you provide are correct, you will get a bonus of 10 points in the end, leading to a total of 100.")
print("Hit ENTER when you're ready!")

unneeded_1 = input("")
greseli = 0
scor = 0
a = 1

# Verbele Neregulate (Liste)

verb0=['a rasari / a se ridica','arise', 'arose', 'arisen']
verb1=['a se trezi', 'awake', 'awoke', 'awoken']

verb2=['a fi / a exista', 'be', 'was/were', 'been']
verb3=['a supota / a suferi', 'bear', 'bore', 'borne']
verb4=['a bate / a lovi', 'beat', 'beat', 'beaten']
verb5=['a deveni', 'become', 'became', 'become']
verb6=['a (se) indoi / a (se) apleca', 'bend', 'bent', 'bent']
verb7=['a paria', 'bet', 'bet', 'bet']
verb8=['a lega / a uni', 'bind', 'bound', 'bound']
verb9=['a musca', 'bite', 'bit', 'bitten']
verb10=['a sangera', 'bleed', 'bled', 'bled']
verb11=['a sufla / a bate vantul / a sufla nasul', 'blow', 'blew', 'blown']
verb12=['a sparge / a strica', 'break', 'broke', 'broken']
verb13=['a aduce', 'bring', 'brought', 'brought']
verb14=['a transmite (la radio sau TV)', 'broadcast', 'broadcast', 'broadcast']
verb15=['a construi', 'build', 'built', 'built']
verb16=['a arde', 'burn', 'burnt', 'burnt']
verb17=['a lovi / a pedepsi', 'bust', 'bust', 'bust']
verb18=['a cumpara', 'buy', 'bought', 'bought']

verb19=['a arunca - starts with c', 'cast', 'cast', 'cast']
verb20=['a prinde', 'catch', 'caught', 'caught']
verb21=['a alege', 'choose', 'chose', 'chosen']
verb22=['a (se) agata (starts with c)', 'cling', 'clung', 'clung']
verb23=['a veni', 'come', 'came', 'come']
verb24=['a costa', 'cost', 'cost', 'cost']
verb25=['a se furisa - starts with c', 'creep', 'crept', 'crept']
verb26=['a taia', 'cut', 'cut', 'cut']

verb27=['a negocia', 'deal', 'dealt', 'dealt']
verb28=['a sapa', 'dig', 'dug', 'dug']
verb29=['a face - starts with d', 'do', 'did', 'done']
verb30=['a trage / a desena', 'draw', 'drew', 'drawn']
verb31=['a visa', 'dream', 'dreamt', 'dreamt']
verb32=['a bea', 'drink', 'drank', 'drunk']
verb33=['a conduce masina', 'drive', 'drove', 'driven']

verb34=['a manca', 'eat', 'ate', 'eaten']

verb35=['a cadea', 'fall', 'fell', 'fallen']
verb36=['a hrani', 'feed', 'fed', 'fed']
verb37=['a simti', 'feel', 'felt', 'felt']
verb38=['a (se) lupta / a (se) certa', 'fight', 'fought', 'fought']
verb39=['a gasi', 'find', 'found', 'found']
verb40=['a (se) potrivi', 'fit', 'fit', 'fit']
verb41=['a zbura', 'fly', 'flew', 'flown']
verb42=['a interzice', 'forbid', 'forbade', 'forbidden']
verb43=['a prognoza (vremea)', 'forecast', 'forecast', 'forecast']
verb44=['a prevedea', 'foresee', 'foresaw', 'foreseen']
verb45=['a prezice', 'foretell', 'foretold', 'foretold']
verb46=['a uita', 'forget', 'forgot', 'forgotten']
verb47=['a ierta', 'forgive', 'forgave', 'forgiven']
verb48=['a parasi (starts with f)', 'forsake', 'forsook', 'forsaken']
verb49=['a ingheta / a congela', 'freeze', 'froze', 'frozen']

verb50=['a primi / a obtine', 'get', 'got', 'got']
verb51=['a da', 'give', 'gave', 'given']
verb52=['a merge / a se duce', 'go', 'went', 'gone']
verb53=['a macina', 'grind', 'ground', 'ground']
verb54=['a creste', 'grow', 'grew', 'grown']

verb55=['a agata / a atarna (starts with h)', 'hang', 'hung', 'hung']
verb56=['a avea', 'have', 'had', 'had']
verb57=['a auzi', 'hear', 'heard', 'heard']
verb58=['a (se) ascunde', 'hide', 'hid', 'hidden']
verb59=['a lovi / a izbi', 'hit', 'hit', 'hit']
verb60=['a tine / a sustine', 'hold', 'held', 'held']
verb61=['a rani', 'hurt', 'hurt', 'hurt']

verb62=['a tine', 'keep', 'kept', 'kept']
verb63=['a inghenunchia', 'kneel', 'knelt', 'knelt']
verb64=['a croseta', 'knit', 'knit', 'knit']
verb65=['a sti', 'know', 'knew', 'known']

verb66=['a pune / a aseza / a pune masa', 'lay', 'laid', 'laid']
verb67=['a conduce (o tara, o echipa)', 'lead', 'led', 'led']
verb68=['a (se) apleca / a (se) rezema', 'lean', 'leant', 'leant']
verb69=['a sari', 'leap', 'leapt', 'leapt']
verb70=['a invata', 'learn', 'learnt', 'learnt']
verb71=['a pleca / a parasi', 'leave', 'left', 'left']
verb72=['a da cu imprumut', 'land', 'lent', 'lent']
verb73=['a lasa / a permite', 'let', 'let', 'let']
verb74=['a sta intins / a zacea', 'lie', 'lay', 'lain']
verb75=['a da foc / a aprinde', 'light', 'lit', 'lit']
verb76=['a citi pe buze', 'lip-read', 'lip-read', 'lip-read']
verb77=['a pierde', 'lose', 'lost', 'lost']

verb78=['a face - starts with m', 'make', 'made', 'made']
verb79=['a insemna', 'mean', 'meant', 'meant']
verb80=['a (se) intalni', 'meet', 'met', 'met']
verb81=['a face ceva gresit', 'misdo', 'misdid', 'misdone']
verb82=['a auzi gresit', 'mishear', 'mishear', 'mishear']
verb83=['a aseza gresit', 'mislay', 'mislaid', 'mislaid']
verb84=['a induce in eroare', 'mislead', 'misled', 'misled']
verb85=['a ortografia gresit', 'misspell', 'misspelt', 'misspelt']
verb86=['a gresi / a confunda', 'mistake', 'mistook', 'mistaken']
verb87=['a intelege gresit', 'misunderstand', 'misunderstood', 'misunderstood']
verb88=['a cosi / a tunde iarba', 'mow', 'mowed', 'mown']

verb89=['a intrece', 'outdo', 'outdid', 'outdone']
verb90=['a depasi (pe sosea) - out...', 'outride', 'outrode', 'outridden']
verb91=['a invinge', 'overcome', 'overcame', 'overcome']
verb92=['a bea prea mult', 'overdrink', 'overdrank', 'overdrunk']
verb93=['a manca in exces', 'overeat', 'overate', 'overeaten']
verb94=['a hrani in exces', 'overfeed', 'overfed', 'overfed']
verb95=['a surprinde', 'overhear', 'overheard', 'overheard']
verb96=['a plati prea mult', 'overpay', 'overpaid', 'overpaid']
verb97=['a depasi - ...ride', 'override', 'overrode', 'overridden']
verb98=['a depasi in fuga', 'overrun', 'overran', 'overrun']
verb99=['a supraveghea', 'oversee', 'oversaw', 'overseen']
verb100=['a vinde la suprapret', 'oversell', 'oversold', 'oversold']
verb101=['a dormi in exces', 'oversleep', 'overslept', 'overslept']
verb102=['a intrece - ...take', 'overtake', 'overtook', 'overtaken']
verb103=['a gandi in exces', 'overthink', 'overthought', 'overthought']
verb104=['a rasturna', 'overthrow', 'overthrew', 'overthrown']

verb105=['a lua parte', 'partake', 'partook', 'partaken']
verb106=['a pleda', 'plead', 'pled', 'pled']
verb107=['a dovedi', 'prove', 'proved', 'proven']
verb108=['a pune', 'put', 'put', 'put']

verb109=['a renunta', 'quit', 'quit', 'quit']

verb110=['a citi', 'read', 'read', 'read']
verb111=['a scapa de ...', 'rid', 'rid', 'rid']
verb112=['a rasari / a (se) ridica', 'rise', 'rose', 'risen']
verb113=['a fugi', 'run', 'ran', 'run']
verb114=['a calari', 'ride', 'rode', 'ridden']
verb115=['a suna', 'ring', 'rang', 'rung']

verb116=['a taia cu fierastraul', 'saw', 'sawed', 'sawn']
verb117=['a spune / a zice - starts with s', 'say', 'said', 'said']
verb118=['a vedea', 'see', 'saw', 'seen']
verb119=['a cauta', 'seek', 'sought', 'sought']
verb120=['a vinde', 'sell', 'sold', 'sold']
verb121=['a trimite', 'send', 'sent', 'sent']
verb122=['a seta / a aseza / a aranja', 'set', 'set', 'set']
verb123=['a coase', 'sew', 'sewed', 'sewn']
verb124=['a (se) scutura / a da mana', 'shake', 'shook', 'shaken']
verb125=['a (se) barbieri', 'shave', 'shaved', 'shaven']
verb126=['a straluci', 'shine', 'shone', 'shone']
verb127=['a impusca', 'shoot', 'shot', 'shot']
verb128=['a arata', 'show', 'showed', 'shown']
verb129=['a se micsora', 'shrink', 'shrank', 'shrunk']
verb130=['a inchide', 'shut', 'shut', 'shut']
verb131=['a canta', 'sing', 'sang', 'sung']
verb132=['a sta asezat', 'sit', 'sat', 'sat']
verb133=['a se scufunda', 'sink', 'sank', 'sunk']
verb134=['a injunghia', 'slay', 'slew', 'slain']
verb135=['a dormi', 'sleep', 'slept', 'slept']
verb136=['a aluneca', 'slide', 'slid', 'slid']
verb137=['a arunca cu prastia', 'sling', 'slung', 'slung']
verb138=['a despica', 'slit', 'slit', 'slit']
verb139=['a mirosi', 'smell', 'smelt', 'smelt']
verb140=['a se furisa - starts with s', 'sneak', 'snuck', 'snuck']
verb141=['a semana', 'sow', 'sowed', 'sown']
verb142=['a vorbi', 'speak', 'spoke', 'spoken']
verb143=['a accelera', 'speed', 'sped', 'sped']
verb144=['a ortografia / a vraji', 'spell', 'spelt', 'spelt']
verb145=['a cheltui / a petrece (timpul)', 'spend', 'spent', 'spent']
verb146=['a varsa', 'spill', 'spilt', 'spilt']
verb147=['a (se) rasuci', 'spin', 'span', 'spun']
verb148=['a scuipa', 'spit', 'spat', 'spat']
verb149=['a taia / a despica', 'split', 'split', 'split']
verb150=['a strica / a rasfata', 'spoil', 'spoilt', 'spoilt']
verb151=['a hrani cu lingura', 'spoon-feed', 'spoon-fed', 'spoon-fed']
verb152=['a imprastia', 'spread', 'spread', 'spread']
verb153=['a sari / a tasni', 'spring', 'sprang', 'sprung']
verb154=['a sta in picioare / a suporta', 'stand', 'stood', 'stood']
verb155=['a fura', 'steal', 'stole', 'stolen']
verb156=['a lipi / a se bloca', 'stick', 'stuck', 'stuck']
verb157=['a intepa (insecte)', 'sting', 'stang', 'stung']
verb158=['a mirosi urat', 'stink', 'stank', 'stunk']
verb159=['a invia / a imprastia', 'strew', 'strewed', 'strewn']
verb160=['a merge agale', 'stride', 'strode', 'stridden']
verb161=['a lovi / a izbi / a soca / a uimi', 'strike', 'struck', 'struck']
verb162=['a insira', 'string', 'strung', 'strung']
verb163=['a se stradui', 'strive', 'strove', 'striven']
verb164=['a face insolatie', 'sunburn', 'sunburnt', 'sunburnt']
verb165=['a jura / a injura', 'swear', 'swore', 'sworn']
verb166=['a matura', 'sweep', 'swept', 'swept']
verb167=['a se umfla / a se inflama', 'swell', 'swelled', 'swollen']
verb168=['a inota', 'swim', 'swam', 'swum']
verb169=['a (se) legana', 'swing', 'swung', 'swung']

verb170=['a lua', 'take', 'took', 'taken']
verb171=['a invata pe cineva', 'teach', 'taught', 'taught']
verb172=['a sfasia / a rupe in bucati', 'tear', 'tare', 'torn']
verb173=['a spune / a povesti', 'tell', 'told', 'told']
verb174=['a face test unei masini', 'test-drive', 'test-drove', 'test-driven']
verb175=['a face test unui avion', 'test-fly', 'test-flew', 'test-flown']
verb176=['a crede / a gandi - starts with t', 'think', 'thought', 'thought']
verb177=['a arunca - starts with t', 'throw', 'threw', 'thrown']
verb178=['a infige', 'thrust', 'thrust', 'thrust']
verb179=['a tarsai picioarele', 'tread', 'trod', 'trodden']
verb180=['a tasta la masina de scris', 'typewrite', 'typewrote', 'typewritten']

verb181=['a deznoda', 'unbend', 'unbent', 'unbent']
verb182=['a dezlega', 'underbind', 'underbound', 'underbound']
verb183=['a hrani foarte putin / a subnutri', 'underfeed', 'underfed', 'underfed']
verb184=['a trece prin ceva greu', 'undergo', 'underwent', 'undergone']
verb185=['a vinde la pret mic', 'undersell', 'undersold', 'undersold']
verb186=['a intelege', 'understand', 'understood', 'understood']
verb187=['a prelua ceva', 'undertake', 'undertook', 'undertaken']
verb188=['a desface orice', 'undo', 'undid', 'undone']


verbe = [verb0, verb1, verb2, verb3, verb4, verb5, verb6, verb7, verb8, verb9, verb10, verb11, verb12, verb13, verb14, verb15, verb16, verb17, verb18, verb19, verb20, verb21, verb22, verb23, verb24, verb25, verb26, verb27, verb28, verb29, verb30, verb31, verb32, verb33, verb34, verb35, verb36, verb37, verb38, verb39, verb40, verb41, verb42, verb43, verb44, verb45, verb46, verb47, verb48, verb49, verb50, verb51, verb52, verb53, verb54, verb55, verb56, verb57, verb78, verb59, verb60, verb61, verb62, verb63, verb64, verb65, verb66, verb67, verb68, verb69, verb70, verb71, verb72, verb73, verb74, verb75, verb76, verb77, verb78, verb79, verb80, verb81, verb82, verb83, verb84, verb85, verb86, verb87, verb88, verb89, verb90, verb91, verb92, verb93, verb94, verb95, verb96, verb97, verb98, verb99, verb100, verb101, verb102, verb103, verb104, verb105, verb106, verb107, verb108, verb109, verb110, verb111, verb112, verb113, verb114, verb115, verb116, verb117, verb118, verb119, verb120, verb121, verb122, verb123, verb124, verb125, verb126, verb127, verb128, verb129, verb130, verb131, verb132, verb133, verb134, verb135, verb136, verb137, verb138, verb139, verb140, verb141, verb142, verb143, verb144, verb145, verb146, verb147, verb148, verb149, verb150, verb151, verb152, verb153, verb154, verb155, verb156, verb157, verb158, verb159, verb160, verb161, verb162, verb163, verb164, verb165, verb166, verb167, verb168, verb169, verb170, verb171, verb172, verb173, verb174, verb175, verb176, verb177, verb178, verb179, verb180, verb181, verb182, verb183, verb184, verb185, verb186, verb187, verb188]

# Selectare verb
def selectie_verb(lista_verbe):
    numar_verb = (random.randint(0, len(lista_verbe) - 1))
    verb_selectat = lista_verbe[numar_verb]
    return verb_selectat

while a < 31:
    verb_actual = selectie_verb(verbe)
    print("")
    print(f"Round {a}")
    print("")
    a = a + 1
    print(f"The verb is: {verb_actual[0]}")
    forma_1 = input("Input the first form -> ")
    forma_2 = input("Input the second form -> ")
    forma_3 = input("Input the third form -> ")
    print("")

    if verb_actual[1] == forma_1 or "to " + verb_actual[1] == forma_1 or "to" + verb_actual[1] == forma_1:
        scor = scor + 1
        print(simple_colors.green("First form: correct!"))
    else:
        greseli = greseli + 1
        print(simple_colors.red(f"First form WRONG! Correct form: {verb_actual[1]}"))

    if verb_actual[2] == forma_2 or "to " + verb_actual[2] == forma_2 or "to" + verb_actual[2] == forma_2:
        scor = scor + 1
        print(simple_colors.green("Second form: correct!"))
    else:
        greseli = greseli + 1
        print(simple_colors.red(f"Second form WRONG! Correct form: {verb_actual[2]}"))

    if verb_actual[3] == forma_3 or "to " + verb_actual[3] == forma_3 or "to" + verb_actual[3] == forma_3:
        scor = scor + 1
        print(simple_colors.green("Third form: correct!"))
    else:
        greseli = greseli + 1
        print(simple_colors.red(f"Third form WRONG! Correct form: {verb_actual[3]}"))

    print("")
    if a < 31:
        next = input("Press Enter to move on!")
    else:
        next = input("You have finished. Press Enter to see your result!")
    verbe.remove(verb_actual)
    print("")

if scor == 90:
    scor = 100
else:
    pass

if greseli == 0:
    print(simple_colors.green(f"CONGRATULATIONS! You have finished with a brilliant result!\n"
          f"Your total score is {scor} points out of 100! You made {greseli} mistakes!"))
elif greseli == 1:
    print(simple_colors.green(f"Well Done! You have finished with a almost perfect result!\n"
          f"Your total score is {scor} points out of 100! You made {greseli} mistake!"))
elif greseli > 1 and greseli < 4:
    print(simple_colors.green(f"Good! You have finished with a nice  result!\n"
          f"Your total score is {scor} points out of 100! You made {greseli} mistakes!"))
elif greseli >= 4 and greseli < 7:
    print(simple_colors.yellow(f"So and so! You have finished with a not so bad result, but there is room for improvement!\n"
          f"Your total score is {scor} points out of 100! You made {greseli} mistakes!"))
elif greseli >= 7 and greseli < 10:
    print(simple_colors.yellow(f"Not so good...! You have finished with an average result. Train more and keep up the good work!\n"
          f"Your total score is {scor} points out of 100! You made {greseli} mistakes!"))
elif greseli >= 10 and greseli < 13:
    print(simple_colors.red(f"Bad..! You have finished with a low result. Train more and you'll see improvements!\n"
          f"Your total score is {scor} points out of 100! You made {greseli} mistakes!"))
else:
    print(simple_colors.red(f"TERRIBLE!!! You have finished with a BAD result. Take some time and train yourself in this!\n"
          f"Your total score is {scor} points out of 100! You made {greseli} mistakes!"))
