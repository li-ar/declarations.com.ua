OLD_DECLARATION_INDEX = 'declarations_v2'
NACP_DECLARATION_INDEX = 'nacp_declarations_new'
CATALOG_INDICES = (OLD_DECLARATION_INDEX, NACP_DECLARATION_INDEX)

NUMBER_OF_SHARDS = 12
NUMBER_OF_REPLICAS = 0

CATALOG_INDEX_SETTINGS = {
    'index.mapping.total_fields.limit': 5000,
    'index.max_result_window': 4500000,
}

BANK_EDRPOUS = {
    "39002",
    "39019",
    "14291780",
    "16293211",
    "14361032",
    "14360506",
    "22906155",
    "09807856",
    "05839888",
    "19356840",
    "14351016",
    "19019775",
    "14358604",
    "19357489",
    "19357762",
    "16397258",
    "20015535",
    "14305909",
    "23494714",
    "19357443",
    "00039025",
    "00032129",
    "20017340",
    "26410155",
    "21685166",
    "21684818",
    "19338316",
    "21673424",
    "21685485",
    "14361575",
    "21665382",
    "20034231",
    "26051650",
    "19364259",
    "19454139",
    "25719206",
    "26253000",
    "21666051",
    "26253023",
    "19193869",
    "26254732",
    "19233095",
    "21753123",
    "23478833",
    "24191588",
    "19361982",
    "14360570",
    "20026838",
    "14352406",
    "20280450",
    "20305925",
    "21322127",
    "23024763",
    "23926846",
    "23928584",
    "21734522",
    "26237202",
    "33972230",
    "34514392",
    "35863708",
    "37731532",
    "37987811",
    "14360080",
    "13566973",
    "19355562",
    "21101701",
    "35345213",
    "20496061",
    "20510134",
    "09806354",
    "13857564",
    "21329000",
    "19358454",
    "24214088",
    "36964568",
    "22868414",
    "23697280",
    "22869483",
    "25959784",
    "21658672",
    "20057663",
    "20077200",
    "22932856",
    "21110655",
    "24363820",
    "24262992",
    "23362711",
    "19358784",
    "21677333",
    "20717958",
    "19357325",
    "19020301",
    "19024948",
    "14362014",
    "19361574",
    "14349442",
    "14359845",
    "14359319",
    "22199930",
    "21133352",
    "19357590",
    "19358419",
    "09322299",
    "21570492",
    "00032112",
    "13550848",
    "19361386",
    "19358282",
    "20026740",
    "19361746",
    "19359784",
    "14371869",
    "20023569",
    "21580639",
    "20023463",
    "21536532",
    "19369239",
    "19364130",
    "21595828",
    "21564391",
    "21593719",
    "21554560",
    "20050951",
    "21684161",
    "21568696",
    "02349410",
    "21574573",
    "20053145",
    "02068095",
    "20685262",
    "20748213",
    "20679755",
    "2070535",
    "2073574",
    "19358632",
    "09801546",
    "09807862",
    "19159542",
    "09306278",
    "01904694",
    "20042809",
    "20935846",
    "19361350",
    "21650966",
    "13881479",
    "20953647",
    "20935649",
    "20971504",
    "14366762",
    "20949114",
    "20041917",
    "20966466",
    "20046323",
    "21986488",
    "09807595",
    "25292831",
    "13986250",
    "21094713",
    "09806437",
    "13486837",
    "20042839",
    "14282829",
    "09804355",
    "09801641",
    "20015050",
    "19388768",
    "20365318",
    "20058668",
    "21955111",
    "26287625",
    "19358767",
    "13641864",
    "19390819",
    "01400564",
    "26120084",
    "19361427",
    "38870739",
    "39037656",
    "39544699",
    "39849797",
    "34353904",
    "09806443",
    "35264721",
    "35917889",
    "09807750",
    "09620081",
    "14360721",
    "14070197",
    "09804119",
    "19358721",
    "14360386",
    "14350784",
    "19358916",
    "19356515",
    "20021814",
    "20015529",
    "22621582",
    "19356610",
    "14253207",
    "09809192",
    "19357516",
    "36061927",
    "38770082",
    "26444836",
    "34001693",
    "26333064",
    "33299878",
    "14263173",
    "26519933",
    "26549574",
    "19359904",
    "33294890",
    "34047020",
    "34540768",
    "33695095",
    "19364584",
    "26379729",
    "20021524",
    "34540113",
    "33305163",
    "34576883",
    "26547581",
    "33308489",
    "26549700",
    "34186061",
    "34693790",
    "34575675",
    "35371070",
    "35574578",
    "35591059",
    "19017842",
    "35590956",
    "34819265",
    "35810511",
    "24425738",
    "35894495",
    "26520464",
    "35960913",
    "36002395",
    "34817907",
    "36301800",
    "36335426",
    "36406512",
    "36470620",
    "36482677",
    "36520434",
    "37119553",
    "20025456",
    "37176171",
    "37515069",
    "37716841",
    "37572263",
    "14360920",
    "38061253",
    "38322199",
    "26520688",
    "38377143",
    "38514375",
    "33881201",
    "38619024",
    "38690683",
    "38781707",
    "38591533",
    "26475516",
    "20929956",
    "16328435",
    "26364113",
    "20028816",
}

