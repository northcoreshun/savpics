init python:

    sprite_path = "Sprites/"
    sound_path = "audio/sounds/"
    audio_path = "audio/"
    image_bg_path = "BackGrounds/"
    image_cg_path = "Cg/"
    fonts_path = "Fonts/"

define dspr = Dissolve(0.2)
    
layeredimage kat:
    always:
        sprite_path + "Katya/katya0.png"
    group pose:
        attribute pose1:
            sprite_path + "Katya/katya1.png"
        attribute pose2:
            sprite_path + "Katya/katya2.png"
    group emotion:
        attribute smile:
            sprite_path + "Katya/katya smile.png"
        attribute sad:
            sprite_path + "Katya/katya sad.png"
        attribute serious:
            sprite_path + "Katya/katya serious.png"
        attribute shy:
            sprite_path + "Katya/katya shy.png"
        attribute surprised:
            sprite_path + "Katya/katya surprised.png"
    

layeredimage nas:
    always:
        sprite_path+"Nastya/nastya0.png"
    group pose:
        attribute pose1:
            sprite_path + "Nastya/nastya1.png"
        attribute pose2:
            sprite_path + "Nastya/nastya2.png"
    group emotion:
        attribute normal:
            sprite_path+"Nastya/nastya normal.png"
        attribute smile:
            sprite_path+"Nastya/nastya smile.png"
        attribute serious:
            sprite_path+"Nastya/nastya serious.png"
        attribute surprised:
            sprite_path+"Nastya/nastya surprised.png"
        attribute angry:
            sprite_path+"Nastya/nastya angry.png"
        attribute sad:
            sprite_path+"Nastya/nastya sad.png"

layeredimage andr:
    always:
        sprite_path+"Andrey/andrey.png"
    group emotion:
        attribute normal:
            sprite_path+"Andrey/andrey normal.png"
        attribute angry:
            sprite_path+"Andrey/andrey angry.png"

layeredimage dim:
    always:
        sprite_path+"Dima/dima.png"
    group emotion:
        attribute normal:
            sprite_path+"Dima/dima normal.png"
        attribute smile:
            sprite_path+"Dima/dima smile.png"
        attribute serious:
            sprite_path+"Dima/dima serious.png"
        attribute surprised:
            sprite_path+"Dima/dima surprised.png"

layeredimage leh:
    always:
        sprite_path+"Leha/leha.png"
    group emotion:
        attribute normal:
            sprite_path+"Leha/leha normal.png"
        attribute think:
            sprite_path+"Leha/leha thinking.png"

define nas = Character('Настя', color="#7ef17e")
define kat = Character('Катя', color="#cd6af5" )
define katk = Character('Катя', color="#cd6af5",what_color = "#ff0000")
define leh = Character('Лёша', color="#3bb1ff" )
define dim = Character('Дима', color="#d84b4b" )
define gol = Character('Голос', color = "#7a2f2f")
define andr = Character('Андрей', color ="#4d1ecf")

define nn = Character(None, kind=nvl)
define nasn = Character('Настя',kind=nvl, color="#7ef17e")
define katn = Character('Катя',kind=nvl, color="#cd6af5" )
define lehn = Character('Лёша',kind=nvl, color="#3bb1ff" )
define dimn = Character('Дима',kind=nvl, color="#d84b4b" )
define odn = Character('Одноклассник',kind=nvl, color="#4d1ecf" )

image cg1 = image_cg_path+"cg1.png"
image cg2 = image_cg_path+"cg2.png"
image cg3 = image_cg_path+"cg3.png"

image menu_slideshow:
        im.Blur(image_bg_path +"bg bus_stop.jpg", 1.5) with dissolve
        pause 5.0
        im.Blur(image_bg_path +"bg roof.jpg",1.5) with dissolve
        pause 5.0
        im.Blur(image_bg_path +"bg podezd.jpg",1.5) with dissolve
        pause 5.0
        im.Blur(image_bg_path +"bg dvor_rassvet.jpg",1.5) with dissolve
        pause 5.0
        repeat
