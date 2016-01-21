label event_loc_wcm_0_no1:
    show wcm
    python:
        st1 = getChar('male')
    show expression 'pic/locations/school/wcm/no1.png' at top as tempPic
    'Зайдя в туалет, вы увидели, что [st1.fname] стоит, и курит сигарету.'
    if st1.getLoy() > 50:
        'Заметив вас, он вежливо здоровается и продолжает курить.'
    else:
        'Заметив вас, он пытается выкинуть сигарету.'
    menu:
        'Наказать':
            $ scoldWho = [st1]
            jump scoldAll
        'Проигнорировать':
            'Вы делаете вид, как будто ничего не произошло, и вы ничего не заметили. [st1.fname] с благодарностью смотрит на вас.'
            $ st1.setLoy(10)
    $ move(curloc)
    
label event_loc_wcm_20_mid1:
    show wcm
    python:
        st1 = getChar('male')
        st2 = getChar('female')
        hadSex(st1,st2)
    'Зайдя в туалет, вы услышали странный стон из кабинки. И женское хихикание. Ну мало ли, может быть от облегчения?'
    'Вы уже собирались уходить, как вдруг поняли, что зашли в мужской туалет. И женское хихикание тут немного неместно.'
    menu:
        'Заглянуть из соседней кабинки':
            show expression 'pic/locations/school/wcm/mid1.jpg' at top as tempPic
            'Аккуратно заглянув в кабинку, вы увидели там любопытную картинку. [st1.fname] стоял и дрочил перед унитазом, в то время, пока [st2.fname] массировала его яички и поглаживала по бёдрам. Спустя минуту парень снова застонал, и начал кончать. [st1.fname] снова глупо захихикала.'
            st1.say 'Посмотрела? - немного угруюмо спросил школьник, повернув голову в вашу сторону.'
            st2.say 'Ага, прикольно всё у вас.  - улыбнулась [st2.fname]'
            st1.say 'Пойдём уже!'
            $ st2.incCorr(5)
        'Не проверять':
            player.say '"Мало ли что там... Не будем нарушать уединения."'
    $ move(curloc)
    
label event_loc_wcm_0_mid2:
    show wcm
    python:
        if dikovna.getCorr() < 30:
            skipEvent()
        st1 = dikovna
        hadSex(st1)
    show movie
    play movie "pic/locations/school/wcm/mid4.gif.webm" loop
    'Пройдясь по туалету, вы увидели [st1.fname] [st1.lname], ласкающую свой немаленький член прямо напротив писсуара.'
    menu:
        'Отчитать':
            player.say 'Что здесь чёрт возьми происходит, [st1.name]? - сурово сдвинув брови, спрашиваете вы учительницу.'
            st1.say 'I am sorry, I am really sorry, - извиняется англичанка, пытаясь спрятать свой член назад под юбку.'
            'Очевидно, что в таком состоянии задача эта не из простейших. Вы наблюдаете за её попытками справиться с членом, пока вдруг не замечаете, что очередное движение не приводит к предсказуемому финалу.'
            stop movie
            hide movie
            show expression 'pic/locations/school/wcm/mid4a.png' at top as tempPic
            'Из члена вырывается поток спермы, забрызгивая всё вокруг.'
            st1.say 'Oh my God, I am so sorry! - [st1.fname] кидается к вам, пытаясь вытереть с Вас свою сперму.'
            player.say 'Достаточно! Уходите! - сурово показываете вы пальцем на дверь, не желая дальше развивать этот фарс.'
            $ player.coverSperm('грудь','попа','ноги')

        'Помочь' if player.getCorr() > 50 and player.getLust() > 40:
            player.say 'Постойте, давайте сделаем всё к обоюдному удовольствию, - попросили вы учительницу, разглядывая её член.'
            play movie "pic/locations/school/wcm/mid5b.gif.webm" loop
            'Аккуратно сняв с себя всё мешающееся, вы завели сотрудницу в ближайшую кабинку, и со стоном ввели её толстенный член в себя. Ваша влажная киска покорно растянулась, принимая в себя мужской орган, и Вы застонали, не в силах сдержать нарастающего внизу живота удовлетворения.'
            '[st1.fname] [st1.lname] совсем не двигалась, позволяя Вам пользоваться её телом как заблагорассудится. Чем Вы и воспользовались. Наминая свои полные груди, Вы скакали на этом великолепном члене, умело доводя себя до оргазма.'
            player.say 'Конча-ю-у-у-у!!!'
            'Вы закричали, когда ощутили тугую струю спермы ударившую в вашу матку. Мышцы влагалища ещё сильнее обхватили ствол, унося вас на вершину оргазма.'
            player.say 'Это было прекрасно! - улыбнули вы англичанке, - В следующий раз приходите с вашей проблемой прямо в мой кабинет.'
            stop movie
            hide movie
            python:
                hadSex(st1,player)
                player.coverSperm('вагина','ноги')
    $ move(curloc)
    
