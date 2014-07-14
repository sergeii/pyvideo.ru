# coding: utf-8
from __future__ import unicode_literals

from django import test

from richard.videos.models import Category, Video, Speaker


class CategorySlugTestCase(test.TestCase):

    slugs = (
        ('Boston Python Meetup', 'boston-python-meetup'),
        ('Chicago Djangonauts', 'chicago-djangonauts'),
        ('ChiPy', 'chipy'),
        ('DjangoCon 2009', 'djangocon-2009'),
        ('DjangoCon 2010', 'djangocon-2010'),
        ('DjangoCon 2011', 'djangocon-2011'),
        ('DjangoCon 2012', 'djangocon-2012'),
        ('DjangoCon AU 2013', 'djangocon-au-2013'),
        ('DjangoCon EU 2010', 'djangocon-eu-2010'),
        ('DjangoCon EU 2011', 'djangocon-eu-2011'),
        ('EuroPython 2011', 'europython-2011'),
        ('EuroPython 2012', 'europython-2012'),
        ('Kiwi PyCon 2009', 'kiwi-pycon-2009'),
        ('Kiwi PyCon 2013', 'kiwi-pycon-2013'),
        ('OpenStack Pycon AU 2013', 'openstack-pycon-au-2013'),
        ('PyCon AU 2010', 'pycon-au-2010'),
        ('PyCon AU 2011', 'pycon-au-2011'),
        ('PyCon AU 2012', 'pycon-au-2012'),
        ('PyCon AU 2013', 'pycon-au-2013'),
        ('PyCon CA 2012', 'pycon-ca-2012'),
        ('PyCon CA 2013', 'pycon-ca-2013'),
        ('PyCon DE 2012', 'pycon-de-2012'),
        ('PyCon DE 2013', 'pycon-de-2013'),
        ('PyCon US 2009', 'pycon-us-2009'),
        ('PyCon US 2010', 'pycon-us-2010'),
        ('PyCon US 2011', 'pycon-us-2011'),
        ('PyCon US 2012', 'pycon-us-2012'),
        ('PyCon US 2013', 'pycon-us-2013'),
        ('PyCon US 2014', 'pycon-us-2014'),
        ('PyData', 'pydata'),
        ('PyGotham 2011', 'pygotham-2011'),
        ('PyGotham 2012', 'pygotham-2012'),
        ('PyOhio 2010', 'pyohio-2010'),
        ('PyOhio 2011', 'pyohio-2011'),
        ('PyOhio 2012', 'pyohio-2012'),
        ('PyOhio 2013', 'pyohio-2013'),
        ('PyTexas 2011', 'pytexas-2011'),
        ('Python Atlanta', 'python-atlanta'),
        ('SciPy 2012', 'scipy-2012'),
        ('SciPy 2013', 'scipy-2013'),
        ('SciPy 2014', 'scipy-2014'),

        ('MoscowDjango', 'moscowdjango'),
        ('Moscow Django', 'moscow-django'),
        ('Moscow Django 2014', 'moscow-django-2014'),
        ('Computer Science Center', 'computer-science-center'),
        ('DUMP', 'dump'),
        ('EkbPy 2012', 'ekbpy-2012'),
        ('Minsk Python Meetup', 'minsk-python-meetup'),
        ('PiterPy 2014', 'piterpy-2014'),
        ('Pycon Russia 2013', 'pycon-russia-2013'),
        ('Pycon Russia 2014', 'pycon-russia-2014'),
        ('PyCon Ukraine 2012', 'pycon-ukraine-2012'),
        ('Разное', 'raznoe'),
        ('Яндекс.Events', 'iandeks-events'),

        ('PYCON AUSTRALIA NATIONAL CONFERENCE', 'pycon-australia-national-conference'),
        ('PyCon SE 2014', 'pycon-se-2014'),

        ('Пайтон Митап', 'paiton-mitap'),
        ('Ежегодная встреча джангонавтов 2050', 'ezhegodnaia-vstrecha-dzhangonavtov-2050'),

        ('Associação Python Brasil', 'associacao-python-brasil'),
    )

    def test_known_values(self):
        for title, slug in self.slugs:
            category = Category.objects.create(title=title)
            self.assertEqual(Category.objects.get(pk=category.pk).slug, slug)

    def test_category_slug_field_values_are_enforced_to_be_unique(self):
        category = Category.objects.create(title='Foo Bar')
        self.assertEqual(Category.objects.get(pk=category.pk).slug, 'foo-bar')

        category = Category.objects.create(title='Foo  Bar')
        self.assertEqual(Category.objects.get(pk=category.pk).slug, 'foo-bar-0')

        category = Category.objects.create(title='Foo   Bar')
        self.assertEqual(Category.objects.get(pk=category.pk).slug, 'foo-bar-1')


