label event_loc_library_0_no1:
    show library
    python:
        st1 = getChar('female')
    show expression 'pic/locations/school/library/no1.jpg' at top as tempPic
    '[st1.fname] судя по всему совсем увлеклась чтением фентези и прочих Леголасов. Даже кота своего притащила, чтобы кормить его не отвлекаясь от чтения.'
    menu:
        'Попросить ученицу убрать животное':
            'Вы просите ученицу убрать кота из библиотеки, потому что он может испортить книги.'
            'Ученица нехотя прерывает чтение и, взяв кота подмышку уходит на улицу.'
            if player.getCorr() > 80:
                show expression 'pic/locations/school/library/no1_1.jpg' at top as tempPic
                player.say '"Кошки - пфф, мелкие проказники! Вот большие собаки - это да! Они и защитят, и убаюкают!"'
                'Ваши мысли затуманились картинкой того, что могло бы произойти, будь у вас собака. Как её огромный член проникает в вашу киску, как в ней раздувается узел, не давая ему выскочить из вас. Вы почти чувствуете, как увлажняется ваша распутная щёлка от подобных мыслей.'
                $ player.incLust(15)
            $ st1.incLoy(-5)
        'Не обращать внимания':
            $ st1.incLoy(5)
            'Вы решаете ничего ей не говорить. И прощаетесь.'
            if rand(1,5) == 1:
                'Как вдруг котяра с воем бросается на ближайшую полку, и раздирает несколько журналов простым прикосновением когтей! Чёрт возьми, эти игры кота встали школе в 500 монет! В наказание вы заставляете ученицу остаться после уроков.'
                $ school.budget -= 500
                $ detentions.append(st1)
    $ move(curloc)
    
label event_loc_library_0_no2:
    show library
    python:
        st1 = getChar('female')
        st2 = getChar('male')
    show expression 'pic/locations/school/library/no2.jpg' at top as tempPic
    'Заметив, что вы идёте, [st1.fname] прикрыла спиной книгу, которую она выбрала для чтения.'
    menu:
        'Узнать, что за книга':
            player.say 'Ну ка, покажи что ты там прячешь!'
            if st1.getCorr() > 20:
                show expression 'pic/locations/school/library/no2_2.jpg' at top as tempPic
                'Смущаясь, ученица протягивает вам обычную мангу с искромётным названием "Мой любимый директор". У вас не находится сил отбирать эту брошюру.'
                $ st1.incLoy(10)
            else:
                'В ответ нехотя ученица протягивает вам "Индульгенция, как способность индидуума абстрагироваться от религиозной самонедостаточности" В.Ю. Фрейта. Вы не видите в ней ничего страшного, и нехотя возвращаете книгу. Была надежда поймать что то более приземлённое, чем религиозная тема.'
                player.say '"Она что, в монашки собралась после школы?"'
                $ st1.incLoy(-5)
        'Не обращать внимания':
            'Вы решаете не обращать внимания на странное поведение, но бросив случайный взгляд на полку, заметили цветастую корку с надписью "Крашмапутра". Уж не эту ли книгу искала ученица? Судя по её румянцу, вы не ошиблись.'
            if player.getCorr() > 60 and st2.getCorr() > 70:
                show expression 'pic/locations/school/library/no2_1.jpg' at top as tempPic
                'Не сдержавшись, вы решаете пролистать этот известный труд, и с удивлением видите, что он проиллюстрирован вполне известными вам людьми. Это [st2.name] и его мама. Подпись к картинке гласит: "И как мать обнимает своего сына, так и вы прижмите своего любовника к своему телу и слейтесь с ним в экстазе. Nбург, [str(year)] год."'
                player.say '"Однако вряд ли они мне будут доставлять проблемы с репутацией. С таким то компроматом!"'
                $ st2.incRep(25)
                $ player.incLust(10)
    $ move(curloc)
    
