#!/usr/bin/env python3
"""Fix untranslated textwidget content in dialacarlondon language versions."""
import re
import os

BASE = "D:/dialacarlondon"

translations = {
    'ar': {
        'minicabs': 'شركة Dial A Car هي شركة الميني كاب الرائدة في لندن، تعمل على مدار 24 ساعة طوال أيام الأسبوع وعلى مدار 365 يوماً في السنة. تتراوح أسطولنا بين سيارات الميني كاب العادية وسيارات VIP مع سائق.',
        'airport': 'تتخصص Dial A Car في خدمات النقل إلى أي من المطارات في لندن وحولها - هيثرو، غاتويك، مطار لندن سيتي، ستانستد ولوتون أو إلى مطار لندن فارنبورو.',
        'chauffeur': 'تهدف خدمة Dial a Chauffeur إلى توفير تجربة قيادة ممتعة مع الراحة والموثوقية والرقي. جميع السائقين لديهم معرفة واسعة بلندن ومكرسون لتقديم خدمات ممتازة.',
        'courier': 'تمتلك Dial A Courier مجموعة متنوعة من مركبات التوصيل لجميع احتياجات الشحن. نحن أحد أكثر خدمات البريد السريع تنافسية وسرعة في لندن وحولها مع الأخذ بعين الاعتبار السلامة والأمان.',
        'iphone': 'متاح على iPhone وAndroid',
    },
    'cs': {
        'minicabs': 'Dial A Car je přední minicab společnost v Londýně, která funguje nepřetržitě 24 hodin denně, 7 dní v týdnu a 365 dní v roce. Naše flotila zahrnuje standardní minicaby až po luxusní vozidla VIP s řidičem.',
        'airport': 'Dial A Car se specializuje na letištní transfery na jakékoli letiště v Londýně a okolí - Heathrow, Gatwick, London City, Stansted a Luton nebo na letiště London Farnborough.',
        'chauffeur': 'Dial a Chauffeur si klade za cíl poskytnout příjemný zážitek z jízdy s komfortem, spolehlivostí a sofistikovaností. Všichni šoféři mají rozsáhlé znalosti Londýna a jsou odhodláni poskytovat vynikající služby.',
        'courier': 'Dial A Courier disponuje různými kurýrními vozidly pro všechny vaše přepravní potřeby. Jsme jednou z nejkonkurenceschopnějších a nejrychlejších kurýrních služeb v Londýně a okolí s důrazem na bezpečnost.',
        'iphone': 'K dispozici na iPhone a Androidu',
    },
    'de': {
        'minicabs': 'Dial A Car ist das führende Minicab-Unternehmen in London und betreibt rund um die Uhr 24 Stunden, 7 Tage die Woche und 365 Tage im Jahr. Unsere Flotte reicht von Standard-Minicabs bis hin zu VIP-Fahrzeugen mit Chauffeur.',
        'airport': 'Dial A Car ist spezialisiert auf Flughafentransfers zu jedem der Flughäfen in und um London - Heathrow, Gatwick, London City, Stansted und Luton oder zum Flughafen London Farnborough.',
        'chauffeur': 'Dial a Chauffeur ist bestrebt, ein angenehmes Fahrerlebnis mit Komfort, Zuverlässigkeit und Raffinesse zu bieten. Alle Chauffeure haben umfangreiche Kenntnisse von London und sind der Bereitstellung exzellenter Dienstleistungen verpflichtet.',
        'courier': 'Dial A Courier verfügt über eine Vielzahl von Kurierfahrzeugen für alle Ihre Versandbedürfnisse. Wir sind einer der wettbewerbsfähigsten und schnellsten Kuriere in und um London mit Fokus auf Sicherheit.',
        'iphone': 'Verfügbar auf iPhone und Android',
    },
    'el': {
        'minicabs': 'Η Dial A Car είναι η κορυφαία εταιρεία minicab στο Λονδίνο, λειτουργεί 24 ώρες το εικοσιτετράωρο, 7 ημέρες την εβδομάδα και 365 ημέρες το χρόνο. Ο στόλος μας κυμαίνεται από τυπικά minicabs έως VIP οχήματα με οδηγό.',
        'airport': 'Η Dial A Car ειδικεύεται στις μεταφορές αεροδρομίου σε οποιοδήποτε από τα αεροδρόμια μέσα και γύρω από το Λονδίνο - Χίθροου, Γκάτγουικ, Σίτι του Λονδίνου, Στάνστεντ και Λούτον ή στο αεροδρόμιο London Farnborough.',
        'chauffeur': 'Η Dial a Chauffeur στοχεύει να παρέχει μια ευχάριστη εμπειρία οδήγησης με άνεση, αξιοπιστία και εκλέπτυνση. Όλοι οι σοφέρ έχουν εκτεταμένη γνώση του Λονδίνου και είναι αφιερωμένοι στην παροχή εξαιρετικών υπηρεσιών.',
        'courier': 'Η Dial A Courier διαθέτει μια ποικιλία οχημάτων courier για όλες τις ανάγκες αποστολής σας. Είμαστε ένας από τους πιο ανταγωνιστικούς και γρήγορους courier στο Λονδίνο και γύρω από αυτό με έμφαση στην ασφάλεια.',
        'iphone': 'Διαθέσιμο σε iPhone και Android',
    },
    'es': {
        'minicabs': 'Dial A Car es la empresa líder de minicab en Londres, opera las 24 horas del día, los 7 días de la semana y los 365 días del año. Nuestra flota va desde minicabs estándar hasta vehículos VIP con conductor.',
        'airport': 'Dial A Car se especializa en traslados al aeropuerto a cualquiera de los aeropuertos dentro y alrededor de Londres: Heathrow, Gatwick, London City, Stansted y Luton o al aeropuerto de London Farnborough.',
        'chauffeur': 'Dial a Chauffeur tiene como objetivo proporcionar una experiencia de conducción placentera con comodidad, fiabilidad y sofisticación. Todos los chóferes tienen un amplio conocimiento de Londres y están dedicados a brindar excelentes servicios.',
        'courier': 'Dial A Courier cuenta con una variedad de vehículos de mensajería para todas sus necesidades de envío. Somos uno de los servicios de mensajería más competitivos y rápidos en Londres y sus alrededores con la seguridad en mente.',
        'iphone': 'Disponible en iPhone y Android',
    },
    'fi': {
        'minicabs': 'Dial A Car on Lontoon johtava minicab-yritys, joka toimii ympäri vuorokauden 24 tuntia, 7 päivää viikossa ja 365 päivää vuodessa. Kalustomme vaihtelee tavallisista minicabeista VIP-kuljettajan ajoneuvoihin.',
        'airport': 'Dial A Car on erikoistunut lentokenttäsiirtoihin mille tahansa Lontoon ja sen ympäristön lentokentälle - Heathrow, Gatwick, Lontoon City, Stansted ja Luton tai Lontoon Farnborough\'n lentokentälle.',
        'chauffeur': 'Dial a Chauffeur pyrkii tarjoamaan miellyttävän ajokokemuksen mukavuudella, luotettavuudella ja hienostuneisuudella. Kaikilla kuljettajilla on laaja tietämys Lontoosta ja he ovat omistautuneet tarjoamaan erinomaisia palveluita.',
        'courier': 'Dial A Courier tarjoaa monipuolisen valikoiman kuriiriajoneuvojasi kaikkia lähettämistarpeitasi varten. Olemme yksi kilpailukykyisimmistä ja nopeimmista kuriiripalveluista Lontoossa ja sen ympäristössä turvallisuus mielessä.',
        'iphone': 'Saatavilla iPhonelle ja Androidille',
    },
    'fr': {
        'minicabs': 'Dial A Car est la principale société de minicab à Londres, opérant 24 heures sur 24, 7 jours sur 7 et 365 jours par an. Notre flotte va des minicabs standard aux véhicules VIP avec chauffeur.',
        'airport': 'Dial A Car se spécialise dans les transferts aéroport vers n\'importe quel aéroport dans et autour de Londres - Heathrow, Gatwick, London City, Stansted et Luton ou vers l\'aéroport London Farnborough.',
        'chauffeur': 'Dial a Chauffeur vise à offrir une expérience de conduite agréable avec confort, fiabilité et sophistication. Tous les chauffeurs ont une connaissance approfondie de Londres et sont dédiés à fournir d\'excellents services.',
        'courier': 'Dial A Courier dispose d\'une variété de véhicules de messagerie pour tous vos besoins d\'expédition. Nous sommes l\'un des services de messagerie les plus compétitifs et les plus rapides de Londres et ses environs avec la sécurité à l\'esprit.',
        'iphone': 'Disponible sur iPhone et Android',
    },
    'hi': {
        'minicabs': 'Dial A Car लंदन की अग्रणी मिनीकैब कंपनी है, जो सप्ताह के 7 दिन, वर्ष के 365 दिन चौबीसों घंटे संचालित होती है। हमारे वाहन बेड़े में मानक मिनीकैब से लेकर VIP चालक-संचालित वाहन शामिल हैं।',
        'airport': 'Dial A Car लंदन के आसपास के किसी भी हवाई अड्डे - हीथ्रो, गैटविक, लंदन सिटी, स्टैनस्टेड और लूटन हवाई अड्डों या लंदन फार्नबरो हवाई अड्डे तक हवाई अड्डा स्थानांतरण में विशेषज्ञ है।',
        'chauffeur': 'Dial a Chauffeur का लक्ष्य आराम, विश्वसनीयता और परिष्कार के साथ एक सुखद ड्राइविंग अनुभव प्रदान करना है। सभी चालकों को लंदन का व्यापक ज्ञान है और वे उत्कृष्ट सेवाएं प्रदान करने के लिए समर्पित हैं।',
        'courier': 'Dial A Courier के पास आपकी सभी शिपिंग जरूरतों के लिए विभिन्न प्रकार के कूरियर वाहन हैं। सुरक्षा को ध्यान में रखते हुए हम लंदन और उसके आसपास के सबसे प्रतिस्पर्धी और तेज कूरियर में से एक हैं।',
        'iphone': 'iPhone और Android पर उपलब्ध',
    },
    'it': {
        'minicabs': 'Dial A Car è la principale compagnia di minicab a Londra, opera 24 ore su 24, 7 giorni su 7 e 365 giorni all\'anno. La nostra flotta va dai minicab standard ai veicoli VIP con autista.',
        'airport': 'Dial A Car è specializzata nei trasferimenti aeroportuali verso qualsiasi aeroporto a Londra e dintorni - Heathrow, Gatwick, London City, Stansted e Luton o all\'aeroporto London Farnborough.',
        'chauffeur': 'Dial a Chauffeur mira a fornire un\'esperienza di guida piacevole con comfort, affidabilità e raffinatezza. Tutti gli autisti hanno una vasta conoscenza di Londra e sono dedicati a fornire servizi eccellenti.',
        'courier': 'Dial A Courier dispone di una varietà di veicoli per corriere per tutte le vostre esigenze di spedizione. Siamo uno dei servizi di corriere più competitivi e veloci a Londra e dintorni con la sicurezza in mente.',
        'iphone': 'Disponibile su iPhone e Android',
    },
    'ja': {
        'minicabs': 'Dial A Carはロンドンの主要なミニキャブ会社で、年間365日、週7日、24時間体制で運営しています。私たちの車両は標準的なミニキャブからVIPシャッフォードリブン車両まで幅広く揃えています。',
        'airport': 'Dial A Carはロンドン及びその周辺の空港（ヒースロー、ガトウィック、ロンドン・シティ、スタンステッド、ルートン空港）またはロンドン・ファーンバラ空港への空港送迎を専門としています。',
        'chauffeur': 'Dial a Chauffeurは、快適さ、信頼性、洗練さを備えた快適なドライブ体験を提供することを目指しています。すべてのショーファーはロンドンに関する豊富な知識を持ち、優れたサービスの提供に専念しています。',
        'courier': 'Dial A Courierはすべての配送ニーズに対応するさまざまな配達車両を保有しています。私たちは安全とセキュリティを念頭に置きながら、ロンドンおよびその周辺で最も競争力があり、迅速なクーリエの一つです。',
        'iphone': 'iPhoneとAndroidで利用可能',
    },
    'ko': {
        'minicabs': 'Dial A Car는 런던의 선도적인 미니캡 회사로 연중무휴 24시간, 주 7일, 연 365일 운영됩니다. 저희 차량은 표준 미니캡부터 VIP 기사 차량까지 다양합니다.',
        'airport': 'Dial A Car는 런던과 주변 공항(히드로, 개트윅, 런던 시티, 스탠스테드, 루턴 공항)이나 런던 판보로 공항까지의 공항 이동을 전문으로 합니다.',
        'chauffeur': 'Dial a Chauffeur는 편안함, 신뢰성, 세련됨을 갖춘 즐거운 드라이브 경험을 제공하는 것을 목표로 합니다. 모든 기사는 런던에 대한 폭넓은 지식을 보유하고 있으며 우수한 서비스 제공에 전념하고 있습니다.',
        'courier': 'Dial A Courier는 모든 배송 필요에 맞는 다양한 택배 차량을 보유하고 있습니다. 저희는 안전과 보안을 염두에 두고 런던과 그 주변에서 가장 경쟁력 있고 빠른 택배 서비스 중 하나입니다.',
        'iphone': 'iPhone 및 Android에서 사용 가능',
    },
    'nl': {
        'minicabs': 'Dial A Car is het toonaangevende minicabbedrijf in Londen en is 24 uur per dag, 7 dagen per week en 365 dagen per jaar in bedrijf. Onze vloot varieert van standaard minicabs tot VIP-voertuigen met chauffeur.',
        'airport': 'Dial A Car is gespecialiseerd in luchthaventransfers naar elk vliegveld in en rond Londen - Heathrow, Gatwick, London City, Stansted en Luton of naar luchthaven London Farnborough.',
        'chauffeur': 'Dial a Chauffeur streeft ernaar een aangenaam rijervaring te bieden met comfort, betrouwbaarheid en verfijning. Alle chauffeurs hebben uitgebreide kennis van Londen en zijn toegewijd aan het leveren van uitstekende diensten.',
        'courier': 'Dial A Courier beschikt over een verscheidenheid aan koeriers voor al uw verzendbehoeften. Wij zijn een van de meest concurrerende en snelste koeriers in en rond Londen met veiligheid in gedachten.',
        'iphone': 'Beschikbaar op iPhone en Android',
    },
    'pl': {
        'minicabs': 'Dial A Car to wiodąca firma minicab w Londynie, działająca przez całą dobę, 7 dni w tygodniu i 365 dni w roku. Nasza flota obejmuje od standardowych minicabów do pojazdów VIP z kierowcą.',
        'airport': 'Dial A Car specjalizuje się w transferach lotniskowych do każdego z lotnisk w Londynie i okolicach - Heathrow, Gatwick, London City, Stansted i Luton lub na lotnisko London Farnborough.',
        'chauffeur': 'Dial a Chauffeur dąży do zapewnienia przyjemnego doświadczenia jazdy z komfortem, niezawodnością i wyrafinowaniem. Wszyscy szoferzy mają rozległą wiedzę o Londynie i są oddani zapewnianiu doskonałych usług.',
        'courier': 'Dial A Courier dysponuje różnorodnymi pojazdami kurierskimi na wszystkie Twoje potrzeby przesyłkowe. Jesteśmy jednym z najbardziej konkurencyjnych i najszybszych kurierów w Londynie i okolicach z myślą o bezpieczeństwie.',
        'iphone': 'Dostępne na iPhonie i Androidzie',
    },
    'pt': {
        'minicabs': 'Dial A Car é a principal empresa de minicab em Londres, operando 24 horas por dia, 7 dias por semana e 365 dias por ano. Nossa frota varia de minicabs padrão a veículos VIP com motorista.',
        'airport': 'Dial A Car é especializada em transfers aeroportuários para qualquer um dos aeroportos em Londres e arredores - Heathrow, Gatwick, London City, Stansted e Luton ou para o aeroporto London Farnborough.',
        'chauffeur': 'Dial a Chauffeur tem como objetivo proporcionar uma experiência de condução agradável com confort, fiabilidade e sofisticação. Todos os choferes têm amplo conhecimento de Londres e estão dedicados a fornecer excelentes serviços.',
        'courier': 'Dial A Courier dispõe de uma variedade de veículos de entrega para todas as suas necessidades de envio. Somos um dos serviços de entrega mais competitivos e rápidos em Londres e arredores, com segurança em mente.',
        'iphone': 'Disponível no iPhone e Android',
    },
    'ro': {
        'minicabs': 'Dial A Car este compania lider de minicab din Londra, funcționând non-stop 24 de ore pe zi, 7 zile pe săptămână și 365 de zile pe an. Flota noastră variază de la minicaburi standard la vehicule VIP cu șofer.',
        'airport': 'Dial A Car este specializată în transferuri la aeroport spre oricare dintre aeroporturile din și din jurul Londrei - Heathrow, Gatwick, London City, Stansted și Luton sau la Aeroportul London Farnborough.',
        'chauffeur': 'Dial a Chauffeur își propune să ofere o experiență de condus plăcută cu confort, fiabilitate și rafinament. Toți șoferii au cunoștințe extinse despre Londra și sunt dedicați furnizării unor servicii excelente.',
        'courier': 'Dial A Courier dispune de o varietate de vehicule de curierat pentru toate nevoile dvs. de expediere. Suntem unul dintre cei mai competitivi și rapizi curieri din Londra și împrejurimi, cu accent pe siguranță și securitate.',
        'iphone': 'Disponibil pe iPhone și Android',
    },
    'ru': {
        'minicabs': 'Dial A Car — ведущая компания по предоставлению услуг миникэба в Лондоне, работающая круглосуточно 24 часа в сутки, 7 дней в неделю и 365 дней в году. Наш автопарк варьируется от стандартных миникэбов до автомобилей VIP с водителем.',
        'airport': 'Dial A Car специализируется на трансферах в аэропорт до любого из аэропортов в Лондоне и его окрестностях — Хитроу, Гатвик, Лондон-Сити, Стэнстед и Лутон или до аэропорта Лондон Фарнборо.',
        'chauffeur': 'Dial a Chauffeur стремится обеспечить приятный опыт вождения с комфортом, надёжностью и изысканностью. Все водители обладают обширными знаниями Лондона и посвящают себя предоставлению отличных услуг.',
        'courier': 'Dial A Courier располагает разнообразными курьерскими автомобилями для всех ваших нужд по доставке грузов. Мы являемся одной из наиболее конкурентоспособных и быстрых курьерских служб в Лондоне и его окрестностях с акцентом на безопасность.',
        'iphone': 'Доступно на iPhone и Android',
    },
    'sk': {
        'minicabs': 'Dial A Car je popredná spoločnosť minicab v Londýne, ktorá funguje nepretržite 24 hodín denne, 7 dní v týždni a 365 dní v roku. Naša flotila zahŕňa od štandardných minicabov až po VIP vozidlá s vodičom.',
        'airport': 'Dial A Car sa špecializuje na letiskové transfery na ktorékoľvek letisko v Londýne a okolí - Heathrow, Gatwick, London City, Stansted a Luton alebo na letisko London Farnborough.',
        'chauffeur': 'Dial a Chauffeur si kladie za cieľ poskytnúť príjemný zážitok z jazdy s pohodlím, spoľahlivosťou a sofistikovanosťou. Všetci šoféri majú rozsiahle znalosti Londýna a sú odhodlaní poskytovať vynikajúce služby.',
        'courier': 'Dial A Courier disponuje rôznymi kuriérskymi vozidlami pre všetky vaše prepravné potreby. Sme jednou z najkonkurencieschopnejších a najrýchlejších kuriérskych služieb v Londýne a okolí s dôrazom na bezpečnosť.',
        'iphone': 'K dispozícii na iPhone a Android',
    },
    'sv': {
        'minicabs': 'Dial A Car är det ledande minicab-företaget i London och är öppet dygnet runt, 7 dagar i veckan och 365 dagar om året. Vår flotta sträcker sig från vanliga minicabs till VIP-fordon med chaufför.',
        'airport': 'Dial A Car är specialiserade på flygplatstransfer till vilken som helst av flygplatserna i och runt London - Heathrow, Gatwick, London City, Stansted och Luton eller till London Farnborough Airport.',
        'chauffeur': 'Dial a Chauffeur strävar efter att ge en trevlig körupplevelse med komfort, tillförlitlighet och sofistikering. Alla chaufförer har bred kunskap om London och är dedikerade till att tillhandahålla utmärkta tjänster.',
        'courier': 'Dial A Courier har en mängd olika kurirfordon för alla dina fraktbehov. Vi är ett av de mest konkurrenskraftiga och snabbaste buden i och runt London med säkerhet i åtanke.',
        'iphone': 'Tillgänglig på iPhone och Android',
    },
    'tr': {
        'minicabs': 'Dial A Car, Londra\'nın önde gelen minicab şirketi olup haftanın 7 günü, yılın 365 günü 24 saat hizmet vermektedir. Filomuz standart minicablardan VIP şoförlü araçlara kadar geniş bir yelpazede yer almaktadır.',
        'airport': 'Dial A Car, Londra\'da ve çevresindeki havalimanlarına - Heathrow, Gatwick, Londra City, Stansted ve Luton Havalimanları veya Londra Farnborough Havalimanı\'na havalimanı transferinde uzmanlaşmıştır.',
        'chauffeur': 'Dial a Chauffeur, konfor, güvenilirlik ve incelikle keyifli bir sürüş deneyimi sunmayı amaçlamaktadır. Tüm şoförler Londra hakkında kapsamlı bilgiye sahip olup mükemmel hizmet sunmaya adanmıştır.',
        'courier': 'Dial A Courier, tüm kargo ihtiyaçlarınız için çeşitli kurye araçlarına sahiptir. Güvenliği ön planda tutarak Londra\'da ve çevresinde en rekabetçi ve hızlı kurye hizmetlerinden biriyiz.',
        'iphone': 'iPhone ve Android\'de mevcut',
    },
    'uk': {
        'minicabs': 'Dial A Car — провідна компанія з надання послуг мінікебів у Лондоні, яка працює цілодобово 24 години на добу, 7 днів на тиждень і 365 днів на рік. Наш автопарк охоплює автомобілі від стандартних мінікебів до VIP-автомобілів з водієм.',
        'airport': 'Dial A Car спеціалізується на трансфері до аеропорту до будь-якого з аеропортів у Лондоні та навколо нього — Хітроу, Гатвік, Лондон-Сіті, Стенстед і Лутон або до аеропорту Лондон-Фарнборо.',
        'chauffeur': 'Dial a Chauffeur прагне забезпечити приємний досвід водіння з комфортом, надійністю та витонченістю. Всі водії мають глибокі знання Лондона та присвячують себе наданню чудових послуг.',
        'courier': 'Dial A Courier має різноманітні кур\'єрські автомобілі для всіх ваших потреб у доставці вантажів. Ми є одним із найконкурентоспроможніших і найшвидших кур\'єрів у Лондоні та навколо нього з акцентом на безпеку.',
        'iphone': 'Доступно на iPhone та Android',
    },
    'zh': {
        'minicabs': 'Dial A Car是伦敦领先的迷你出租车公司，全年365天、每周7天、每天24小时运营。我们的车队从标准迷你出租车到VIP专业司机车辆一应俱全。',
        'airport': 'Dial A Car专门提供伦敦及周边所有机场的接送服务——希思罗、盖特威克、伦敦城市、斯坦斯特德和卢顿机场，或伦敦法恩伯勒机场。',
        'chauffeur': 'Dial a Chauffeur致力于提供舒适、可靠、优雅的愉悦驾乘体验。所有司机对伦敦了如指掌，致力于提供卓越的服务。',
        'courier': 'Dial A Courier拥有各种快递车辆，满足您所有的货运需求。我们是伦敦及周边地区最具竞争力、最快捷的快递服务之一，始终将安全放在首位。',
        'iphone': '适用于iPhone和Android',
    },
}