class SpeakerSlugTestCase(test.TestCase):

    slugs = (
        ('Amaury Forgeot d\'Arc', 'amaury-forgeot-darc'),
        ('Amir Salihefendic', 'amir-salihefendic'),
        ('Andrew Godwin', 'andrew-godwin'),
        ('Andriy Khavryuchenko', 'andriy-khavryuchenko'),
        ('Armin Ronacher', 'armin-ronacher'),
        ('Benoit Chesneau', 'benoit-chesneau'),
        ('David Cramer', 'david-cramer'),
        ('Dr. Russell Keith-Magee', 'dr-russell-keith-magee'),
        ('Hall A day 2', 'hall-a-day-2'),
        ('Holger Krekel', 'holger-krekel'),
        ('Jeff Lindsay', 'jeff-lindsay'),
        ('Kjetil Olsen', 'kjetil-olsen'),
        ('Kostia Lopuhin', 'kostia-lopuhin'),
        ('Michał Jastrzębski', 'michal-jastrzebski'),
        ('Niko Skrypnik', 'niko-skrypnik'),
        ('Tomasz Rybak', 'tomasz-rybak'),
        ('Vasyl Dizhak', 'vasyl-dizhak'),
        ('Łukasz Langa', 'lukasz-langa'),
        ('Александр Будкарь', 'aleksandr-budkar'),
        ('Александр Васильев', 'aleksandr-vasilev'),
        ('Александр Емелин', 'aleksandr-emelin'),
        ('Александр Кошелев', 'aleksandr-koshelev'),
        ('Александр Лябах', 'aleksandr-liabakh'),
        ('Александр Соловьев', 'aleksandr-solovev'),
        ('Алексей Качаев', 'aleksei-kachaev'),
        ('Алексей Кинёв', 'aleksei-kiniov'),
        ('Алексей Кирпичников', 'aleksei-kirpichnikov'),
        ('Андрей Власовских', 'andrei-vlasovskikh'),
        ('Андрей Григорьев', 'andrei-grigorev'),
        ('Андрей Зарубин', 'andrei-zarubin'),
        ('Андрей Попп', 'andrei-popp'),
        ('Андрей Светлов', 'andrei-svetlov'),
        ('Антон Патрушев', 'anton-patrushev'),
        ('Артем Безукладичный', 'artem-bezukladichnyi'),
        ('Валентин Синицын', 'valentin-sinitsyn'),
        ('Владимир Кириллов', 'vladimir-kirillov'),
        ('Владимир Пузанов', 'vladimir-puzanov'),
        ('Владимир Рудных', 'vladimir-rudnykh'),
        ('Владимир Филонов', 'vladimir-filonov'),
        ('Всеволод Соловьёв', 'vsevolod-soloviov'),
        ('Геннадий Чибисов', 'gennadii-chibisov'),
        ('Гриша Костюк', 'grisha-kostiuk'),
        ('Данила Штань', 'danila-shtan'),
        ('Денис Колодин', 'denis-kolodin'),
        ('Дмитрий Двойников', 'dmitrii-dvoinikov'),
        ('Дмитрий Прокофьев', 'dmitrii-prokofev'),
        ('Евгений Генералов', 'evgenii-generalov'),
        ('Екатерина Тузова', 'ekaterina-tuzova'),
        ('Иван Колодяжный', 'ivan-kolodiazhnyi'),
        ('Игорь Давыденко', 'igor-davydenko'),
        ('Илья Барышев', 'ilia-baryshev'),
        ('Илья Биин', 'ilia-biin'),
        ('Илья Глуховский', 'ilia-glukhovskii'),
        ('Илья Шаляпин', 'ilia-shaliapin'),
        ('Константин Лопухин', 'konstantin-lopukhin'),
        ('Константин Рыбников', 'konstantin-rybnikov'),
        ('Костя Лопухин', 'kostia-lopukhin'),
        ('Леонид Васильев', 'leonid-vasilev'),
        ('Максим Климишин', 'maksim-klimishin'),
        ('Марк Коренберг', 'mark-korenberg'),
        ('Михаил Коробов', 'mikhail-korobov'),
        ('Михаил Юматов', 'mikhail-iumatov'),
        ('Николай Телепенин', 'nikolai-telepenin'),
        ('Николай Ходов', 'nikolai-khodov'),
        ('Олег Евсегнеев', 'oleg-evsegneev'),
        ('Павел Зиновкин', 'pavel-zinovkin'),
        ('Павел Коломиец', 'pavel-kolomiets'),
        ('Разные', 'raznye'),
        ('Роман Иманкулов', 'roman-imankulov'),
        ('Роман Соколов', 'roman-sokolov'),
        ('Руслан Гроховецкий', 'ruslan-grokhovetskii'),
        ('Сергей Коваль', 'sergei-koval'),
        ('Сергей Матвеенко', 'sergei-matveenko'),
        ('Тарас Мурашко', 'taras-murashko'),
        ('Эдуард Снесарев', 'eduard-snesarev'),
        ('Юрий Юревич', 'iurii-iurevich'),

        # borrowed from http://pyvideo.org/api/v2/speaker/
        ('Aakash Prasad', 'aakash-prasad'),
        ('Aaron Brady', 'aaron-brady'),
        ('Aaron Meurer', 'aaron-meurer'),
        ('Aaron Oliver', 'aaron-oliver'),
        ('Aaron O\'Mullan', 'aaron-omullan'),
        ('Aashish Chaudhary', 'aashish-chaudhary'),
        ('A Bessas', 'a-bessas'),
        ('A Bingham', 'a-bingham'),
        ('Achiel van der Mandele', 'achiel-van-der-mandele'),
        ('A Cuni', 'a-cuni'),
        ('Adam Fast', 'adam-fast'),
        ('Adam Forsyth', 'adam-forsyth'),
        ('adam goucher', 'adam-goucher'),
        ('Adam Hitchcock', 'adam-hitchcock'),
        ('Adam Hughes', 'adam-hughes'),
        ('Adam Jenkins', 'adam-jenkins'),
        ('Adam Lowry', 'adam-lowry'),
        ('Adam McKerlie', 'adam-mckerlie'),
        ('Adam Miskiewicz', 'adam-miskiewicz'),
        ('Adam Moore', 'adam-moore'),
        ('Adam Nelson', 'adam-nelson'),
        ('Adam Terrey', 'adam-terrey'),
        ('Adam T. Lindsay', 'adam-t-lindsay'),
        ('Aditya Atluri', 'aditya-atluri'),
        ('Adrian Holovaty', 'adrian-holovaty'),
        ('A. Jesse Jiryu Davis', 'a-jesse-jiryu-davis'),
        ('Akand W. Islam', 'akand-w-islam'),
        ('A Kanterakis', 'a-kanterakis'),
        ('Akkana Peck', 'akkana-peck'),
        ('Alan Barber II', 'alan-barber-ii'),
        ('Alan Franzoni', 'alan-franzoni'),
        ('Alan Wang', 'alan-wang'),
        ('Alan Williams', 'alan-williams'),
        ('Al Barrentine', 'al-barrentine'),
        ('Albert O\'Connor', 'albert-oconnor'),
        ('Alejandro Weinstein', 'alejandro-weinstein'),
        ('Alessandro Amici', 'alessandro-amici'),
        ('Alessandro Dentella', 'alessandro-dentella'),
        ('Alessandro Molina', 'alessandro-molina'),
        ('Alessandro Pasotti', 'alessandro-pasotti'),
        ('Alexander Dutton', 'alexander-dutton'),
        ('Alexander Gaudio', 'alexander-gaudio'),
        ('Alexandra Strong', 'alexandra-strong'),
        ('Alexandre Bourget', 'alexandre-bourget'),
        ('Alex DeCaria', 'alex-decaria'),
        ('Alexey Malashkevich', 'alexey-malashkevich'),
        ('Alex Ezell', 'alex-ezell'),
        ('Alex Gaynor', 'alex-gaynor'),
        ('Alex Gray', 'alex-gray'),
        ('Alex Kouznetsov', 'alex-kouznetsov'),

        ('Gavin M. Roy', 'gavin-m-roy'),
        ('G. Clifford Williams', 'g-clifford-williams'),
        ('Geoffrey French', 'geoffrey-french'),
        ('Geoffrey M. Poore', 'geoffrey-m-poore'),
        ('Geoff Schmidt', 'geoff-schmidt'),
        ('George Kappel', 'george-kappel'),
        ('George Peristerakis', 'george-peristerakis'),
        ('Georgina Wilcox', 'georgina-wilcox'),
        ('Geremy Condra', 'geremy-condra'),
        ('Giovanni Bajo', 'giovanni-bajo'),
        ('Gisle Aas', 'gisle-aas'),
        ('Glen W. Mabey', 'glen-w-mabey'),
        ('Glyph', 'glyph'),
        ('Glyph Lefkowitz', 'glyph-lefkowitz'),
        ('Godfrey Ejroghene Akpojotor', 'godfrey-ejroghene-akpojotor'),
        ('Gökhan Sever', 'gokhan-sever'),
        ('Graeme Cross', 'graeme-cross'),
        ('Graham Dumpleton', 'graham-dumpleton'),
        ('Graham P Dumpleton', 'graham-p-dumpleton'),
        ('Grant Paton-Simpson', 'grant-paton-simpson'),
        ('Greg Darke', 'greg-darke'),
        ('Greg Kettler', 'greg-kettler'),
        ('Greg Lindstrom', 'greg-lindstrom'),
        ('Greg Malcolm', 'greg-malcolm'),
        ('Greg Surges', 'greg-surges'),
        ('Greg Turner', 'greg-turner'),
        ('Greg Ward', 'greg-ward'),
        ('Greg Wilson', 'greg-wilson'),
        ('Grig Gheorghiu', 'grig-gheorghiu'),
        ('Guido van Rossum', 'guido-van-rossum'),
        ('Guido Van Rossum', 'guido-van-rossum-0'),
        ('Guilherme Chapiewski', 'guilherme-chapiewski'),
        ('Guillaume Ardaud', 'guillaume-ardaud'),
        ('Guto Maia', 'guto-maia'),
        ('Guy Kloss', 'guy-kloss'),
        ('Hadrien David', 'hadrien-david'),
        ('Hamish Campbell', 'hamish-campbell'),
        ('Hannah Aizenman', 'hannah-aizenman'),
        ('Hannu Krosing', 'hannu-krosing'),
        ('Harald Armin Massa', 'harald-armin-massa'),
        ('Harald Massa', 'harald-massa'),
        ('Harinarayan Krishnan', 'harinarayan-krishnan'),
        ('Harry Percival', 'harry-percival'),
        ('Henrique Bastos', 'henrique-bastos'),
        ('Hilary James Oliver', 'hilary-james-oliver'),
        ('Hilary Mason', 'hilary-mason'),
        ('H Krosing', 'h-krosing'),
        ('H Krossing', 'h-krossing'),
        ('Horse and Unicorn', 'horse-and-unicorn'),

        ('Johan Euphrosine', 'johan-euphrosine'),
        ('Johnathan Ellis', 'johnathan-ellis'),
        ('John Barham', 'john-barham'),
        ('John F Burkhart', 'john-f-burkhart'),
        ('John Hampton', 'john-hampton'),
        ('John Hunter', 'john-hunter'),
        ('John Kitchin', 'john-kitchin'),
        ('John Mulder', 'john-mulder'),
        ('John Perry Barlow', 'john-perry-barlow'),
        ('John Rittenhouse', 'john-rittenhouse'),
        ('John Wetherill', 'john-wetherill'),
        ('Jonas Bardino', 'jonas-bardino'),
        ('Jon Åslund', 'jon-aslund'),
        ('Jonas Obrist', 'jonas-obrist'),
        ('Jonathan Ellis', 'jonathan-ellis'),
        ('Jonathan Fine', 'jonathan-fine'),
        ('Jonathan Foote', 'jonathan-foote'),
        ('Jonathan Frederic', 'jonathan-frederic'),
        ('Jonathan Hartley', 'jonathan-hartley'),
        ('Jonathan J. Helmus', 'jonathan-j-helmus'),
        ('Jonathan Riehl', 'jonathan-riehl'),
        ('Jonathan Rocher', 'jonathan-rocher'),
        ('Jonathan S. Brumberg', 'jonathan-s-brumberg'),
        ('Jonathan Schemoul', 'jonathan-schemoul'),
        ('Jon Nials', 'jon-nials'),
        ('Jon Riehl', 'jon-riehl'),
        ('Jon Wong', 'jon-wong'),
        ('Jordan Bettis', 'jordan-bettis'),
        ('Jorge L Vargas', 'jorge-l-vargas'),
        ('Jörg Kantel', 'jorg-kantel'),
        ('Josef Heinen', 'josef-heinen'),
        ('Joseph Lisee', 'joseph-lisee'),
        ('Josh Bartlett', 'josh-bartlett'),
        ('Josh Marshall', 'josh-marshall'),
        ('Joshua Bloom', 'joshua-bloom'),
        ('Joshua Ginsberg', 'joshua-ginsberg'),
        ('J Page', 'j-page'),
        ('Juan Gomez', 'juan-gomez'),
        ('Juan Lavista Ferres', 'juan-lavista-ferres'),
        ('Juan Nunez-Iglesias', 'juan-nunez-iglesias'),
        ('Juergen Brendel', 'juergen-brendel'),
        ('Juergen Schackmann', 'juergen-schackmann'),
        ('Jukka Lehtosalo', 'jukka-lehtosalo'),
        ('Julia Elman', 'julia-elman'),
        ('Julia Evans', 'julia-evans'),
        ('Julia Grace', 'julia-grace'),
        ('Julie Lavoie', 'julie-lavoie'),
        ('Julien Phalip', 'julien-phalip'),
        ('Julie Pagano', 'julie-pagano'),
        ('Julie Steele', 'julie-steele'),

        ('Reimar Bauer', 'reimar-bauer'),
        ('Reinhard Wobst', 'reinhard-wobst'),
        ('Remy DeCausemaker', 'remy-decausemaker'),
        ('Renee Chu', 'renee-chu'),
        ('Rev. Johnny Healey', 'rev-johnny-healey'),
        ('Rhydwyn Mcguire', 'rhydwyn-mcguire'),
        ('Rhys Elsmore', 'rhys-elsmore'),
        ('Rhys Rhaven', 'rhys-rhaven'),
        ('Ricardo Kirkner', 'ricardo-kirkner'),
        ('Ricardo Vazquez', 'ricardo-vazquez'),
        ('Richard Clark', 'richard-clark'),
        ('Richard Crowley', 'richard-crowley'),
        ('Richard D. Copeland, Jr.', 'richard-d-copeland-jr'),
        ('Richard Gloo', 'richard-gloo'),
        ('Richard Jones', 'richard-jones'),
        ('Richard M. Murray', 'richard-m-murray'),
        ('Richard Tew', 'richard-tew'),
        ('Richard T. Saunders', 'richard-t-saunders'),
        ('Rich Leland', 'rich-leland'),
        ('Rick Branson', 'rick-branson'),
        ('Rick Copeland', 'rick-copeland'),
        ('Rick Harding', 'rick-harding'),
        ('R Lawley', 'r-lawley'),
        ('Robbie Clemons', 'robbie-clemons'),
        ('Rob Collins', 'rob-collins'),
        ('Robert Brewer', 'robert-brewer'),
        ('Robert Collins', 'robert-collins'),
        ('Robert Coup', 'robert-coup'),
        ('Robert E Brewer', 'robert-e-brewer'),
        ('Robert Elwell', 'robert-elwell'),
        ('Robert Hancock', 'robert-hancock'),
        ('Robert Johansson', 'robert-johansson'),
        ('Robert Kluin', 'robert-kluin'),
        ('Robert Layton', 'robert-layton'),
        ('Robert Lehmann', 'robert-lehmann'),
        ('Roberto Allende', 'roberto-allende'),
        ('Roberto De Ioris', 'roberto-de-ioris'),
        ('Rob Ludwick', 'rob-ludwick'),
        ('Roger Barnes', 'roger-barnes'),
        ('Rohit Sankaran', 'rohit-sankaran'),
        ('Roman Joost', 'roman-joost'),
        ('Rory Geoghegan', 'rory-geoghegan'),
        ('Ross Heflin', 'ross-heflin'),
        ('Ross Lawley', 'ross-lawley'),
        ('Roy Hyunjin Han', 'roy-hyunjin-han'),
        ('Roy Rapoport', 'roy-rapoport'),
        ('Ruchi Varshney', 'ruchi-varshney'),
        ('Runa Sandvik', 'runa-sandvik'),
        ('Rupa Dachere', 'rupa-dachere'),
        ('Russell Keith-Magee', 'russell-keith-magee'),
    )

    def test_known_values(self):
        for name, slug in self.slugs:
            speaker = Speaker.objects.create(name=name)
            self.assertEqual(Speaker.objects.get(pk=speaker.pk).slug, slug)

    def test_speaker_slug_field_values_are_enforced_to_be_unique(self):
        speaker = Speaker.objects.create(name='Foo Bar Ham')
        self.assertEqual(Speaker.objects.get(pk=speaker.pk).slug, 'foo-bar-ham')

        speaker = Speaker.objects.create(name='Foo-Bar Ham')
        self.assertEqual(Speaker.objects.get(pk=speaker.pk).slug, 'foo-bar-ham-0')

        speaker = Speaker.objects.create(name='Foo-Bar-Ham')
        self.assertEqual(Speaker.objects.get(pk=speaker.pk).slug, 'foo-bar-ham-1')