label event_loc_library_0_no3:
    show library
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        setLust(5,10)
    show expression 'pic/locations/school/library/no3.jpg' at top as tempPic
    '[st1.fname] и [st2.fname], сидя на полу, читают какую то брошюрку. Блин, они же так простудятся, будут болеть дома, и не посещать школу!'
    if player.getCorr() < 40:
        'Вы просите девчёнок пересесть за стол, благо строительная компания озаботилась не только стенами, но и мебелью.'
    else:
        show expression 'pic/locations/school/library/no3_1.jpg' at top as tempPic
        player.say '"Надеюсь это какой то хентай, с кучей молодых тел, множеством членов и спермы, и главное - без цензуры!"'
    $ move(curloc)
    
label event_loc_library_0_no4:
    show library
    python:
        st1 = getChar('female')
        st2 = getChar('female')
        setLust(5,5)
    show expression 'pic/locations/school/library/no4.jpg' at top as tempPic
    'Похоже [st1.fname] просто без ума от трусиков своей подружки, которая достаёт книгу с верхней полки! Или она себе просто хочет такие же?'
    if player.getCorr() > 30:
        show expression 'pic/locations/school/library/no4_1.jpg' at top as tempPic
        player.say '"Интересно, как много я не знаю про своих учениц? Может быть они уже давным давно после уроков изучают не только домашнее задание, но и свои киски?"'
        'Вы представляете, как [st1.fname] и [st2.fname] после школы заходят домой, и начинают срывать с себя форму, страстно целуясь. Как уже на кровати переплетаются их молодые тела в попытке доставить удовольствие друг дружке. Как стоны срываются с их губ, когда пальчики наконец то находят самые эрогенные точки...'
        player.say '"Да... одно непонятно, зачем мальчиком то игнорировать?"'
    $ move(curloc)
    
label event_loc_library_0_no5:
    show library
    python:
        st1 = getChar('female')
        st2 = getChar('male')
    show expression 'pic/locations/school/library/no5.jpg' as tempPic:
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    player.say '"Мыши? Всюду мыши. Так и от книг ничего не останется! Надо срочно выделить денег на котов!"'
    menu:
        'Выделить 500 монет на котов' if school.budget > 500:
            'Вы позвонили в фирму по борьбе с вредителями и вам пообещали доставить лучших крысоловов! Главное чтобы решение не оказалось хуже проблемы. Судя по всему, ученики подкармливают мышат, и особых проблем с ними пока не видно... Хотя кто знает, сколько ценной литературы вы спасли своими действиями!'
            $ school.budget -= 500
            $ setEdu(10,5)
        'Не обращать внимания':
            'Вы решили не обращать внимания на этих милых мышат, и возможно правильно сделали. Ученики очень любят с ними играть, и будут благодарны, если вы оставите их в покое!'
            $ setLoy(5,5)
            if rand(1,3) == 1:
                $ setEdu(10,-5)
    $ move(curloc)
    
label event_loc_library_0_no6:
    show library
    python:
        st1 = getChar('female')
        st2 = getChar('male')
        setLust(5,5)
    show expression 'pic/locations/school/library/no6.jpg' at top as tempPic
    'Упс! Похоже [st1.fname] упала с лестницы прямо на мимопроходящего одноклассника! Хорошо, что он смягчил падение!'
    'Или всё не так, как вам кажется? Уж слишком томительное молчание повисло, когда вы их заметили.'
    player.say 'Я пойду, прогуляюсь, я всё понимаю... Ну несчастный случай, главное, что все целы!'
    if st1.getCorr() > 40:
        $ player.incLust(10)
        'И вы действительно уходите, чтобы спустя 5 минут вновь вернуться к тому же месту.'
        show expression 'pic/locations/school/library/no6_1.jpg' at top as tempPic
        player.say '"Ага, ну это, безусловно просто такая форма благодарности за смягчение падения!"'
        'Вы наблюдаете за размашистыми, но скучающими движениями головы ученицы. Она умело использует свой язык, чтобы приблизить парня к оргазму, и наконец то выправить свою карму. Удивительно, что она вообще согласилась на подобный способ сказать "спасибо"!'
        menu:
            'Наказать их':
                $ scoldWho = [st1,st2]
                jump scoldAll
            'Не обращать внимания':
                $ hadSex(st1,st2)
    $ move(curloc)
    