def fix_language(lang, t):
    path = os.path.join(BASE, lang, 'index.html')
    if not os.path.exists(path):
        print(f"SKIP {lang}: file not found")
        return

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Fix the 4 service card textwidgets using widget ID as anchor
    # Pattern: id="text-N" ... <div class="textwidget">ANYTHING</div>
    for widget_id, key in [('text-2', 'minicabs'), ('text-3', 'airport'), ('text-4', 'chauffeur'), ('text-5', 'courier')]:
        pattern = r'(id="' + widget_id + r'"[^>]*>.*?<div class="textwidget">)[^<]*(</div>)'
        replacement = r'\g<1>' + t[key] + r'\g<2>'
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        if new_content == content:
            print(f"  WARNING [{lang}] no match for {widget_id} ({key})")
        content = new_content

    # Fix carousel "Available on iPhone and Android" (appears twice, in text-6 and text-8)
    # The pattern is: textwidget"> Available on iPhone and Android
    content = re.sub(
        r'(<div class="textwidget">) Available on iPhone and Android',
        r'\1 ' + t['iphone'],
        content
    )

    if content == original:
        print(f"  NO CHANGES [{lang}]")
        return

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  OK [{lang}]")

print("Fixing translations in all language versions...")
for lang, t in translations.items():
    fix_language(lang, t)
print("Done.")