class VideoSlugTestCase(test.TestCase):

    slugs = (
        ('Lighting Talks Андрей Светлов',
            'lighting-talks-andrei-svetlov'),

        ('На что уходит память?',
            'na-chto-ukhodit-pamiat'),

        ('Auto scaling on the Cloud the right way',
            'auto-scaling-on-the-cloud-the-right-way'),

        ('Behavior Driven Development in Python',
            'behavior-driven-development-in-python'),

        ('Explore your data',
            'explore-your-data'),

        ('Lightning talks 1',
            'lightning-talks-1'),

        ('Pony ORM - маппер нового поколения',
            'pony-orm-mapper-novogo-pokoleniia'),

        ('Python 3 and the Road Ahead',
            'python-3-and-the-road-ahead'),

        ('Python для анализа данных.',
            'python-dlia-analiza-dannykh'),

        ('Python-разработка в части Яндекс-вселенной',
            'python-razrabotka-v-chasti-iandeks-vselennoi'),

        ('The Sorry State of SSL',
            'the-sorry-state-of-ssl'),

        ('Writing Secure APIs',
            'writing-secure-apis'),

        ('Выжимаем максимум из шаблонизатора',
            'vyzhimaem-maksimum-iz-shablonizatora'),

        ('Извлечение информации из веб страниц',
            'izvlechenie-informatsii-iz-veb-stranits'),

        ('Использование SOA для построения сложных веб проектов',
            'ispolzovanie-soa-dlia-postroeniia-slozhnykh-veb-proe'),

        ('Как не надо делать, чтобы ваш Open Source продукт стал пользоваться успехом',
            'kak-ne-nado-delat-chtoby-vash-open-source-produkt'),

        ('Как писать для asyncio',
            'kak-pisat-dlia-asyncio'),

        ('Многозадачность в Python и других языках',
            'mnogozadachnost-v-python-i-drugikh-iazykakh'),

        ('Нагрузочное тестирование с помощью Яндекс.Танка',
            'nagruzochnoe-testirovanie-s-pomoshchiu-iandeks-tanka'),

        ('Понятные и расширяемые отчеты для Python+PyTest из коробки',
            'poniatnye-i-rasshiriaemye-otchety-dlia-python-pytest-i'),

        ('Почему Python нужен (был) свой underscore',
            'pochemu-python-nuzhen-byl-svoi-underscore'),

        ('Разработка мобильных приложений на Python',
            'razrabotka-mobilnykh-prilozhenii-na-python'),

        ('Декларативное программирование и алгебраические типы данных в примерах для Django',
            'deklarativnoe-programmirovanie-i-algebraicheskie-t'),

        ('Нахрена программисту свой интернет-магазин',
            'nakhrena-programmistu-svoi-internet-magazin'),

        ('Pathlib. Маленькие вкусности Python 3.4',
            'pathlib-malenkie-vkusnosti-python-3-4'),

        ('Python для ленивых или как сделать свою жизнь проще',
            'python-dlia-lenivykh-ili-kak-sdelat-svoiu-zhizn-pro'),

        ('Unittesting. Как?',
            'unittesting-kak'),

        ('Python for switch-heads',
            'python-for-switch-heads'),

        ('Redis. Как мы боролись со сложностью',
            'redis-kak-my-borolis-so-slozhnostiu'),

        ('Обзор фреймворка Twisted',
            'obzor-freimvorka-twisted'),

        ('Behavior-Driven Development',
            'behavior-driven-development'),

        ('Pyramid Traversal — правильный способ обработки URL',
            'pyramid-traversal-pravilnyi-sposob-obrabotki-u'),

        ('Python & enterprise: сложности перевода',
            'python-enterprise-slozhnosti-perevoda'),

        ('Python и программирование GPU',
            'python-i-programmirovanie-gpu'),

        ('SaltStack и Ansible — средства управления конфигурацией на языке Python',
            'saltstack-i-ansible-sredstva-upravleniia-konfigu'),

        ('"Вингардиум Левиоса". Или основы декларативной магии',
            'vingardium-leviosa-ili-osnovy-deklarativnoi-ma'),

        ('Работаем с RabbitMQ в Python используя kombu + gevent',
            'rabotaem-s-rabbitmq-v-python-ispolzuia-kombu-ge'),

        ('Работа с ошибками. Как ловить исключения и что потом с ними делать',
            'rabota-s-oshibkami-kak-lovit-iskliucheniia-i-chto-po'),

        ('Разработка декстопных приложений для linux',
            'razrabotka-dekstopnykh-prilozhenii-dlia-linux'),

        ('Разработка на Python с применением подхода Literate Programming',
            'razrabotka-na-python-s-primeneniem-podkhoda-litera'),

        ('Python и real-time',
            'python-i-real-time'),

        ('Tulip и Асинхронное Программирование в Python 3',
            'tulip-i-asinkhronnoe-programmirovanie-v-python-3'),

        ('Google Summer of Code',
            'google-summer-of-code'),

        ('Non standard library',
            'non-standard-library'),

        ('Обзор способов написания конкурентных программ в питоне',
            'obzor-sposobov-napisaniia-konkurentnykh-programm-v'),

        ('Проект Pebble',
            'proekt-pebble'),

        ('Полезные и вредные индексы MySQL',
            'poleznye-i-vrednye-indeksy-mysql'),

        ('Рвем жинжу на китайский флаг',
            'rvem-zhinzhu-na-kitaiskii-flag'),

        ('Сборка Python-проекта',
            'sborka-python-proekta'),

        ('Очередной скучный доклад про логгирование',
            'ocherednoi-skuchnyi-doklad-pro-loggirovanie'),

        ('Комментирование исходников',
            'kommentirovanie-iskhodnikov'),

        ('Пишем ИИ для Russian AI Cup',
            'pishem-ii-dlia-russian-ai-cup'),

        ('Flask: гордость и предубеждение',
            'flask-gordost-i-predubezhdenie'),

        ('Асинхронное распределенное выполнение задач. Stdlib, Celery, RQ и собственные велосипеды',
            'asinkhronnoe-raspredelennoe-vypolnenie-zadach-stdl'),

        ('Введение в GIL и новый GIL',
            'vvedenie-v-gil-i-novyi-gil'),

        ('Использование gevent для эмуляции высокой нагрузки',
            'ispolzovanie-gevent-dlia-emuliatsii-vysokoi-nagruzk'),

        ('Опциональная типизация в Python',
            'optsionalnaia-tipizatsiia-v-python'),

        ('Django 1.6',
            'django-1-6'),

        ('Оптимизируйте управление облачными ресурсами и отдыхайте',
            'optimiziruite-upravlenie-oblachnymi-resursami-i-ot'),

        ('Jinja2 в Django',
            'jinja2-v-django'),

        ('Libusb vs linux kernel — сравнение userspace & kernelspace API',
            'libusb-vs-linux-kernel-sravnenie-userspace-ke'),

        ('The Best of LinuxCon Europe 2013 (imho)﻿',
            'the-best-of-linuxcon-europe-2013-imho'),

        ('Измерение удобства современных оконных интерфейсов',
            'izmerenie-udobstva-sovremennykh-okonnykh-interfeiso'),

        ('Обзор базовых лицензий свободного ПО',
            'obzor-bazovykh-litsenzii-svobodnogo-po'),

        ('Портируем на Python 3',
            'portiruem-na-python-3'),

        ('Недостатки Python',
            'nedostatki-python'),

        ('Социальный игровой сервер на Python',
            'sotsialnyi-igrovoi-server-na-python'),

        ('GIL в Python: зачем он нужен и как с этим жить',
            'gil-v-python-zachem-on-nuzhen-i-kak-s-etim-zhit'),

        ('Модули на С. Инструменты и правила — разбираем на примере',
            'moduli-na-s-instrumenty-i-pravila-razbiraem-na'),

        ('Go для python программистов',
            'go-dlia-python-programmistov'),

        ('Профилирование и отладка Django',
            'profilirovanie-i-otladka-django'),

        ('Garbage collector and a bit of memory management',
            'garbage-collector-and-a-bit-of-memory-management'),

        ('Flask как хорошее решение для веб проекта',
            'flask-kak-khoroshee-reshenie-dlia-veb-proekta'),

        ('Красота и изящность стандартной библиотеки Python',
            'krasota-i-iziashchnost-standartnoi-biblioteki-python'),

        ('Объекты и классы в Python',
            'obekty-i-klassy-v-python'),

        ('Про асинхронное сетевое программирование',
            'pro-asinkhronnoe-setevoe-programmirovanie'),

        ('Dictionary в Python. По мотивам Objects/dictnotes.txt',
            'dictionary-v-python-po-motivam-objects-dictnotes'),

        ('Python - пробуем функциональный стиль',
            'python-probuem-funktsionalnyi-stil'),

        ('"Внутренности" CPython, часть II',
            'vnutrennosti-cpython-chast-ii'),

        ('Неочевидное поведение некоторых конструкций',
            'neochevidnoe-povedenie-nekotorykh-konstruktsii'),

        ('Fabric для управления серверами',
            'fabric-dlia-upravleniia-serverami'),

        ('Python: легко и просто. Красивые решения обычных задач',
            'python-legko-i-prosto-krasivye-resheniia-obychnykh'),

        ('Беглый обзор внутренностей интерпретатора Python',
            'beglyi-obzor-vnutrennostei-interpretatora-python'),

        ('Дескрипторы в теории и на практике',
            'deskriptory-v-teorii-i-na-praktike'),

        ('Опыт программирования роботов на языке высокого уровня (python)',
            'opyt-programmirovaniia-robotov-na-iazyke-vysokogo-u'),

        ('Преимущества разработки средствами BEM + Python + node.js',
            'preimushchestva-razrabotki-sredstvami-bem-python'),

        ('Building Public Infrastructure with Autosustainable Services',
            'building-public-infrastructure-with-autosustainab'),

        ('Celery для внутреннего API в инфраструктуре SOA',
            'celery-dlia-vnutrennego-api-v-infrastrukture-soa'),

        ('Django 1.6 and beyond: The Django Roadmap',
            'django-1-6-and-beyond-the-django-roadmap'),

        ('Lighting Talks #2',
            'lighting-talks-2'),

        ('Redis, the hacker\'s database',
            'redis-the-hackers-database'),

        ('Re-inventing Python packaging and testing',
            're-inventing-python-packaging-and-testing'),

        ('Tornado - это не только web-сайты',
            'tornado-eto-ne-tolko-web-saity'),

        ('Распределенное исполнение python кода на 10000+ серверах',
            'raspredelennoe-ispolnenie-python-koda-na-10000-s'),

        ('Эволюция системы синхронизации данных между сервисами',
            'evoliutsiia-sistemy-sinkhronizatsii-dannykh-mezhdu-servi'),

        ('A Common Scientific Compute Environment for Research and Education',
            'a-common-scientific-compute-environment-for-resea'),

        ('Airspeed Velocity: Tracking Performance of Python Projects Over Their Lifetime',
            'airspeed-velocity-tracking-performance-of-python'),

        ('Anatomy of Matplotlib - Part 1',
            'anatomy-of-matplotlib-part-1'),

        ('Anatomy of Matplotlib - Part 2',
            'anatomy-of-matplotlib-part-2'),

        ('Anatomy of Matplotlib - Part 3',
            'anatomy-of-matplotlib-part-3'),

        ('Astropy and astronomical tools Part I',
            'astropy-and-astronomical-tools-part-i'),

        ('Bayesian Statistical Analysis using Python - Part 1',
            'bayesian-statistical-analysis-using-python-part'),

        ('Bayesian Statistical Analysis using Python - Part 2',
            'bayesian-statistical-analysis-using-python-part-0'),

        ('Bayesian Statistical Analysis using Python - Part 3',
            'bayesian-statistical-analysis-using-python-part-1'),

        ('Bokeh: Interactive Visualizations in the Browser',
            'bokeh-interactive-visualizations-in-the-browser'),

        ('Conda: A Cross Platform Package Manager for any Binary Distribution',
            'conda-a-cross-platform-package-manager-for-any-b'),

        ('Creating a browser based virtual computer lab for classroom instruction',
            'creating-a-browser-based-virtual-computer-lab-for'),

        ('Frequentism and Bayesianism: What\'s the Big Deal?',
            'frequentism-and-bayesianism-whats-the-big-deal'),

        ('Fundamentals of the IPython Display Architecture+Interactive Widgets',
            'fundamentals-of-the-ipython-display-architecture'),

        ('Geospatial data in Python: Database, Desktop, and the Web part 1',
            'geospatial-data-in-python-database-desktop-and'),

        ('Geospatial data in Python: Database, Desktop, and the Web part 2',
            'geospatial-data-in-python-database-desktop-and-0'),

        ('Geospatial data in Python: Database, Desktop and the Web - Part 3',
            'geospatial-data-in-python-database-desktop-and-1'),

        ('HDF5 is for Lovers part 2',
            'hdf5-is-for-lovers-part-2'),

        ('HDF5 is for Lovers, Tutorial part 1',
            'hdf5-is-for-lovers-tutorial-part-1'),

        ('Image analysis in Python with scipy and scikit image 4',
            'image-analysis-in-python-with-scipy-and-scikit-im'),
    )

    def setUp(self):
        self.category = Category.objects.create(title='Foo')

    def test_known_values(self):
        for title, slug in self.slugs:
            video = self.category.video_set.create(title=title)
            self.assertEqual(Video.objects.get(pk=video.pk).slug, slug)

    def test_video_slugs_are_enforced_to_be_unique(self):
        video = self.category.video_set.create(title='Foo Bar in Baz')
        self.assertEqual(Video.objects.get(pk=video.pk).slug, 'foo-bar-in-baz')

        video = self.category.video_set.create(title='Foo  Bar  in  Baz')
        self.assertEqual(Video.objects.get(pk=video.pk).slug, 'foo-bar-in-baz-0')

        video = self.category.video_set.create(title='Foo-Bar-in-Baz')
        self.assertEqual(Video.objects.get(pk=video.pk).slug, 'foo-bar-in-baz-1')