INCOME_TYPES = [
    "заробітна плата отримана за основним місцем роботи",
    "дохід від зайняття підприємницькою діяльністю",
    "заробітна плата отримана за сумісництвом",
    "подарунок у грошовій формі",
    "дивіденди",
    "подарунок у негрошовій формі",
    "гонорари та інші виплати згідно з цивільно-правовим правочинами",
    "роялті",
    "дохід від надання майна в оренду",
    "інвестиційний прибуток",
    "премія",
    "заробітна плата",
    "відрядження",
    "матеріальна допомога за основним місцем роботи",
    "майно, надане роботою",
    "часткова компенсація вартості путівок",
    "подарунок",
    "майно надане роботою",
    "переказ",
    "матеріальне заохочення",
    "новорічні подарунки",
    "кошти на відрядження",
    "витрати роботодавця на підвищення кваліфікації працівника",
    "подарунковий сертифікат",
    "піднайом житла",
    "компенсація за невикористану відпустку",
    "грошова премія",
    "санаторно-курортна путівка",
    "грошова компенсація за піднайом житла",
    "лікарняні",
    "добові",
    "майно,надане роботодавцем",
    "відрядні",
    "майно, надане работодавцем",
    "подарунок у негрошовій формі",
    "вартість путівок на відпочинок, оздоровлення",
    "заохочувальна відзнака",
    "оздоровчі",
    "подарунки",
    "компенсація вартості путівки",
    "подяка",
    "дикретна відпустка",
    "майно, надане роботодавцем безоплатно або у тимчасове користування в межах закону",
    "майно надане работодавцем",
    "трудова угода",
    "лікарняна каса",
    "за піднайом житла",
    "відшкодування витрат",
    "доходи",
    "майно, надане роботодавцем (спецодяг)",
    "матеріальна допомога отримана за основним місцем роботи",
    "виплата за піднайом житла",
    "надання послуг",
    "майно надане роботодавцем безоплатно або у тимчасове користування в межах закону",
    "путівки",
    "витрати роботодавця на підвищення кваліфікації",
    "премія до свята",
    "лікарняний",
    "майно, надане роботодавцем",
    "майно надане роботодавцем",
    "вартість путівки на оздоровлення",
    "путівка на оздоровлення",
    "сума грошового забезпечення",
    "заробітна плата за попереднім місцем роботи",
    "вихідна допомога при звільненні",
    "новорічні дитячі подарунки",
    "дохід виплачений самозайнятій особі",
    "одноразова допомога при звільненні",
    "заробітна плата з попереднього місця роботи",
    "дохід за цивільно-правовим договором",
    "оздоровлення",
]

MONETARY_ASSETS_TYPES = [
    "кошти, позичені третім особам"
]

VALID_RELATIONS = [
    "Син",
    "Дружина",
    "Чоловік",
    "Донька",
    "Дочка",
    "Мати",
    "Батько",
    "Жінка",
    "Брат",
    "Дружина брата",
    "Сестра",
    "Теща",
    "Онук",
    "Мама",
    "Невістка",
    "Племінник",
    "Баба",
    "Пасинок",
    "Дитина",
    "Матір",
    "Онука",
    "Зять",
    "Діти",
    "Свекор",
    "Бабуся",
    "Племінниця",
    "Донечка",
    "Тесть",
    "Внучка",
    "Сын",
    "Чоловик",
    "Співмешканець",
    "Супруга",
    "Допька",
    "Дружіна",
    "Падчерка",
    "Внук",
    "Свекруха",
    "Мать",
    "Доч",
    "Батьки",
    "Тітка",
    "Співмешканака",
    "Онучка",
    "Тато",
    "Жена",
]

NACP_SELECTORS_TO_TRANSLATE = "h2 span, legend i, label strong, label, th, header, span.block b, b, p, span, td"
PAPER_SELECTORS_TO_TRANSLATE = "td .l-weiss-form__row, td .weiss-digit, .l-weiss-form__item_lined"