label event_loc_library_0_no7:
    show library
    python:
        st1 = getChar('female')
    if 'попа' not in st1.getCover() and player.getCorr() > 40:
        show expression 'pic/locations/school/library/no7_1.jpg' at top as tempPic
        player.say '"Ух ты!"'
        'Чудесный вид вам открылся, когда ученица нагнулась за какой то книжкой, упавшей с верхней полки. Эта попка и блестящая киска могла бы смотреться лучше только в одном случае.'
        show expression 'pic/locations/school/library/no7_2.jpg' at top as tempPic
        player.say '"Да, если бы какой нибудь парень заляпал их своей спермой после бурного соития!"'
        $ player.incLust(15)
        $ st1.incCorr(2)
    else:
        show expression 'pic/locations/school/library/no7.jpg' at top as tempPic
        'Оппа! Какой прекрасный вид открылся вам на белоснежные высоты! Хотя вот [st1.fname] не разделяет радости. Уж слишком недвусмысленное выражение застыло на вашем лице.'
        $ st1.incLoy(-5)
        $ player.incLust(5)
    $ move(curloc)
    
label event_loc_library_0_no8:
    show library
    python:
        st1 = getChar('female')
    show expression 'pic/locations/school/library/no8.jpg' at top as tempPic
    '[st1.fname] случайно зацепилась юбкой за стопку книг, открыв вам вид на свои трусики.'
    menu:
        'Отвернуться':
            'Вы отворачиваетесь, чтобы не смущать ученицу, и уходите.'
            $ st1.incLoy(5)
        'Смотреть':
            if st1.getCorr() < 20:
                st1.say 'Хватит за мной подглядывать!'
                'Раздражённая ученица одёргивает юбку, и уходит.'
                $ st1.incLoy(-5)
            else:
                st1.say 'Чёртова юбка! Вечно ты мешаешься! То с Васей, который вечно в ней путается, то тут!'
                show expression 'pic/locations/school/library/no8_1.jpg' at top as tempPic
                'Ученица с ненавистью срывает с себя юбку, и уходит, оставляя вас в недоумении от того, что только что произошло.'
    $ move(curloc)
    
label event_loc_library_0_no9:
    show library
    python:
        st1 = getChar('female')
        setLust(5,5)
    show expression 'pic/locations/school/library/no9.jpg' as tempPic:
        xalign 1.0 yalign 0.0
        ease  10.0 yalign 1.0
        ease  10.0 yalign 0.0
        repeat
    '[st1.fname] прижимает к груди томик Жана Поля Пруссака, с романтическими стихами, и, смотря на вас даже не замечает ветра, приподнявшего ей юбочку. Уж слишком романтичное у неё настроение. А у всех посетителей библиотеки оно стало ещё и эротичным.'
    if player.getCorr() > 30:
        player.say '"Ох уж эти романтики!"'
        show expression 'pic/locations/school/library/no9_1.jpg' at top as tempPic
        'Вам почему то вспомнилась ваша школьная подружка, тоже особа весьма романтическая, которая потеряла девственность в портовом борделе с моряком.'
        player.say '"Тоже вначале "Пруссак", "Коленьё", "Маразмама"... А как дошло до дела, только и повизгивала под толстым членом морячка. Хотя тот за всю жизнь прочёл разве что правила пользования гальюном. Да и то только из за запора от селёдки."'
        player.say '"А как она визжала в оргазме, когда тот начал кончать! Я тогда к окну и подбежала, думала, что убивает он её... И убил ведь... Всю романтичность... Последний раз, когда мы с ней встречались, так она за двадцатку предлагала отлизать."'
        $ player.incLust(10)
    $ move(curloc)
    