# Игра начинается здесь:
label start:
    scene black with dissolve 
    play music gorod fadein 1.0 volume 0.2
    scene bg podezd with dissolve:
        xcenter 0.5 ycenter 0.5 zoom 1.15
        ease 5 zoom 1
    "В начале лета 2к17-го из своего дома на юге Нижнего\n Новгорода вышла девушка, чтобы встретиться с подругой." with dissolve
    show kat pose1 smile with dissolve
    show kat pose1 smile:
        anchor(.5,.5) pos(.5,.567)
        ease 1 pos(.25,.567)
        ease 1 zoom 2.5 pos(.0,1.1)
    pause 2
    show kat pose2 smile:
        anchor(0.5,0.5) pos(.0,1.1)
        ease 2 zoom 1.25 pos(0.5,0.567)
    pause 2
    show kat pose2 smile:
        anchor(.5,.5) pos(.5,0.567) 
        ease 1 xpos(.75)
    nas "Дратути! Ну наконец-то можем пойти погулять!"
    kat "Привет! да, я так рада!"
    nas "Блин, нифига ты модная! Это что, Гоша??"
    show kat pose1 smile with dspr
    kat "Да, недавно купила. Ну что, пойдём?"
    nas "Да, погнали!"
    scene black with dissolve
    pause 0.5
    scene bg bus_stop with dissolve:
        xcenter 0.5 ycenter 0.5 zoom 1.15
        ease 5 zoom 1
    window hide
    play sound stoppingtrolleybus volume 0.5
    nn "Оживлённо разговаривая, девчонки дошли до остановки и сели на троллейбус до центра." with dissolve
    nn "Входя в троллейбус, Катя зачем-то оглянулась, будто кого-то увидела." 
    katn "Тут одно место только."
    nasn "Да садись, я постою."
    katn "Ой, спасибо."
    nvl clear
    stop music
    scene black with dissolve
    scene bg trolleybus with dissolve:
        xcenter 0.5 ycenter 0.5 zoom 1.15
        ease 5 zoom 1
    play music insidetrolleybus fadein 1.0 volume 0.5
    show nas pose1 normal with dissolve:
        xpos 0.2 ypos 0.09
    kat "Блин, я так рада, что наконец-то каникулы.\n Что мы с тобой сейчас едем гулять."
    show nas pose1 serious with dspr
    nas "Да, а то ты со своим лицеем из учёбы совсем не вылезаешь."
    kat "Ну а что, надо было всё сдать. Прикинь,\n у нас на прошлой неделе шли контрольные."
    nas "Ну и че, у нас тоже."
    kat "У нас ещё по задачам ЕГЭ было. в один день математику, в другой\n день по физике. Ещё зачёт по биологии, где надо было билеты учить."
    show nas pose2 surprised with dspr
    nas "Пиздец… и как, сдала?"
    kat "Оф корс, а как же иначе?"
    show nas pose2 smile with dspr
    nas "Молодец."
    "Катя немного помолчала."
    kat "Насть… я опять его видела. Он за нами наблюдал."
    show nas pose2 surprised with dspr
    nas "Кого?"
    kat "Кого-кого… Андрея."
    show nas pose2 normal with dspr
    nas "Ну хз, может мимо проходил."
    kat "Он же далеко живёт, чё ему тут делать?"
    nas "Не знаю… Кать, да забей."
    kat "Я его не в первый раз вижу. Когда с лицея\n приезжаю, тоже замечала не раз его."
    nas "Ну… может, друг рядом живёт. Не переживай ты так."
    kat "Ладно… как сестра?"
    show nas pose1 normal with dspr
    nas "Молли? Да нормально. Сидит в компе, рисует и играет."
    nas "Мне не жалко, я всё равно в телефоне сижу."
    hide nas with dspr
    "Сказала Настя и в подтверждение своих слов уткнулась в телефон."
    "Минуту девочки молчали, вдруг Настя заговорила."
    show nas pose1 normal with dspr
    nas "Смотри, тут в Овсянке мем “Какой твой шмот по цифре твоего лайка”."
    nas "5-6 это Суприм, 7-8 это Томи Хилфигер."
    nas "Блин, я если лайк поставлю, будет 5-6, мне не нравится."
    kat "Ну скинь мне быстро, я лайк поставлю сначала.\n Затем ты и будет 7-8."
    show nas pose1 smile with dspr
    nas "Ок, сыпыс."
    scene black with dissolve
    scene bg stad with dissolve:
        xcenter 0.5 ycenter 0.5 zoom 1.15
        ease 5 zoom 1
    nvl clear 
    play music intro fadein 1.5 volume 0.3
    nn "Долго ли, коротко ли, девчонки доехали до большой красивой площади с памятником пролетарскому писателю."with dissolve
    nn "И тут как бы типичный сценарий прогулки любого уважающего себя нижегородца – по главной улице до местного Кремля, но Катя начала ныть."
    nvl clear
    katn "Да мы тут тыщу раз были, Насть!"
    nasn "Ладно, знаю одно место, пойдём туда."
    nn "Настя повела Катю через арку по улицам и переулкам\n центра. Пройдя дворами они внезапно вышли на стадион."
    nn "Тот самый стадион, засветившийся в фильме Балабанова."with dissolve
    nvl clear
    show kat pose2 surprised with dissolve:
        xpos 0.2 ypos 0.135
        xzoom -1.0
    kat "Блин, нифига, не знала, что тут пройти можно. Мы\n сюда на физру ходим из лицея, но другой дорогой."
    show nas pose1 serious with dissolve:
        xpos 0.6 ypos 0.09
        xzoom -1.0
    "Катя с Настей ушли подальше от оффников, тренирующихся\n у спортшколы, на другой конец и забрались на гаражи."
    scene bg roof with dissolve
    nas "Ну, наконец-то."
    show kat pose1 serious:
        anchor(.5,.5) pos(.7,.567)
    with dspr
    show nas pose1 angry:
        anchor(.5,.5) pos(.4,.567)
    with dspr
    kat "Ты е-ба-ну-та-я? А ниче, что тут жарко и солнце светит?"
    nas "Ты а-дек-ват вообще? А ничо то, что тебе вообще нигде не нравится."
    "Настя достала из сумки… две бутылки гаража."
    show kat pose2 surprised with dspr
    "Катя оторопела."
    kat "Насть, я ж не пью."
    nas "Да ладно те, тут немного."
    kat "Ну, я не знаю."
    nas "Давай, тебе подруга предлагает."
    show kat pose2 sad with dspr
    "Катя поломалась, поборолась с собой внутри и согласилась."
    show nas pose2 smile with dspr
    nas "Ну, за окончание десятого!"
    play sound botlle 
    show kat pose2 smile with dspr
    "Девчонки звонко чокнулись бутылками."
    "Следующие несколько минут можно описать так: на крыше гаража\n Настя уговорила Катю уговорить совместно бутылку-другую гаража."
    "Всё было обсуждено: пацаны, бурно\n развивающиеся в тот год мода и культура мемов."
    "Не забыли на этом празднике жизни и про музыку: Настя\n прихватила с собой “жи-би-эль”, благодаря которому\n июньский день окончательно перестал быть томным."
    show kat pose1 smile with dspr
    "Алкоголь нехило подействовал на светловолосую\n ботанку, возможно сказались недавние бессонные ночи."
    show nas pose1 smile with dspr
    nas "А вот это новая группа, послушай."
    "Из колонки полилась современная бодрая перепевка\n песенки группы Рефлекс."
    hide kat with dissolve
    hide nas with dissolve
    "Катя встала и начала дэнсить. В тот момент она не замечала\n никаких проблем с попаданием в ритм, изящностью движений и т.д."
    "Как и не заметила футбольного мяча, вылетевшего из-\nза барьера и коршуном спикировавшего на её умную голову."
    with vpunch
    play sound ball volume 2 
    stop music fadeout 2.0
    scene black with dissolve 
    pause 2
    scene bg l_room with dissolve:
        xcenter 0.5 ycenter 0.5 zoom 1.15
        ease 5 zoom 1
    "Несколькими часами ранее в другом месте города у себя дома\n сидел парень шестнадцати лет. Сидел и от скуки скроллил ленту."
    "Вдруг его глаз зацепился за фото девушки.\n Недолго думая, он добавил её в «Сохранённые»."
    "Увидел имя – Екатерина Мохова. Это имя ему показалось\n знакомым. Он начал вспоминать, но его отвлекло сообщение вк."
    show dim:
        anchor(.5,.5) pos(.3,.567)
        alpha .5
        matrixcolor BrightnessMatrix(-1)
    with dissolve
    nvl clear
    play music inyourroom fadein 1.0 volume 0.2
    nn "– Лёх, здорова" with dissolve
    nn "– Идёшь седня?"
    hide dim with dissolve
    "Лёша быстро ответил, собрался и пошёл."
    "Лишь недавно у него появилось полное право выйти из дома и\n пойти, куда ему нужно. Не потому, что он убегал из дома или\n как-то ещё косячил. Просто родители  поддерживали жёсткий\n порядок. По факту – держали сына под домашним арестом."
    "Благо Лёша почти всё время был занят учёбой и\n сидением в интернете и планов побега не строил."
    "Но всему приходит конец, правила жизни смягчаются, после учёбы наступают\n каникулы и вот наш герой идёт к тому, кто ему писал. К своему другу Диме."
    scene bg road2stad with dissolve
    play music morning_city fadein 1.0 
    "Парни подружились на кружке программирования в дворце детского\n творчества. Были же всё-таки у Лёши какие-то увлечения, позволявшие\n ещё куда-то выходить из дома. Были же всё-таки у Димы какие-то\n серьёзные увлечения, куда он ходил развиваться, а не просто тусить."
    "Они встретились недалеко и пошли, общаясь."
    show dim smile with dissolve
    dim "Как же много альбомов дропнули. ЛСП, АТЛ."
    leh "Обладает “Файлы” ещё дропнул."
    dim "Но мы с тобой ждём главного."
    leh "Именно, баттла Окси и Гнойного."
    dim "Я хейтер, я ненавижу ваш рэп, ваш трэк, ваш текст, мягкий, как паштет!"
    show dim surprised with dspr
    leh "Это барокамера и номера за номинал{nw}"
    leh "Вам пора бы кавера петь на На-На Я нагинал{nw}"
    leh "Ваш надменный криминал, я бока вам наминал{nw}"
    leh "Чтобы ты запоминал — твой рот номинант на болт{nw}"
    pause 1
    dim "Ебать…"
    leh "Полдня заучивал, чтобы зачитать."
    dim "Нихуя ты чевапчич."
    show dim smile with dspr
    dim "Всё дома сидишь, а уже лето началось."
    dim "Последнее ведь! Планы есть какие?"
    leh "Да хз, дома буду сидеть."
    dim "Да ты чё! Последнее лето перед ЕГЭ, а он… дома."
    dim "Девушку найти надо."
    leh "Да не знаю, я ж уехать думаю.\n И зачем мне тогда отношения?"
    dim "Ну это же не на всю жизнь."
    leh "Ну а смысл тогда, если знаешь, что они закончатся?"
    dim "Романтик ты, Лёх…"
    scene black with dissolve
    scene bg football_field with dissolve:
        xcenter 0.5 ycenter 0.5 zoom 1.15
        ease 5 zoom 1
    "Наконец, пришли к месту. Парни зашли на одно из полей."
    leh "О, а мы сюда на физру ходим."
    show dim smile with dissolve:
        xpos 0.1 ypos 0.05
    dim "Везёт же вам."
    dim "Так, ждём остальных пока."
    show dim normal with dspr
    nvl clear
    nn "В своё время Дима втянул Лёшу в свою футбольную тусовку. Она\n была создана для чилловой игры, входного порога и требований\n не было. Это и стало причиной, почему Лёха со своим сидением\n дома и отсутствием “дворовой” жизни смог войти в их круг." with dissolve
    nn "Периодически ребята собирались поиграть на коробках у школ и на\n стадионах. Между играми умеющие ребята могли подтянуть аутсайдеров.\n В тот день это и делал Дима, проводил ликбез как бить по воротам."
    show dim serious with dspr
    dim "Смотри, прямо носком бить не надо, ногу при ударе немного подворачиваешь."with dissolve
    leh "Окей, я пока попрактикуюсь."
    show dim normal with dspr
    dim "А я пока чекну где наши."
    hide dim with dissolve
    "Где-то недалеко была слышна речь и играла музыка."
    leh "Дим, а кто там?"
    dim "Да забей, какие-то челы."
    "Ответил Дима, не отрывая глаз от телефона."
    dim "Бля, они вообще на другую коробку пошли!"
    leh "Чего??"
    show dim surprised with dspr
    play sound football
    "В этот момент Лёша как раз готовился ударить по мячу. В моменте\n небольшая обида на товарищей, не предупредивших их, выросла до сильного\n импульса и он   ударил со всей силы. Мяч улетел вверх и скрылся за крышей." with vpunch
    "Там, куда улетел мяч, послышалась какая-то возня."
    show dim serious with dspr
    dim "Бля, Лёх. Нахуя…"
    dim "Ну чё, автор бежит за мячом."
    leh "Ой, извини. Ну, я побежал."
    scene black with dissolve 
    pause 1
    scene bg roof with dissolve:
        xcenter 0.5 ycenter 0.5 zoom 1.15
        ease 5 zoom 1
    "От удара мячом с Катей случилось нечто странное."
    show nas pose1 surprised with dissolve:
        xpos 0.5 ypos 0.09
        xzoom -1.0
    show kat pose2 surprised with dissolve:
        xpos 0.25 ypos 0.135
        xzoom -1.0
    nas "Кать, ты чего? Какая пандемия, какая..? Ох, и сильно же\n тебя ударило! Пойдём дослушаем Молли в другом месте."
    play music meeting fadein 1 volume 0.7
    "Из-за гаража послышался голос Лёши."
    leh "Извините, можете нам мяч скинуть…"
    show nas pose1 angry:
        matrixcolor TintMatrix("#d84b4b")
        ease .05 xoffset -10
        ease .05 xoffset 20
        ease .05 xoffset -10
        repeat
    nas "ВЫ ЧЁ БЛЯТЬ ДЕЛАЕТЕ?! ВЫ ЧЁ СОВСЕМ ОХУЕЛИ?! ВЫ ЕЁ НАХУЙ ЧУТЬ НЕ УБИЛИ!" with vpunch
    hide nas with dspr
    nas "Слышь, сюда иди, я те этот мяч засуну в…"
    show kat pose1 sad with dspr
    show nas pose1 serious with dissolve:
        xpos 0.5 ypos 0.135
        xzoom -1.0
    kat "Насть, не ори пожалуйста! Со мной всё нормально."
    hide kat with dspr
    "Лёша неуклюже залез на гараж. И увидел девчонок – Настя метала на него\n свирепые взгляды, Катя сочувствующе смотрела и держала у головы бутылку."
    leh "Блин, извини, я случайно!"
    show kat pose1 sad with dspr:
        anchor(.5,.5) pos(.4,.567)
    kat "Всё нормально. Солнечный удар наверное."
    show nas pose1 serious:
        anchor(.5,.5) pos(0.6,0.55) 
        ease 0.5 xpos(.8) 
    show kat pose1 sad:
        anchor(.5,.5) pos(0.4,0.6) 
        ease 0.5 xpos(.6) 
    show dim surprised:
        anchor(.5,.5) pos(-0.8,0.55) 
        ease 0.5 xpos(.25) 
    "Внезапно на крыше возник ещё и Дима, подоспевший на крик."
    dim "Чё случилось?"
    nas "Вы своим мячом чуть мою подругу не убили!"
    show dim smile with dspr
    "Дима окинул взглядом ребят, понял что к чему..."
    play sound ohmygod
    "... и громко выразил своё изумление."
    dim "Ничоси ты Лёх меткий!"
    dim "Сорян, девчат, он перестарался немного."
    show kat pose1 smile with dspr
    show nas pose1 normal with dspr
    nas "Вы блин перестарались, а нам… ух ты, это Палас?"
    show dim serious with dspr
    dim "Ну да"
    nas "Круто, где брал?"
    dim "Да в секонде одном."
    dim "Такое, не советую."
    nas "Жаль"
    "Ссора начала переходить в знакомство."
    show dim smile with dspr
    nas "С какой школы хоть?"
    leh "А что?"
    show nas pose1 serious with dspr
    nas "Жаловаться буду!"
    leh "Блин…"
    dim "Лёх, она шутит."
    show nas pose2 smile with dspr
    nas "Конечно, шучу!"
    "Парни сказали номера школ. Когда назвал Лёша, девчонки оживились."
    nas "Кать, смотри, он ещё и с твоего лицея!"
    kat "Какой класс?"
    leh "Десятый, физмат."
    kat "Я с десятого, биохим."
    show nas pose1 smile with dspr
    nas "Ладно, пойдёмте. Ты ещё Кате мороженое\n должен за своё поведение. И мне ещё."
    leh "А тебе за что?"
    nas "Как за что? Я такой стресс пережила из-за подруги. Кать, что скажешь?"
    kat "Не знаю…"
    leh "Эээ… у меня нет денег."
    dim "Да ладно Лёх, я займу."
    "Смеясь сказал Дима."
    leh "Погоди, а как же ребята?"
    show dim normal with dspr
    dim "Какие ребята? Которые нас кинули?"
    show dim smile with dspr
    dim "Пойдём, не отлынивай от проставы девчонкам."
    nas "Вот, правильно!"
    stop music
    scene black with dissolve 
    pause 1
    play music gorod fadein 1.0 volume 0.2
    scene bg shaurma with dissolve:
        xcenter 0.5 ycenter 0.5 zoom 1.15
        ease 5 zoom 1
    "Следующие пару часов прошли просто прекрасно: Настя\n и Дима нашли коннект на обсуждении рэпа и секондов,\n Катя и Лёша – на обсуждении нелёгкой учёбы в лицее."
    show nas pose1 smile with dissolve:
        xpos 0.6 ypos 0.09
        xzoom -1.0
    show kat pose2 smile with dissolve:
        xpos 0.3 ypos 0.14
        xzoom -1.0
    kat "… выступала с презентацией. И мне поставили не \n«пять», а «четыре», потому что в конце я указала \nссылку на яндекс, а не на конкретную научную статью."
    show kat pose2 serious with dspr
    kat "А я уже забыла, что за статья. Сказали, если \nхочешь работать в науке, должна всегда понимать, \nс какими источниками работать. Так обидно."
    nas "Да уж, проблемы отличников."
    leh "Не расстраивайся, у меня вообще всегда «четыре» выходило."
    kat "А… ты на медаль не идёшь разве?"
    leh "Не, не хочу. У меня любимые предметы физика и инфа, \nпо ним твёрдо «пять»."
    show kat pose2 smile with dspr:
    kat "А учителя говорят – ты умный."
    leh "Умный, но немного ленивый, хахах."
    "Прогулка новоиспечённой компании закончилась у шаурмичной.\n Место, которое знала вся молодёжь города"
    nas "Ну чё, рады были знакомству."
    kat "И спасибо за мороженое."
    nas "Приезжайте к нам в Щербы. У нас тоже есть, где затусить."
    hide kat 
    hide nas
    with dissolve
    "Автобус забрал девчонок. Так и закончилась та прогулка."
    stop music
    scene black with dissolve 
    pause 1

    "Пока родителей Кати не было, она пригласила\n Настю к себе на ночевку. Девчонки решили посмотреть\n хайповый сериал про будни норвежских школьников."
    play music sunsettower volume 0.3 fadein 1 
    scene bg windowview with dissolve:
        xcenter 0.5 ycenter 0.5 zoom 1.15
        ease 5 zoom 1
    "После просмотра Настя решила выйти на балкон насладиться закатом."
    "Ах, закаты, закаты! Как же они в то время были прекрасны!"
    "Именно закаты стали символом того времени, той ушедшей эстетики.\n Закат – основа той атмосферы."
    "В любом году в любой день оптика может показать нам\n фокусы, окрасив небо под разными углами разными цветами."
    "Но именно тогда интернет начал восхищаться ими, наполняя себя\n гигабайтами картинок с закатами и подписями “со смыслом”."
    "Настя тоже восхищалась."
    show nas pose2 surprised with dissolve:
        xpos 0.1 ypos 0.09
    nas "Нихуясе! Вот это высота!"
    kat "Шестнадцатый этаж, конечно высоко."
    nas "Да у вас весь город видно!"
    show nas pose1 smile with dspr
    "Настя восхищённо начала перечислять, что видит. Когда ей это\n надоело, она устроила фотосессию, с чем Катя ей конечно же\n помогла, ибо красивые фото на фоне заката ей тоже не были чужды."
    "Когда и это занятие подошло к концу, они начали подводить итоги дня."
    kat "Хороший день сегодня был."
    nas "Да уж Кать, хороший. Тебе сегодня мячом по голове прилетело."
    kat "Блин, ну он случайно!"
    nas "Хотя Дима ничего такой, приятный. Сасный, хахахах."
    kat "Да ну."
    show nas pose1 normal with dspr
    kat "Типикал пустышка, модник-огородник и\n бабник. Насть, ты опять на те же грабли?"
    show nas pose1 serious with dspr
    nas "А кто лучше-то? Этот ботан? Кать, у вас вроде в\n лицее парней полно и можно найти нормального."
    kat "А я думаю Лёша нормальный."
    nas "Сори Кать, но даже Андрей…"
    show nas pose1 normal with dspr
    kat "ОЙ ВОТ НЕ НАДО ТОЛЬКО!" with vpunch
    nas "Ладно, не буду."
    kat "Это имя вообще не должно тут звучать. У меня\n уже год как жизнь с чистого листа началась."
    kat "Без него, без этой школы…"
    show nas pose1 sad with dspr
    nas "Без меня…"
    "Катя осеклась."
    kat "Нет… конечно нет!"
    nas "В классе иногда говорят, что да."
    kat "Насть, ты – моя лучшая подруга. И ею остаёшься."
    nas "А что, в лицее не с кем общаться?"
    kat "Там есть нормальные ребята…"
    nas "Но это не повод забывать тех, кто был до них."
    kat "Ну да."
    "Катя немного помолчала."
    kat "Думаю, рано сейчас про мальчиков говорить.\n Приедут к нам, посмотрим ещё."
    nas "Да… пофиг на них. Ты-то как?"
    kat "Непросто. Год был тяжкий."
    kat "Учёба, не вылажу из неё. Еле-еле год на пятёрки закрыла."
    kat "Папа после той ситуации жёстче стал. Решил\n меня повоспитывать. В шестнадцать лет, рофл…"
    kat "Лучше ты о себе расскажи."
    show nas pose1 smile with dspr
    nas "Я… потихоньку. Наш дружный класс сама знаешь."
    show nas pose1 normal with dspr
    nas "Тебя не хватает..."
    nas "Хотя чё… ребята прикольные есть."
    kat "На крышу ходите?"
    nas "А, нет…"
    show nas pose1 normal with dspr
    nas "Нету уже той тусовки, Кать. После девятого\n многие ушли, уже как-то не так весело."
    "Настя помолчала, а потом добавила."
    show nas pose1 normal with dspr
    nas "Чё хоть за челик твой Лёша?"
    nas "Давай-ка его глянем."
    show nas pose1 surprised with dspr
    "Девчонки глянули… и нашли в сохрах Лёши… Катину фотку!"
    show nas pose1 smile with dspr
    nas "Да он запал на тебя!"
    nas "Нет, это зашквар я считаю."
    kat "А что такого? Хорошая фотка."
    nas "Ну он не шарит что ли, что сохраненки это типа витрина твоих вкусов.\n Ну типа это как если бы он написал на стене, что влюблён в тебя."
    kat "Да почему сразу это? Может он меня не знал и добавил."
    nas "А поставь лайк ему! Пусть охуеет, хахахах."
    kat "Не надо! Я бы очень напугалась на его месте."
    show nas pose1 normal with dspr
    nas "Ну как хочешь."
    scene black with dissolve
    play music conspiracy volume 0.5 fadein 1
    nvl clear
    nn "Девчонки ещё поговорили и легли спать." with dissolve
    nn "Пока Настя лежа залипала в телефон перед сном, ей пришло сообщение."
    nn "Писал её одноклассник."
    nvl clear
    nn "– Даров, куда с Катюхой ходили?"
    nn "– а ты че следил за нами"
    nn "– и не Катюха она тебе"
    nn "– Да просто знаю"
    nvl clear
    nn "И всё могло бы быть в дальнейшей жизни героев по-другому, гораздо проще и прозаичнее."
    nn "Но тут включилось одно свойство натуры Насти."
    nvl clear
    nn "– у неё парень есть)"
    nn "– Че"
    nn "– в лицее нашла"
    nn "– ща коечо скину))"
    nvl clear
    nn "Настя кинула ссылку на фото Кати в сохраненках Лёши."
    nn "У неё возникла идея, как ей казалось, лучшего пранка 2к17."
    kat "Насть, кто тебе там пишет? Я спать не могу, мне светит."
    nas "Да.. Машка пишет. Спрашивает, где я. Ща отвечу."
    nvl clear
    nn "Катя чуть было не сорвала пранк: она бы точно\n прервала движ, если бы увидела, с {i}кем{/i} Настя общалась."
    scene black with dissolve 
    pause 1
    play music inyourroom fadein 1.0 volume 0.2
    scene bg l_room with dissolve:
        xcenter 0.5 ycenter 0.5 zoom 1.15
        ease 5 zoom 1
    "Утром Лёха проснулся как обычно и заглянул в телефон.\n Его ждал сюрприз: уведомление о нескольких\n лайках и сообщения от какого-то Андрея."
    "Всё это вогнало Лёшу в ступор и навязало ему нарратив\n о том, что он, такой-сякой, познакомился с девушкой\n уважаемого на своём районе пацана и добавил её фотку себе в СОХРЫ.\n А лайки незнакомых челов сработали как осмеяние его промаха."
    "Пришлось ему извиниться и удалить фото."
    "Всё это, конечно, вызвало у нашего героя чувство\ подавленности."
    "Однако, когда он поделился ситуацией с Димой, тот его\n успокоил, дескать может это всё прикол и вообще, сохры\n закрытыми держать лучше. А то постучатся не в личку\n вк и не какой-то хрен с горы, а… лучше не думать даже."

    "Вся эта нервотрёпка чуть не сорвала вторую встречу\n парней с девчонками, ведь Лёша думал после того\n инцидента, стоит ли ехать, но Дима уговорил его:"
    nvl clear
    show dim normal with dissolve:
        xpos 0.15 ypos 0.11
        alpha 0.5
    dimn "– Подумаешь, какой-то еблан тебе в лс поугрожал"
    dimn "– Я тоже так могу и своих знакомых попросить чет понаписать"
    dimn "– Забей крч"
    scene black with dissolve 
    pause 1
    play music gorod fadein 1.0 volume 0.2
    scene bg tz with dissolve:
        xcenter 0.5 ycenter 0.5 zoom 1.15
        ease 5 zoom 1
    play sound stoppingtrolleybus volume 0.7
    "Как и предложила Настя, ребята приехали туда,\n где живут девчата – микрорайон «Щербинки-3»."
    show dim smile:
        xpos 0.05 ypos 0.02
    show nas pose2 smile:
        xpos 0.32 ypos 0.1
        xzoom -1
    show kat pose2 smile:
        xpos 0.7 ypos 0.15
    with dissolve
    "Настя с Димой всё также весело общались, а вот Лёша\n побаивался заговорить с Катей и смотрел на неё\n затравленно. Катя видела это, но не понимала, в чём дело."
    "А вдруг это правда и она встречается с ним?"
    "Зачем тогда она гуляет с нами?"
    "В конце прогулки ребята стояли у входа в местный ТЦ и разговаривали."
    nas "Чё, может на крышу сходим? Мы там раньше постоянно чиллили."
    "И только Лёша отринул сомнения и расслабился, случилось это."
    show nas pose2 serious
    show dim serious
    show kat pose2 serious 
    with dspr
    stop music
    play music attack fadein 1 volume 0.7
    "С улицы послышался шум и ребята произвольно посмотрели в его сторону.\n К ним приближалась компания парней. Увидев одного из них, у Кати\n сердце в пятки ушло. Лёша тоже узнал его. А он узнал их и подскочил."
    show andr normal:
        xzoom -1
        anchor(.5,.5) pos(-0.2,0.57) 
        ease 0.5 xpos(.3) 
        
    pause 2
    show dim surprised
    show nas pose2 surprised
    with dspr
    play sound head_punch
    "Со словами “Ты чё тут делаешь?” отвесил Лёше подзатыльник." with vpunch
    show andr normal:
        anchor(.5,.5) pos(.3,0.57) 
        ease 0.5 xpos(.6) 
    show kat pose2 shy with dspr
    play sound zamah volume 10
    "Затем той же рукой резким движением замахнулся\n на Катю. Та испугалась и зажмурилась."
    show andr normal:
        anchor(.5,.5) pos(.6,0.57) 
        ease 0.5 xpos(1.2) 
    "Однако налётчик не стал бить её и оперативно скрылся в Макдональдсе.\n Так быстро, что не услышал посланное вдогонку Настино\n “Ты чё творишь?!”."
    show kat pose2 sad with dspr
    "Компания стояла в шоке от этого: Лёша потирал место\n удара, Катя приходила в себя, Настя сокрушённо\n материлась, Дима… просто стоял с глазами по пять копеек."
    show nas pose2 angry with dspr
    nas "И хуй ли ты не ответил ему? Ты чё такой тормоз…{nw}"
    show kat pose2 serious with dspr
    kat "Насть."
    show nas pose2 surprised with dspr
    "Вдруг тяжёлым голосом сказала Катя."
    katk "Рот закрой."
    "Катя сказала это негромко, но с такой злобой и силой\n в голосе, что даже парни не решились что-то говорить."
    show nas pose1 normal
    with dspr
    show dim serious with dspr
    nas "Пойдёмте отсюда."
    kat "Я домой пойду. Хватит на сегодня."
    show dim normal with dspr
    dim "Да, мы тогда тоже пойдём."
    show kat pose1 sad with dspr
    kat "Лёш, можешь дойти со мной? Тут недалеко."
    leh "Хорошо."
    scene black with dissolve 
    pause 1
    play music gorod fadein 1.0 volume 0.2
    scene bg podezd with dissolve:
        xcenter 0.5 ycenter 0.5 zoom 1.15
        ease 5 zoom 1
    "Они пошли вверх по проспекту, но никак не могли начать разговор."
    show kat pose2 sad:
        xpos 0.7 ypos 0.15
    with dissolve
    kat "Ты как, нормально?"
    show leh think:
        xpos 0.05 ypos 0.07
        xzoom -1
    with dissolve
    leh "Да я-то норм, ты как?"
    kat "Пойдёт. Я хотела сказать."
    kat "Мне жаль, что это случилось."
    kat "Тот, кто тебя ударил это…"
    leh "Андрей."
    show kat pose2 surprised with dspr
    kat "Ты его знаешь?"
    show kat pose2 sad with dspr
    leh "Был моментик."
    show leh normal with dspr
    leh "Слушай, мне нужно кое в чём признаться."
    leh "В день, когда мы встретились… ну там, на Воднике."
    leh "Я увидел твою фотку в ленте вк. Ну и…"
    show kat pose2 smile with dspr
    kat "Добавил в сохранёнки."
    leh "А, ты знаешь."
    kat "Случайно узнали. Ну, и что такого?"
    leh "Он мне написал. А я не знал, что ты с ним встречаешься."
    show kat pose2 surprised with dspr
    kat "Эм, что?"
    leh "Он мне написал."
    show kat pose2 serious with dspr
    kat "А, ох как."
    kat "Нет, Лёш, всё не так."
    kat "Это мой бывший и мы расстались год назад."
    kat "Он не может оставить меня в покое."
    kat "Вот тебе и досталось."
    leh "Понятно."
    leh "Ладно… я думаю мы что-нибудь с этим придумаем."
    kat "Надеюсь."
    "Ребята попрощались и пошли домой."
    scene black with dissolve 
    pause 1
    play music conspiracy fadein 1.0 volume 0.2
    scene bg l_room with dissolve:
        xcenter 0.5 ycenter 0.5 zoom 1.15
        ease 5 zoom 1
    nvl clear
    nn "Последние события начали сильно давить на Лёху. К имевшимся комплексам добавилась злость на Андрея, злость на себя, что не смог ответить. И самое главное – не смог защитить Катю."
    nn "Долго он так протянуть не смог. В какой-то момент, когда Лёха сидел и загонялся, пришла его мать с испорченным на работе настроением."
    nvl clear
    nn "В итоге, после всех прений непонятный руководящий импульс подбил нашего героя на ещё одно спонтанное действие."
    nn "Направление побега было определено сразу\n – к Кате. Она примет, выслушает, поймёт."
    scene black with dissolve 
    pause 1
    play music gorod fadein 1.0 volume 0.2
    scene bg podezd_evening with dissolve:
        xcenter 0.5 ycenter 0.5 zoom 1.15
        ease 5 zoom 1
    "Подходя к дому Кати, Лёша вдруг встретил… Настю."
    show nas pose1 smile with dissolve:
        xpos 0.65 ypos 0.1
        xzoom -1
    show leh think:
        xpos 0.05 ypos 0.07
        xzoom -1
    with dissolve
    nas "Опа, ты чё здесь делаешь?"
    "Лёша рассказал. Настю это крайне развеселило."
    nas "Бляя, ну ты смелый конечно. Малый по-взрос-лел."
    nas "А мы на вписку с Катей идём. Но тебя не возьмём,\n маленький ещё. На автобус посадим, домой поедешь."
    "Настя открыла телефон."
    show nas pose1 serious with dspr
    nas "Да в смысле?!"
    leh "Что?"
    nas "Катя не сможет. Ладно, пойдёшь тогда за неё."
    show nas pose2 smile with dspr
    nas "А что, сбежал от мамки, нормальный повод."
    scene black with dissolve 
    pause 1
    play sound walking fadein 1.0 
    scene bg dvor_night with dissolve:
        xcenter 0.5 ycenter 0.5 zoom 1.15
        ease 5 zoom 1
    nvl clear
    nn "Лёша с Настей ушли в глубь района." 
    nn "Жилой массив напоминал тёмный лес, полный опасностей, но Лёша пошёл."
    nn "Надавило то желание побывать на тех самых вписках, о которых он регулярно читал в интернете."
    play sound domofona_vhod
    nn "Они с Настей долго шли по тёмным улицам и дворам, а затем зашли в подъезд дома. Одного из многих панельных девятиэтажек, коими застроен весь город."
    scene black with dissolve 
    pause 1
    play music welcome2thevpiska fadein 1.0 volume 0.5 
    scene bg vpiskaroom with dissolve:
        xcenter 0.5 ycenter 0.5 zoom 1.15
        ease 5 zoom 1
    "На входе Лёша был встречен громкой хайповой музыкой, игравшей на всю хату."
    play sound ohmygod
    "Настю, как местную топовую тян, встретили громогласным одобряющим воем."
    show leh normal:
        xpos 0.02 ypos 0.07
        xzoom -1
    show nas pose1 smile:
        xpos 0.25 ypos 0.14
    with dissolve
    nas "Эт Лёша, он сёдня впервые сбежал из дому."
    play sound ohmygod
    "Народ тоже ответил одобряющим воем. Спросили школу."
    nas "Он в лицее, где Катюха Мохова. Из параллельного класса."
    stop music fadeout 1.0
    play music srach fadein 1.0 volume 0.5
    gol "И че, как там Катя учится? Небось на тройки одни?"
    show nas pose1 serious with dspr
    "Голос показался знакомым. Тут же Лёша узнал и напрягся."
    nas "Чё ты несёшь, хорошо она учится."
    show andr normal:
        anchor(.5,.5) pos(1.2,0.57) 
        ease 0.5 xpos(.85) 
    andr "Да чё она может? Я ей скатывать давал."
    nas "Да закрой рот блять! Не позорься и на Катю\n не наговаривай! Все знают, что ты пиздишь!"
    "Настя смогла загасить в этой словесной перепалке. Лёше\n же стало понятно, что легко эта вписка не пройдёт."
    show andr angry:
        xzoom -1
        anchor(.5,.5) pos(.85,0.57) 
        ease 1 xpos(1.82)
    pause 1.0
    scene bg vpiskaroom with dissolve:
        xcenter 0.5 ycenter 0.5 zoom 1.15
        ease 5 zoom 1 
    "Делать было нечего во всех смыслах. Возвращаться домой было уже\n поздно: транспорт не ходил, а Лёша жил на другом конце города.\n На такси денег не нашлось, а занимать не хотелось. На вписке обсуждались\n чисто местные темы, да и не отличался Лёха особой общительностью."
    "Оставалось ждать раннего утра, садиться на первый\n транспорт и косплеить «Возвращение блудного сына»."
    scene black with dissolve 
    pause 1
    play music na_kuhne fadein 1.0 volume 8
    scene bg kitchen with dissolve:
        xcenter 0.5 ycenter 0.5 zoom 1.15
        ease 5 zoom 1
    "Посидев со всеми в гостиной, он попал на кухню. К середине ночи там\n сидел один чел, который был готов бухать практически в одиночестве."
    "Лёша слушал его рассказы про претенциозность\n подрастающего поколения, про пост- и метамодернизм."
    "В конце концов чел ушёл на балкон, оставив пустую бутылку на\n столе. И причём никак не возвращался её выкинуть, негодник."
    "Это было не по правилам культурного отдыха в Восточной\n Европе, а Лёша знал правила после семейных застолий,\n поэтому взял бутылку в руку и понёс выкинуть в мусор."
    "Тем временем Настя выпила немного больше, чем\n было нужно и ушла отдыхать в другую комнату."
    "На кухне Лёша услышал суету – в коридоре кто-то напряжённо\n общался, а затем несколько человек зашли в комнату."
    "Лёша пошёл посмотреть, в чём дело и зашёл в комнату."
    scene black with dissolve 
    pause 1
    play music draka fadein 1.0 volume 0.7
    scene bg bedroom with dissolve:
        xcenter 0.5 ycenter 0.5 zoom 1.15
        ease 5 zoom 1
    nvl clear
    
    
    nn "Всё начало происходить быстро."
    nn "Трое парней схватили Настю."
    play sound punch1
    nn "На Лёшино “Вы чё делаете?!” один из них, в котором Лёша узнал Андрея, отвлёкся и начал месить его кулаками."
    play sound punch2
    play sound punch1
    nn "Однако это порушило весь их план. Настя успела ударить ногой одного из нападавших, да так удачно, что тот отлетел в сторону, ударился головой об стену и был нейтрализован."
    play sound punch1
    nn "Второй испугался и просто выбежал из комнаты."
    nvl clear
    play sound punch2
    nn "Настя начала подниматься, но удар по голове её отбросил обратно на кровать."
    nn "Андрей озверел и держал Настю в одиночку. У неё не было сил сопротивляться…"
    scene black with dissolve 
    nvl clear
    nn "Наше тело сковано множеством запретов и блокировок, которые ставятся во время жизни в обществе."
    nn "Эти блокировки призваны не навредить другим людям, если человек испытывает сильные эмоции. Но в чрезвычайных ситуациях, эти тормоза могут отключиться для защиты себя."
    nvl clear
    nn "Гораздо легче это произойдёт, если человек долго держал в себе негатив."

    nn "Лёша уже страдал от импульсивности: когда слышал что-то расстраивающее его, он совершал необдуманные поступки."
    nn "Когда Андрей начал его бить, он и отключил Лёхе тормоза."
    nn "Если бы Андрей не отвлёкся, Лёха бы начал отвечать и исход борьбы был бы непредсказуемым, но скорее всего не в его пользу, так как Андрей был опытнее мог просто взять Лёшу на болевой."
    nvl clear
    nn "Но всё произошло иначе."

    nn "Андрей держал Настю крепкой хваткой и начал лапать её свободной\n рукой. Казалось, всё кончено. И он даже не заметил как…"
    play sound bottlecrash
    scene cg1 with dissolve:
        xcenter 0.5 ycenter 0.5 zoom 1.15
        ease 5 zoom 1
    "Как бутылка, описав дугу в пространстве комнаты, ударилась об его\n больную голову. Удар сразу отключил Андрея и он обмяк на теле Насти."
    "Она увидела то, чего испугалась не меньше изнасилования.\n Перед ней стоял Лёша. Вместо затравленного взгляда она\n увидела абсолютную злобу в его глазах. С губ текла\n кровь, в руке он сжимал розочку, оставшуюся после удара."
    "Лёша схватил её за шкирку и поволок из комнаты. Дверь он выбил\n ногой. Увидев изумлённых посетителей вписки, выглядывающих\n из гостиной, Лёха обматерил их, чтобы не подходили."
    "В это время они успели обуться, Лёша широко\n распахнул дверь и потащил Настю со вписки."
    scene black with dissolve 
    pause 1
    play music morning_city fadein 1.0 
    scene bg dvor_rassvet with dissolve:
        xcenter 0.5 ycenter 0.5 zoom 1.15
        ease 5 zoom 1
    play sound domofon_exit
    "Вместе выбежали на улицу."
    "Выскочив из подъезда, она побежала. Лёша побежал за ней."
    show nas pose2 surprised with dissolve:
        xpos 0.65 ypos 0.1
        xzoom -1
    nas "ААА! ОТСТАНЬ ОТ МЕНЯ!"
    nas "Не трогай меня!"
    show leh normal:
        xpos 0.05 ypos 0.07
        xzoom -1
    with dissolve
    leh "ДА ТИХО ТЫ! Никто тебя не тронет теперь!"
    leh "Побежали отсюда! Сюда менты щас приедут."
    play sound running_back
    show leh normal:
        anchor(.5,.5) pos(0.2,0.56) 
        ease 0.5 xpos(1.3) 
    show nas pose2 surprised:
        anchor(.5,.5) pos(0.75,0.6) 
        ease 0.5 xpos(1.3) 
        xzoom -1
    "И они драпанули по району, особо не разбирая\n дороги. Но Настя знала район и они не заблудились."
    scene black with dissolve 
    pause 1
    play music importanttalk fadein 1.0 volume 0.3
    scene cg2 with dissolve:
        xcenter 0.5 ycenter 0.5 zoom 1.15
        ease 5 zoom 1
    "Спустя несколько минут они присели отдышаться в укромном\n месте за памятником на площади, чтобы не привлекать внимания\n возможного ночного патруля, который мог неожиданно появиться."
    nas "Что... это было??"
    leh "Ну я так понял..."
    leh "Тебя хотели изнасиловать, а я помешал."
    nas "Пиздец..."
    nas "Как же так..."
    leh "Классная вписка. Спасибо, мне понравилось."
    leh "А эти твои друзья… они с нами в одной комнате были там?"
    "Настя начала рыдать. Лёша просто молчал. Для них обоих\n за последние полчаса мир перевернулся с ног на голову."
    nas "А зачем... ты меня спас?"
    leh "Ну а как иначе?"
    nas "Ну, просто... я так вела себя…"
    leh "Но ты попала в беду. Я обязан был тебе помочь."
    leh "Но честно... меня заебал этот Андрей."
    leh "Этот урод много себе позволяет."
    leh "Ты правильно его урыла. Но видимо он решил отомстить."
    leh "А Катя с ним встречалась. Правильно\n говорят, девушкам всякие долбоёбы нравится."
    nas "Он раньше другим был. С Катей он прилично себя вёл,\n ну... на людях. Но наедине... Катя жаловалась, но\n я думала она просто много требует от отношений."
    leh "Чтоб не насиловали? Это много?"
    "Настя ничего не ответила, лишь снова заплакала."
    leh "Слушай, а как Андрей узнал, что я её фотку\n добавил в сохраненки. Не Катя же ему это сказала?"
    nas "Прости пожалуйста! Это всё из-за меня!"
    nas "Я просто пошутить хотела. А вышло…"
    leh "Я не зол на тебя. Думаю, карма тебе уже прилетела. Даже с процентами."
    "Ребята ещё посидели молча. Вдруг Лёша спохватился."
    leh "Блин они же меня ментам сдадут!"
    nas "Не сдадут. Хата вообще ничья, сняли на ночь."
    leh "Найдут по копии паспорта"
    nas "Так они поддельные хозяину дали. Типа им 18 есть"
    nas "Да и вообще. Не думаю, что соседи или ребята ментов вызывали.\n Никто там с полицией общаться не захочет лишний раз."
    leh "А Андрей и его дружки?"
    nas "Пусть только попробует. Я скажу, что он меня изнасиловать пытался."
    nas "Поедет к челу, который Шурыгину трахнул, хахах."
    nas "Ты как? Сильно же он тебя отпиздил."
    leh "Да ничего."
    nas "Может в аптеку схожу? Тут круглосутка рядом есть."
    leh "Не надо."
    "Ребята ещё посидели."
    leh "Ты далеко живёшь?"
    nas "Полчаса отсюда идти."
    leh "Пойдём. Как раз пока дойдём автобусы начнут ходить."
    scene black with dissolve 
    pause 1
    play music morning_city fadein 1.0 
    scene bg podezd_nasty with dissolve:
        xcenter 0.5 ycenter 0.5 zoom 1.15
        ease 5 zoom 1
    "Они пошли вниз по проспекту. Настя жила в одном из\n дальних кварталов на отшибе, но Лёху такая\n мелочь не испугала. Он проводил её до подъезда."
    "В конце она остановилась."
    show nas pose2 surprised with dissolve
    nas "Ты как, дойдёшь?"
    leh "Да. Дойду до конечки. Через час дома буду."
    nas "Ладно."
    show nas pose2 serious:
        anchor(.5,.5) pos(.5,.567)
        ease 1 pos(.25,.567)
        ease 1 zoom 2.5 pos(.0,1.1)
    "Вдруг Настя обняла Лёшу."
    nas "Спасибо тебе."
    show nas pose2 normal:
        anchor(0.5,0.5) pos(.0,1.1)
        ease 2 zoom 1.25 pos(0.5,0.567)
    pause 3
    stop music
    scene black with dissolve 
    "Дома Лёша сказал, что просто переночевал у\n друга. Про то, откуда синяки, ничего не ответил."
    play music intro fadein 1.0 volume 0.3
    scene bg l_room with dissolve:
        xcenter 0.5 ycenter 0.5 zoom 1.15
        ease 5 zoom 1
    pause 2
    "Проснувшись, Лёша снова увидел кучу уведомлений вк. В этот\n раз стало приятно: Настя беспокоилась о самочувствии. Катя\n просила позвонить. Быстро ответив первой, он позвонил."
    nvl clear
    show kat pose1 smile with dissolve:
        xpos 0.15 ypos 0.2
        alpha 0.5
    katn "Привет!" with dissolve
    katn "Я узнала, что случилось."
    katn "Я хочу сказать…"
    katn "Хотя… Лучше приедь ко мне пожалуйста. Нетелефонный разговор."
    hide kat with dissolve 
    "Лёша переживал, как его приключения восприняла\n Катя. Может, наоборот, ей не понравилось." with dissolve
    scene black with dissolve 
    scene bg podezd_sunset with dissolve:
        xcenter 0.5 ycenter 0.5 zoom 1.15
        ease 5 zoom 1
    show kat pose1 smile with dissolve:
        anchor(.5,.5) pos(.5,.567)
        ease 0.6 pos(.25,.567)
        ease 1 zoom 2.5 pos(.0,1.1)
    pause 2
    "Но все сомнения пропали при встрече.\n Катя подбежала и крепко обняла его."
    show kat pose2 smile:
        anchor(0.5,0.5) pos(.0,1.1)
        ease 2 zoom 1.25 pos(0.5,0.567)
    pause 2
    show kat pose2 smile:
        anchor(.5,.5) pos(.5,0.567) 
        ease 1 xpos(.8) zoom 1
    show leh think:
        xpos 0.05 ypos 0.07
        xzoom -1
    with dissolve
    kat "Настя мне рассказала всё, что случилось."
    kat "Я очень благодарна, что ты её спас."
    kat "Я не знаю, как пережила бы то, что они с ней хотели сделать."
    kat "И я бы не смогла её спасти."
    kat "Ты большой молодец! Ты настоящий герой и все это знают!"
    show kat pose1 sad with dspr
    kat "Но это нельзя оставить так."
    show leh normal with dspr
    leh "Почему? Он же получил по заслугам."
    show kat pose1 smile with dspr
    kat "Он снова возьмётся за старое. Нет, в\n этой истории надо ставить жирную точку."
    leh "Поймаем его в подворотне и изобьём?"
    show kat pose1 surprised with dspr
    kat "Нет! Ты чё, а если он в полицию пойдёт?!\n Он бы уже на тебя настучал, если бы не то, что он Настю\n пытался изнасиловать и это могут подтвердить."
    show kat pose1 serious with dspr
    leh "Ладно-ладно, про подворотню пошутил.\n Не нужно действовать силой,\n мы пойдём иным путём."
    kat "У тебя есть идея?"
    leh "Возможно."
    stop music fadeout 2
    scene black with dissolve
    "Прошло несколько дней. Катя с Лёшей всё обдумали и отправились на дело."
    play music draka fadein 1.0 volume 0.7
    scene bg bus_stop with dissolve:
        xcenter 0.5 ycenter 0.5 zoom 1.15
        ease 5 zoom 1
    show andr normal with dissolve:
        xpos 0.03 ypos 0.05
        xzoom -1     
    show leh think:
        xpos 0.6 ypos 0.07
    show kat pose2 serious:
        anchor(.5,.5) pos(.6,0.567) 
    "Катя выманила Андрея просьбой встретиться с ней. Только\n его ждал сюрприз – ждала она его не одна, а с Лёхой."
    andr "Это че за..."
    kat "А это так, Андрюш, для безопасности."
    kat "А то ты тут такое исполняешь."
    kat "Я знала, что ты гниль. Но ты свой рекорд побил, поздравляю!"
    andr "Че..."
    kat "Рот закрой, шлюха! Так ты меня называл, да?!"
    kat "Только реальная шлюха здесь ты!\n Готов воспользоваться любой беззащитной девушкой."
    "Катя истерила, Андрей понял, что разговор не клеится."
    andr "Слышь, как тебя там, Лёха? Давай отойдём\n нормально поговорим хоть... без бабья этого"
    leh "Не о чем мне с тобой говорить"
    leh "Ты, блядь, вообще самый жалкий человек, которого я видел."
    leh "Всё, что можешь, это взять на понт, \nзастигнуть врасплох. Напасть на слабого"
    leh "Да, ты можешь меня отпиздить тут.\n Да, я ботан, который не умеет драться, а ты умеешь."
    leh "Только я всё равно буду презирать тебя. И Катя тоже будет."
    leh "Ничего ты этим не добьёшься."
    leh "Короче, давай так. Не трогай Катю, меня, Настю, наших близких."
    leh "Иначе будут такие последствия, что ты не вывезешь."
    "Андрей послушал это всё, но не нашёл что ответить."
    show andr normal:
        ease .5 xpos -.4
    "Всё, на что его хватило это махнуть рукой, буркнуть\n под нос и уйти."
    stop music fadeout 1
    scene black with dissolve 
    pause 1.0
    play music intheend fadein 1.0 volume 0.6
    scene cg3 with dissolve:
        xcenter 0.5 ycenter 0.5 zoom 1.15
        ease 5 zoom 1
    "Катя с Лёшей сидели на крыше дома. После этих напряжённых дней\n они, наконец, могли расслабиться и провести время вместе."
    kat "Лёш."
    leh "М?"
    kat "А если бы я была на месте Насти."
    leh "Ты бы меня спас?"
    leh "Ну, конечно."
    kat "Хорошо… Я верю."
    leh "Красиво было бы. Прям как в сказке."
    kat "Да… Но не всё бывает как в книгах."
    kat "Нет, я бы не хотела пережить то, что\n случилось с Настей. Главное, что всё позади."
    kat "Давай сходим погулять в центр? Только вдвоём."
    leh "Давай. Ещё только чуть-чуть посидим тут. Тут так хорошо."
    kat "Окей."
    "Катя закрыла глаза, задумавшись о чём-то приятном. А Лёша\n просто смотрел, как река Ока плывёт на свидание к реке Волге."
    pause 3

    window hide
    show black:
        subpixel True
        align (.5,.5)
        crop (480,60,850,60)
    show text "{size=40}СПАСИБО ЗА ПРОЧТЕНИЕ!"with dissolve:
        align (0.5, 0.5)
    pause 2.0  

    hide text 
    hide black
    with dissolve
    pause 1.0  
    show black:
        subpixel True
        align (.5,.5)
        crop (480,60,750,60)
    show text "{size=40}ДЛЯ ВАС СТАРАЛИСЬ:"with dissolve:
        align (0.5, 0.5)
    pause 3
    show black:
        subpixel True
        align (.5,.5)
        crop (480,60,1350,60)
    show text "{size=40}СЦЕНАРИЙ, АУДИО – АНДРЕЙ КОРШУНОВ"with dissolve:
        align (0.5, 0.5)
    pause 3
    show black:
        subpixel True
        align (.5,.5)
        crop (480,60,1000,60)
    show text "{size=40}КОД, АУДИО – Квас-Квасыч"with dissolve:
        align (0.5, 0.5)
    pause 3
    show black:
        subpixel True
        align (.5,.5)
        crop (480,60,900,60)
    show text "{size=40}ХУДОЖНИК – ТАЙМ ПЕЙНТ"with dissolve:
        align (0.5, 0.5)
    pause 3
    show black:
        subpixel True
        align (.5,.5)
        crop (0,60,1850,60)
    show text "{size=40}БЛАГОДАРНОСТИ – YTROGGRENADA, TECQUO, MYSTISS"with dissolve:
        align (0.5, 0.5)
    pause 3
    hide text 
    hide black
    with dissolve

    pause 5.0 
    hide text with dissolve
    stop music fadeout 3
    scene black with dissolve
    pause 2
return