label event_loc_wcm_45_mid3:
    show wcm
    python:
        st1 = getChar('male')
        st2 = getChar('female')
        hadSex(st1,st2)
    'Зайдя в туалет, вы услышали довольно громкие стоны из кабинки.'
    menu:
        'Подсмотреть из соседней кабинки':
            show expression 'pic/locations/school/wcm/mid2.jpg' at top as tempPic
            'Зайдя в соседнюю кабинку, вы прильнули в небольшой щели в стенке, и попытались рассмотреть, что же происходит рядом с вами. Рядом [st2.fname] и [st1.fname] предавались большой любви. Сразу было видно, что у парня любовь большая, а у девочки она узкая.'
            'Ваши ноздри щекотал приятный мускусный запах пота трахающейся парочки. Ученица не скрываясь стонала и подпрыгивала на члене, плотно зажимая его между ног. [st2.fname] прижимал её своими руками к телу, и бёдрами пытался протолкнуть свой ствол поглубже.'
            'Вы неволей залюбовались его мускулистыми руками и членом, и опустили свои руки ближе к киске, начиная её медленно поглаживать. Вас остановило только то, что вы сейчас находитесь в мужском туалете. Надо решаться, либо наказывать их, либо уходить.'
            menu:
                'Наказать':
                    $ scoldWho = [st1,st2]
                    jump scoldAll
                'Аккуратно уйти':
                    $ st1.incLoy(5)
                    $ st2.incLoy(5)
                    pass
        'Не проверять':
            player.say '"Мало ли что там... Не будем нарушать уединения."'
    $ move(curloc)    
    
label event_loc_wcm_15_mid4:
    show wcm
    python:
        st1 = getChar('male')
        hadSex(st1)
    'Зайдя в туалет, вы услышали чпокающие звуки из кабинки.'
    menu:
        'Подсмотреть':
            show expression 'pic/locations/school/wcm/mid3.jpg' at top as tempPic
            'Вы остророжно приоткрываете дверь, и видите своего ученика, который яростно наяривает свой член. Похоже он черезчур перевозбуждён после физкультуры, и даже не успел переодеться.'
            player.say '"Хммм. Может помочь ему сбросить напряжение?"'
            menu:
                'Помочь'  if player.getCorr() > 40:
                    show expression 'pic/locations/school/wcm/mid3a.jpg' at top as tempPic
                    player.say 'Давай я тебе помогу, - сказали Вы ученику, заходя в кабинку и нежно обхватывая его сзади. Ваши руки блуждали по телу школьника, пока не достигли члена, вызвав у него тихий стон. Вы начали массировать этот мускулистый орган, поглаживая спину парня другой рукой.'
                    player.say 'Наклонись немного, чтобы мы побыстрее закончили, - попросили вы, ставя ученика в нужную вам позу. Смазав указательный палец в слюне, вы неспеша вставили его в анус, преодолевая сопротивление парня. Быстро найдя бугорочек простаты, вы приступили к массажу, не забывая передёргивать ствол в вашей правой руке. [st1.fname] напрягся, и его член начал дёргаться, выстреливая из себя струи спермы, заливающие кабинку и ваши руки.'
                    player.say 'Вот и молодец! А теперь иди, скоро начнуться занятия. - отправили вы довольного ученика, хлопнув по его попе.'
                    $ st1.incCorr(5)
                    $ st1.setLust(0)
                    $ player.incCorr(3)
                'Аккуратно закрыть дверь и выйти':
                    pass
        'Выйти':
            player.say '"Мало ли что там... Не будем нарушать уединения."'
    $ move(curloc)