label event_loc_library_0_no10:
    show library
    python:
        st1 = getChar('female')
    show expression 'pic/locations/school/library/no10.jpg' at top as tempPic
    'Сидя на полу, [st1.fname] делает домашнее задание. Как правильный, заботливый директор, вы настойчиво просите пересесть её за стол.'
    'Ученица встаёт, и уходит за самый дальний стол.'
    if st1.getCorr() > 20 and st1.getLust() > 50:
        'Вы уже и сами собираетесь покидать помещение, как вдруг слышите тихое копошение сзади.'
        show expression 'pic/locations/school/library/no10_1.png' as tempPic:
            xalign 1.0 yalign 0.0
            ease  10.0 yalign 1.0
            ease  10.0 yalign 0.0
            repeat
        player.say '"Ну мать перемать! Лучше бы я оставила её на месте... Она хотя бы занималась чем то. Хотя она вроде и счас занимается. И вроде даже интенсивней, чем раньше."'
        'Действительно, [st1.fname] похоже решила повременить с учёбой, вспомнив сюжет из какой то книги, и вплотную занялась своей зудящей киской.'
        player.say '"И что их всех так тянет савокупляться со столами? Парней чтоли нет вокруг, или стесняются до сих пор?"'
        'Вы хмыкнули, и решили, что уж путь девочка сбросит напряжение привычным ей способом в кединённом месте, чем будет публично мастурбивать, ставя под угрозу вашу репутацию.'
    $ move(curloc)
    
label event_loc_library_0_no11:
    show library
    python:
        st1 = getChar('female')
        st1.incEdu(5)
    show expression 'pic/locations/school/library/no11.jpg' at top as tempPic
    'Вы с умилением наблюдаете как [st1.name] так увлеклась книгой, что не замечает ничего и никого вокруг. Может из этой девочки вырастет ученый! Хоть кто-то в наши, наполненные развратом, времена любит читать.'
    if player.getCorr() > 50:
        show expression 'pic/locations/school/library/no11_1.jpg' at top as tempPic
        'Вам представилось, что лет через пять, вместе со своим мужем, она продолжит читать даже в то время, когда правоверный будет исследовать глубины её попки.'
        player.say '"Хех! Да, я бы этому мужу не позавидовала бы..."'
        $ player.incLust(10)
    $ move(curloc)
    
label event_loc_library_0_no12:
    show library
    python:
        st1 = getChar('female')
        st1.removeItems(studpantiesF.name)
        player.incEnergy(-100)
        player.incLust(5)
    show expression 'pic/locations/school/library/no12.jpg' as tempPic:
            xalign 1.0 yalign 0.0
            ease  10.0 yalign 1.0
    '[st1.fname] потянулась за книгой на верхней полке и, не успели вы поприветстовать ее, как внезапно от неудачного движения ученицы книги полетели вниз, взметнув юбку ученицы вверх. Уловив умоляющий взгляды испуганной девочки, вы упустили одну из книг, которая прилетела вам прямо в лоб!'
    show expression 'pic/locations/school/library/no12_1.png' at center as tempPic
    'Первое, что вы увидели, придя в сознание, это рваные колготки ученицы и ничем не прикрытое то, что должно быть прикрытым всегда у приличной женщины.'
    st1.say 'Я, я кинулась вам помочь и тоже упала-а-а-а!'
    'Ученица бросается в слёзы. Вы быстренько выясняете, ничего ли она себе не сломала, и говорите, что ссадины до свадьбы заживут!'
    player.say '"Чего нельзя сказать о девственной плеве, особенно учитывая такое нерегулярное ношение нижнего белья!"'
    $ move(curloc)